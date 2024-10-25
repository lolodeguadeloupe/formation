import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      "/api": {
        target: "http://0.0.0.0:8080",
        changeOrigin: true,
        secure: false,
        autoRewrite: true,
      },
    },
    cors: false,
  },
});
