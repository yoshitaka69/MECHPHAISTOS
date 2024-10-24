// eventService.js
import axios from 'axios';

const BASE_URL = 'http://127.0.0.1:8000/api/events'; // 適切なAPIエンドポイントを指定

export default {
  // イベントデータを取得
  async fetchEvents() {
    try {
      const response = await axios.get(`${BASE_URL}/`);
      return response.data;  // イベントデータを返す
    } catch (error) {
      console.error("イベントの取得に失敗しました:", error);
      return [];
    }
  },

  // イベントデータを保存
  async saveEvent(event) {
    try {
      await axios.post(`${BASE_URL}/${event.id}/update/`, event);
      console.log('イベントが保存されました:', event);
    } catch (error) {
      console.error("イベントの保存に失敗しました:", error);
    }
  },

  // イベントを削除
  async deleteEvent(eventId) {
    try {
      await axios.delete(`${BASE_URL}/${eventId}/`);
      console.log(`イベントID: ${eventId} が削除されました`);
    } catch (error) {
      console.error("イベントの削除に失敗しました:", error);
    }
  }
};
