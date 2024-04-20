import { defineStore } from 'pinia';
import axios from 'axios';

export const useUserStore = defineStore('user', {
  state: () => ({
    //userName: '',
    //email: '',
    //companyCode: '',
    //以下開発用
    userName: 'Taro Yamada',
    email: 'TaroYamada@test.com',
    companyCode: '001-testChemical-001',
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
  },
});
