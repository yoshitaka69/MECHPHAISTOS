import{m as F,_ as m,r as d,o as b,c as y,e as i,b as e,n as M,k as C,l as h,V as $,d as w,q as R,p as I,j as A,a as P}from"./index-c1603a00.js";import{H,a as _}from"./handsontable.full-0e1d021e.js";import{P as g}from"./plotly.min-539e9c80.js";F();function N(a,t,s,r,n,o,l){_.renderers.TextRenderer.apply(this,arguments),r===14&&(o==="High+"?(t.style.backgroundColor="#FF0000",t.style.color="black"):o==="High"?(t.style.backgroundColor="#FFC000",t.style.color="black"):o==="Low"&&(t.style.backgroundColor="#00B050",t.style.color="black"))}function T(a,t,s,r,n,o,l){if(_.renderers.TextRenderer.apply(this,arguments),r===15)switch(o){case"要対策":t.style.backgroundColor="#FF0000",t.style.color="black";break;case"対策検討":t.style.backgroundColor="#FFC000",t.style.color="black";break;case"適切":t.style.backgroundColor="#92D050",t.style.color="black";break;case"見直検討":t.style.backgroundColor="#00B050",t.style.color="black";break}}function L(a,t,s,r,n,o,l){switch(_.renderers.TextRenderer.apply(this,arguments),o){case"対策済":t.style.backgroundColor="#92D050",t.style.color="black";break;case"見直検討":t.style.backgroundColor="#00B050",t.style.color="black";break;case"保全タスク":t.style.backgroundColor="#FFFF00",t.style.color="black";break}const c=15,p=a.getDataAtCell(s,c),f=14,u=a.getDataAtCell(s,f);o==="対策済"||o==="見直検討"||o==="保全タスク"||(u==="High+"||p==="要対策"?(t.style.backgroundColor="#FF0000",t.style.color="black"):(u==="High"||p==="対策検討")&&(t.style.backgroundColor="#FFC000",t.style.color="black"))}function E(a,t,s,r,n,o,l){_.renderers.TextRenderer.apply(this,arguments),o==="遅延"&&(t.style.backgroundColor="#FFFF00",t.style.color="black")}function D(a,t,s,r,n,o,l){_.renderers.TextRenderer.apply(this,arguments);const c=4,p=5,f=a.getDataAtCell(s,c),u=a.getDataAtCell(s,p),v=Math.max(f,u);t.innerHTML=v===0?"":v}const S=M({data(){return{hotSettings:{data:[["PlantA","モーターA","N401/A plant__","4","10","6","10","4","今年","2022-10-02","3","2019-11-01","0","","High+","","対策済","A plant/変換器室 変換器盤1-3パワーサプライ交換","10000","3","2025","","Standard","","","","",""],["PlantA","モーターA","N401/A plant__/OX2_","3","10","6","10","4","","","4","2018-08-10","","","High","対策検討","","","750000","3","","遅延","","","","","",""],["PlantB","Attach系機械設備","N401/A plant__/OX2_/A","3","10","6","10","今年","2","2022-05-20","0","","","","","注意","","A plant/Di槽撹拌機交換（A）","5000","","","","","","","","",""],["PlantC","回収温水熱交","N401/A plant__/OX2_/A/5E-09","3","10","60","10","4","","","","","","","Low","見直検討","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""],["","","","","","","","","","","","","","","","","","","","","","","","","","","",""]],nestedHeaders:[["","","",{label:"Impact",colspan:5},{label:"Probability of failure",colspan:6},{label:"Critical equipment Level",colspan:3},"","","","","",{label:"Spare parts",colspan:2},{label:"Status of measures",colspan:4},{label:"Order",colspan:2}],["Plant","Equipment","Function","Level set <br>value","Construction <br>period","Parts <br>delivery date","MTTR","Possibility of <br>production Lv","Count <br>of PM02","Latest <br>PM02","Count <br>of PM03","Latest <br>PM03","Count <br>of PM04","Latest <br>PM04","Impact for <br>production","Probability <br>of failure","Assessment","Task of PM02","Labor <br>Cost(PM02)","Period","Next <br>event year","situation","Category","Stock","RCA or <br>Replace(hard)","Spear parts or <br>Alternative(soft)","Covered <br>from task","Two <br>ways"]],columns:[{type:"text"},{type:"text"},{type:"text"},{type:"numeric"},{type:"numeric"},{type:"numeric"},{type:"numeric",renderer:D},{type:"numeric",className:"htRight",readOnly:!0},{width:100,className:"htRight",type:"numeric"},{width:100,className:"htRight",type:"date",dateFormat:"YYYY-MM-DD",correctFormat:!1},{width:100,className:"htRight",type:"numeric"},{width:100,className:"htRight",type:"date",dateFormat:"YYYY-MM-DD",correctFormat:!1},{width:100,className:"htRight",type:"numeric"},{width:100,className:"htRight",type:"date",dateFormat:"YYYY-MM-DD",correctFormat:!1},{renderer:N,width:100,className:"htCenter",readOnly:!0},{renderer:T,width:100,className:"htCenter",readOnly:!0},{renderer:L,readOnly:!0,width:100,className:"htCenter"},{type:"text"},{type:"numeric"},{type:"numeric"},{className:"htRight",type:"date",dateFormat:"YYYY-MM-DD",correctFormat:!1},{className:"htCenter",renderer:E},{className:"htRight",type:"dropdown",source:["Standard","Inventory","consumables"]},{type:"dropdown",source:["有","無"],className:"htCenter"},{width:100,className:"htCenter",type:"checkbox"},{width:100,className:"htCenter",type:"checkbox"},{width:100,className:"htCenter",type:"checkbox"},{width:100,className:"htCenter",type:"checkbox"}],width:"100%",height:"auto",stretchH:"all",contextMenu:!0,autoWrapRow:!0,autoWrapCol:!0,fixedColumnsStart:2,fixedRowsTop:2,manualColumnFreeze:!0,manualColumnResize:!0,manualRowResize:!0,filters:!0,dropdownMenu:!0,comments:!0,fillHandle:{autoInsertRow:!0},licenseKey:"non-commercial-and-evaluation"}}},methods:{updateData:function(){const a=this.$refs.hotTableComponent.hotInstance.getData(),t="http://127.0.0.1:8000/api/v1/ceList/";C.post(t,a).then(s=>{console.log(s.data)}).catch(s=>{console.error(s)})}},components:{HotTable:H}}),q=S,O={id:"CeList"},V=e("br",null,null,-1);function Y(a,t,s,r,n,o){const l=d("hot-table");return b(),y("div",O,[i(l,{ref:"hotTableComponent",settings:a.hotSettings},null,8,["settings"]),V,e("button",{onClick:t[0]||(t[0]=(...c)=>a.updateData&&a.updateData(...c)),class:"controls"},"Update Data")])}const B=m(q,[["render",Y]]),z={data(){return{values:{},error:null}},mounted(){C.get("http://127.0.0.1:8000/api/v1/ceList/").then(a=>{const t=a.data.map(o=>o.assessment);console.log("typeArray:",t),this.values=t.reduce((o,l)=>(o[l]=(o[l]||0)+1,o),{});let s={type:"pie",values:Object.values(this.values),labels:Object.keys(this.values),textinfo:"label+percent",insidetextorientation:"radial"};const r={height:400,width:400,automargin:!0},n={responsive:!0};document.getElementById("AssessmentRate")?(console.log("Before plotting"),g.newPlot("AssessmentRate",[s],r,n),console.log("After plotting")):console.error("Element with id 'AssessmentRate' not found.")}).catch(a=>{console.error("Error fetching data:",a)})}},j=e("div",{id:"AssessmentRate"},null,-1);function K(a,t,s,r,n,o){return b(),y("div",null,[i(R,null,{default:h(()=>[i($,null,{default:h(()=>[w("Assessment rate")]),_:1}),j]),_:1})])}const U=m(z,[["render",K]]);const W={mounted(){try{{const s=this.$el.querySelector("#rMatrix tbody td[s='3']").cellIndex,r=this.$el.querySelector("#rMatrix tbody tr[lh='3']").cells[s];r.style.border="3px solid",r.style.boxShadow="-5px 5px 20px 20px rgba(14, 1, 1, 0.17), -15px -11px 20px 5px rgba(14, 14, 14, 0.22)",r.style.borderStyle="dashed"}}catch(s){console.error(s)}}},k=a=>(I("data-v-271621f1"),a=a(),A(),a),X={class:"table table-bordered table-responsive",id:"rMatrix"},G=k(()=>e("thead",null,[e("tr",null,[e("th"),e("th",{colspan:"2"},"STATUS OF EVENT"),e("th",{colspan:"5"},"RISK CLASS")])],-1)),J=k(()=>e("tbody",null,[e("tr",{lh:"5"},[e("td",{rowspan:"5",class:"r-header",style:{"text-align":"center"}},"LIKELIHOOD OF EVENT HAPPENING"),e("td",{style:{"min-width":"50px"}},"5"),e("td",null,"It is or has already happened"),e("td",{class:"M"},"M"),e("td",{class:"H"},"H"),e("td",{class:"H"},"H"),e("td",{class:"VH"},"VH"),e("td",{class:"VH"},"VH")]),e("tr",{lh:"4"},[e("td",null,"4"),e("td",null,"It will probably happen"),e("td",{class:"M"},"M"),e("td",{class:"M"},"M"),e("td",{class:"H"},"H"),e("td",{class:"VH"},"VH"),e("td",{class:"VH"},"VH")]),e("tr",{lh:"3"},[e("td",null,"3"),e("td",null,"It could possibly Happen"),e("td",{class:"L"},"L"),e("td",{class:"M"},"M"),e("td",{class:"M"},"M"),e("td",{class:"H"},"H"),e("td",{class:"H"},"H")]),e("tr",{lh:"2"},[e("td",null,"2"),e("td",null,"It is to Happen"),e("td",{class:"L"},"L"),e("td",{class:"L"},"L"),e("td",{class:"M"},"M"),e("td",{class:"M"},"M"),e("td",{class:"H"},"H")]),e("tr",{lh:"1"},[e("td",null,"1"),e("td",null,"It is unlikely to Happen"),e("td",{class:"L"},"L"),e("td",{class:"L"},"L"),e("td",{class:"L"},"L"),e("td",{class:"M"},"M"),e("td",{class:"M"},"M")]),e("tr",null,[e("td",{rowspan:"3",class:"r-header"},"LIKELY OUTCOME OF EVENT"),e("td",{colspan:"2",class:"r-header"},"SAFETY"),e("td",null,"Near Miss"),e("td",null,"Minor Inquiry"),e("td",null,"Lost Time Accident"),e("td",null,"Major Inquiry"),e("td",null,"Fatality")]),e("tr",null,[e("td",{colspan:"2",class:"r-header"},"ENVIRONMENT"),e("td",null,"Potential Event"),e("td",null,"Minor Event"),e("td",null,"Important Event"),e("td",null,"Significant Event"),e("td",null,"Major Event")]),e("tr",null,[e("td",{colspan:"2",class:"r-header"},"COST"),e("td",null,"< 1k $ "),e("td",null,"< 10k $ "),e("td",null,"< 100k $ "),e("td",null,"< 300k $ "),e("td",null,"> 500k $")]),e("tr",null,[e("td"),e("td",{colspan:"2",class:"r-header"},"SEVERITY"),e("td",{s:"1"},"1"),e("td",{s:"2"},"2"),e("td",{s:"3"},"3"),e("td",{s:"4"},"4"),e("td",{s:"5"},"5")])],-1)),Q=[G,J];function Z(a,t,s,r,n,o){return b(),y("table",X,Q)}const ee=m(W,[["render",Z],["__scopeId","data-v-271621f1"]]),te={mounted(){let a=[["・Recovery possible by operator・Replacement device or easy recovery possible・Equipment is divided into two lines, making recovery easy.Spare parts are on hand and restoration is easily possible with WI"],["・Recovery within 1 day・Recovery by operator is not possible・Restoration by knowledgeable and professional contractors.Spare parts and replacement machines available・Parts delivery time for restoration is within 3 days"],["・Recovery within 1 to 3 days・Recovery by operator is not possible・Restoration by knowledgeable and professional contractors.No spare parts or replacement equipment available・The parts delivery time required for restoration is between 1 and 3 days."],["・Recovery within 3 to 14 days・Manufacturing by changing manufacturing conditions such as single-lung operation・Irregular operations by operators occur after provisional recovery・Special parts are required and the parts delivery time is 3 days or more."],["・Due to severe equipment damage, recovery with replacement equipment is not possible.・Individual response is required after coordinating with each department"]],t="grey",s="lightgrey",r="white",n={type:"table",columnwidth:[400,400,400,400,400],header:{values:[["<b>1 - Operator recovery possible</b>"],["<b>2 - Spare parts and replacement machines are available, allowing for quick recovery.</b>"],["<b>3 - Recovery that requires specialized contractors and involves irregularities</b>"],["<b>4 - Temporary recovery in situations where production schedule or quality is affected</b>"],["<b>5 - Recovery not possible</b>"]],align:"center",line:{width:1,color:"black"},fill:{color:t},font:{family:"Arial",size:12,color:"white"}},cells:{values:a,align:["center"],fill:{color:[r,s,r,s,r]},font:{family:"Arial",size:12,color:["black"]}}};const o={title:"Definition of impact for production",height:500,width:780,margin:{t:40,r:10,b:0,l:10},displayModeBar:!1,displaylogo:!1},l={responsive:!0};g.newPlot("LvDescriptionImpact",[n],o,l)}},ae=e("div",{id:"LvDescriptionImpact",style:{width:"800px"}},null,-1),se=[ae];function oe(a,t,s,r,n,o){return b(),y("div",null,se)}const re=m(te,[["render",oe]]),ne={mounted(){let a=[["・No failures have occurred in the past 5 years.・Equipment operating rate is low, and the possibility of failure occurring in the future is low."],["・Failures have occurred less than twice in the past five years.・Preventive maintenance has been performed in the past five years.・Countermeasures for past problems have been implemented through RCA, etc., and are showing sufficient effectiveness.Managed by preventive maintenance tasks, with regular maintenance observations and actions taken."],["・Failures have occurred 2 or more times but less than 3 times in the past 5 years.・It is managed by preventive maintenance tasks, and early abnormalities can be detected.・Countermeasures for past problems have been implemented through RCA, etc., and are showing sufficient effectiveness.・PM has not been implemented for a long time."],["・Failures have occurred 2 or more times but less than 3 times in the past 5 years.Although managed by preventive maintenance tasks, a certain number of failures occur.Countermeasures for past problems caused by RCA, etc. have not been implemented, or their effects have not been sufficiently effective.・The cause of the trouble is clear and its occurrence can be predicted."],["- Failures have occurred three or more times during repairs over the past five years.Not managed by preventive maintenance tasks, and initial abnormalities are not noticed.Countermeasures for past problems have not been implemented or their effects have not been sufficiently effective.The cause of the problem is not clear."]],t="lightgrey",s="white",r={type:"table",columnwidth:[400,400,400,400,400],header:{values:[["<b>1 - Extremely rare</b>"],["<b>2 - Rare</b>"],["<b>3 - Occasionally</b>"],["<b>4 - Often</b>"],["<b>5 - Frequently</b>"]],align:"center",line:{width:1,color:"black"},fill:{color:["#00B050","#92D050","#FFFF00","#FFC000","#FF0000"]},font:{family:"Arial",size:12,color:"black"}},cells:{values:a,align:["center"],fill:{color:[s,t,s,t,s]},font:{family:"Arial",size:12,color:["black"]}}};const n={title:"Definition of probability of failure",height:500,width:780,margin:{t:40,r:10,b:0,l:10},displayModeBar:!1,displaylogo:!1},o={responsive:!0};g.newPlot("LvDescriptionFailure",[r],n,o)}},le=e("div",{id:"LvDescriptionFailure",style:{width:"800px"}},null,-1),ie=[le];function ce(a,t,s,r,n,o){return b(),y("div",null,ie)}const de=m(ne,[["render",ce]]),pe={components:{Critical_equipment_list:B,Assessment_rate:U,Risk_matrix:ee,Impact_for_production:re,Probability_of_failure:de}},ue={class:"base-content"},he=P('<section class="content-header"><div class="container-fluid"><div class="row mb-2"><div class="col-sm-6"><h1>Critical Equipment List</h1></div><div class="col-sm-6"><ol class="breadcrumb float-sm-right"><li class="breadcrumb-item"><a href="#">How to use detail</a></li><li class="breadcrumb-item"><a href="#">Spare parts list</a></li><li class="breadcrumb-item active">MECHPHAISTOS</li></ol></div></div></div></section>',1),me={class:"content"},be={class:"card card-solid"},ye={class:"line-height-3 m-0"},fe=e("br",null,null,-1),_e=e("br",null,null,-1),ve={class:"row"},ge=e("div",{class:"col-12 xl:col-8"},[e("div",{class:"card",style:{"background-color":"#f2f2f2"}})],-1),Ce={class:"col-12 xl:col-4"},we={class:"card",style:{"background-color":"#f2f2f2"}},ke={class:"line-height-3 m-0"};function xe(a,t,s,r,n,o){const l=d("Critical_equipment_list",!0),c=d("TabPanel"),p=d("Assessment_rate"),f=d("Risk_matrix"),u=d("Impact_for_production"),v=d("Probability_of_failure"),x=d("TabView");return b(),y("div",ue,[he,e("section",me,[e("div",be,[i(x,null,{default:h(()=>[i(c,{header:"Critical equipment list"},{default:h(()=>[e("p",ye,[w(" Critical Equipment List. This data is sample. "),fe,_e,i(l)])]),_:1}),i(c,{header:"Priority Tasks"},{default:h(()=>[e("div",ve,[ge,e("div",Ce,[e("div",we,[i(p)])])])]),_:1}),i(c,{header:"Risk-Matrix"},{default:h(()=>[e("p",ke,[i(f)]),i(u),i(v)]),_:1})]),_:1})])])])}const Re=m(pe,[["render",xe]]);export{Re as default};