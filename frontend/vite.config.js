import { fileURLToPath, URL } from 'node:url';

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig(() => {
    return {
        plugins: [vue()],
        resolve: {
            alias: {
              '@': fileURLToPath(new URL('./src', import.meta.url))
            },
            extensions: [//importする際に拡張子を省略できる設定
              '.js',
              '.json',
              '.jsx',
              '.mjs',
              '.ts',
              '.tsx',
              '.vue',
            ],
          },
          server: {
            port: 4001,
             // ↓/api へのアクセスを localhost:3000 への転送
            proxy: {
              "/api": {
                target: "http://127.0.0.1:8000",
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/api/, ""),
              },
            },
          },
    };
});
