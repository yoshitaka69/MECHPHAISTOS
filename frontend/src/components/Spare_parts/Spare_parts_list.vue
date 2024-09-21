<template>
    <div id="SparePartsList">
        <!-- 成功時または失敗時のアラート表示 -->
        <Save_Alert v-if="showAlert" :type="alertType" :message="alertMessage" :errorMessages="errorMessages" />

        <!-- companyCode 表示 -->
        <div class="company-code-container">
            <span>Company Code: {{ companyCode }}</span>
        </div>

        <div class="legend">
            <div class="legend-item">
                <div class="color-box" style="background-color: #f0a0a0"></div>
                <span>Form input format is incorrect</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background-color: #f0f0f0"></div>
                <span>Input not allowed. Value is automatically filled.</span>
            </div>
        </div>

        <!-- 行数選択ドロップダウン -->
        <div class="row-count-container">
            <span>表示する行数:</span>
            <select v-model="rowsToShow" @change="updateRowCount">
                <option value="10">10行</option>
                <option value="30">30行</option>
                <option value="50">50行</option>
                <option value="100">100行</option>
            </select>
        </div>

        <hot-table ref="hotTableComponent" :settings="hotSettings"></hot-table>

        <div class="button-container">
            <input type="number" v-model="rowsToAdd" placeholder="Number of rows" />
            <Button label="Add Rows" icon="pi pi-plus" class="p-button-primary blue-button" @click="addRows" />
            <Button label="Save Data" icon="pi pi-save" class="p-button-primary blue-button ml-3" @click="saveData" />
            <Button label="Export CSV" icon="pi pi-file-excel" class="p-button-primary green-button ml-3" @click="exportCSV" />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import Handsontable from 'handsontable';
import { defineComponent } from 'vue';
import { HotTable } from '@handsontable/vue3';
import { registerAllModules } from 'handsontable/registry';
import 'handsontable/dist/handsontable.full.css';
import { useUserStore } from '@/stores/userStore'; // Piniaストアをインポート
import Save_Alert from '@/components/Alert/Save_Alert.vue'; // 新しいアラートコンポーネントをインポート
import Button from 'primevue/button'; // PrimeVue Button コンポーネントをインポート

// register Handsontable's modules
registerAllModules();

function customRendererForAlertOrder(instance, td, row, col, prop, value, cellProperties) {
    Handsontable.renderers.TextRenderer.apply(this, arguments); // 常に基本のテキストレンダラーを適用
    if (value === 'order') {
        td.style.backgroundColor = '#FF0000'; // 注文が必要な場合は赤色
        td.style.color = 'black';
    } else if (value === 'ordered') {
        td.style.backgroundColor = '#00FF00'; // 注文済みの場合は緑色
        td.style.color = 'black';
    } else if (cellProperties.readOnly) {
        td.style.backgroundColor = '#f5f5f5'; // 読み取り専用のセルは薄い灰色
    } else {
        td.style.backgroundColor = ''; // デフォルトの背景色
        td.style.color = ''; // デフォルトのテキスト色
    }
}

function imageRenderer(instance, td, row, col, prop, value, cellProperties) {
    td.innerHTML = ''; // セルをクリア

    const partsNo = instance.getDataAtRowProp(row, 'partsNo'); // partsNo を取得
    const link = document.createElement('a');
    link.href = `/spare_parts_detail/${partsNo}`;
    link.target = '_blank';

    if (partsNo && value) {
        const img = document.createElement('img');
        img.src = value;
        img.style.width = '50px';
        img.style.height = '50px';
        link.appendChild(img);

        const url = document.createElement('div');
        url.innerText = value; // 画像のURLを表示
        url.style.fontSize = '10px';
        link.appendChild(url);
    } else if (partsNo) {
        link.innerText = 'no image';
    }

    td.appendChild(link);
}

