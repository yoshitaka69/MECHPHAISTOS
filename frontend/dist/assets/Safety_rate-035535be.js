import{P as s}from"./plotly.min-4d357279.js";import{_ as i,r as c,o as d,c as u,e,w as t,V as g,f as _,d as f,b as p}from"./index-a4a98369.js";const x={mounted(){let a={type:"indicator",mode:"number+gauge+delta",value:180,delta:{reference:200},domain:{x:[.25,1],y:[.08,.25]},title:{text:"Revenue"},gauge:{shape:"bullet",axis:{range:[null,300]},threshold:{line:{color:"black",width:2},thickness:.75,value:170},steps:[{range:[0,150],color:"gray"},{range:[150,250],color:"lightgray"}],bar:{color:"black"}}},l={type:"indicator",mode:"number+gauge+delta",value:35,delta:{reference:200},domain:{x:[.25,1],y:[.4,.6]},title:{text:"Profit"},gauge:{shape:"bullet",axis:{range:[null,100]},threshold:{line:{color:"black",width:2},thickness:.75,value:50},steps:[{range:[0,25],color:"gray"},{range:[25,75],color:"lightgray"}],bar:{color:"black"}}},o={type:"indicator",mode:"number+gauge+delta",value:220,delta:{reference:200},domain:{x:[.25,1],y:[.7,.9]},title:{text:"Satisfaction"},gauge:{shape:"bullet",axis:{range:[null,300]},threshold:{line:{color:"black",width:2},thickness:.75,value:210},steps:[{range:[0,150],color:"gray"},{range:[150,250],color:"lightgray"}],bar:{color:"black"}}};const n={width:600,height:250,margin:{t:10,r:25,l:25,b:10}};s.newPlot("ind",[a,l,o],n)}},b=p("div",{id:"ind"},null,-1);function y(a,l,o,n,h,m){const r=c("v-flex");return d(),u("div",null,[e(r,null,{default:t(()=>[e(g,null,{default:t(()=>[e(_,null,{default:t(()=>[f("Indicator")]),_:1}),b]),_:1})]),_:1})])}const C=i(x,[["render",y]]),v={mounted(){let a={type:"pie",values:[2,3,4,4],labels:["Wages","Operating expenses","Cost of sales","Insurance"],textinfo:"label+percent",insidetextorientation:"radial"};const l={height:700,width:700};s.newPlot("Rate",[a],l)}},k=p("div",{id:"Rate"},null,-1);function $(a,l,o,n,h,m){const r=c("v-flex");return d(),u("div",null,[e(r,null,{default:t(()=>[e(g,null,{default:t(()=>[e(_,null,{default:t(()=>[f("Safety factor")]),_:1}),k]),_:1})]),_:1})])}const P=i(v,[["render",$]]);export{C as S,P as a};