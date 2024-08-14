<template>
  <div class="background">
    <div class="text-900 font-semibold text-lg mt-3">
      Parts List
    </div>
    <Divider />

    <div class="card">
        <h2 class="text-center font-bold mb-4">パーツリスト</h2>
        <DataView :value="parts" layout="list" paginator :rows="5">
            <template #list="slotProps">
                <div class="flex flex-col">
                    <div v-for="(part, index) in slotProps.items" :key="index" class="item-row">
                        <div class="flex flex-col sm:flex-row sm:items-center p-6 gap-16">
                            <div class="relative" style="width: 250px; height: auto; margin-right: 60px; border: 1px solid black;">
                                <img 
                                    class="block mx-auto rounded no-image" 
                                    :src="`https://example.com/images/${part.image}`" 
                                    :alt="part.name" 
                                    @error="handleImageError"
                                    style="width: 100%; height: auto;" 
                                />
                                <div class="dark:bg-surface-900 absolute rounded-border" style="left: 4px; top: 4px">
                                    <Tag :value="part.inventoryStatus" :severity="getSeverity(part)"></Tag>
                                </div>
                            </div>
                            <div class="flex flex-1 items-center justify-between">
                                <div class="flex flex-col" style="flex: 2; margin-right: 40px;">
                                    <div class="text-group">
                                        <span class="font-bold">{{ part.category }}</span>
                                        <div class="font-bold">{{ part.name }}</div>
                                        <div class="font-bold">型式: {{ part.model }}</div>
                                        <div class="font-bold">メーカー: {{ part.manufacturer }}</div>
                                        <div class="font-bold">ストック個数: {{ part.stock }}</div>
                                    </div>
                                    <div class="bg-surface-100 p-1 mt-4" style="border-radius: 30px; width: fit-content;">
                                        <div class="bg-surface-0 flex items-center gap-2 justify-center py-1 px-2" style="border-radius: 30px; box-shadow: 0px 1px 2px 0px rgba(0, 0, 0, 0.04), 0px 1px 2px 0px rgba(0, 0, 0, 0.06)">
                                            <span class="text-surface-900 font-medium text-sm">{{ part.rating }}</span>
                                            <i class="pi pi-star-fill text-yellow-500"></i>
                                        </div>
                                    </div>
                                </div>
                                <div class="flex flex-col items-end" style="flex: 1;">
                                    <span class="text-xl font-semibold">${{ part.price }}</span>
                                    <div class="flex gap-2 mt-4">
                                        <Button icon="pi pi-heart" outlined></Button>
                                        <Button icon="pi pi-shopping-cart" label="購入する" :disabled="part.inventoryStatus === 'OUTOFSTOCK'" class="flex-auto md:flex-initial whitespace-nowrap"></Button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </template>
        </DataView>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import noImage from '@/assets/no_image.jpg';  // no_image.jpgのインポート
import Divider from "primevue/divider";

// 更新されたサンプルデータ
const parts = ref([
  {
      id: 1,
      name: "パーツA",
      category: "カテゴリ1",
      model: "XYZ-1000",
      manufacturer: "メーカーA",
      stock: 150,
      image: "part-a.jpg",
      price: 1000,
      rating: 4.5,
      inventoryStatus: "INSTOCK"
  },
  {
      id: 2,
      name: "パーツB",
      category: "カテゴリ2",
      model: "ABC-2000",
      manufacturer: "メーカーB",
      stock: 80,
      image: "part-b.jpg",
      price: 1500,
      rating: 4.0,
      inventoryStatus: "LOWSTOCK"
  },
  {
      id: 3,
      name: "パーツC",
      category: "カテゴリ3",
      model: "DEF-3000",
      manufacturer: "メーカーC",
      stock: 0,
      image: "part-c.jpg",
      price: 2000,
      rating: 3.5,
      inventoryStatus: "OUTOFSTOCK"
  }
  // 他のパーツデータをここに追加
]);

const getSeverity = (part) => {
  switch (part.inventoryStatus) {
      case 'INSTOCK':
          return 'success';

      case 'LOWSTOCK':
          return 'warn';

      case 'OUTOFSTOCK':
          return 'danger';

      default:
          return null;
  }
};

// 画像エラーハンドラー
const handleImageError = (event) => {
  event.target.src = noImage;  // インポートした画像を設定
};
</script>

<style scoped>
.background {
  background-color: #f5f5f5;  /* 背景を薄い灰色に設定 */
  padding: 20px;
}

.card {
  max-width: 1400px;  /* より横長のレイアウトをサポートするために幅を広げる */
  margin: 0 auto;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  background-color: #fff;
}

.text-center {
  text-align: center;
}

.flex-col {
  display: flex;
  flex-direction: column;
}

.no-image {
  width: 100%;  /* 親要素に合わせた幅に調整 */
  height: auto;  /* アスペクト比を維持して高さを自動調整 */
}

.font-bold {
  font-weight: bold;
}

/* 行間とフォントサイズを統一 */
.text-group > * {
  font-size: 1rem; /* 16px */
  line-height: 1.5rem; /* 24px */
  margin: 0.25rem 0; /* 上下に4pxのマージン */
}

/* 列間の線を追加 */
.item-row {
  border-bottom: 1px solid #ddd;
}
</style>
