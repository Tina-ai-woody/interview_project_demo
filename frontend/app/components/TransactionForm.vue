<script setup lang="ts">
export type TransactionInput = {
  step: number
  type: 'CASH_IN' | 'CASH_OUT' | 'DEBIT' | 'PAYMENT' | 'TRANSFER'
  amount: number
  oldbalanceOrg: number
  newbalanceOrig: number
  oldbalanceDest: number
  newbalanceDest: number
  isFlaggedFraud: 0 | 1
}

export type ModelName = 'xgboost' | 'decision_tree' | 'logistic_regression'

export type PredictionInput = {
  transaction: TransactionInput
  model_name: ModelName
}

const emit = defineEmits<{
  submit: [payload: PredictionInput]
}>()

const form = reactive<TransactionInput>({
  step: 1,
  type: 'TRANSFER',
  amount: 1000,
  oldbalanceOrg: 5000,
  newbalanceOrig: 4000,
  oldbalanceDest: 2000,
  newbalanceDest: 3000,
  isFlaggedFraud: 0,
})

const modelName = ref<ModelName>('xgboost')

function onSubmit() {
  emit('submit', { transaction: { ...form }, model_name: modelName.value })
}
</script>

<template>
  <UCard>
    <template #header>
      <div class="flex items-center gap-2">
        <UIcon name="i-heroicons-document-text" class="w-5 h-5 text-primary" />
        <h2 class="text-lg font-semibold text-gray-900 dark:text-white">Transaction Details</h2>
      </div>
    </template>

    <form @submit.prevent="onSubmit">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <UFormGroup label="Step" name="step" help="The step representing the time.">
          <UInput v-model.number="form.step" type="number" min="1" icon="i-heroicons-clock" />
        </UFormGroup>

        <UFormGroup label="Transaction Type" name="type">
          <USelect
            v-model="form.type"
            :options="['CASH_IN', 'CASH_OUT', 'DEBIT', 'PAYMENT', 'TRANSFER']"
          />
        </UFormGroup>

        <UFormGroup label="Amount" name="amount">
          <UInput v-model.number="form.amount" type="number" min="0" step="0.01" icon="i-heroicons-currency-dollar" />
        </UFormGroup>

        <UFormGroup label="Old Balance Origin" name="oldbalanceOrg">
          <UInput v-model.number="form.oldbalanceOrg" type="number" step="0.01" />
        </UFormGroup>

        <UFormGroup label="New Balance Origin" name="newbalanceOrig">
          <UInput v-model.number="form.newbalanceOrig" type="number" step="0.01" />
        </UFormGroup>

        <UFormGroup label="Old Balance Destination" name="oldbalanceDest">
          <UInput v-model.number="form.oldbalanceDest" type="number" step="0.01" />
        </UFormGroup>

        <UFormGroup label="New Balance Destination" name="newbalanceDest">
          <UInput v-model.number="form.newbalanceDest" type="number" step="0.01" />
        </UFormGroup>

        <UFormGroup label="Flagged Fraud" name="isFlaggedFraud">
          <USelect
            v-model.number="form.isFlaggedFraud"
            :options="[{ label: '0', value: 0 }, { label: '1', value: 1 }]"
          />
        </UFormGroup>

        <UFormGroup label="Prediction Model" name="modelName" class="md:col-span-2">
          <USelect
            v-model="modelName"
            :options="[
              { label: 'XGBoost (Recommended)', value: 'xgboost' },
              { label: 'Decision Tree', value: 'decision_tree' },
              { label: 'Logistic Regression', value: 'logistic_regression' }
            ]"
          />
        </UFormGroup>
      </div>

      <div class="mt-8 flex justify-end">
        <UButton
          type="submit"
          icon="i-heroicons-magnifying-glass"
          label="Analyze Risk"
          size="lg"
          block
          class="sm:w-auto"
        />
      </div>
    </form>
  </UCard>
</template>

<style scoped>
/* Scoped styles removed in favor of Tailwind classes and Nuxt UI defaults */
</style>
