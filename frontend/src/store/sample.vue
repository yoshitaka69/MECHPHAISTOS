<template>
    <div>
      <button v-if="!isLoggedIn" @click="handleLogin">Login</button>
      <button v-else @click="handleLogout">Logout</button>
    </div>
  </template>
  
  <script>
  import { useAuthStore } from '@/stores/auth';
  
  export default {
    setup() {
      const authStore = useAuthStore();
      const isLoggedIn = computed(() => authStore.isLoggedIn);
  
      function handleLogin() {
        // ログイン処理を行い、成功したら下記を呼び出す
        authStore.login({ name: 'User' }, 'jwt-token');
      }
  
      function handleLogout() {
        authStore.logout();
      }
  
      return { isLoggedIn, handleLogin, handleLogout };
    },
  };
  </script>
  