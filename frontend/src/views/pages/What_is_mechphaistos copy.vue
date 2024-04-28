<template>
    <!--AdminLTE copy-->

    <div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->
        <section class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1>What's MECHPHAISTOS</h1>
                    </div>
                    <div class="col-sm-6">
                        <ol class="breadcrumb float-sm-right">
                            <li class="breadcrumb-item"><a href="#">Home</a></li>
                            <li class="breadcrumb-item active">MECHPHAISTOS</li>
                        </ol>
                    </div>
                </div>
            </div>
        </section>

        <section class="content">
            <div class="card card-solid">
                <div class="card-body">
                    <div class="row">
                        <nav class="w-100">
                            <div class="nav nav-tabs" id="product-tab" role="tablist">
                                <a class="nav-item nav-link active" id="product-desc-tab" data-toggle="tab"
                                    href="#product-desc" role="tab" aria-controls="product-desc" aria-selected="true">What's
                                     MECHPHAISTOS</a>

                                <a class="nav-item nav-link" id="product-about-us-tab" data-toggle="tab"
                                    href="#product-about-us" role="tab" aria-controls="product-about-us"
                                    aria-selected="false">About us</a>

                                <a class="nav-item nav-link" id="product-for-who-tab" data-toggle="tab"
                                    href="#product-for-who" role="tab" aria-controls="product-for-who"
                                    aria-selected="false">For Who ?</a>

                                <a class="nav-item nav-link" id="product-message-tab" data-toggle="tab"
                                    href="#product-message" role="tab" aria-controls="product-message"
                                    aria-selected="false">Message</a>

                                <a class="nav-item nav-link" id="product-features-tab" data-toggle="tab"
                                    href="#product-features" role="tab" aria-controls="product-features"
                                    aria-selected="false">Features</a>

                                <a class="nav-item nav-link" id="product-vision-tab" data-toggle="tab"
                                    href="#product-vision" role="tab" aria-controls="product-vision"
                                    aria-selected="false">Vision</a>

                                <a class="nav-item nav-link" id="product-special-thanks-tab" data-toggle="tab"
                                    href="#product-special-thanks" role="tab" aria-controls="product-special-thanks"
                                    aria-selected="false">Special Thanks</a>
                            </div>
                        </nav>

                        <div class="tab-content p-3" id="nav-tabContent">
                            <div class="tab-pane fade show active" id="product-desc" role="tabpanel"
                                aria-labelledby="product-desc-tab">
                                <h1>MECHPHAISTOS optimizes your maintenance task</h1>
                                <p class="des-text">MECHPHAISTOS provides powerful support for managing many complicated
                                    tasks.
                                    <br>Maintenance working is in a trade off between money and maintenance task. We cannot
                                    stop
                                    production due to machine trouble, so we plant a machine maintenance as preventive
                                    maintenance.
                                    <br>However, they may be over-maintained and are not kind to management. Additionally,
                                    it is
                                    not easy to determine whether those maintenance tasks were necessary.
                                    <br>MECHPHAISTOS has tree factor to help your datermine. Critical Equipment, Repairing
                                    Cost,
                                    Maintenance Task. Then MECHPHAISTOS provide a good maintenance plan to yours.
                                    <br>All you need is a list of machines in your factory, maintenance records, and a
                                    willingness to try out this tool.
                                </p>

                                <figure class="desc-ternary">
                                    <img src="@/assets/newplot.jpg" alt="MECHPHAISTOSの概念">
                                </figure>
                                <br>
                                <br>
                                <p class="des-text">Of course, by continuously inputting current values and digital signals
                                    from equipment,
                                    it becomes a tool with higher possibilities, but I would like you to use it as a
                                    stepping stone for cost-saving DX.</p>
                            </div>


                            <div class="tab-pane fade" id="product-about-us" role="tabpanel"
                                aria-labelledby="product-about-us-tab">

                                <h1>Hello,I'm Yoshitaka Noto. <p>I developed MECHPHAISTOS.</p>
                                </h1>
                                <br>
                                <div class="intro">
                                    <figure class="self-intro">
                                        <img src="@/assets/self_photo.png" class="self-photo" alt="自分の写真">
                                    </figure>
                                    <p class="intro-text">I have been doing plant maintenance as a mechanical engineer for
                                        over 10 years.
                                        <br>I studied fluid mechanics(cavitation) at university, and as a researcher I
                                        studied image analysis technology for high-speed fluids.
                                        <br>Since graduating from university, I have been involved in plant maintenance in
                                        areas such as architecture, air conditioning, electricity, machinery, automation,
                                        safety, and law, without focusing on one field.
                                        <br>So,I learned that this maintenance work is very tough work and is important for
                                        the plant.
                                        <br>I also hope that this tool will be a good one for people involved in plant
                                        maintenance like me.
                                        <br>
                                        <br>
                                        <br>Thank you, Y.noto
                                    </p>
                                </div>

                            </div>


                            <div class="tab-pane fade" id="product-for-who" role="tabpanel"
                                aria-labelledby="product-for-who-tab">
                                <h1>MECHPHAISTOS for all maintenance worker.</h1>
                                <div class="for-who">
                                    <figure class="for-who-photo">
                                        <img src="@/assets/for_who.jpg" class="for-who-photo">
                                    </figure>
                                    <p class="for-who-text">
                                        <br>I made this tools to help for maintenance worker.
                                        <br>Of course, I know that maintenance work is very important, but it's difficult to
                                        convey to those around you the importance of their work and the difficulty of their
                                        work.
                                        <br>This is because their technology is so wonderfully specific that it is difficult
                                        for those around them to understand it.
                                        <br>We created this tool not only to make their work more efficient, but also to
                                        emphasize the importance of their work.
                                        <br>And more I hope that this tools to be a community are for maintenance worker
                                        such as machinery engineer,electrician,programmer.
                                    </p>
                                </div>

                            </div>

                            <div class="tab-pane fade" id="product-message" role="tabpanel"
                                aria-labelledby="product-message-tab">
                                <div class="maintenance">
                                    <h1>The status of us engineers should be a little higher.</h1>
                                    <br>
                                    <figure class="maintenance-worker">
                                        <img src="@/assets/engineer.jpg" class="maintenance-worker">
                                    </figure>
                                    <p class="message-text">
                                        <br>I think that all engineer should be evaluated.Our brain and experience are great
                                        and special.
                                        <br>However our situation are not good.and more AI will be help our work and rib
                                        too. Our situation will change to next stage we have never experienced.And our
                                        result was not simple and a little be like a blackbox.
                                        <br>So I made this tools for all engineer to be able to appeal more.Use this tool
                                        for your maintenance work.
                                    </p>
                                </div>


                            </div>
                            <div class="tab-pane fade" id="product-features" role="tabpanel"
                                aria-labelledby="product-features-tab">
                                <div class="features">
                                    <h1>Risk-Matrix and SNS collaborate</h1>
                                    <p class="features-text">

                                        <br>MECHPHAISTOS don't need install some inspection censor such as ammeter, pressure
                                        gage, flowmeter, thermocouple...etc.
                                        <br>Of course, the digital signals from them are essential for understanding the
                                        condition of the equipment.
                                        <br>However, installing these sensors is also expensive. Additionally, as I'm sure
                                        maintenance workers will understand, you may or may not be able to see the signs
                                        from those sensors. For example, even if the current value is monitored every day,
                                        the current value may suddenly become high in some equipment, and the machine may
                                        stop a few seconds later.
                                        <br>So what I'm saying is that monitoring the condition of equipment with digital
                                        signals is reliable in many cases, but not for all machines. Also, the initial cost
                                        is high. Under such circumstances, MECHPHAISTOS evaluates the past maintenance
                                        records and the importance of the equipment from a list matrix and proposes the
                                        optimal maintenance task.
                                        <br>If you carry out the daily maintenance suggested there, you can perform optimal
                                        maintenance tasks without relying on digital signals. That is this MECHPHAISTOS.
                                    </p>
                                    <br>
                                    <br>
                                    <figure class="Risk-matrix">
                                        <img src="@/assets/Risk_matrix.png" class="Risk-matrix">
                                    </figure>
                                    <br>

                                    <p class="features-text">
                                        In addition, there is another important feature. MECHPHAISTOS is a SaaS.
                                        <br>By sharing equipment condition information and equipment maintenance tasks from
                                        sites using similar equipment, we can share even larger amounts of big data with
                                        everyone.(Of course, confidential matters of each direct company will not be
                                        shared.)
                                        <br>This part is one of the major features of MECHPHAISTOS that is different from
                                        local CMMS(computerized maintenance management system) tools.
                                    </p>
                                </div>
                            </div>

                            <div class="tab-pane fade" id="product-vision" role="tabpanel"
                                aria-labelledby="product-vision-tab">
                                <div class="vision">
                                    <h1>Transformation from maintenance</h1>
                                    <p class="vision-text">
                                        First of all, maintenance work has very big impact for management.
                                        <br>Our maintenance work is very difficult for everyone to understand and tough work.
                                        <br>So,I would like to take on the challenge of developing this MECHPHAISTOS as a tool that can more powerfully support everyone.
                                        <br>In the near future, many factories will promote digitalization. 
                                        </p>

                                    <figure class="AI_image">
                                        <img src="@/assets/AI_image.jpg" class="AI_image">
                                    </figure>
                                    <p class="vision-text">
                                        <br>I believe that MECHPHAISTOS can exist as a pillar of DX as a tool.
                                        <br>There are also many new technologies emerging.
                                        <br>In particular, AI technology is a wonderful thing. MECHPHAISTOS intends to exist as a pioneer of AI technology.
                                    </p>
                                </div>


                            </div>

                            <div class="tab-pane fade" id="product-special-thanks" role="tabpanel"
                                aria-labelledby="product-special-thanks-tab">
                                <h1>Special Thanks</h1>
                                <p class="thanks-text">
                                I spent time in my life for mechanical engineer.
                                <br>So I don't have tech for program
                                below site help me to make this site.
                                I wanna to say thanks.
                                <br>Thank you!!
                                <br>
                                <br>Please contact us if you have any problems.
                                <ol>
                                    <li>link</li>
                                    <li>photo</li>
                                </ol>
                                
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </div>
</template>


<style>
p.des-text {
    font-size: 16px;
    line-height: 30px;
}

.desc-ternary {
    text-align: center;
}

img.self-photo {
    width: 75%;
    margin-left: 10%;
}



.intro {
    display: flex;
}

p.intro-text {
    font-size: 16px;
    line-height: 30px;
    max-width: 1500px;
}


img.for-who-photo {
    max-width: 800px;
    margin-left: 10%;
    width: 70%;
}

.for-who {
    display: flex;
}

p.for-who-text {
    font-size: 16px;
    line-height: 30px;
    max-width: 1500px;
}


img.maintenance-worker {
    max-width: 800px;
    margin-left: 30%;
    width: 35%;
}

p.message-text {
    font-size: 16px;
    line-height: 30px;
}

img.Risk-matrix {
    margin-left: 35%;
    width: 20%;
}

p.features-text {
    font-size: 16px;
    line-height: 30px;
}

img.AI_image{
    margin-left: 10%;
    width: 50%;
}

p.vision-text{
    font-size: 16px;
    line-height: 30px;
}

p.thanks-text{
    font-size: 16px;
    line-height: 30px;
}


</style>
