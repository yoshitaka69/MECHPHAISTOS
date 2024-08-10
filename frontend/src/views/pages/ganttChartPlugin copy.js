import { ref, reactive, computed } from "vue"; // computedをインポート
import dayjs from "dayjs";

// ガントチャートのロジックを管理するカスタムフック
export function useGanttChart() {
  const BLOCK_SIZE = 20; // 各日付ブロックの幅
  const TOP_TASK_WIDTH = 300; // 上部タスクの固定部分の幅
  const BOTTOM_TASK_WIDTH = 480; // 下部タスクの固定部分の幅

  // 操作中の状態を管理するリアクティブな変数
  const dragging = ref(false); // ドラッグ中のフラグ
  const leftResizing = ref(false); // 左側リサイズ中のフラグ
  const rightResizing = ref(false); // 右側リサイズ中のフラグ
  const target = reactive({
    pageX: 0, // 現在のマウスX座標
    element: null, // 操作対象のDOM要素
    task: null, // 操作対象のタスク
    taskList: null, // 操作対象のタスクリスト
    direction: null, // リサイズの方向
  });

  // ガントチャートの表示に関する設定
  const blockWidth = ref(BLOCK_SIZE); // 各ブロックの幅
  const topTaskWidth = ref(TOP_TASK_WIDTH); // 上部タスクの幅
  const bottomTaskWidth = ref(BOTTOM_TASK_WIDTH); // 下部タスクの幅
  const topViewWidth = ref(0); // 上部ビューの幅
  const bottomViewWidth = ref(0); // 下部ビューの幅
  const contentWidth = ref(0); // コンテンツ全体の幅
  const totalDays = ref(0); // 表示期間の合計日数
  const startMonth = ref(dayjs().add(0, "month").format("YYYY-MM")); // 開始月
  const endMonth = ref(dayjs().add(1, "month").format("YYYY-MM")); // 終了月
  const calendars = ref([]); // 月のカレンダー情報
  const tasks = ref([]); // タスク情報
  const topTasks = ref([]); // 上部のタスク情報
  const calendar = ref(null); // 現在のカレンダー要素
  const scrollbarOffset = 20; // スクロールバーのオフセット
  const taskRowHeight = 40; // タスク行の高さ

  // ビューを初期化する関数
  function initView() {
    serCalendar(); // カレンダー情報を設定
    totalDays.value = calendars.value.reduce((p, c) => p + c.days.length, 0); // 総日数を計算
    contentWidth.value = totalDays.value * blockWidth.value; // コンテンツ幅を設定
    topViewWidth.value = topTaskWidth.value + contentWidth.value; // 上部ビュー幅を設定
    bottomViewWidth.value = bottomTaskWidth.value + contentWidth.value; // 下部ビュー幅を設定
    if (calendar.value) {
      // カレンダーがあればスクロールを調整
      calendar.value.scrollLeft = bottomTodayPosition.value - BOTTOM_TASK_WIDTH;
    }
  }

  // 指定された月の日付情報を取得する関数
  function getDays(startMonth) {
    const dayOfWeek = ["日", "月", "火", "水", "木", "金", "土"]; // 曜日リスト
    const days = []; // 日付リスト
    for (let i = 0; i < startMonth.daysInMonth(); i++) {
      const targetDate = startMonth.add(i, "day"); // 対象日付を計算
      days.push({
        date: targetDate.date(), // 日付を取得
        dayOfWeek: dayOfWeek[targetDate.day()], // 曜日を取得
      });
    }
    return days; // 日付情報を返す
  }

  // カレンダー情報を設定する関数
  function serCalendar() {
    const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得
    const endMonthDate = dayjs(endMonth.value); // 終了月の日付を取得
    const betweenMonth = endMonthDate.diff(startMonthDate, "month"); // 月の差分を計算
    for (let i = 0; i <= betweenMonth; i++) {
      const targetMonth = startMonthDate.add(i, "month"); // 対象月を計算
      calendars.value.push({
        title: targetMonth.format("YYYY-MM"), // 月タイトルを設定
        days: getDays(targetMonth), // 日付情報を取得
      });
    }
  }

  // タスクを移動開始する際のマウスダウンイベントハンドラ
  function onMouseDown_MoveStart(e, task, taskList) {
    dragging.value = true; // ドラッグ開始フラグをセット
    target.pageX = e.pageX; // 開始時のマウスX座標をセット
    target.element = e.target; // 対象要素をセット
    target.task = task; // 対象タスクをセット
    target.taskList = taskList; // タスクリストをセット

    document.addEventListener("mousemove", onMouseDown_Moving); // マウス移動イベントを登録
    document.addEventListener("mouseup", onMouseDown_MoveStop); // マウスアップイベントを登録
  }

  // タスク移動中のマウス移動イベントハンドラ
  function onMouseDown_Moving(e) {
    if (!dragging.value) return; // ドラッグ中でなければ終了

    const realX = calcMovePositionX(e.pageX); // 新しいX座標を計算
    target.element.style.transform = `translateX(${realX}px)`; // 要素を移動
  }

  // タスク移動終了時のマウスアップイベントハンドラ
  function onMouseDown_MoveStop(e) {
    if (!dragging.value) return; // ドラッグ中でなければ終了

    const realX = calcMovePositionX(e.pageX); // 新しいX座標を計算
    const days = Math.round((target.task.pos.x - realX) / BLOCK_SIZE); // 移動日数を計算

    if (days !== 0) {
      // 移動があればタスクの日付を更新
      const task = target.taskList.find((t) => t.id === target.task.id);
      task.startDate = dayjs(task.startDate).add(-days, "day").format("YYYY-MM-DD");
      task.endDate = dayjs(task.endDate).add(-days, "day").format("YYYY-MM-DD");
      updateTaskDates(task); // タスクの日付情報を更新
    } else {
      target.element.style.transform = `translateX(${target.task.pos.x}px)`; // 元の位置に戻す
    }

    resetDragState(); // ドラッグ状態をリセット
  }

  // タスクリサイズ開始時のマウスダウンイベントハンドラ
  function onMouseDown_ResizeStart(e, task, direction, taskList) {
    if (direction === "left") {
      leftResizing.value = true; // 左リサイズフラグをセット
    } else {
      rightResizing.value = true; // 右リサイズフラグをセット
    }
    target.pageX = e.pageX; // 開始時のマウスX座標をセット
    target.element = e.target.parentElement; // 対象要素をセット
    target.task = task; // 対象タスクをセット
    target.direction = direction; // リサイズ方向をセット
    target.taskList = taskList; // タスクリストをセット

    document.addEventListener("mousemove", onMouseDown_Resizing); // マウス移動イベントを登録
    document.addEventListener("mouseup", onMouseDown_ResizeStop); // マウスアップイベントを登録
  }

  // タスクリサイズ中のマウス移動イベントハンドラ
  function onMouseDown_Resizing(e) {
    if (!leftResizing.value && !rightResizing.value) return; // リサイズ中でなければ終了

    const realWidth = calcResizeWidth(e.pageX, target.direction); // 新しい幅を計算
    const realX = target.direction === "left" ? calcResizePositionX(e.pageX) : target.task.pos.x; // 新しいX座標を計算
    target.element.style.transform = `translateX(${realX}px)`; // 要素を移動
    target.element.style.width = `${realWidth}px`; // 幅を変更
  }

  // タスクリサイズ終了時のマウスアップイベントハンドラ
  function onMouseDown_ResizeStop(e) {
    if (!leftResizing.value && !rightResizing.value) return; // リサイズ中でなければ終了

    const realWidth = calcResizeWidth(e.pageX, target.direction); // 新しい幅を計算
    const days = Math.round((target.task.pos.width - realWidth) / BLOCK_SIZE); // リサイズ日数を計算

    if (days !== 0) {
      // リサイズがあればタスクの日付を更新
      const task = target.taskList.find((t) => t.id === target.task.id);
      if (leftResizing.value) {
        task.startDate = dayjs(task.startDate).add(days, "day").format("YYYY-MM-DD");
      } else {
        task.endDate = dayjs(task.endDate).add(-days, "day").format("YYYY-MM-DD");
      }
      updateTaskDates(task); // タスクの日付情報を更新
    } else {
      target.element.style.transform = `translateX(${target.task.pos.x}px)`; // 元の位置に戻す
      target.element.style.width = `${target.task.pos.width}px`; // 元の幅に戻す
    }

    resetResizeState(); // リサイズ状態をリセット
  }

  // ドラッグ状態をリセットする関数
  function resetDragState() {
    dragging.value = false; // ドラッグ中フラグを解除
    target.element = null; // 対象要素をクリア
    target.task = null; // 対象タスクをクリア
    target.pageX = 0; // マウスX座標をクリア

    document.removeEventListener("mousemove", onMouseDown_Moving); // マウス移動イベントを解除
    document.removeEventListener("mouseup", onMouseDown_MoveStop); // マウスアップイベントを解除
  }

  // リサイズ状態をリセットする関数
  function resetResizeState() {
    leftResizing.value = false; // 左リサイズフラグを解除
    rightResizing.value = false; // 右リサイズフラグを解除
    target.element = null; // 対象要素をクリア
    target.task = null; // 対象タスクをクリア
    target.pageX = 0; // マウスX座標をクリア

    document.removeEventListener("mousemove", onMouseDown_Resizing); // マウス移動イベントを解除
    document.removeEventListener("mouseup", onMouseDown_ResizeStop); // マウスアップイベントを解除
  }

  // マウス移動に基づいて新しいX座標を計算する関数
  function calcMovePositionX(currentPageX) {
    const diff = target.pageX - currentPageX; // 開始位置と現在位置の差分を計算
    return keepThreshold(target.task.pos.x - diff, 0, contentWidth.value - target.task.pos.width); // 閾値を超えないように位置を調整
  }

  // マウス移動に基づいてリサイズのための新しいX座標を計算する関数
  function calcResizePositionX(currentPageX) {
    const diff = target.pageX - currentPageX; // 開始位置と現在位置の差分を計算
    return keepThreshold(target.task.pos.x - diff, 0, target.task.pos.x + target.task.pos.width - BLOCK_SIZE); // 閾値を超えないように位置を調整
  }

  // マウス移動に基づいてリサイズのための新しい幅を計算する関数
  function calcResizeWidth(currentPageX, direction) {
    const diff = target.pageX - currentPageX; // 開始位置と現在位置の差分を計算
    if (direction === "left") {
      return keepThreshold(target.task.pos.width + diff, BLOCK_SIZE, target.task.pos.width + target.task.pos.x); // 左リサイズ時の幅を調整
    } else {
      return keepThreshold(target.task.pos.width - diff, BLOCK_SIZE, contentWidth.value - target.task.pos.x); // 右リサイズ時の幅を調整
    }
  }

  // 値が指定の範囲内に収まるようにする関数
  function keepThreshold(value, min, max) {
    if (value <= min) return min; // 最小値を下回らないように調整
    if (value >= max) return max; // 最大値を上回らないように調整
    return value; // 範囲内ならそのまま返す
  }

  // 曜日に応じた背景色を返す関数
  function weekendColor(dayOfWeek) {
    switch (dayOfWeek) {
      case "土":
        return "bg-blue-100"; // 土曜日の背景色
      case "日":
        return "bg-red-100"; // 日曜日の背景色
      default:
        return ""; // 平日はデフォルトの背景色
    }
  }

  // テストデータを生成する関数
  function makeTestData() {
    const today = dayjs(); // 今日の日付を取得
    for (let i = 1; i <= 3; i++) {
      // 上部タスクデータを生成
      topTasks.value.push({
        id: i,
        name: `plant - ${i}`,
        startDate: today.format("YYYY-MM-DD"),
        endDate: today.add(Math.floor(Math.random() * 5), "day").format("YYYY-MM-DD"),
      });
    }
    for (let i = 4; i <= 10; i++) {
      // 下部タスクデータを生成
      tasks.value.push({
        id: i,
        name: `task - ${i}`,
        pmType: `PM-${i % 3 + 1}`,
        startDate: today.format("YYYY-MM-DD"),
        endDate: today.add(Math.floor(Math.random() * 5), "day").format("YYYY-MM-DD"),
      });
    }
  }

  // タスクの日付情報を更新する関数
  function updateTaskDates(task) {
    const dateFrom = dayjs(task.startDate); // 開始日を取得
    const dateTo = dayjs(task.endDate); // 終了日を取得
    const between = dateTo.diff(dateFrom, "day") + 1; // 開始日と終了日の間の日数を計算
    const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得
    const start = dateFrom.diff(startMonthDate, "day"); // 開始月からの差分日数を計算

    const pos = {
      x: start * BLOCK_SIZE, // 開始位置を計算
      width: BLOCK_SIZE * between, // 幅を計算
    };

    // タスクが正しく見つかっているか確認
    const taskToUpdate = tasks.value.find((t) => t.id === task.id) || topTasks.value.find((t) => t.id === task.id);
    if (taskToUpdate) {
      taskToUpdate.style = taskToUpdate.style || {}; // デフォルトのスタイルオブジェクトを設定
      taskToUpdate.style.width = `${pos.width}px`; // スタイルの幅を設定
      taskToUpdate.style.transform = `translateX(${pos.x}px)`; // スタイルの位置を設定
    } else {
      console.error("Task not found for updating:", task.id); // タスクが見つからない場合にエラーログ
    }
  }

  // 上部タスクの名前を更新する関数
  function updateTopTaskName(task) {
    const taskToUpdate = topTasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
    if (taskToUpdate) {
      taskToUpdate.name = task.name; // タスク名を更新
    }
  }

  // タスクの名前を更新する関数
  function updateTaskName(task) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
    if (taskToUpdate) {
      taskToUpdate.name = task.name; // タスク名を更新
    }
  }

  // タスクのPMタイプを更新する関数
  function updateTaskPmType(task) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
    if (taskToUpdate) {
      taskToUpdate.pmType = task.pmType; // PMタイプを更新
    }
  }

  // タスクの担当者を更新する関数
  function updateTaskResponsible(task) {
    const taskToUpdate = tasks.value.find((t) => t.id === task.id); // 更新対象のタスクを検索
    if (taskToUpdate) {
      taskToUpdate.responsible = task.responsible; // 担当者を更新
    }
  }

  // 今日の日付の上部位置を計算するcomputedプロパティ
  const topTodayPosition = computed(() => {
    const today = dayjs(); // 今日の日付を取得
    const startDate = dayjs(startMonth.value); // 開始月の日付を取得
    const endDate = dayjs(endMonth.value); // 終了月の日付を取得
    const diffFuture = today.diff(startDate, "day"); // 今日と開始日の差分を計算
    const diffPast = endDate.diff(today, "day") + endDate.daysInMonth(); // 今日と終了日の差分を計算
    return diffFuture >= 0 && diffPast > 0 ? diffFuture * BLOCK_SIZE + topTaskWidth.value : -1; // 今日の日付が範囲内の場合に位置を計算
  });

  // 今日の日付の下部位置を計算するcomputedプロパティ
  const bottomTodayPosition = computed(() => {
    const today = dayjs(); // 今日の日付を取得
    const startDate = dayjs(startMonth.value); // 開始月の日付を取得
    const endDate = dayjs(endMonth.value); // 終了月の日付を取得
    const diffFuture = today.diff(startDate, "day"); // 今日と開始日の差分を計算
    const diffPast = endDate.diff(today, "day") + endDate.daysInMonth(); // 今日と終了日の差分を計算
    return diffFuture >= 0 && diffPast > 0 ? diffFuture * BLOCK_SIZE + bottomTaskWidth.value : -1; // 今日の日付が範囲内の場合に位置を計算
  });

  // 上部タスク行を計算するcomputedプロパティ
  const topTaskRows = computed(() => {
    const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得

    return topTasks.value.map((task) => {
      const dateFrom = dayjs(task.startDate); // 開始日を取得
      const dateTo = dayjs(task.endDate); // 終了日を取得
      const between = dateTo.diff(dateFrom, "day") + 1; // 開始日と終了日の間の日数を計算
      const start = dateFrom.diff(startMonthDate, "day"); // 開始月からの差分日数を計算

      const pos = {
        x: start * BLOCK_SIZE, // 開始位置を計算
        width: BLOCK_SIZE * between, // 幅を計算
      };

      const style = {
        width: `${pos.width}px`, // スタイルの幅を設定
        transform: `translateX(${pos.x}px)`, // スタイルの位置を設定
      };

      return {
        style, // スタイルを返す
        pos, // 位置情報を返す
        ...task, // タスク情報を返す
      };
    });
  });

  // 下部タスク行を計算するcomputedプロパティ
  const bottomTaskRows = computed(() => {
    const startMonthDate = dayjs(startMonth.value); // 開始月の日付を取得

    return tasks.value.map((task) => {
      const dateFrom = dayjs(task.startDate); // 開始日を取得
      const dateTo = dayjs(task.endDate); // 終了日を取得
      const between = dateTo.diff(dateFrom, "day") + 1; // 開始日と終了日の間の日数を計算
      const start = dateFrom.diff(startMonthDate, "day"); // 開始月からの差分日数を計算

      const pos = {
        x: start * BLOCK_SIZE, // 開始位置を計算
        width: BLOCK_SIZE * between, // 幅を計算
      };

      const style = {
        width: `${pos.width}px`, // スタイルの幅を設定
        transform: `translateX(${pos.x}px)`, // スタイルの位置を設定
      };

      return {
        style, // スタイルを返す
        pos, // 位置情報を返す
        ...task, // タスク情報を返す
      };
    });
  });

  // カスタムフックが返すデータと関数
  return {
    dragging,
    leftResizing,
    rightResizing,
    blockWidth,
    topTaskWidth,
    bottomTaskWidth,
    topViewWidth,
    bottomViewWidth,
    contentWidth,
    totalDays,
    startMonth,
    endMonth,
    calendars,
    tasks,
    topTasks,
    calendar,
    topTaskRows,
    bottomTaskRows,
    topTodayPosition,
    bottomTodayPosition,
    initView,
    getDays,
    serCalendar,
    onMouseDown_MoveStart,
    onMouseDown_Moving,
    onMouseDown_MoveStop,
    onMouseDown_ResizeStart,
    onMouseDown_Resizing,
    onMouseDown_ResizeStop,
    resetDragState,
    resetResizeState,
    calcMovePositionX,
    calcResizePositionX,
    calcResizeWidth,
    keepThreshold,
    weekendColor,
    makeTestData,
    updateTaskDates,
    updateTopTaskName,
    updateTaskName,
    updateTaskPmType,
    updateTaskResponsible,
    scrollbarOffset,
    taskRowHeight,
  };
}
