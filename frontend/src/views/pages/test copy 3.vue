<BlockViewer header="Group Layout" :code="block3" recent>
    <nav class="surface-overlay px-4 lg:px-6 shadow-2 flex justify-content-between relative lg:static" style="min-height: 84px">
        <img src="/images/blocks/logos/bastion-700.svg" alt="Image" height="40" class="mr-0 lg:mr-6 align-self-center" />
        <a
            v-ripple
            class="p-ripple cursor-pointer block lg:hidden align-self-center text-700"
            v-styleclass="{
                selector: '@next',
                enterClass: 'hidden',
                leaveToClass: 'hidden',
                hideOnOutsideClick: true
            }"
        >
            <i class="pi pi-bars text-4xl"></i>
        </a>
        <div class="flex-grow-1 justify-content-between hidden lg:flex absolute lg:static w-full surface-overlay left-0 top-100 z-1 shadow-2 lg:shadow-none">
            <ul class="list-none p-0 m-0 flex select-none flex-column lg:flex-row">
                <li>
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <i class="pi pi-home mr-2"></i>
                        <span>Home</span>
                    </a>
                </li>
                <li>
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <i class="pi pi-users mr-2"></i>
                        <span>Customers</span>
                    </a>
                </li>
                <li>
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <i class="pi pi-calendar mr-2"></i>
                        <span>Calendar</span>
                    </a>
                </li>
                <li>
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <i class="pi pi-chart-line mr-2"></i>
                        <span>Stats</span>
                    </a>
                </li>
            </ul>
            <ul class="list-none p-0 m-0 flex select-none flex-column lg:flex-row border-top-1 surface-border lg:border-top-none">
                <li>
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <i class="pi pi-inbox text-base lg:text-2xl mr-2 lg:mr-0"></i>
                        <span class="block lg:hidden font-medium">Inbox</span>
                    </a>
                </li>
                <li>
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <i class="pi pi-bell text-base lg:text-2xl mr-2 lg:mr-0"></i>
                        <span class="block lg:hidden font-medium">Notifications</span>
                    </a>
                </li>
                <li class="border-top-1 surface-border lg:border-top-none">
                    <a
                        v-ripple
                        class="p-ripple flex px-6 p-3 h-full lg:px-3 lg:py-2 align-items-center text-600 border-left-2 lg:border-bottom-2 lg:border-left-none border-transparent hover:border-blue-500 font-medium cursor-pointer transition-colors transition-duration-150"
                    >
                        <img src="/images/blocks/avatars/circle/avatar-f-1.png" class="mr-3 lg:mr-0" style="width: 28px; height: 28px" />
                        <div class="block lg:hidden">
                            <div class="text-900 font-medium">Josephine Lillard</div>
                            <span class="text-600 font-medium text-sm">Marketing Specialist</span>
                        </div>
                    </a>
                </li>
            </ul>
        </div>
    </nav>
    <nav class="surface-overlay px-4 lg:px-6 py-4 px-4 lg:px-6 border-y-1 surface-border flex flex-column flex-wrap md:flex-row gap-3 w-full md:justify-content-between md:align-items-center">
        <ul class="list-none m-0 p-0 flex flex-row justify-content-between lg:justify-content-start lg:mb-0">
            <li>
                <a v-ripple class="p-ripple flex align-items-center cursor-pointer p-3 border-round hover:surface-200 transition-duration-150 transition-colors" :class="{ 'surface-200': activeTab3 === 0 }" @click="activeTab3 = 0">
                    <i
                        class="pi pi-chart-line md:hidden"
                        :class="{
                            'text-700': activeTab3 === 0,
                            'text-600': activeTab3 !== 0
                        }"
                    ></i>
                    <span
                        class="font-medium hidden md:block"
                        :class="{
                            'text-900': activeTab3 === 0,
                            'text-600': activeTab3 !== 0
                        }"
                        >Overview</span
                    >
                </a>
            </li>
            <li>
                <a v-ripple class="p-ripple flex align-items-center cursor-pointer p-3 border-round hover:surface-200 transition-duration-150 transition-colors" :class="{ 'surface-200': activeTab3 === 1 }" @click="activeTab3 = 1">
                    <i
                        class="pi pi-user md:hidden"
                        :class="{
                            'text-700': activeTab3 === 1,
                            'text-600': activeTab3 !== 1
                        }"
                    ></i>
                    <span
                        class="font-medium hidden md:block"
                        :class="{
                            'text-900': activeTab3 === 1,
                            'text-600': activeTab3 !== 1
                        }"
                        >Profile</span
                    >
                </a>
            </li>
            <li>
                <a v-ripple class="p-ripple flex align-items-center cursor-pointer p-3 border-round hover:surface-200 transition-duration-150 transition-colors" :class="{ 'surface-200': activeTab3 === 2 }" @click="activeTab3 = 2">
                    <i
                        class="pi pi-bolt md:hidden"
                        :class="{
                            'text-700': activeTab3 === 2,
                            'text-600': activeTab3 !== 2
                        }"
                    ></i>
                    <span
                        class="font-medium hidden md:block"
                        :class="{
                            'text-900': activeTab3 === 2,
                            'text-600': activeTab3 !== 2
                        }"
                        >Activity</span
                    >
                </a>
            </li>
            <li>
                <a v-ripple class="p-ripple flex align-items-center cursor-pointer p-3 border-round hover:surface-200 transition-duration-150 transition-colors" :class="{ 'surface-200': activeTab3 === 3 }" @click="activeTab3 = 3">
                    <i
                        class="pi pi-users md:hidden"
                        :class="{
                            'text-700': activeTab3 === 3,
                            'text-600': activeTab3 !== 3
                        }"
                    ></i>
                    <span
                        class="font-medium hidden md:block"
                        :class="{
                            'text-900': activeTab3 === 3,
                            'text-600': activeTab3 !== 3
                        }"
                        >Members & Roles</span
                    >
                </a>
            </li>
            <li>
                <a v-ripple class="p-ripple flex align-items-center cursor-pointer p-3 border-round hover:surface-200 transition-duration-150 transition-colors" :class="{ 'surface-200': activeTab3 === 4 }" @click="activeTab3 = 4">
                    <i
                        class="pi pi-lock md:hidden"
                        :class="{
                            'text-700': activeTab3 === 4,
                            'text-600': activeTab3 !== 4
                        }"
                    ></i>
                    <span
                        class="font-medium hidden md:block"
                        :class="{
                            'text-900': activeTab3 === 4,
                            'text-600': activeTab3 !== 4
                        }"
                        >Security</span
                    >
                </a>
            </li>
            <li>
                <a v-ripple class="p-ripple flex align-items-center cursor-pointer p-3 border-round hover:surface-200 transition-duration-150 transition-colors" :class="{ 'surface-200': activeTab3 === 5 }" @click="activeTab3 = 5">
                    <i
                        class="pi pi-dollar md:hidden"
                        :class="{
                            'text-700': activeTab3 === 5,
                            'text-600': activeTab3 !== 5
                        }"
                    ></i>
                    <span
                        class="font-medium hidden md:block"
                        :class="{
                            'text-900': activeTab3 === 5,
                            'text-600': activeTab3 !== 5
                        }"
                        >Team Plan</span
                    >
                </a>
            </li>
        </ul>
        <span class="p-input-icon-right w-full mt-2 md:mt-0 md:w-15rem">
            <i class="pi pi-search"></i>
            <InputText type="text" placeholder="Search" class="w-full md:w-15rem border-round" />
        </span>
    </nav>
    <section class="surface-overlay px-4 lg:px-6 py-4 px-4 lg:px-6 border-top-1 surface-border">
        <div class="border-bottom-1 surface-border">
            <h2 class="mt-0 mb-2 text-900 font-bold text-4xl">Members & Roles</h2>
            <p class="mt-0 mb-5 text-700 font-normal text-base">You can easily manage your team on this page</p>
        </div>
        <section class="flex flex-wrap gap-3 py-6 justify-content-between border-bottom-1 surface-border">
            <div class="flex-shrink-0 w-15rem">
                <h3 class="mb-4 mt-0 text-900 font-medium text-xl">Members</h3>
                <p class="mb-4 mt-0 text-700 font-normal text-base">Manage your member in this project</p>
                <Button label="Invite a member" class="w-auto"></Button>
            </div>
            <div class="overflow-x-scroll">
                <DataTable :value="members" rowHover>
                    <Column style="min-width: 25rem">
                        <template #header>
                            <span class="font-semibold text-sm text-color-secondary">Name</span>
                        </template>
                        <template #body="{ data }">
                            <div class="flex align-items-center gap-3">
                                <Avatar :image="'/images/blocks/avatars/circle/' + data.image + '.png'" class="mr-2" size="large" shape="circle"></Avatar>
                                <div>
                                    <p class="mt-0 mb-2 font-medium text-lg text-color-primary">
                                        {{ data.name }}
                                    </p>
                                    <p class="mt-0 mb-2 font-normal text-base text-color-secondary">
                                        {{ data.username }}
                                    </p>
                                </div>
                            </div>
                        </template>
                    </Column>
                    <Column style="min-width: 14rem">
                        <template #header>
                            <span class="font-semibold text-sm text-color-secondary">Joined Date</span>
                        </template>
                        <template #body="{ data }">
                            <p class="mt-0 mb-2 font-normal text-base text-color-secondary">
                                {{ data.date }}
                            </p>
                        </template>
                    </Column>
                    <Column style="min-width: 13rem">
                        <template #header>
                            <span class="font-semibold text-sm text-color-secondary">Last Active</span>
                        </template>
                        <template #body="{ data }">
                            <p class="mt-0 mb-2 font-normal text-base text-color-secondary">
                                {{ data.active }}
                            </p>
                        </template>
                    </Column>
                    <Column style="min-width: 8rem">
                        <template #body>
                            <Button type="button" icon="pi pi-ellipsis-v" class="p-button-text p-button-secondary" @click="$refs.menu.toggle($event)"></Button>
                            <Menu ref="menu" appendTo="body" popup :model="items"></Menu>
                        </template>
                    </Column>
                </DataTable>
            </div>
        </section>
        <section class="flex flex-wrap gap-3 py-6 justify-content-between border-bottom-1 surface-border">
            <div class="flex-shrink-0 w-15rem">
                <h3 class="mb-4 mt-0 text-900 font-medium text-xl">Roles</h3>
                <p class="mb-4 mt-0 text-700 font-normal text-base">Edit roles in this project</p>
                <Button label="Add a role" class="w-auto"></Button>
            </div>
            <div class="overflow-x-scroll">
                <DataTable :value="roles" rowHover>
                    <Column style="min-width: 25rem">
                        <template #header>
                            <span class="font-semibold text-sm text-color-secondary">Alias Name</span>
                        </template>
                        <template #body="{ data }">
                            <div class="flex align-items-center">
                                <span class="border-circle mr-2" :class="data.color" style="width: 7px; height: 7px"></span>
                                <p class="mt-0 mb-0 font-medium text-lg text-color-primary">
                                    {{ data.alias }}
                                </p>
                            </div>
                        </template>
                    </Column>
                    <Column style="min-width: 14rem">
                        <template #header>
                            <span class="font-semibold text-sm text-color-secondary">Last Edit</span>
                        </template>
                        <template #body="{ data }">
                            <p class="mt-0 mb-0 font-normal text-base text-color-secondary">
                                {{ data.date }}
                            </p>
                        </template>
                    </Column>
                    <Column style="min-width: 13rem">
                        <template #header>
                            <span class="font-semibold text-sm text-color-secondary">Users</span>
                        </template>
                        <template #body="{ data }">
                            <p class="mt-0 mb-0 font-normal text-base text-color-secondary">
                                {{ data.users }}
                            </p>
                        </template>
                    </Column>
                    <Column style="min-width: 8rem">
                        <template #body>
                            <Button type="button" icon="pi pi-ellipsis-v" class="p-button-text p-button-secondary" @click="$refs.menu.toggle($event)"></Button>
                            <Menu ref="menu" appendTo="body" popup :model="items"></Menu>
                        </template>
                    </Column>
                </DataTable>
            </div>
        </section>
    </section>
</BlockViewer>