import { resolve } from 'path'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react()
  ],
  build: {
    manifest: true,
    rollupOptions: {
      input: resolve(__dirname, "src/main.tsx")
    }
  },
  server: {
    host: "0.0.0.0",
    port: 3003
  }
})
