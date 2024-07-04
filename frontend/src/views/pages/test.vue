<template>
<BlockViewer header="Two Columns and Stacked" :code="block1">
  <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
      <div class="grid">
          <div class="col-12 lg:col-2">
              <div class="text-900 font-medium text-xl mb-3">Profile</div>
              <p class="m-0 p-0 text-600 line-height-3 mr-3">Odio euismod lacinia at quis risus sed vulputate odio.</p>
          </div>
          <div class="col-12 lg:col-10">
              <div class="grid formgrid p-fluid">
                  <div class="field mb-4 col-12">
                      <label for="nickname" class="font-medium text-900">Nickname</label>
                      <InputText id="nickname" type="text" />
                  </div>
                  <div class="field mb-4 col-12">
                      <label for="avatar" class="font-medium text-900">Avatar</label>
                      <div class="flex align-items-center">
                          <img src="" class="mr-4" />
                          <FileUpload mode="basic" name="avatar" url="./upload.php" accept="image/*" :maxFileSize="1000000" class="p-button-outlined p-button-plain" chooseLabel="Upload Image"></FileUpload>
                      </div>
                  </div>
                  <div class="field mb-4 col-12">
                      <label for="bio" class="font-medium text-900">Bio</label>
                      <Textarea id="bio" type="text" :rows="5" :autoResize="true"></Textarea>
                  </div>
                  <div class="field mb-4 col-12 md:col-6">
                      <label for="email" class="font-medium text-900">Email</label>
                      <InputText id="email" type="text" />
                  </div>
                  <div class="field mb-4 col-12 md:col-6">
                      <label for="country" class="font-medium text-900">Country</label>
                      <Dropdown id="country" v-model="selectedCountry1" :options="countries" optionLabel="name" :filter="true" filterBy="name" :showClear="true" placeholder="Select a Country">
                          <template #option="slotProps">
                              <div class="flex align-items-center">
                                  <img src="" :class="'mr-2 flag flag-' + slotProps.option.code.toLowerCase()" style="width: 18px" />
                                  <div>{{ slotProps.option.name }}</div>
                              </div>
                          </template>
                      </Dropdown>
                  </div>
                  <div class="field mb-4 col-12 md:col-6">
                      <label for="city" class="font-medium text-900">City</label>
                      <InputText id="city" type="text" />
                  </div>
                  <div class="field mb-4 col-12 md:col-6">
                      <label for="state" class="font-medium text-900">State</label>
                      <InputText id="state" type="text" />
                  </div>
                  <div class="field mb-4 col-12">
                      <label for="website" class="font-medium text-900">Website</label>
                      <div class="p-inputgroup">
                          <span class="p-inputgroup-addon">www</span>
                          <InputText id="website" type="text" />
                      </div>
                  </div>
                  <div class="field mb-4 col-12">
                      <label for="privacy" class="font-medium text-900">Privacy</label>
                      <div class="flex align-items-center">
                          <Checkbox id="privacy" v-model="checked1" :binary="true"></Checkbox>
                          <span class="ml-2">Share my data with contacts</span>
                      </div>
                  </div>
                  <div class="col-12">
                      <Button label="Save Changes" class="w-auto mt-3"></Button>
                  </div>
              </div>
          </div>
      </div>
  </div>
</BlockViewer>
</template>