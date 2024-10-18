<template>
  <div>
    <h2>5-level Hierarchical Data in TreeTable</h2>
    <TreeTable :value="data" tableStyle="min-width: 50rem">
      <Column field="name" header="Level 1: Category" expander></Column>
      <Column field="subCategory" header="Level 2: Sub-category"></Column>
      <Column field="productName" header="Level 3: Product"></Column>
      <Column field="details" header="Level 4: Details"></Column>
      <Column field="specs" header="Level 5: Specifications"></Column>
    </TreeTable>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const data = ref([
      {
        key: '1',
        data: { name: 'Fruits', subCategory: '', productName: '', details: '', specs: '' },
        children: [
          {
            key: '1-1',
            data: { name: '', subCategory: 'Citrus', productName: '', details: '', specs: '' },
            children: [
              {
                key: '1-1-1',
                data: { name: '', subCategory: '', productName: 'Orange', details: '', specs: '' },
                children: [
                  {
                    key: '1-1-1-1',
                    data: { name: '', subCategory: '', productName: '', details: 'Sweet and Juicy', specs: '' },
                    children: [
                      {
                        key: '1-1-1-1-1',
                        data: { name: '', subCategory: '', productName: '', details: '', specs: 'Medium size, Organic' },
                      },
                    ],
                  },
                ],
              },
            ],
          },
          {
            key: '1-2',
            data: { name: '', subCategory: 'Berries', productName: '', details: '', specs: '' },
            children: [
              {
                key: '1-2-1',
                data: { name: '', subCategory: '', productName: 'Strawberry', details: '', specs: '' },
                children: [
                  {
                    key: '1-2-1-1',
                    data: { name: '', subCategory: '', productName: '', details: 'Fresh and Ripe', specs: '' },
                    children: [
                      {
                        key: '1-2-1-1-1',
                        data: { name: '', subCategory: '', productName: '', details: '', specs: 'Large, Organic' },
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
      {
        key: '2',
        data: { name: 'Vegetables', subCategory: '', productName: '', details: '', specs: '' },
        children: [
          {
            key: '2-1',
            data: { name: '', subCategory: 'Root', productName: '', details: '', specs: '' },
            children: [
              {
                key: '2-1-1',
                data: { name: '', subCategory: '', productName: 'Carrot', details: '', specs: '' },
                children: [
                  {
                    key: '2-1-1-1',
                    data: { name: '', subCategory: '', productName: '', details: 'Crunchy and Fresh', specs: '' },
                    children: [
                      {
                        key: '2-1-1-1-1',
                        data: { name: '', subCategory: '', productName: '', details: '', specs: 'Medium size, Organic' },
                      },
                    ],
                  },
                ],
              },
            ],
          },
        ],
      },
    ]);

    return { data };
  },
};
</script>

<style scoped>
/* 必要に応じてスタイルを追加 */
</style>
