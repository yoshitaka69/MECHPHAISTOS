<template>
    <div class="surface-section px-4 py-8 md:px-6 lg:px-8">

        <!--左側 Side Bar-->
        <div class="grid">
            <div class="col-12 lg:col-2">
                <div class="text-900 font-medium text-xl mb-3">Work Order Input Form</div>
                <p class="m-0 p-0 text-600 line-height-3 mr-3">Odio euismod lacinia at quis risus sed vulputate odio.</p>
            </div>


            <div class="col-12 lg:col-10">

                <div class="grid formgrid p-fluid">
                    <div class="field mb-4 col-12">
                        <label for="title" class="font-medium text-900">Title</label>
                        <InputText id="nickname" type="text" />
                    </div>

                    <div class="field mb-4 col-12">
                        <label for="avatar" class="font-medium text-900">Picture</label>
                        <div class="flex align-items-center">
                            <img src="" class="mr-4" />
                            <FileUpload mode="basic" name="avatar" url="./upload.php" accept="image/*" :maxFileSize="1000000" class="p-button-outlined p-button-plain" chooseLabel="Upload Image"></FileUpload>
                        </div>
                    </div>

                    <div class="field mb-4 col-12 md:col-6">
                        <label for="email" class="font-medium text-900">Plant</label>
                        <InputText id="email" type="text" />
                    </div>


                    <div class="field mb-4 col-12 md:col-6">
                        <label for="city" class="font-medium text-900">Equipment</label>
                        <InputText id="city" type="text" />
                    </div>

                    <div class="field mb-4 col-12 md:col-6">
                        <label for="state" class="font-medium text-900">Request State Date</label>
                        <InputText id="state" type="date" />
                    </div>

                    <div class="field mb-4 col-12 md:col-6">
                        <label for="state" class="font-medium text-900">Request End Date</label>
                        <InputText id="state" type="date" />
                    </div>


                    <!--詳細入力フォーム-->
                    <div class="field mb-4 col-12">
                        <label for="description" class="font-medium text-900">Description</label>
                        <Textarea id="description" type="text" :rows="10" :autoResize="true"></Textarea>
                    </div>
                    <div class="field mb-4 col-12">
                        <label for="privacy" class="font-medium text-900">Relation to GanttSticks ?</label>
                        <div class="flex align-items-center">
                            <Checkbox id="privacy" v-model="checked1" :binary="true"></Checkbox>
                            <span class="ml-2">If you check this box, this form relate to Ganttstick</span>
                        </div>
                    </div>
                    <!--Save button-->
                    <div class="col-12">
                        <Button label="Save Changes" class="w-auto mt-3"></Button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>