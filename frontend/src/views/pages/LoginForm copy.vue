<template>
  <div>
    <input v-model="email" type="text" placeholder="email" />
    <input v-model="password" type="password" placeholder="パスワード" />
    <button @click="login">ログイン</button>
  </div>
</template>

<script>
import axios from 'axios';
import router from '../../router';

export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          email: this.email,
          password: this.password
        });
        localStorage.setItem('access', response.data.access);
        router.push('/');
      } catch (error) {
        console.error(error);
      }
    }
  }
};
</script>