<EasyDataTable
class="table-dark table-striped"
show-index
must-sort
:headers="headers"
:items="items"
v-model:server-options="serverOptions"
:server-items-length="serverItemsLength"
:loading="loading"
> </EasyDataTable>

<script setup>
import { ref, onMounted, watch } from 'vue'



import request from '@/helpers/index' // this costum helper, axios
const ApiUrl = "http://localhost:3000" // this my enpoind API base URI

const users = ref({})
const isFetching = ref(false)
const { get, deleteOption } = request()

const headers = [
  { text: 'Avatar', value: 'img' },
  { text: 'Nama', value: 'name' },
  { text: 'Email', value: 'email' },
  { text: 'Nomor Telepon', value: 'phone' },
  { text: 'Saldo', value: 'balance' },
  { text: 'Role', value: 'roles', width: 25 },
  { text: 'action', value: 'action' }
]
const items = ref([])
const loading = ref(false)
const serverItemsLength = ref(0)
const keyword = ref('')

const serverOptions = ref({
  page: 1,
  rowsPerPage: 10,
  sortBy: '',
  sortType: 'desc'
})

const fetchUsers = () => {
  if (isFetching.value) {
    return
  }

  isFetching.value = true
  loading.value = true

  const fetchData = async () => {
    try {
      const params = {
        page: serverOptions.value.page,
        limit: serverOptions.value.rowsPerPage,
        keyword: keyword.value, // this my costum param
        sortBy: serverOptions.value.sortBy,
        sortType: serverOptions.value.sortType,
        status: 3  // this my costum param
      }
      const API_URL = `${ApiUrl}/data${new URLSearchParams(params)}`
      const response = await get(API_URL)
      // console.log(response.data)
      users.value = response.data
      serverItemsLength.value = response.meta.total
      items.value = response.data
      loading.value = false
    } catch (error) {
      console.error(error)
    } finally {
      isFetching.value = false
    }
  }

  fetchData()
}

onMounted(() => {
  fetchUsers()
})
const cari = () => {
  //page
  serverOptions.value.page = 1
  fetchUsers()
}
watch(
  [serverOptions],
  () => {
    fetchUsers()
  },
  { deep: true }
)

</script>