<template>
  <div class="min-h-screen flex flex-col">
    <AppNavbar />
    
    <main class="flex-grow">
      <UContainer class="py-10">
        <slot />
      </UContainer>
    </main>

    <AppFooter />
  </div>
</template>
