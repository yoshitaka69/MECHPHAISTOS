<template>
  <div class="col-12 lg:col-6 xl:col-4">
    <div class="card mb-0">
      <div class="flex justify-content-between mb-3">
        <div>
          <span class="block text-500 font-medium mb-3">Number of near misses</span>
          <div class="text-900 font-medium text-xl">{{ orderAlert }}</div>
        </div>
        <div class="flex align-items-center justify-content-center bg-orange-100 border-round"
          style="width: 2.5rem; height: 2.5rem">
          <i class="pi pi-map-marker text-orange-500 text-xl"></i>
        </div>
      </div>
      <span class="text-green-500 font-medium">%52+ </span>
      <span class="text-500">since last month</span>
    </div>
  </div>
</template>
