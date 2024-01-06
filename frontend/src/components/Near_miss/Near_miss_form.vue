<template>
    <!--参考記事　https://qiita.com/naganagu/items/1e011819212c3ec6051f-->
  <v-container>
    <v-row justify="center">
      <v-col cols="10">
        <v-card>
          <v-card-title>Near miss form</v-card-title>
          <v-card-text>
            <v-row>
              <v-col cols="2">
                <v-subheader>代表者</v-subheader>
              </v-col>
              <v-col cols="5">
                <v-text-field
                  label="名前"
                  v-model="repName"
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  label="年齢"
                  v-model="repAge"
                  suffix="歳"
                ></v-text-field>
              </v-col>
            </v-row>
        
            <v-row>
              <v-col cols="2">
                <v-subheader>電話番号</v-subheader>
              </v-col>
              <v-col cols="8">
                <v-text-field
                  label="電話番号"
                  v-model="tel"
                ></v-text-field>
              </v-col>
            </v-row>
        
            <v-row>
              <v-col cols="2">
                <v-subheader>メールアドレス</v-subheader>
              </v-col>
              <v-col cols="8">
                <v-text-field
                  label="メールアドレス"
                  v-model="mail"
                ></v-text-field>
              </v-col>
            </v-row>
        
            <v-row v-if="memberList.length == 0">
              <v-col cols="2">
                <v-subheader>同行者</v-subheader>
              </v-col>
              <v-col cols="8">
                同行者なし
              </v-col>
              <v-col cols="2">
                <v-btn 
                  dark 
                  small 
                  color="grey" 
                  class="ma-2" 
                  @click="addInput(0)"
                >
                  <v-icon dark>mdi-plus</v-icon>
                </v-btn>
              </v-col>
            </v-row>

            <v-row v-for="member in memberList" :key="member.id">
              <v-col cols="2">
                <v-subheader>同行者 {{member.id + 1}}人目</v-subheader>
              </v-col>
              <v-col cols="5">
                <v-text-field
                  label="名前"
                  v-model="member.name"
                ></v-text-field>
              </v-col>
              <v-col cols="3">
                <v-text-field
                  label="年齢"
                  v-model="member.age"
                  suffix="歳"
                ></v-text-field>
              </v-col>
              <v-col cols="2">
                <v-btn 
                  dark 
                  small 
                  color="grey" 
                  class="ma-2" 
                  @click="addInput(member.id)"
                  v-if="memberList.length < 4"
                >
                  <v-icon dark>mdi-plus</v-icon>
                </v-btn>
                <v-btn 
                  dark 
                  small 
                  color="grey" 
                  class="ma-2" 
                  @click="removeInput(member.id)"
                >
                  <v-icon dark>mdi-minus</v-icon>
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue"
              dark
            >
              登録
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: 'Sample',
    data: () => ({
      repName: "田中太郎",
      repAge: 25,
      tel: "000-0000-0000",
      mail: "example@gmail.com",
      memberList: [{id: 0, name: "", age: null}]
    }),

    methods: {
      // 入力欄追加
      addInput (id) {
        let inputList = this.memberList;
        inputList.splice(id+1, 0, {id: null, name: "", age: null});
        this.memberList = this.makeNewInput(inputList);
      },

      // 入力欄削除
      removeInput (id) {
        let inputList = this.memberList;
        inputList = inputList.filter((input) => { return input.id !== id;});
        this.memberList = this.makeNewInput(inputList);
      },

      // ID振り直し
      makeNewInput (inputList) {
        let newInputList = [];
        for (let i = 0; i < inputList.length; i++) {
          newInputList.push ({
            id: i,
            name: inputList[i].name,
            age: inputList[i].age
          });
        }
        return newInputList;
      }
    }
  }
</script>