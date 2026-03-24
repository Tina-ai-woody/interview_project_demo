// @ts-ignore
import { defineNuxtConfig } from 'nuxt/config';

export default defineNuxtConfig({
  compatibilityDate: '2026-03-17',
  future: { compatibilityVersion: 4 },
  modules: ['@nuxt/ui'],
  devtools: { enabled: true },
  runtimeConfig: {
    public: {
      featureApiBase: process.env.NUXT_PUBLIC_FEATURE_API_BASE || 'http://localhost:8001',
      modelApiBase: process.env.NUXT_PUBLIC_MODEL_API_BASE || 'http://localhost:8002'
    }
  },
  css: ['~/assets/css/main.css']
})
