import{P as d}from"./plotly.min-539e9c80.js";import{_ as m,r as h,o as f,c as D,e as r,l as c,k as y,q as b,V as x,d as _,b as g}from"./index-c1603a00.js";const M={data(){return{sustainabilityData:[]}},mounted(){(async()=>{try{const s=(await y.get("http://127.0.0.1:8000/api/sustainability/co2/?format=json")).data;for(const o of s){const a=o.Co2.map(t=>({date:t.date,co2:t.co2}));this.sustainabilityData.push({plant:o.plant,co2Data:a})}}catch(e){throw console.error("Error fetching Sustainability data:",e),e}})().then(()=>{const e=this.sustainabilityData.map((a,t)=>{const i=a.co2Data.map(l=>l.date),u=a.co2Data.map(l=>l.co2);return Math.min(...i),Math.max(...i),{type:"scatter",mode:"lines",name:`${a.plant} Co2`,x:i,y:u,line:{color:`#${Math.floor(Math.random()*16777215).toString(16)}`}}}),s=Math.min(...this.sustainabilityData.flatMap(a=>a.co2Data.map(t=>t.date))),o=Math.max(...this.sustainabilityData.flatMap(a=>a.co2Data.map(t=>t.date))),n={xaxis:{autorange:!0,range:[s,o],rangeselector:{buttons:[{count:1,label:"1m",step:"month",stepmode:"backward"},{count:6,label:"6m",step:"month",stepmode:"backward"},{step:"all"}]},rangeslider:{range:[s,o]},type:"date"},yaxis:{autorange:!0,range:[Math.min(...this.sustainabilityData.flatMap(a=>a.co2Data.map(t=>t.co2))),Math.max(...this.sustainabilityData.flatMap(a=>a.co2Data.map(t=>t.co2)))],type:"linear"}};d.newPlot("co2",e,n)})}},V=g("div",{id:"co2"},null,-1);function C(p,e,s,o,n,a){const t=h("v-flex");return f(),D("div",null,[r(t,null,{default:c(()=>[r(b,null,{default:c(()=>[r(x,null,{default:c(()=>[_("Co2 trend")]),_:1}),V]),_:1})]),_:1})])}const k=m(M,[["render",C]]);export{k as default};