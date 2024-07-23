<template>
  <Dialog :visible="visible" @hide="hideModal" modal :closable="false">
    <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
      <div class="p-fluid flex flex-column lg:flex-row">
        <ul class="list-none m-0 p-0 flex flex-row lg:flex-column justify-content-evenly md:justify-content-between lg:justify-content-start mb-5 lg:pr-8 lg:mb-0">
          <li>
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-user md:mr-2"></i>
              <span class="font-medium hidden md:block">Profile</span>
            </a>
          </li>
          <li>
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-cog md:mr-2"></i>
              <span class="font-medium hidden md:block">Account</span>
            </a>
          </li>
          <li>
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-palette md:mr-2"></i>
              <span class="font-medium hidden md:block">Appearance</span>
            </a>
          </li>
          <li>
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-sun md:mr-2"></i>
              <span class="font-medium hidden md:block">Accessibility</span>
            </a>
          </li>
          <li>
            <a v-ripple class="flex align-items-center cursor-pointer p-3 border-round text-800 hover:surface-hover transition-duration-150 transition-colors p-ripple">
              <i class="pi pi-bell md:mr-2"></i>
              <span class="font-medium hidden md:block">Notifications</span>
            </a>
          </li>
        </ul>
        <div class="surface-card p-5 shadow-2 border-round flex-auto">
          <div class="text-900 font-semibold text-lg mt-3">Work Order Entry</div>
          <Divider></Divider>
          <div class="flex gap-5 flex-column-reverse md:flex-row">
            <div class="flex-auto p-fluid">
              <div class="mb-4">
                <label for="workOrderNo" class="block font-medium text-900 mb-2">Work Order No</label>
                <InputText id="workOrderNo" v-model="localEntry.workOrderNo" type="text" />
              </div>
              <div class="mb-4">
                <label for="plant" class="block font-medium text-900 mb-2">Plant</label>
                <InputText id="plant" v-model="localEntry.plant" type="text" />
              </div>
              <div class="mb-4">
                <label for="equipment" class="block font-medium text-900 mb-2">Equipment</label>
                <InputText id="equipment" v-model="localEntry.equipment" type="text" />
              </div>
              <div class="mb-4">
                <label for="description" class="block font-medium text-900 mb-2">Description</label>
                <Textarea id="description" v-model="localEntry.description" type="text" rows="5" :autoResize="true"></Textarea>
              </div>
              <div class="mb-4">
                <label for="status" class="block font-medium text-900 mb-2">Status</label>
                <Dropdown id="status" v-model="localEntry.status" :options="statuses" optionLabel="label" optionValue="value" placeholder="Select a Status" />
              </div>
              <div>
                <Button label="Save" icon="pi pi-check" @click="submitEntry" />
                <Button label="Cancel" icon="pi pi-times" @click="cancelNewEntry" class="p-button-secondary ml-2" />
              </div>
            </div>
            <div class="flex flex-column align-items-center flex-or">
              <span class="font-medium text-900 mb-2">Profile Picture</span>
              <img src="" class="h-10rem w-10rem" />
              <Button type="button" icon="pi pi-pencil" class="p-button-rounded -mt-4"></Button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Dialog>
</template>

<script setup>
import { ref, watch, defineEmits, defineProps } from 'vue';
import InputText from 'primevue/inputtext';
import Textarea from 'primevue/textarea';
import Button from 'primevue/button';
import Dropdown from 'primevue/dropdown';
import Dialog from 'primevue/dialog';
import Divider from 'primevue/divider';

const props = defineProps(['visible', 'statuses', 'entry']);
const emit = defineEmits(['update:visible', 'submit', 'cancel']);

const localEntry = ref({ ...props.entry });

const hideModal = () => {
  cancelNewEntry();
};

const submitEntry = () => {
  emit('submit', localEntry.value);
  emit('update:visible', false);
};

const cancelNewEntry = () => {
  emit('cancel');
  emit('update:visible', false);
};

watch(() => props.visible, (newValue) => {
  if (!newValue) {
    localEntry.value = { ...props.entry };
  }
});
</script>

<style scoped>
.surface-ground {
  padding: 1rem;
}
</style>
