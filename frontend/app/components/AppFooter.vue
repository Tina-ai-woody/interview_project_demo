<template>
  <footer class="border-t border-gray-200 dark:border-gray-800 bg-white dark:bg-gray-900 py-12 mt-auto">
    <UContainer>
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="col-span-1 md:col-span-1">
          <NuxtLink to="/" class="flex items-center gap-2 mb-4">
            <UIcon name="i-heroicons-shield-check" class="w-6 h-6 text-primary-500" />
            <span class="text-lg font-bold">FraudRisk</span>
          </NuxtLink>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            Advanced fraud risk management solutions for modern businesses. Empowering trust with AI.
          </p>
        </div>
        
        <div>
          <h3 class="font-semibold text-sm mb-4">Product</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="#" class="text-sm text-gray-500 hover:text-primary-500 transition-colors">Features</NuxtLink></li>
            <li><NuxtLink to="#" class="text-sm text-gray-500 hover:text-primary-500 transition-colors">API Reference</NuxtLink></li>
            <li><NuxtLink to="#" class="text-sm text-gray-500 hover:text-primary-500 transition-colors">Integrations</NuxtLink></li>
          </ul>
        </div>

        <div>
          <h3 class="font-semibold text-sm mb-4">Company</h3>
          <ul class="space-y-2">
            <li><NuxtLink to="#" class="text-sm text-gray-500 hover:text-primary-500 transition-colors">About Us</NuxtLink></li>
            <li><NuxtLink to="#" class="text-sm text-gray-500 hover:text-primary-500 transition-colors">Blog</NuxtLink></li>
            <li><NuxtLink to="#" class="text-sm text-gray-500 hover:text-primary-500 transition-colors">Careers</NuxtLink></li>
          </ul>
        </div>

        <div>
          <h3 class="font-semibold text-sm mb-4">Stay Connected</h3>
          <div class="flex items-center gap-4">
            <UButton icon="i-simple-icons-github" color="neutral" variant="ghost" />
            <UButton icon="i-simple-icons-x" color="neutral" variant="ghost" />
            <UButton icon="i-simple-icons-linkedin" color="neutral" variant="ghost" />
          </div>
        </div>
      </div>
      
      <div class="border-t border-gray-100 dark:border-gray-800 mt-12 pt-8 flex flex-col md:flex-row justify-between items-center gap-4">
        <span class="text-xs text-gray-500">
          © {{ new Date().getFullYear() }} FraudRisk Inc. All rights reserved.
        </span>
        <div class="flex gap-6">
          <NuxtLink to="#" class="text-xs text-gray-500 hover:text-primary-500">Privacy Policy</NuxtLink>
          <NuxtLink to="#" class="text-xs text-gray-500 hover:text-primary-500">Terms of Service</NuxtLink>
        </div>
      </div>
    </UContainer>
  </footer>
</template>
