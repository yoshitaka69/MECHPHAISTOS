<template>
	<!--AdminLTE copy-->
	<div class="base-content"> <!--AdminLTEのcssがわからなかったから適当に作った-->

		<section class="content-header">
			<div class="container-fluid">
				<div class="row mb-2">
					<div class="col-sm-6">
						<h1>Work Order</h1>
					</div>
					<div class="col-sm-6">
						<ol class="breadcrumb float-sm-right">
							<li class="breadcrumb-item"><a href="#">How to use detail</a></li>
							<li class="breadcrumb-item"><a href="#">Spare parts list</a></li>
							<li class="breadcrumb-item active">MECHPHAISTOS</li>
						</ol>
					</div>
				</div>
			</div>
		</section>


		<section class="content">
			<div class="card card-solid">
				<!--Tabはsakai-vue-template-->

				<TabView>
					<TabPanel header="Work permission">
						<p class="line-height-3 m-0">
						</p>
					</TabPanel>
					<TabPanel header="Work Order List">
						<p class="line-height-3 m-0">
						</p>
					</TabPanel>
					<TabPanel header="Work order">
						<p class="line-height-3 m-0">
						</p>
					</TabPanel>
				</TabView>
			</div>
		</section>
	</div>
</template>