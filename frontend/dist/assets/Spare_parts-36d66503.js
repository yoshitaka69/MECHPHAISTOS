import{j as b}from"./index-6633d5ff.js";import{_ as l,o as c,c as d,b as t,r as s,e as i,w as r,a as f}from"./index-a4a98369.js";import"./_commonjsHelpers-725317a4.js";const x={name:"sheet",data(){return{VRHeadSets:[["","1","(ex.) Motor","Standard","RX-78-5.7","1234569-9","change motor","900000","1","pieces","warehouse 1","8","when we change No.1 agitator, we have to change this motor too"],["","2","(ex.) agitator","Standard","ag89-78-5.7","1233333-9","replace agitator","180000","4","pieces","warehouse 2","14","This agitator is bad actor,we keep this agitator every time"],["","3","(ex.) pump","Standard","zew99-0045","135455333-9","exchange pump","550000","2","pieces","plantA","60","This pump is needed exchange by operator"]]}},computed:{jSpreadSheetOptins(){return{data:this.VRHeadSets,columns:[{type:"image",title:"Image",width:120},{type:"text",title:"Id",width:50},{type:"text",title:"Name",width:200},{type:"dropdown",title:"Category",width:"130px",source:["Assembly","Standard","consumables","supplies"]},{type:"text",title:"Model",width:150},{type:"text",title:"serial number",width:150},{type:"text",title:"Task name",width:250},{type:"text",title:"Price",width:120,mask:"$ #.##,00",decimal:","},{type:"text",title:"Number of ~",width:100},{type:"text",title:"Unit",width:80},{type:"text",title:"Location",width:150},{type:"text",title:"Delivery time",width:100},{type:"text",title:"Description",width:600}],filters:!0,csvFileName:"BOM",search:!0,toolbar:[{type:"i",content:"undo",onclick:function(){table.undo()}},{type:"i",content:"redo",onclick:function(){table.redo()}},{type:"i",content:"save",onclick:function(){table.download()}},{type:"select",k:"font-family",v:["Arial","Verdana"]},{type:"select",k:"font-size",v:["9px","10px","11px","12px","13px","14px","15px","16px","17px","18px","19px","20px"]},{type:"i",content:"format_align_left",k:"text-align",v:"left"},{type:"i",content:"format_align_center",k:"text-align",v:"center"},{type:"i",content:"format_align_right",k:"text-align",v:"right"},{type:"i",content:"format_bold",k:"font-weight",v:"bold"},{type:"color",content:"format_color_text",k:"color"},{type:"color",content:"format_color_fill",k:"background-color"}]}}},methods:{getHeaders:function(){alert(this.jspreadsheetObj.getHeaders())}},mounted:function(){const o=b(this.$refs.refspreadsheet,this.jSpreadSheetOptins);Object.assign(this,{jspreadsheetObj:o})}},y={class:"wrapper"},v=t("br",null,null,-1),w=t("br",null,null,-1),g={id:"HeadSetSpreadSheet",ref:"refspreadsheet"},S=t("br",null,null,-1),k=t("br",null,null,-1);function $(o,e,p,h,u,n){return c(),d("div",y,[t("input",{type:"button",value:"行を追加",onClick:e[0]||(e[0]=a=>o.jspreadsheetObj.insertRow())}),v,t("input",{type:"button",value:"ヘッダー一覧を取得",onClick:e[1]||(e[1]=a=>n.getHeaders())}),w,t("div",g,null,512),S,t("input",{type:"button",value:"csvをダウンロード",onClick:e[2]||(e[2]=a=>o.jspreadsheetObj.download())}),k])}const j=l(x,[["render",$]]),O={components:{BOM:j}},H={class:"base-content"},T=f('<section class="content-header"><div class="container-fluid"><div class="row mb-2"><div class="col-sm-6"><h1>Spare Parts List</h1></div><div class="col-sm-6"><ol class="breadcrumb float-sm-right"><li class="breadcrumb-item"><a href="#">How to use detail</a></li><li class="breadcrumb-item"><a href="#">Spare parts list</a></li><li class="breadcrumb-item active">MECHPHAISTOS</li></ol></div></div></div></section>',1),V={class:"content"},B={class:"card card-solid"},C={class:"line-height-3 m-0"};function M(o,e,p,h,u,n){const a=s("BOM"),m=s("TabPanel"),_=s("TabView");return c(),d("div",H,[T,t("section",V,[t("div",B,[i(_,null,{default:r(()=>[i(m,{header:"Spare Parts List"},{default:r(()=>[t("p",C,[i(a)])]),_:1})]),_:1})])])])}const R=l(O,[["render",M]]);export{R as default};