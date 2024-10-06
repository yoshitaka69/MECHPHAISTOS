let eventGuid = 0
let todayStr = new Date().toISOString().replace(/T.*$/, '') 
// 今日の日付を ISO 文字列形式で取得

export const INITIAL_EVENTS = [
  {
    id: createEventId(),
    title: 'Work Order Event',
    start: todayStr,
    type: 'work order' // 種類を追加
  },
  {
    id: createEventId(),
    title: 'Daily Report Event',
    start: todayStr + 'T12:00:00',
    type: 'Daily report' // 種類を追加
  },
  {
    id: createEventId(),
    title: 'Task Event',
    start: '2024-10-05',
    type: 'Task' // 種類を追加
  },
  {
    id: createEventId(),
    title: 'Failure Date Event',
    start: '2024-10-10',
    type: 'Failure Date' // 種類を追加
  },
  {
    id: createEventId(),
    title: 'Another Task Event',
    start: '2024-10-12',
    type: 'Task' // 種類を追加
  }
]

export function createEventId() {
  return String(eventGuid++)
}
