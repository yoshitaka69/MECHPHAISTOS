<template>
    <div>
        <div class="block-category-title">Content Sections</div>
        <BlockViewer header="3 Columns" :code="block3">
            <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
                <div class="py-4 text-center md:text-left border-round bg-cover h-20rem lg:h-30rem flex flex-column justify-content-end mb-5" style="background: url('/images/blocks/content/content-4.png')">
                    <div class="grid">
                        <div class="col lg:col-offset-2 px-5">
                            <div class="text-5xl font-bold text-white">Create Your Own PrimeBlock with Built-in Dark Mode</div>
                            <p class="line-height-3 text-white text-lg text-center md:text-left mt-3">Published May 16, 2022 by Jessica Doe</p>
                        </div>
                    </div>
                </div>
                <div class="grid">
                    <div class="col-12 lg:col-2">
                        <div class="flex flex-row lg:flex-column lg:border-right-1 surface-border gap-5 mb-4 lg:px-5">
                            <div class="text-900 flex flex-row align-items-center justify-content-end">
                                <span class="font-semibold mr-3">71</span>
                                <i class="pi pi-bookmark"></i>
                            </div>
                            <div class="text-900 flex flex-row align-items-center justify-content-end">
                                <span class="font-semibold mr-3">298</span>
                                <i class="pi pi-heart"></i>
                            </div>
                            <div class="text-900 flex flex-row align-items-center justify-content-end">
                                <span class="font-semibold mr-3">34</span>
                                <i class="pi pi-comments"></i>
                            </div>
                        </div>
                    </div>
                    <div class="col-12 lg:col lg:px-5">
                        <div class="flex flex-wrap align-items-center justify-content-between mb-5 gap-5">
                            <div class="flex flex-row">
                                <span class="text-900 surface-100 inline-flex font-semibold py-2 px-3 mr-2 border-round">New</span>
                                <span class="text-900 surface-100 inline-flex font-semibold py-2 px-3 mr-2 border-round">Technology</span>
                                <span class="text-900 surface-100 inline-flex font-semibold py-2 px-3 border-round">Education</span>
                            </div>
                            <div class="flex align-items-center gap-4">
                                <i class="pi pi-twitter cursor-pointer"></i>
                                <i class="pi pi-facebook cursor-pointer"></i>
                                <i class="pi pi-link cursor-pointer"></i>
                            </div>
                        </div>
                        <div class="line-height-3 text-xl text-900 mb-5">Metus aliquam eleifend mi in nulla posuere. In vitae turpis massa sed elementum tempus egestas sed. Dui ut ornare lectus sit. Massa ultricies mi quis hendrerit.</div>
                        <div class="line-height-3 text-lg text-900 mb-4">
                            This page explains how to use the task list.
This task list is linked to the Critical Equipment List, which is MECHPHAISTOS's main system.
This task list allows you to keep track of the implementation status of the maintenance tasks and the future schedule.

By optimizing the implementation status, you can reduce over-maintenance and optimize repair costs.
*From a management perspective, reducing repair costs is a requirement these days, but this is ultimately optimization.


Fill in the task names and tasks in the list below and set the maintenance cycle to understand future task schedules and repair budgets.

First, enter the task name and the associated BOMCode.

You may be wondering what BOMcode is, but there are many parts generated for one task. There is a limit to expressing them in a table format like this, so they are linked by BOMCode like this.

For example, task-001 will have part001, part002, part003, and these are managed as BOMList.

Clicking on the BomCode will display it in the next modal, so you can add or delete it here.

This BomCode is also managed in a separate table by sparePartsList, so you can edit it here.

Here you can check the delay status of maintenance tasks and understand the costs associated with them.
You can also simulate maintenance costs for this year, next year, and up to 10 years into the future by filling in the check boxes.

