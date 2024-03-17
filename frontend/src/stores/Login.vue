<template>
    <div>
      <p>User Name: {{ user.userName }}</p>
      <p>Email: {{ user.eMail }}</p>
      <p>Company Code: {{ user.companyCode }}</p>
    </div>
  </template>
  
  <script>
  import { useUserStore } from './stores/userStore';
  
  export default {
    setup() {
      const user = useUserStore();
  
      // マウント時にユーザーデータを取得
      user.fetchUserData();
  
      return { user };
    },
  };
  </script>
  