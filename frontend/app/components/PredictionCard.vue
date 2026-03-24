<script setup lang="ts">
const props = defineProps<{
  fraudProb: number
  riskLevel: 'LOW' | 'MEDIUM' | 'HIGH'
  tMid?: number
  tHigh?: number
  modelUsed?: string
}>()

const riskConfig = computed(() => {
  if (props.riskLevel === 'HIGH') return { color: 'error' as const, icon: 'i-heroicons-exclamation-triangle' }
  if (props.riskLevel === 'MEDIUM') return { color: 'warning' as const, icon: 'i-heroicons-exclamation-circle' }
  return { color: 'success' as const, icon: 'i-heroicons-check-circle' }
})
</script>

<template>
  <UCard :ui="{ body: 'p-0' }">
    <template #header>
      <div class="flex items-center justify-between">
        <div class="flex items-center gap-2">
          <UIcon name="i-heroicons-chart-bar" class="w-5 h-5 text-primary" />
          <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Prediction Results</h2>
        </div>
        <UBadge :color="riskConfig.color" variant="subtle" size="lg" class="font-bold">
          {{ riskLevel }} RISK
        </UBadge>
      </div>
    </template>

    <div class="p-6 space-y-6">
      <div class="flex flex-col items-center justify-center py-4 bg-gray-50 dark:bg-gray-800/50 rounded-xl">
        <span class="text-sm text-gray-500 dark:text-gray-400 font-medium uppercase tracking-wider">Fraud Probability</span>
        <span class="text-5xl font-black tabular-nums mt-1" :class="`text-${riskConfig.color}-600 dark:text-${riskConfig.color}-400`">
          {{ (fraudProb * 100).toFixed(2) }}%
        </span>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
        <div class="flex items-center gap-2 p-3 border border-gray-100 dark:border-gray-800 rounded-lg">
          <UIcon name="i-heroicons-cpu-chip" class="w-5 h-5 text-gray-400" />
          <div>
            <div class="text-xs text-gray-500 uppercase font-bold tracking-tight">Model Used</div>
            <div class="font-medium">{{ modelUsed || 'N/A' }}</div>
          </div>
        </div>

        <div v-if="tMid !== undefined && tHigh !== undefined" class="flex items-center gap-2 p-3 border border-gray-100 dark:border-gray-800 rounded-lg">
          <UIcon name="i-heroicons-adjustments-horizontal" class="w-5 h-5 text-gray-400" />
          <div>
            <div class="text-xs text-gray-500 uppercase font-bold tracking-tight">Thresholds</div>
            <div class="font-medium tabular-nums">M: {{ tMid }} | H: {{ tHigh }}</div>
          </div>
        </div>
      </div>
    </div>
  </UCard>
</template>

<style scoped>
/* Scoped styles removed */
</style>
