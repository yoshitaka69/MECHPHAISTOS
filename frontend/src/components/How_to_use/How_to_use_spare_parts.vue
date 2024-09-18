<template>
    <div>
        <div class="block-category-title">Content Sections</div>
        <div class="surface-section px-4 py-8 md:px-6 lg:px-8">
            <div class="py-4 text-center md:text-left border-round bg-cover h-20rem lg:h-30rem flex flex-column justify-content-end mb-5" :style="{ backgroundImage: `url(${Spare_part})` }">
                <div class="grid">
                    <div class="col lg:col-offset-2 px-5">
                        <div class="text-5xl font-bold text-black">How to use Risk Matrix in MECHPHAISTOS</div>
                        <p class="line-height-3 text-black text-lg text-center md:text-left mt-3">Published May 16, 2024 by Yoshitaka Noto</p>
                    </div>
                </div>
            </div>
            <!--左側のサイドのいいね！など-->
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

                <!--メインページ-->
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
                    <div class="line-height-3 text-xl text-900 mb-5">
                        ここでは、スペアパーツリストについて説明します。スペアパーツマネージメントは、設備修繕費、メンテナンス、資産管理において非常に重要です。
                        このリストでは、スペアパーツの一覧を表します。よくある部品台帳と異なるのは、メンテナンスタスクやクリティカルエクイップメントと紐づいてるので、各修繕での対応が出来ます。
                        部品管理で重要なのは、その部品があるかないかです。
                        ですので、WorkingReportやDaily Rewportでの使用したパーツの個数と、名称をしっかり記入してください。
                        入荷された際には、以下のフォームで入力したことをちゃんと記入して頂ければ、パーツを把握することができます。各パーツの所在がわかれば、タスクに紐づいているので、parts alertによって、パーツの有無を警告してくれます。
                        
                        このパーツリストは、以下のような項目が表示されてます。
                        特に、型式とメーカーなどを記入しておけば、他の工場で不足した際にも同様な設備であれば、補うことができます。
                        
                        
                    </div>
                    <div class="text-center mb-5">
                        <img src="" alt="Related content image" class="w-full border-round mb-2" />
                        <span class="block text-600 line-height-3">Risk Matrix</span>
                    </div>
                    <div class="line-height-3 text-lg text-900 mb-4">Critical Equipment Listの使い方について説明していきます。 Critical Equipment Listは以下のデータリストのよって構成されてます。</div>
                    <ul class="text-lg mb-5 mt-0 mr-0 ml-3 p-0 text-900 font-light">
                        <li class="mb-3">Risk Matrix</li>
                        <li class="mb-3">Spare Parts List</li>
                        <li class="mb-3">Task List</li>
                    </ul>

                    <div class="text-3xl text-800 mb-4">1.Input formやエクセルをアップロードし、リストにデータを入力してください。</div>
                    <div class="line-height-3 text-lg text-900 mb-5">Lacus viverra vitae congue eu consequat ac felis donec et。 A lacus vestibulum sed arcu non...</div>
                    <div class="text-3xl text-800 mb-4">2.リスト内のPM02やPM03等の補修履歴を確認してください。</div>
                    <div class="line-height-3 text-lg text-900 mb-5">Lacus viverra vitae congue eu consequat ac felis donec et。 A lacus vestibulum sed arcu non...</div>
                    <div class="text-3xl text-800 mb-4">3.Risk Matrixの評価方法を検討してください。</div>
                    <div class="line-height-3 text-lg text-900 mb-5">Lacus viverra vitae congue eu consequat ac felis donec et。 A lacus vestibulum sed arcu non...</div>
                    <div class="text-3xl text-800 mb-4">4.Input formやエクセルをアップロードし、リストにデータを入力してください。</div>
                    <div class="line-height-3 text-lg text-900 mb-5">Lacus viverra vitae congue eu consequat ac felis donec et。 A lacus vestibulum sed arcu non...</div>

                    <!-- Back to Previous Page and Go to Next Page -->
                    <div class="flex flex-wrap justify-content-between align-items-center gap-3 bg-primary text-primary-700 p-3 border-round">
                        <div class="flex align-items-center cursor-pointer">
                            <i class="pi pi-arrow-left mr-3"></i>
                            <span class="font-bold">Back to PREVIOUS PAGE</span>
                        </div>
                        <span class="font-medium text-2xl">Risk Matrix</span>
                        <div class="flex align-items-center cursor-pointer">
                            <span class="font-bold mr-3">Go to NEXT PAGE</span>
                            <i class="pi pi-arrow-right"></i>
                        </div>
                    </div>
                </div>

                <!--右側のポストページ-->
                <div class="col-12 lg:col-3 lg:border-left-1 surface-border">
                    <div class="p-3">
                        <div class="flex border-bottom-1 surface-border pb-4 mb-5">
                            <img :src="authorImage" alt="Author image" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Jessica Doe</span>
                                <span class="text-600 font-medium mb-2">1.7K Followers</span>
                                <Button label="Follow" class="p-button-rounded p-button-primary"></Button>
                            </div>
                        </div>
                        <span class="text-900 font-medium text-xl block mb-5">Other Posts</span>
                        <div class="flex pb-4">
                            <img src="" alt="Post thumbnail" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                        <div class="flex pb-4">
                            <img src="" alt="Post thumbnail" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                        <div class="flex pb-4">
                            <img src="" alt="Post thumbnail" class="mr-3 h-5rem w-5rem" />
                            <div class="flex flex-column align-items-start">
                                <span class="text-lg text-900 font-medium mb-1">Post Title</span>
                                <span class="text-600 mb-2">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                        <div class="flex flex-column gap-3">
                            <div class="w-full h-full p-5 border-round" :style="{ backgroundImage: `linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%、#000000 100%)、url('/images/blocks/content/content-8.png')` }">
                                <span class="text-white font-medium mb-3">Post Title</span>
                                <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi innulla posuere。</span>
                            </div>
                            <div class="w-full h-full p-5 border-round" :style="{ backgroundImage: `linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%、#000000 100%)、url('/images/blocks/content/content-9.png')` }">
                                <span class="text-white font-medium mb-3">Post Title</span>
                                <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi innulla posuere。</span>
                            </div>
                            <div class="w-full h-full p-5 border-round" :style="{ backgroundImage: `linear-gradient(180deg, rgba(0, 0, 0, 0.4) 0%、#000000 100%)、url('/images/blocks/content/content-10.png')` }">
                                <span class="text-white font-medium mb-3">Post Title</span>
                                <span class="text-white-alpha-70 block line-height-3">Metus aliquam eleifend mi in nulla posuere。</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup>
import Spare_part from '@/assets/Spare_parts.png';
import authorImage from '@/assets/self_photo.png';
</script>
