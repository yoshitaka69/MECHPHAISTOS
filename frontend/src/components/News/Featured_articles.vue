<template>
    <BlockViewer header="3 Columns with Images" :code="block1">
        <div class="surface-ground px-4 py-8 md:px-6 lg:px-8">
            <div class="font-bold text-5xl text-900 mb-5 text-center">Featured Articles</div>
            <div class="grid nogutter">
                <div class="col-12 lg:col-4 p-3">
                    <div class="shadow-2 border-round h-full surface-card">
                        <img src="" alt="Image" class="block w-full border-round-top" />
                        <div class="p-4">
                            <span class="block font-medium text-blue-600 mb-3">Crime</span>
                            <div class="text-xl text-900 font-medium mb-3 line-height-3">Fugitive flamingo spotted in
                                Florida</div>
                            <div class="line-height-3 mb-3 text-700">Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</div>
                            <div class="flex">
                                <Avatar image="" shape="circle"></Avatar>
                                <div class="ml-2">
                                    <div class="text-sm font-bold text-900 mb-1">Anna Lane</div>
                                    <div class="text-sm flex align-items-center text-700">
                                        <i class="pi pi-calendar mr-1 text-sm"></i>
                                        <span>Apr 5, 2021</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12 lg:col-4 p-3">
                    <div class="shadow-2 border-round h-full surface-card">
                        <img src="" alt="Image" class="block w-full border-round-top" />
                        <div class="p-4 flex flex-column">
                            <span class="block font-medium text-pink-600 mb-3">Wildlife</span>
                            <div class="text-xl text-900 font-medium mb-3 line-height-3">Journey to the Ends of the
                                Earth</div>
                            <div class="line-height-3 mb-3 text-700">Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</div>
                            <div class="flex">
                                <Avatar image="" shape="circle"></Avatar>
                                <div class="ml-2">
                                    <div class="text-sm font-bold text-900 mb-1">Arlene McCoy</div>
                                    <div class="text-sm flex align-items-center text-700">
                                        <i class="pi pi-calendar mr-1 text-sm"></i>
                                        <span>Apr 6, 2021</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-12 lg:col-4 p-3">
                    <div class="shadow-2 border-round h-full surface-card">
                        <img src="" alt="Image" class="block w-full border-round-top" />
                        <div class="p-4">
                            <span class="block font-medium text-orange-600 mb-3">Marine</span>
                            <div class="text-xl text-900 font-medium mb-3 line-height-3">'Real and imminent' extinction
                                risk</div>
                            <div class="line-height-3 mb-3 text-700">Lorem ipsum dolor sit amet, consectetur adipiscing
                                elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.</div>
                            <div class="flex">
                                <Avatar image="" shape="circle"></Avatar>
                                <div class="ml-2">
                                    <div class="text-sm font-bold text-900 mb-1">Diane Miles</div>
                                    <div class="text-sm flex align-items-center text-700">
                                        <i class="pi pi-calendar mr-1 text-sm"></i>
                                        <span>Apr 9, 2021</span>
                                    </div>
                                </div>
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
	components: {

	},
}
</script>