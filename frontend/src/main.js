//Bootstraps Vuetify and other plugins then mounts the App
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import axios from 'axios'
import VueAxios from 'vue-axios'

import { loadFonts } from './plugins/webfontloader'


// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

//sakai-vue style
import PrimeVue from 'primevue/config';
import '@/assets/styles.scss';

//あさめしコードをwork order用
// import 'primevue/resources/themes/bootstrap4-light-blue/theme.css'
// import 'primevue/resources/themes/nova-vue/theme.css'
import "primevue/resources/themes/tailwind-light/theme.css";
// import 'primevue/resources/themes/md-light-indigo/theme.css'
import "/node_modules/primeflex/primeflex.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";

//いつかグローバルcssの統一が必要かも…
import "@/assets/global.scss";


// Table
import Button from "primevue/button";
import TieredMenu from "primevue/tieredmenu";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import ColumnGroup from "primevue/columngroup"; //optional for column grouping
import Row from "primevue/row";
import Card from "primevue/card";
import Menu from "primevue/menu";
import Paginator from "primevue/paginator";
import ProgressSpinner from "primevue/progressspinner";
import Tooltip from "primevue/tooltip";


// FORM
import AutoComplete from "primevue/autocomplete";
import InputText from "primevue/inputtext";
import Password from "primevue/password";
import Textarea from "primevue/textarea";
import Checkbox from "primevue/checkbox";

// Modal
import Dialog from "primevue/dialog";
import OverlayPanel from "primevue/overlaypanel";
import ToggleButton from "primevue/togglebutton";
import ToastService from "primevue/toastservice";
import MultiSelect from "primevue/multiselect";
import RadioButton from "primevue/radiobutton";
import Badge from "primevue/badge";
import Dropdown from "primevue/dropdown";
import TriStateCheckbox from "primevue/tristatecheckbox";
import SplitButton from "primevue/splitbutton";
import SelectButton from "primevue/selectbutton";
import Calendar from "primevue/calendar";
// System Guide View
import TabView from 'primevue/tabview';
import TabPanel from 'primevue/tabpanel';

//vue3-easy-data-table
import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';

//handsontable
import Handsontable from 'handsontable/base';

import {
    registerCellType,
    NumericCellType,
  } from 'handsontable/cellTypes';
  
  import {
    registerPlugin,
    UndoRedo,
  } from 'handsontable/plugins';


loadFonts()

const app = createApp(App)

//vuetify用プラグイン
//pinia,vue-router,vuetifyはプラグイン管理
registerPlugins(app)


app.use(ToastService);
// app.use(moment);
app.component("Button", Button);
app.component("TieredMenu", TieredMenu);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("ColumnGroup", ColumnGroup);
app.component("Row", Row);
app.component("Card", Card);
app.component("Menu", Menu);

// FORM
app.component("AutoComplete", AutoComplete);
app.component("InputText", InputText);
app.component("Password", Password);
app.component("Dialog", Dialog);
app.component("OverlayPanel", OverlayPanel);
app.component("ToggleButton", ToggleButton);
app.component("MultiSelect", MultiSelect);
app.component("Textarea", Textarea);
app.component("RadioButton", RadioButton);
app.component("Paginator", Paginator);
app.component("Badge", Badge);
app.component("Dropdown", Dropdown);
app.component("TriStateCheckbox", TriStateCheckbox);
app.component("SplitButton", SplitButton);
app.component("SelectButton", SelectButton);
app.component("ProgressSpinner", ProgressSpinner);
app.component("Calendar", Calendar);
app.component("Checkbox", Checkbox);
app.component("TabView", TabView);
app.component("TabPanel", TabPanel);
app.directive("Tooltip", Tooltip);

//vue3-easy-data-table
app.component('EasyDataTable', Vue3EasyDataTable);

registerCellType(NumericCellType);
registerPlugin(UndoRedo);

app.use(PrimeVue,{ripple : true})
app.use(VueAxios, axios)
app.mount('#app')