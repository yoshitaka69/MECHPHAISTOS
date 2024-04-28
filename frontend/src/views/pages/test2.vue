<template>

  <BlockViewer header="Emphasized Post" :code="block5">
    <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
      <div class="text-900 font-bold text-5xl mb-6">Recent Posts</div>
      <div class="flex flex-wrap">
        <div class="w-full xl:w-6 pr-0 xl:pr-6">
          <img src="" alt="Image" class="w-full" />
          <div class="flex align-items-center mt-4">
            <img src="" class="mr-3 flex-shrink-0" width="28" height="28" />
            <span class="text-900 font-medium text-lg white-space-nowrap">Darrel Steward</span>
            <span class="text-500 font-medium text-lg mx-3">|</span>
            <span class="text-500 font-medium text-lg white-space-nowrap">Oct 7</span>
          </div>
          <div class="text-900 font-bold text-3xl mt-4">Circumpolar Cooperation</div>
          <p class="line-height-3 text-700 my-4">Purus sit amet volutpat consequat mauris nunc congue. Odio pellentesque
            diam volutpat commodo sed egestas egestas fringilla phasellus.</p>
          <div class="flex align-items-center">
            <span class="text-600 text-sm font-medium">15 min read</span>
            <span class="text-600 font-medium text-sm mx-3">|</span>
            <span class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">Poles</span>
            <span class="bg-green-100 text-green-600 text-sm block py-1 px-2 border-round">Nature</span>
          </div>
        </div>
        <div class="w-full xl:w-6">
          <div class="flex flex-wrap align-items-start mb-8 mt-8 xl:mb-6 xl:mt-0">
            <div class="w-full xl:w-6 pr-0 xl:pr-4 mb-4 xl:mb-0">
              <img src="" alt="Image" class="w-full" />
            </div>
            <div class="w-full xl:w-6">
              <div class="flex align-items-center">
                <img src="" class="mr-3 flex-shrink-0" width="28" height="28" />
                <span class="text-900 font-medium text-lg white-space-nowrap">Bessie Cooper</span>
                <span class="text-500 font-medium text-lg mx-3">|</span>
                <span class="text-500 font-medium text-lg white-space-nowrap">Oct 7</span>
              </div>
              <div class="text-900 font-bold text-3xl mt-4">World Famous Fish</div>
              <p class="line-height-3 text-700 my-4">Quisque sagittis purus sit amet volutpat consequat mauris.</p>
              <div class="flex align-items-center">
                <span class="text-600 text-sm font-medium">12 min read</span>
                <span class="text-600 font-medium text-sm mx-3">|</span>
                <span class="bg-blue-100 text-blue-600 text-sm block py-1 px-2 border-round mr-3">Ocean</span>
                <span class="bg-green-100 text-green-600 text-sm block py-1 px-2 border-round">Nature</span>
              </div>
            </div>
          </div>
          <div class="flex flex-wrap align-items-start">
            <div class="w-full xl:w-6 pr-0 xl:pr-4 mb-4 xl:mb-0">
              <img src="" alt="Image" class="w-full" />
            </div>
            <div class="w-full xl:w-6">
              <div class="flex align-items-center">
                <img src="" class="mr-3 flex-shrink-0" width="28" height="28" />
                <span class="text-900 font-medium text-lg white-space-nowrap">Jenna Clark</span>
                <span class="text-500 font-medium text-lg mx-3">|</span>
                <span class="text-500 font-medium text-lg white-space-nowrap">Oct 10</span>
              </div>
              <div class="text-900 font-bold text-3xl mt-4">Extinction and Origination</div>
              <p class="line-height-3 text-700 my-4">Bibendum enim facilisis gravida neque convallis a cras.</p>
              <div class="flex align-items-center">
                <span class="text-600 text-sm font-medium">10 min read</span>
                <span class="text-600 font-medium text-sm mx-3">|</span>
                <span class="bg-blue-100 text-blue-600 text-sm block py-1 px-2 border-round mr-3">Ocean</span>
                <span class="bg-green-100 text-green-600 text-sm block py-1 px-2 border-round">Nature</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </BlockViewer>

</template>