function imageEditor(instance, td, row, col, prop, value, cellProperties) {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = 'image/*';
    input.style.display = 'none';

    input.addEventListener('change', (event) => {
        const file = event.target.files[0];
        const formData = new FormData();
        formData.append('image', file);

        axios
            .post('http://127.0.0.1:8000/api/spareParts/upload_image/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            })
            .then((response) => {
                const imageUrl = response.data.imageUrl;
                instance.setDataAtCell(row, col, imageUrl);
            })
            .catch((error) => {
                console.error('Image upload failed:', error);
            });
    });

    td.appendChild(input);
    input.click();
}

const SparePartsComponent = defineComponent({
    components: {
        HotTable,
        Save_Alert,
        Button // PrimeVue Button コンポーネントを登録
    },

    data() {
        return {
            hotSettings: {
                data: [], // **修正**: 初期データを空に設定しました
                colHeaders: [
                    'Image',
                    'parts No',
                    'BOM <br>Code.',
                    'Parts Name',
                    'Plant',
                    'Category',
                    'Model/Size',
                    'Manufacturer',
                    'Serial Number',
                    'Task List No',
                    'Price',
                    'Number <br>of ~',
                    'Unit',
                    'Summed <br>Parts Cost',
                    'Location',
                    'Delivery <br>Time',
                    'Alert <br>order',
                    'Order <br>situation',
                    'classification',
                    'inventory<br>Turnover',
                    'Description'
                ],
                rowHeaders: true, // ここで行ヘッダーを有効にします
                columns: [
                    {
                        //Image
                        data: 'image',
                        renderer: imageRenderer,
                        editor: imageEditor
                    },
                    {
                        //Parts No
                        data: 'partsNo',
                        type: 'text',
                        readOnly: true,
                        renderer: function (instance, td, row, col, prop, value, cellProperties) {
                            Handsontable.renderers.TextRenderer.apply(this, arguments);
                            td.style.backgroundColor = '#f5f5f5'; // 背景色を灰色に設定
                            td.style.color = 'black'; // テキスト色を黒に設定
                        }
                    },
                    {
                        //BOM Code.
                        data: 'bomCode',
                        type: 'text'
                    },
                    {
                        //PartsName
                        data: 'partsName',
                        type: 'text',
                        className: 'htCenter'
                    },
                    {
                        // Plant（新しく追加）
                        data: 'plant', // データのプロパティ名
                        type: 'text' // プラント名をテキストとして入力
                    },
                    {
                        //Category
                        data: 'category',
                        className: 'htRight',
                        type: 'dropdown',
                        source: ['Inventory', 'Standard', 'Consumables']
                    },
                    {
                        //Model
                        data: 'partsModel',
                        type: 'text'
                    },
                    {
                        //Manufacturer（新しく追加）
                        data: 'manufacturer', // ここに追加
                        type: 'text'
                    },
                    {
                        //SerialNumber
                        data: 'serialNumber',
                        type: 'text',
                        className: 'htRight'
                    },
                    {
                        //Task List No
                        data: 'taskListNo',
                        type: 'text',
                        className: 'htCenter'
                    },
                    {
                        //PartsCost
                        data: 'partsCost',
                        type: 'numeric',
                        className: 'htRight'
                    },
                    {
                        //Number of ~
                        data: 'numberOf',
                        width: 60,
                        className: 'htRight',
                        type: 'numeric'
                    },
                    {
                        //Unit
                        data: 'unit',
                        width: 60,
                        type: 'text',
                        className: 'htRight'
                    },
                    {
                        //Summed Parts Cost（新規追加）
                        data: 'summedPartsCost',
                        type: 'numeric',
                        className: 'htRight',
                        readOnly: true // 自動計算なので読み取り専用に設定
                    },
                    {
                        //Location
                        data: 'location',
                        className: 'htRight',
                        type: 'text',
                        className: 'htRight'
                    },
                    {
                        //Delivery Parts time
                        data: 'partsDeliveryTime',
                        width: 60,
                        className: 'htRight',
                        type: 'numeric'
                    },
                    {
                        //Alert order
                        data: 'orderAlert',
                        width: 80,
                        className: 'htCenter',
                        type: 'text',
                        renderer: customRendererForAlertOrder,
                        readOnly: true
                    },
                    {
                        //Order situation
                        data: 'orderSituation',
                        width: 100,
                        className: 'htCenter',
                        type: 'checkbox'
                    },
                    {
                        //classification
                        data: 'classification',
                        width: 100,
                        className: 'htCenter',
                        type: 'dropdown',
                        source: ['', 'Long-Term Stock Items', 'Short-Term Stock Items', 'Dead Stock Items', 'Critical Stock Items', 'Safety Stock Items', 'Irregular Use Stock Items']
                    },
                    {
                        //inventoryTurnover
                        data: 'inventoryTurnover',
                        width: 100,
                        className: 'htCenter',
                        type: 'text'
                    },
                    {
                        //Description
                        data: 'partsDescription',
                        className: 'htCenter',
                        type: 'text'
                    }
                ],

                afterGetColHeader: (col, TH) => {
                    if (col === -1) {
                        // ヘッダー行の場合
                        return;
                    }
                    // 全ヘッダーセルに薄い青色の背景を設定
                    TH.style.backgroundColor = '#E6F7FF'; // 薄い青色
                    TH.style.color = 'black'; // テキスト色を黒に設定
                    TH.style.fontWeight = 'bold'; // テキストを太字に設定
                },

                afterChange: function (changes, source) {
                    if (changes) {
                        changes.forEach(([row, prop, oldValue, newValue]) => {
                            // 値が変更された場合にsummedPartsCostを更新
                            if (prop === 'partsCost' || prop === 'numberOf') {
                                const hotInstance = this;
                                const price = hotInstance.getDataAtCell(row, 10); // partsCost の列番号（0から数えて10列目）
                                const quantity = hotInstance.getDataAtCell(row, 11); // numberOf の列番号（0から数えて11列目）
                                const summedPartsCost = (parseFloat(price) || 0) * (parseFloat(quantity) || 0);
                                hotInstance.setDataAtCell(row, 13, summedPartsCost); // summedPartsCost の列番号（0から数えて13列目）

                                // `price` が 0 より大きく `numberOf` が 0 の場合に `order` を設定
                                if (price > 0 && quantity === 0) {
                                    hotInstance.setDataAtCell(row, 16, 'order'); // `orderAlert` の列番号（0から数えて16列目）
                                } else if (quantity > 0) {
                                    // `numberOf` が 0 より大きい場合に `order` を消す
                                    hotInstance.setDataAtCell(row, 16, '');
                                }
                            }

                            if (prop === 'orderSituation') {
                                const alertOrderValue = this.getDataAtCell(row, 16);
                                if (newValue === true && alertOrderValue === 'order') {
                                    this.setDataAtCell(row, 16, 'ordered');
                                } else if (newValue === false && alertOrderValue === 'ordered') {
                                    this.setDataAtCell(row, 16, 'order');
                                }
                            }
                        });
                    }
                },

                cells: function (row, col, prop) {
                    const cellProperties = {};
                    const readOnlyColumns = ['inventoryTurnover'];

                    if (readOnlyColumns.includes(this.columns[col].data)) {
                        cellProperties.readOnly = true; // 列を読み取り専用に設定
                        cellProperties.renderer = customRendererForAlertOrder; // すべての読み取り専用列にカスタムレンダラーを適用
                    }
                    return cellProperties;
                },

                width: '100%',
                height: 'auto',
                stretchH: 'all', // 'none' is default 様子見
                contextMenu: true, //コンテキストメニュー
                autoWrapRow: true,
                autoWrapCol: true,
                fixedColumnsStart: 2, //カラム固定
                fixedRowsTop: 0, //列固定
                manualColumnFreeze: true, //コンテキストメニュー手動でコラム解除
                manualColumnResize: true, //手動での列幅調整
                manualRowResize: true, //列の手動高さ調整
                filters: true,
                dropdownMenu: true,
                comments: true, //コメントの有り無し
                fillHandle: {
                    autoInsertRow: true
                },

                licenseKey: 'non-commercial-and-evaluation'
            },
            rowsToAdd: 1, // 追加する行数のデフォルト値
            rowsToShow: 10, // デフォルトで表示する行数
            sparePartsDataStore: [], // データストア
            showAlert: false, // アラート表示用のフラグ
            alertType: 'success', // 'success' か 'error' を指定
            alertMessage: 'データが正常に保存されました。',
            errorMessages: [], // エラーメッセージのリスト
            companyCode: '' // companyCode を追加
        };
    },

    created() {
        this.getDataAxios();
    },

    watch: {
        rowsToShow() {
            this.updateRowCount();
        }
    },

    methods: {
        getDataAxios() {
            const userStore = useUserStore(); // Piniaストアからユーザー情報を取得
            const userCompanyCode = userStore.companyCode; // ユーザーの companyCode を取得

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const url = `http://127.0.0.1:8000/api/spareParts/sparePartsByCompany/?format=json&companyCode=${userCompanyCode}`;

            axios
                .get(url, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    withCredentials: true
                })
                .then((response) => {
                    const sparePartsData = response.data;

                    // データのcompanyCodeをセット
                    if (sparePartsData && sparePartsData.length > 0) {
                        this.companyCode = sparePartsData[0].companyCode; // 取得したcompanyCodeを設定
                    }

                    const index = [
                        'image',
                        'partsNo',
                        'bomCode',
                        'partsName',
                        'plant',
                        'category',
                        'partsModel',
                        'manufacturer',
                        'serialNumber',
                        'taskListNo',
                        'partsCost',
                        'numberOf',
                        'unit',
                        'summedPartsCost',
                        'location',
                        'partsDeliveryTime',
                        'orderAlert',
                        'orderSituation',
                        'classification',
                        'inventoryTurnover',
                        'partsDescription'
                    ];

                    // テーブルデータの変換と整形
                    const tableData = sparePartsData.flatMap((companyData) =>
                        companyData.sparePartsList.flatMap((partData) => {
                            const rowData = {};
                            index.forEach((key) => {
                                rowData[key] = key === 'partsCost' || key === 'numberOf' || key === 'summedPartsCost' ? parseFloat(partData[key]) || 0 : partData[key];
                                if (key === 'image' && !partData[key]) {
                                    rowData[key] = '';
                                }
                            });
                            // summedPartsCost を初期設定
                            rowData.summedPartsCost = rowData.partsCost * rowData.numberOf;

                            // `price` が 0 より大きく `numberOf` が 0 の場合に `order` を設定
                            if (rowData.partsCost > 0 && rowData.numberOf === 0) {
                                rowData.orderAlert = 'order';
                            }

                            return rowData;
                        })
                    );

                    tableData.sort((a, b) => (parseInt(a.partsNo, 10) || 0) - (parseInt(b.partsNo, 10) || 0));

                    this.sparePartsDataStore = tableData;
                    this.updateRowCount(); // 初回データ取得後に行数を更新
                })
                .catch((error) => {
                    console.error('Error fetching data:', error);
                });
        },

        addRows() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const blankRows = Array.from({ length: this.rowsToAdd }, () => {
                return {
                    companyCode: userCompanyCode,
                    partsNo: '',
                    bomCode: '',
                    partsName: '',
                    plant: '',
                    category: '',
                    partsModel: '',
                    manufacturer: '',
                    serialNumber: '',
                    taskListNo: '',
                    partsCost: 0,
                    numberOf: 0,
                    unit: '',
                    summedPartsCost: 0, // summedPartsCost を初期化
                    location: '',
                    partsDeliveryTime: 0,
                    orderAlert: '',
                    orderSituation: false,
                    classification: '',
                    inventoryTurnover: '',
                    partsDescription: ''
                };
            });

            this.sparePartsDataStore = this.sparePartsDataStore.concat(blankRows);
            this.updateRowCount(); // 新しい行を追加後に行数を更新
        },

        updateRowCount() {
            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const newData = this.sparePartsDataStore.slice(0, this.rowsToShow); // rowsToShowに基づいてデータをスライス

            // データ更新前にバリデーション
            hotInstance.validateCells(() => {
                hotInstance.loadData(newData); // loadDataを使ってデータを設定
            });

            console.log('表示する行数:', this.rowsToShow); // rowsToShowの値を確認するためのログ
        },

        saveData() {
            const userStore = useUserStore();
            const userCompanyCode = userStore.companyCode;

            if (!userCompanyCode) {
                console.error('Error: No company code found for the user.');
                return;
            }

            const hotInstance = this.$refs.hotTableComponent.hotInstance;
            const tableData = hotInstance.getData();

            const formattedData = tableData.map((row) => {
                return {
                    companyCode: userCompanyCode,
                    partsNo: row[1],
                    bomCode: row[2],
                    partsName: row[3],
                    plant: row[4],
                    category: row[5],
                    partsModel: row[6],
                    manufacturer: row[7],
                    serialNumber: row[8],
                    taskListNo: row[9],
                    partsCost: row[10],
                    numberOf: row[11],
                    unit: row[12],
                    summedPartsCost: row[13], // summedPartsCost を追加
                    location: row[14],
                    partsDeliveryTime: row[15],
                    orderAlert: row[16],
                    orderSituation: row[17] !== null ? row[17] : false,
                    classification: row[18],
                    inventoryTurnover: row[19],
                    partsDescription: row[20]
                };
            });

            console.log('送信するデータ:', JSON.stringify(formattedData, null, 2));

            const url = `http://127.0.0.1:8000/api/spareParts/spareParts/`;

            axios
                .post(url, formattedData, {
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    withCredentials: true
                })
                .then((response) => {
                    console.log('Data saved successfully:', response.data);
                    this.alertType = 'success';
                    this.alertMessage = 'データが正常に保存されました。';
                    this.showAlert = true;
                    setTimeout(() => {
                        this.showAlert = false;
                    }, 3000);
                })
                .catch((error) => {
                    console.error('Error saving data:', error);
                    this.alertType = 'error';
                    this.alertMessage = 'データの保存に失敗しました。エラーを確認してください。';
                    this.errorMessages = ['エラーが発生しました。再度試してください。'];
                    this.showAlert = true;
                    setTimeout(() => {
                        this.showAlert = false;
                    }, 5000);
                });
        },
        exportCSV() {
            const headers = [
                'Image',
                'Parts No',
                'BOM Code',
                'Parts Name',
                'Plant',
                'Category',
                'Model',
                'Manufacturer',
                'Serial Number',
                'Task List No',
                'Price',
                'Number of ~',
                'Unit',
                'Summed Parts Cost', // summedPartsCost を追加
                'Location',
                'Delivery Time',
                'Alert order',
                'Order situation',
                'Classification',
                'Inventory Turnover',
                'Description'
            ];

            // CSVデータを配列に変換
            const csvContent = [headers];

            this.sparePartsDataStore.forEach((item) => {
                csvContent.push([
                    item.image,
                    item.partsNo,
                    item.bomCode,
                    item.partsName,
                    item.plant,
                    item.category,
                    item.partsModel,
                    item.manufacturer,
                    item.serialNumber,
                    item.taskListNo,
                    item.partsCost,
                    item.numberOf,
                    item.unit,
                    item.summedPartsCost, // summedPartsCost を追加
                    item.location,
                    item.partsDeliveryTime,
                    item.orderAlert,
                    item.orderSituation,
                    item.classification,
                    item.inventoryTurnover,
                    item.partsDescription
                ]);
            });

            // CSV文字列を作成
            const csvString = csvContent.map((row) => row.join(',')).join('\n');
            const blob = new Blob([csvString], { type: 'text/csv;charset=utf-8;' });

            // ダウンロード用リンクを作成してクリックイベントをトリガー
            const link = document.createElement('a');
            const url = URL.createObjectURL(blob);
            link.href = url;
            link.setAttribute('download', 'spare_parts_list.csv');
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }
    }
});

export default SparePartsComponent;
</script>

<style scoped>
#SparePartsList {
    padding: 20px;
}

.company-code-container {
    display: flex;
    justify-content: flex-end;
    margin-bottom: 10px;
    font-weight: bold;
}

.row-count-container {
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    justify-content: flex-end; /* 右寄せに変更 */
}

.row-count-container span {
    margin-right: 10px;
    font-weight: bold;
}

.button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 20px;
}

.legend {
    margin-bottom: 10px;
    display: flex;
    align-items: center;
}

.legend-item {
    display: flex;
    align-items: center;
    margin-right: 15px;
}

.color-box {
    width: 20px;
    height: 20px;
    margin-right: 10px;
    border: 1px solid #000;
}

.blue-button {
    background-color: #007bff;
    border-color: #007bff;
    color: white;
}

.green-button {
    background-color: #28a745;
    border-color: #28a745;
    color: white;
}
</style>
