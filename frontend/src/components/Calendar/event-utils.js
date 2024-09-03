let eventGuid = 0
let todayStr = new Date().toISOString().replace(/T.*$/, '') // 今日の日付を ISO 文字列形式で取得

export const INITIAL_EVENTS = [
  {
    id: createEventId(),
    title: 'All-day event',
    start: todayStr
  },
  {
    id: createEventId(),
    title: 'Timed event',
    start: todayStr + 'T12:00:00'
  }
]

export function createEventId() {
  return String(eventGuid++)
}
