<template>
	<table class="table table-bordered table-responsive" id="rMatrix">
		<thead>
			<tr>
				<th></th>
				<th colspan="2">STATUS OF EVENT</th>
				<th colspan="5">RISK CLASS</th>
			</tr>
		</thead>
		<tbody>
			<tr lh="5">
				<td rowspan="5" class="r-header" style="text-align:center">LIKELIHOOD OF EVENT HAPPENING</td>
				<td style="min-width:50px">5</td>
				<td>It is or has already happened</td>
				<td class="M">M</td>
				<td class="H">H</td>
				<td class="H">H</td>
				<td class="VH">VH</td>
				<td class="VH">VH</td>
			</tr>
			<tr lh="4">
				<td>4</td>
				<td>It will probably happen</td>
				<td class="M">M</td>
				<td class="M">M</td>
				<td class="H">H</td>
				<td class="VH">VH</td>
				<td class="VH">VH</td>
			</tr>
			<tr lh="3">
				<td>3</td>
				<td>It could possibly Happen</td>
				<td class="L">L</td>
				<td class="M">M</td>
				<td class="M">M</td>
				<td class="H">H</td>
				<td class="H">H</td>
			</tr>
			<tr lh="2">
				<td>2</td>
				<td>It is to Happen</td>
				<td class="L">L</td>
				<td class="L">L</td>
				<td class="M">M</td>
				<td class="M">M</td>
				<td class="H">H</td>
			</tr>
			<tr lh="1">
				<td>1</td>
				<td>It is unlikely to Happen</td>
				<td class="L">L</td>
				<td class="L">L</td>
				<td class="L">L</td>
				<td class="M">M</td>
				<td class="M">M</td>
			</tr>
			<tr>
				<td rowspan="3" class="r-header">LIKELY OUTCOME OF EVENT</td>
				<td colspan="2" class="r-header">SAFETY</td>
				<td>Near Miss</td>
				<td>Minor Inquiry</td>
				<td>Lost Time Accident</td>
				<td>Major Inquiry</td>
				<td>Fatality</td>
			</tr>
			<tr>
				<td colspan="2" class="r-header">ENVIRONMENT</td>
				<td>Potential Event</td>
				<td>Minor Event</td>
				<td>Important Event</td>
				<td>Significant Event</td>
				<td>Major Event</td>
			</tr>
			<tr>
				<td colspan="2" class="r-header">COST</td>
				<td>&lt; 1k $ </td>
				<td>&lt; 10k $ </td>
				<td>&lt; 100k $ </td>
				<td>&lt; 300k $ </td>
				<td>&gt; 500k $</td>
			</tr>
			<tr>
				<td></td>
				<td colspan="2" class="r-header">SEVERITY</td>
				<td s="1">1</td>
				<td s="2">2</td>
				<td s="3">3</td>
				<td s="4">4</td>
				<td s="5">5</td>
			</tr>
		</tbody>
	</table>
</template>
  
<script>
export default {
	mounted() {
		// rowIndexとcolumnIndexの取得はVueのデータとして扱い、jQueryを使用しない方法で行うことが推奨されます。
		const rowIndex = 3; // 仮の値
		const columnIndex = 3; // 仮の値
		try {
			if (rowIndex !== undefined && columnIndex !== undefined) {
				const column = this.$el.querySelector(`#rMatrix tbody td[s='${columnIndex}']`).cellIndex;
				const cell = this.$el.querySelector(`#rMatrix tbody tr[lh='${rowIndex}']`).cells[column];
				cell.style.border = '3px solid';
				cell.style.boxShadow = '-5px 5px 20px 20px rgba(14, 1, 1, 0.17), -15px -11px 20px 5px rgba(14, 14, 14, 0.22)';
				cell.style.borderStyle = 'dashed';
			}
		} catch (ex) {
			console.error(ex);
		}
	},
};
</script>
  
<style scoped>
/* スタイルは scoped を使用してコンポーネント内に閉じ込めることができます */
.VH {
	background-color: #f90909;
	font-weight: 550 !important;
}

.H {
	background-color: #f99d09;
	font-weight: 550 !important;
}

.M {
	background-color: #f9d909;
	height: 60px;
	font-weight: 550 !important;
}

.L {
	background-color: #4c7c04;
	font-weight: 550 !important;
}

#rMatrix>tbody>tr>td,
#rMatrix>tbody>tr>th,
#rMatrix>tfoot>tr>td,
#rMatrix>tfoot>tr>th,
#rMatrix>thead>tr>td,
#rMatrix>thead>tr>th {
	vertical-align: middle;
	text-align: center;
	font-weight: 550;
}
</style>
  