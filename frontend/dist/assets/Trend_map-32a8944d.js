import{P as a}from"./plotly.min-539e9c80.js";import{_ as c,o as r,c as s,e as n,V as i,b as l}from"./index-c1603a00.js";const m={mounted(){let e={type:"scattermapbox",mode:"markers",locations:["FRA","DEU","RUS","ESP"],marker:{size:[20,30,15,10],color:[10,20,40,50],cmin:0,cmax:50,colorscale:"Greens",colorbar:{title:"Some rate",ticksuffix:"%",showticksuffix:"last"},line:{color:"black"}},name:"europe data"};const o={mapbox:{style:"light",center:{lat:20}},width:1200,height:600,margin:{l:50,r:50,b:50,t:50,pad:4}},t={mapboxAccessToken:"pk.eyJ1IjoieW9zaGl0YWthNjkiLCJhIjoiY2xyd2hjNmFoMDNwajJrbnU5NWV4ODh2ZiJ9.4QE8gwFBapcj7kO3_gtkNw"};a.newPlot("TRmap",[e],o,t)}},p=l("div",{id:"TRmap"},null,-1);function d(e,o,t,_,k,f){return r(),s("div",null,[n(i),p])}const x=c(m,[["render",d]]);export{x as T};