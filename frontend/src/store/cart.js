import { defineStore } from 'pinia';
import {useStoreProducts} from './products';

export const useStoreCart = defineStore('cart', {
  state: () => ({
    items: [],
  }),
  getters:{
    total:(state) => {
      return state.items.reduce((total,product) => {
        return total + product.price*product.quantity;
      },0);
    },
  },
  actions: {
    addCart(product) {
      const { decrementInventory } = useStoreProducts();
      const item = this.items.find((item) => item.id === product.id);
      if (item) {
        item.quantity++;
      } else {
        this.items.push({ ...product, quantity: 1 });
      }
      decrementInventory(product.id);
    },
  },
});