<script>
export default {
  name: 'Blog',
  data() {
    return {

      block5: `
<div class="surface-section px-4 py-8 md:px-6 lg:px-8">
  <div class="text-900 font-bold text-5xl mb-6">Recent Posts</div>
  <div class="flex flex-wrap">
      <div class="w-full xl:w-6 pr-0 xl:pr-6">
          <img src="/images/blocks/blog/blog-9.png" alt="Image" class="w-full" />
          <div class="flex align-items-center mt-4">
              <img src="/images/blocks/avatars/circle/avatar-f-3.png" class="mr-3 flex-shrink-0" width="28" height="28" />
              <span class="text-900 font-medium text-xl white-space-nowrap">Darrel Steward</span>
              <span class="text-500 font-medium text-xl mx-3">|</span>
              <span class="text-500 font-medium text-xl white-space-nowrap">Oct 7</span>
          </div>
          <div class="text-900 font-bold text-4xl mt-4">Circumpolar Cooperation</div>
          <p class="line-height-3 text-700 my-4">Purus sit amet volutpat consequat mauris nunc congue. Odio pellentesque diam volutpat commodo sed egestas egestas fringilla phasellus.</p>
          <div class="flex align-items-center">
              <span class="text-600 text-sm font-medium">15 min read</span>
              <span class="text-600 font-medium text-sm mx-3">|</span>
              <span class="bg-indigo-100 text-indigo-600 text-sm block py-1 px-2 border-round mr-3">Poles</span>
              <span class="bg-green-100 text-green-600 text-sm block py-1 px-2 border-round">Nature</span>
          </div>
      </div>
      <div class="w-full xl:w-6">
          <div class="flex flex-wrap align-items-start mb-8 mt-8 xl:mb-6 xl:mt-0">
              <div class="w-full xl:w-6 pr-0 xl:pr-4 mb-4 xl:mb-0">
                  <img src="/images/blocks/blog/blog-10.png" alt="Image" class="w-full" />
              </div>
              <div class="w-full xl:w-6">
                  <div class="flex align-items-center">
                      <img src="/images/blocks/avatars/circle/avatar-f-2.png" class="mr-3 flex-shrink-0" width="28" height="28"/>
                      <span class="text-900 font-medium text-xl white-space-nowrap">Bessie Cooper</span>
                      <span class="text-500 font-medium text-xl mx-3">|</span>
                      <span class="text-500 font-medium text-xl white-space-nowrap">Oct 7</span>
                  </div>
                  <div class="text-900 font-bold text-4xl mt-4">World Famous Fish</div>
                  <p class="line-height-3 text-700 my-4">Quisque sagittis purus sit amet volutpat consequat mauris.</p>
                  <div class="flex align-items-center">
                      <span class="text-600 text-sm font-medium">12 min read</span>
                      <span class="text-600 font-medium text-sm mx-3">|</span>
                      <span class="bg-blue-100 text-blue-600 text-sm block py-1 px-2 border-round mr-3">Ocean</span>
                      <span class="bg-green-100 text-green-600 text-sm block py-1 px-2 border-round">Nature</span>
                  </div>
              </div>
          </div>
          <div class="flex flex-wrap align-items-start">
              <div class="w-full xl:w-6 pr-0 xl:pr-4 mb-4 xl:mb-0">
                  <img src="/images/blocks/blog/blog-11.png" alt="Image" class="w-full" />
              </div>
              <div class="w-full xl:w-6">
                  <div class="flex align-items-center">
                      <img src="/images/blocks/avatars/circle/avatar-f-3.png" class="mr-3 flex-shrink-0" width="28" height="28"/>
                      <span class="text-900 font-medium text-xl white-space-nowrap">Jenna Clark</span>
                      <span class="text-500 font-medium text-xl mx-3">|</span>
                      <span class="text-500 font-medium text-xl white-space-nowrap">Oct 10</span>
                  </div>
                  <div class="text-900 font-bold text-4xl mt-4">Extinction and Origination</div>
                  <p class="line-height-3 text-700 my-4">Bibendum enim facilisis gravida neque convallis a cras.</p>
                  <div class="flex align-items-center">
                      <span class="text-600 text-sm font-medium">10 min read</span>
                      <span class="text-600 font-medium text-sm mx-3">|</span>
                      <span class="bg-blue-100 text-blue-600 text-sm block py-1 px-2 border-round mr-3">Ocean</span>
                      <span class="bg-green-100 text-green-600 text-sm block py-1 px-2 border-round">Nature</span>
                  </div>
              </div>
          </div>
      </div>
  </div>
</div>`,

    };
  }
};
</script>
