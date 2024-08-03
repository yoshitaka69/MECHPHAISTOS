<template>
    <section class="content">
      <div class="card card-solid">
        <TabView v-model:activeIndex="activeIndex" @tab-change="onTabChange">
          <TabPanel header="What's MECHPHAISTOS">
            <h1>MECHPHAISTOS optimizes your maintenance task</h1>
            <p class="text">
              MECHPHAISTOS provides powerful support for managing many complicated tasks.
              <br />
              Maintenance working is in a trade-off between money and maintenance task. We cannot stop
              production due to machine trouble, so we plant a machine maintenance as preventive
              maintenance.
              <br />
              However, they may be over-maintained and are not kind to management. Additionally, it is
              not easy to determine whether those maintenance tasks were necessary.
              <br />
              MECHPHAISTOS has three factors to help your determination: Critical Equipment, Repairing Cost,
              Maintenance Task. Then MECHPHAISTOS provides a good maintenance plan to yours.
              <br />
              All you need is a list of machines in your factory, maintenance records, and a
              willingness to try out this tool.
            </p>
            <figure class="desc-ternary">
              <img src="@/assets/newplot.jpg" alt="MECHPHAISTOSの概念" />
            </figure>
            <p class="des-text">
              Of course, by continuously inputting current values and digital signals from equipment,
              it becomes a tool with higher possibilities, but I would like you to use it as a
              stepping stone for cost-saving DX.
            </p>
          </TabPanel>
          <TabPanel header="About us">
            <h1>Hello, I'm Yoshitaka Noto.<br /> I developed MECHPHAISTOS.</h1>
            <figure class="self-intro">
              <img src="@/assets/self_photo.png" class="self-photo" alt="自分の写真" />
            </figure>
            <p class="text">
              I have been doing plant maintenance as a mechanical engineer for over 10 years.
              <br />
              I studied fluid mechanics (cavitation) at university, and as a researcher I studied image analysis technology for high-speed fluids.
              <br />
              Since graduating from university, I have been involved in plant maintenance in areas such as architecture, air conditioning, electricity, machinery, automation, safety, and law, without focusing on one field.
              <br />
              So, I learned that this maintenance work is very tough work and is important for the plant.
              <br />
              I also hope that this tool will be a good one for people involved in plant maintenance like me.
              <br />
            </p>
            <p class="right-align">Thank you, Y.noto</p>
          </TabPanel>
          <TabPanel header="For Who ?">
            <h1>MECHPHAISTOS for all maintenance workers.</h1>
            <figure class="for-who-photo">
              <img src="@/assets/for_who.jpg" class="for-who-photo" />
            </figure>
            <p class="for-who-text">
              I made this tool to help maintenance workers.
              <br />
              Of course, I know that maintenance work is very important, but it's difficult to convey to those around you the importance of their work and the difficulty of their work.
              <br />
              This is because their technology is so wonderfully specific that it is difficult for those around them to understand it.
              <br />
              We created this tool not only to make their work more efficient, but also to emphasize the importance of their work.
              <br />
              And more I hope that this tool will be a community for maintenance workers such as machinery engineers, electricians, programmers.
            </p>
          </TabPanel>
          <TabPanel header="Message">
            <h1>The status of us engineers should be a little higher.</h1>
            <figure class="maintenance-worker">
              <img src="@/assets/engineer.jpg" class="maintenance-worker" />
            </figure>
            <p class="message-text">
              I think that all engineers should be evaluated. Our brain and experience are great and special.
              <br />
              However, our situation is not good. Moreover, AI will help our work and rib too. Our situation will change to the next stage we have never experienced. And our result was not simple and a little bit like a black box.
              <br />
              So I made this tool for all engineers to be able to appeal more. Use this tool for your maintenance work.
            </p>
          </TabPanel>
          <TabPanel header="Features">
            <h1>Risk-Matrix and SNS collaborate</h1>
            <p class="features-text">
              MECHPHAISTOS doesn't need to install some inspection sensor such as ammeter, pressure gauge, flowmeter, thermocouple...etc.
              <br />
              Of course, the digital signals from them are essential for understanding the condition of the equipment.
              <br />
              However, installing these sensors is also expensive. Additionally, as I'm sure maintenance workers will understand, you may or may not be able to see the signs from those sensors. For example, even if the current value is monitored every day, the current value may suddenly become high in some equipment, and the machine may stop a few seconds later.
              <br />
              So what I'm saying is that monitoring the condition of equipment with digital signals is reliable in many cases, but not for all machines. Also, the initial cost is high. Under such circumstances, MECHPHAISTOS evaluates the past maintenance records and the importance of the equipment from a list matrix and proposes the optimal maintenance task.
              <br />
              If you carry out the daily maintenance suggested there, you can perform optimal maintenance tasks without relying on digital signals. That is this MECHPHAISTOS.
            </p>
            <figure class="Risk-matrix">
              <img src="@/assets/Risk_matrix.png" class="Risk-matrix" />
            </figure>
            <p class="features-text">
              In addition, there is another important feature. MECHPHAISTOS is a SaaS.
              <br />
              By sharing equipment condition information and equipment maintenance tasks from sites using similar equipment, we can share even larger amounts of big data with everyone. (Of course, confidential matters of each direct company will not be shared.)
              <br />
              This part is one of the major features of MECHPHAISTOS that is different from local CMMS (computerized maintenance management system) tools.
            </p>
          </TabPanel>
          <TabPanel header="Vision">
            <h1>Transformation from maintenance</h1>
            <p class="vision-text">
              First of all, maintenance work has a very big impact on management.
              <br />
              Our maintenance work is very difficult for everyone to understand and tough work.
              <br />
              So, I would like to take on the challenge of developing this MECHPHAISTOS as a tool that can more powerfully support everyone.
              <br />
              In the near future, many factories will promote digitalization.
            </p>
            <figure class="AI_image">
              <img src="@/assets/AI_image.jpg" class="AI_image" />
            </figure>
            <p class="vision-text">
              I believe that MECHPHAISTOS can exist as a pillar of DX as a tool.
              <br />
              There are also many new technologies emerging.
              <br />
              In particular, AI technology is a wonderful thing. MECHPHAISTOS intends to exist as a pioneer of AI technology.
            </p>
          </TabPanel>
          <TabPanel header="Special Thanks">
            <h1>Special Thanks</h1>
            <p class="thanks-text">
              I spent time in my life as a mechanical engineer.
              <br />
              So I don't have tech for programming, the below site helped me to make this site. I want to say thanks.
              <br />
              Thank you!!
              <br />
              <br />
              Please contact us if you have any problems.
              <ol>
                <li>link</li>
                <li>photo</li>
              </ol>
            </p>
          </TabPanel>
        </TabView>
      </div>
    </section>
  </template>
  
  <script>
  export default {
    data() {
      return {
        activeIndex: parseInt(localStorage.getItem('mechphaistosTabIndex')) || 0, // キー名を変更
      };
    },
    methods: {
      onTabChange(event) {
        this.activeIndex = event.index;
        localStorage.setItem('mechphaistosTabIndex', this.activeIndex); // キー名を変更
      },
    },
  };
  </script>
  
  <style>
  h1 {
    font-weight: bold;
    text-align: center;
    margin-bottom: 20px;
  }
  
  p,
  .text,
  .des-text,
  .for-who-text,
  .message-text,
  .features-text,
  .vision-text,
  .thanks-text {
    padding: 20px;
    font-size: 16px;
    line-height: 1.6;
  }
  
  figure {
    display: block;
    margin: 0 auto;
    text-align: center;
    margin-bottom: 20px;
  }
  
  img {
    max-width: 100%;
    height: auto;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  }
  
  .right-align {
    text-align: right;
    margin-top: 20px;
  }
  
  ol {
    padding-left: 40px;
  }
  </style>
  