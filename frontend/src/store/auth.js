// stores/auth.js
import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,  // ユーザー情報
    token: null, // 認証トークン
  }),

  getters: {
    isLoggedIn: (state) => !!state.user,  // ユーザーがログインしているかどうか
  },

  actions: {
    login(user, token) {
      this.user = user;
      this.token = token;
      // ここで必要に応じて永続化処理（例えば、localStorageへの保存）を行う
    },

    logout() {
      this.user = null;
      this.token = null;
      // ここで必要に応じて永続化処理のクリアを行う
    },
  },
});
