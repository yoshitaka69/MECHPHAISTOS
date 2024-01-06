import Critical_equipment_list from '@/components/Critical_equipment_list/Critical_equipment_list.vue';
<template>
    <!--AdminLTE copy-->
    <div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

        <section class="content-header">
            <div class="container-fluid">
                <div class="row mb-2">
                    <div class="col-sm-6">
                        <h1>How to use</h1>
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
                <h1>How to use pages</h1>
                <ul class="list">
                    <li>Critical_equipment_list</li>                    
                    <li>Repairing cost</li>
                    <li>NearMiss</li>
                    <li>Communications</li>
                    <li>schedule</li>
                    <li>Trend & Demand</li>
                    <li>Work Order</li>
                    <li>Benefit</li>
                </ul>
            </div>
        </section>
    </div>
</template>

<style>

ul.list{
    font-size:25px;
    line-height: 200%;
}

</style>