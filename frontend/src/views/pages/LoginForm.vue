<template>
  <div>
    <form @submit.prevent="login">
      <div>
        <label for="userName">Username:</label>
        <input type="text" id="userName" v-model="username" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <button type="submit">Login</button>
      <div v-if="loginError" class="error">{{ loginError }}</div>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { useUserStore } from '@/stores/userStore';

export default {
  setup() {
    const username = ref('');
    const email = ref('');
    const loginError = ref('');
    const userStore = useUserStore();

    const login = async () => {
      await userStore.fetchUser(username.value, email.value);
      if (userStore.companyCode) {
        // ログイン成功時の処理
        console.log('Login successful', userStore.companyCode);
        // ここでログイン成功後のナビゲーションや状態更新を行う
      } else {
        // ログイン失敗時の処理
        loginError.value = 'Invalid username or email';
      }
    };

    return { username, email, login, loginError };
  },
};
</script>

<style>
.error {
  color: red;
}
</style>
