import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    // 開発用の初期データ
    userName: 'Taro Yamada',
    email: 'TaroYamada@test.com',
    companyCode: '001-testChemical-001',
    favoriteHistoryPossibility: 3,  // 3番目のヒストリーデータをお気に入りに設定

    // 各設定のインパクトに対するお気に入りの履歴インデックス
    favoriteHistoryImpactLow: 4,    // Low設定のお気に入り履歴インデックス
    favoriteHistoryImpactMiddle: 5, // Middle設定のお気に入り履歴インデックス
    favoriteHistoryImpactHigh: 6,   // High設定のお気に入り履歴インデックス
  }),
  actions: {
    async fetchUser(userName, email) {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/accounts/userByCompany/?format=json');
        const companies = response.data;

        // ユーザーリストの中から一致するユーザーを探す
        let foundUser = null;
        for (const company of companies) {
          foundUser = company.users.find(user => user.userName === userName && user.email === email);
          if (foundUser) {
            // 一致するユーザーが見つかった場合、その会社コードを使用する
            this.companyCode = company.companyCode;
            break;
          }
        }

        if (foundUser) {
          this.userName = userName;
          this.email = email;
        } else {
          console.error('User not found');
        }
      } catch (error) {
        console.error('Error fetching user data:', error);
      }
    },

    // お気に入りの履歴インデックスを設定するアクション
    setFavoriteHistoryPossibility(index) {
      this.favoriteHistoryPossibility = index;
    },

    // お気に入りの履歴インデックスを取得するアクション
    getFavoriteHistoryPossibility() {
      return this.favoriteHistoryPossibility;
    },

    // インパクトごとのお気に入り履歴インデックスを設定するアクション
    setFavoriteHistoryImpact(setting, index) {
      if (setting === 1) {
        this.favoriteHistoryImpactLow = index;
      } else if (setting === 2) {
        this.favoriteHistoryImpactMiddle = index;
      } else if (setting === 3) {
        this.favoriteHistoryImpactHigh = index;
      }
    },

    // インパクトごとのお気に入り履歴インデックスを取得するアクション
    getFavoriteHistoryImpact(setting) {
      if (setting === 1) {
        return this.favoriteHistoryImpactLow;
      } else if (setting === 2) {
        return this.favoriteHistoryImpactMiddle;
      } else if (setting === 3) {
        return this.favoriteHistoryImpactHigh;
      }
      return null;
    }
  },
});