The GAP of the maintenance costs incurred is displayed in the Benefit table.
As we have said many times before, from a management perspective, 
reducing repair costs is a welcome thing, but please be aware that there are times when such repairs are unavoidable when considering the soundness of the facilities.
                        </div>
                        <blockquote class="surface-50 line-height-3 text-xl text-800 mb-4 py-3 px-3 border-round mx-0">
                            “In short, GPU.js is a JavaScript acceleration library that can be used for general-purpose computations on GPUs using JavaScript. It supports browsers, Node.js and TypeScript.”
                        </blockquote>
                        <div class="line-height-3 text-lg text-900 mb-4">
                            Convallis tellus id interdum velit laoreet id donec ultrices. Lacus sed viverra tellus in hac habitasse platea dictumst. Ultricies tristique nulla aliquet enim. Nunc scelerisque viverra mauris in aliquam sem fringilla.
                            Laculis urna id volutpat lacus laoreet.
                        </div>
                        <ul class="text-lg mb-5 mt-0 mr-0 ml-3 p-0 text-900 font-light">
                            <li class="mb-3">Nunc sed velit dignissim sodales ut.</li>
                            <li class="mb-3">Lorem mollis aliquam ut porttitor.</li>
                            <li>Urna nec tincidunt praesent semper feugiat nibh sed.</li>
                        </ul>
                        <div class="text-center mb-5">
                            <img src="" alt="Image" class="w-full border-round mb-2" />
                            <span class="block text-600 line-height-3">Id porta nibh venenatis cras sed felis eget velit.</span>
                        </div>
                        <div class="text-3xl text-800 mb-4">Massa vitae tortor condimentum lacinia</div>
                        <div class="line-height-3 text-lg text-900 mb-5">
                            Lacus viverra vitae congue eu consequat ac felis donec et. A lacus vestibulum sed arcu non. Mauris vitae ultricies leo integer malesuada nunc vel. Dolor sit amet consectetur adipiscing elit ut aliquam purus. Ac tincidunt
                            vitae semper quis lectus nulla at volutpat. Enim lobortis scelerisque fermentum dui faucibus in ornare. In mollis nunc sed id semper. Vitae ultricies leo integer malesuada nunc vel risus commodo.
                        </div>
                        <div class="flex flex-wrap justify-content-between align-items-center gap-3 bg-primary text-primary-700 p-3 border-round">
                            <span class="font-medium text-2xl">Content Section Title</span>
                            <div class="flex align-items-center cursor-pointer">
                                <span class="font-bold mr-3">View Post Statistics</span>
                                <i class="pi pi-arrow-right"></i>
                            </div>
                        </div>
                    </div>

                    <div class="col-12 lg:col-3 lg:border-left-1 surface-border">
                        <div class="p-3">
                            <div class="flex border-bottom-1 surface-border pb-4 mb-5">
                                <img src="" class="mr-3 h-5rem w-5rem" />
                                <div class="flex flex-column align-items-start">
                                    <span class="text-lg text-900 font-medium mb-1">Jessica Doe</span>
                                    <span class="text-600 font-medium mb-2">1.7K Followers</span>
                                    <Button label="Follow" class="p-button-rounded p-button-primary"></Button>
                                </div>
                            </div>
                            <span class="text-900 font-medium text-xl block mb-5">Other Posts</span>
                            <div class="flex pb-4">
                                <img src="" class="mr-3 h-5rem w-5rem" />
                                <div class="flex flex-column align-items-start">
                                    <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                    <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere.</span>
                                </div>
                            </div>
                            <div class="flex pb-4">
                                <img src="" class="mr-3 h-5rem w-5rem" />
                                <div class="flex flex-column align-items-start">
                                    <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                    <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere.</span>
                                </div>
                            </div>
                            <div class="flex pb-4">
                                <img src="" class="mr-3 h-5rem w-5rem" />
                                <div class="flex flex-column align-items-start">
                                    <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                    <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere.</span>
                                </div>
                            </div>
                            <div class="flex flex-column gap-3">
                                <div class="w-full h-full p-5 border-round" style="background: linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, #000000 100%), url('/images/blocks/content/content-8.png')">
                                    <span class="text-white font-medium mb-3">Post Title</span>
                                    <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi innulla posuere.</span>
                                </div>
                                <div class="w-full h-full p-5 border-round" style="background: linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, #000000 100%), url('/images/blocks/content/content-9.png')">
                                    <span class="text-white font-medium mb-3">Post Title</span>
                                    <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi innulla posuere.</span>
                                </div>
                                <div class="w-full h-full p-5 border-round" style="background: linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%, #000000 100%), url('/images/blocks/content/content-10.png')">
                                    <span class="text-white font-medium mb-3">Post Title</span>
                                    <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi in nulla posuere.</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </BlockViewer>
    </div>
</template>
