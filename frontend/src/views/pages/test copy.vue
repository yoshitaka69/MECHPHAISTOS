<template>
    <div>
        Safety correlation diagram
        <div id="scd"></div>
    </div>
</template>

<script>
import Plotly from 'plotly.js-dist-min';
import axios from 'axios';
import { useUserStore } from '@/stores/userStore'; // Pinia ストアをインポート
import { useLayout } from '@/layout/composables/layout';
import { ref, watch } from 'vue'; // refをインポートする

export default {
    data() {
        return {
            isSidebarOpen: false, // サイドバーの開閉状態
            plotInitialized: false, // グラフ初期化フラグ
            plotData: null, // グラフのデータ
            plotLayout: null // グラフのレイアウト
        };
    },

    mounted() {
        const userStore = useUserStore();
        const userCompanyCode = userStore.companyCode;

        if (!userCompanyCode) {
            console.error('Error: No company code found for the user.');
            return; // companyCodeがない場合、処理を中断
        }

        const url = `http://127.0.0.1:8000/api/nearMiss/nearMissByCompany/?companyCode=${userCompanyCode}`;

        axios
            .get(url)
            .then((response) => {
                const nearMissData = response.data;
                let rows = [];

                // nearMissData の全ての要素（各会社）をループ処理
                for (const companyData of nearMissData) {
                    // 各会社の nearMissList をループ処理
                    for (const nearMiss of companyData.nearMissList) {
                        // ここで nearMiss の各データを rows に追加
                        rows.push(nearMiss);
                    }
                }

                // グラフデータとレイアウトを作成
                const departmentMap = {};
                const departmentValues = rows.map((item) => {
                    if (!(item.department in departmentMap)) {
                        departmentMap[item.department] = Object.keys(departmentMap).length + 1;
                    }
                    return departmentMap[item.department];
                });

                // whereの各要素に番号を振り、順序を保持する
                const placeOfOccurrenceMap = {};
                const placeOfOccurrenceValues = rows.map((item) => {
                    if (!(item.placeOfOccurrence in placeOfOccurrenceMap)) {
                        placeOfOccurrenceMap[item.placeOfOccurrence] = Object.keys(placeOfOccurrenceMap).length + 1;
                    }
                    return placeOfOccurrenceMap[item.placeOfOccurrence];
                });

                const maxDepartmentValue = Object.keys(departmentMap).length;
                const maxPlaceOfOccurrenceValue = Object.keys(placeOfOccurrenceMap).length;

                const levelMap1 = { A: 5, B: 4, C: 3, D: 2, E: 1 };
                const levelMap2 = {
                    others: 1,
                    'protective equipment violation': 2,
                    'impossible movement': 3,
                    'traffic accIdent': 4,
                    conflagration: 5,
                    rupture: 6,
                    explosion: 7,
                    'electric shock': 8,
                    'contact with organic matter': 9,
                    'contact with hot or cold objects': 10,
                    drown: 11,
                    'treading on something sharp': 12,
                    'cut/Rubbing': 13,
                    'got caught up in': 14,
                    'hit by something': 15,
                    collapse: 16,
                    'accIdental fall': 17,
                    collision: 18,
                    'fall/slip': 19,
                    'fall down': 20
                };
                const levelMap3 = { others: 1, Rule: 2, Person: 3, Methods: 4, Equipment: 5 };

                let typeOfAccidentValues = [];
                let factorValues = [];
                let injuredLvValues = [];
                let equipmentDamageLvValues = [];
                let affectOfEnviromentValues = [];
                let newsCoverageValues = [];
                let measuresValues = [];

                // Extracting values for each dimension
                rows.forEach((item) => {
                    typeOfAccidentValues.push(levelMap2[item.typeOfAccident]);
                    factorValues.push(levelMap3[item.factor]);
                    injuredLvValues.push(levelMap1[item.injuredLv]);
                    equipmentDamageLvValues.push(levelMap1[item.equipmentDamageLv]);
                    affectOfEnviromentValues.push(levelMap1[item.affectOfEnviroment]);
                    newsCoverageValues.push(levelMap1[item.newsCoverage]);
                    measuresValues.push(levelMap1[item.measures]);
                });

                console.log('departmentValues:', departmentValues);
                console.log('placeOfOccurrenceValues:', placeOfOccurrenceValues);
                console.log('accidentTypeValues:', typeOfAccidentValues);
                console.log('factorValues:', factorValues);
                console.log('injuredLvValues:', injuredLvValues);
                console.log('equipmentDamageLvValues:', equipmentDamageLvValues);
                console.log('affectOfEnviromentValues:', affectOfEnviromentValues);
                console.log('newsCoverageValues:', newsCoverageValues);
                console.log('measuresValues:', measuresValues);

                this.plotData = {
                    type: 'parcoords',
                    line: {
                        color: 'blue'
                    },
                    dimensions: [
                        {
                            range: [1, maxDepartmentValue],
                            label: 'Department',
                            values: departmentValues,
                            tickvals: Array.from({ length: departmentValues.length }, (_, index) => index + 1),
                            ticktext: Object.keys(departmentMap)
                        },
                        {
                            range: [1, maxPlaceOfOccurrenceValue],
                            label: 'Where',
                            values: placeOfOccurrenceValues,
                            tickvals: Array.from({ length: placeOfOccurrenceValues.length }, (_, index) => index + 1),
                            ticktext: Object.keys(placeOfOccurrenceMap)
                        },
                        {
                            range: [1, 20],
                            label: 'Accident type',
                            values: typeOfAccidentValues,
                            tickvals: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
                            ticktext: [
                                'others',
                                'protective equipment violation',
                                'impossible movement',
                                'traffic accIdent',
                                'conflagration',
                                'rupture',
                                'explosion',
                                'electric shock',
                                'contact with organic matter',
                                'contact with hot or cold objects',
                                'drown',
                                'treading on something sharp',
                                'cut/Rubbing',
                                'got caught up in',
                                'hit by something',
                                'collapse',
                                'accIdental fall',
                                'collision',
                                'fall/slip',
                                'fall down'
                            ]
                        },
                        {
                            range: [1, 5],
                            label: 'Factor',
                            values: factorValues,
                            tickvals: [1, 2, 3, 4, 5],
                            ticktext: ['others', 'Rule', 'Person', 'Methods', 'Equipment']
                        },
                        {
                            range: [1, 5],
                            label: 'injured Lv',
                            values: injuredLvValues,
                            tickvals: [1, 2, 3, 4, 5],
                            ticktext: ['E', 'D', 'C', 'B', 'A']
                        },
                        {
                            range: [1, 5],
                            label: 'Equipment Damage Lv',
                            values: equipmentDamageLvValues,
                            tickvals: [1, 2, 3, 4, 5],
                            ticktext: ['E', 'D', 'C', 'B', 'A']
                        },
                        {
                            range: [1, 5],
                            label: 'Affect Of Enviroment',
                            values: affectOfEnviromentValues,
                            tickvals: [1, 2, 3, 4, 5],
                            ticktext: ['E', 'D', 'C', 'B', 'A']
                        },
                        {
                            range: [1, 5],
                            label: 'News Coverage',
                            values: newsCoverageValues,
                            tickvals: [1, 2, 3, 4, 5],
                            ticktext: ['E', 'D', 'C', 'B', 'A']
                        },
                        {
                            range: [1, 5],
                            label: 'Measures',
                            values: measuresValues,
                            tickvals: [1, 2, 3, 4, 5],
                            ticktext: ['E', 'D', 'C', 'B', 'A']
                        }
                    ]
                };

                this.plotLayout = {
                    width: 1000,
                    // グラフのレイアウト
                };

                // 初期化が完了したのでフラグを設定
                this.plotInitialized = true;

// サイドバーの開閉状態が変更されたときに、グラフをリサイズする
watch(() => useLayout().isSidebarActive, (newVal) => {
  if (this.plotInitialized) {
    if (newVal) {
      Plotly.Plots.resize('scd');
    }
  }
});
})
.catch((error) => {
console.error('データの取得に失敗しました', error);
});
}
};
</script>
