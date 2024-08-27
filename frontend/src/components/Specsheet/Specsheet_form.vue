<template>
  <div class="specification-form">
    <div class="pages">
      <!-- Page 1: Cover Page -->
      <div class="page cover-page">
        <div class="outer-box">
          <div class="inner-box">
            <div class="form-fields">
              <input v-model="companyName" type="text" placeholder="会社名" />
              <input v-model="title" type="text" placeholder="タイトル" />
              <input v-model="date" type="date" placeholder="日付" />
              <input v-model="revisionDate" type="date" placeholder="改定日" />
            </div>
          </div>
        </div>
      </div>

      <!-- Page 2: Content Page with Vertical Line and Aligned Forms -->
      <div v-for="(page, index) in pages" :key="index" class="page content-page">
        <div class="content-layout">
          <div class="left-side">
            <input v-model="page.leftInput" type="text" placeholder="左側の入力フォーム" />
          </div>
          <div class="vertical-line"></div>
          <div class="right-side" @contextmenu.prevent="showContextMenu($event, index)">
            <input v-model="page.rightInput" type="text" placeholder="右側の入力フォーム" />
          </div>
        </div>
      </div>
    </div>

    <div class="buttons">
      <button @click="addPage">ページを追加</button>
      <button @click="generatePDF">PDF作成</button>
    </div>

    <!-- Context Menu -->
    <ul v-if="isContextMenuVisible" :style="{ top: `${contextMenuY}px`, left: `${contextMenuX}px` }" class="context-menu">
      <li @click="insertImage">画像を入力</li>
      <li @click="addColumn">列の追加</li>
    </ul>
  </div>
</template>

<script>
import jsPDF from 'jspdf';
import html2canvas from 'html2canvas';

export default {
  data() {
    return {
      companyName: '',
      title: '',
      date: '',
      revisionDate: '',
      pages: [
        {
          leftInput: '',
          rightInput: ''
        }
      ], // Initial page for page 2
      isContextMenuVisible: false,
      contextMenuX: 0,
      contextMenuY: 0,
      selectedPageIndex: null
    };
  },
  methods: {
    addPage() {
      this.pages.push({ leftInput: '', rightInput: '' });
    },
    generatePDF() {
      const pdf = new jsPDF('p', 'mm', 'a4');
      const pages = document.querySelectorAll('.page');
      pages.forEach((page, index) => {
        if (index > 0) {
          pdf.addPage();
        }
        html2canvas(page).then((canvas) => {
          const imgData = canvas.toDataURL('image/png');
          pdf.addImage(imgData, 'PNG', 0, 0, 210, 297);
          if (index === pages.length - 1) {
            pdf.save('specification.pdf');
          }
        });
      });
    },
    showContextMenu(event, index) {
      this.contextMenuX = event.clientX;
      this.contextMenuY = event.clientY;
      this.isContextMenuVisible = true;
      this.selectedPageIndex = index;
      document.addEventListener('click', this.hideContextMenu);
    },
    hideContextMenu() {
      this.isContextMenuVisible = false;
      document.removeEventListener('click', this.hideContextMenu);
    },
    insertImage() {
      alert('画像を入力');
      this.hideContextMenu();
    },
    addColumn() {
      alert('列の追加');
      this.hideContextMenu();
    }
  }
};
</script>

<style scoped>
.specification-form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.pages {
  display: flex;
  flex-direction: row;
}

.page {
  width: 210mm; /* A4 width */
  height: 297mm; /* A4 height */
  margin: 10px;
  border: 1px solid black;
  box-sizing: border-box;
  background-color: white; /* White background */
  position: relative;
}

.cover-page .outer-box {
  width: 100%;
  height: 100%;
  border: 3px solid black; /* Bold outer border */
  display: flex;
  align-items: center;
  justify-content: center;
}

.cover-page .inner-box {
  width: 80%;
  height: 80%;
  border: 1px solid black; /* Thin inner border */
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.form-fields {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

input {
  margin-top: 10px;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  box-sizing: border-box;
}

input::placeholder {
  color: lightgray; /* Light gray placeholder text */
}

.content-page .content-layout {
  display: flex;
  height: calc(100% - 20px); /* Adjust height to align with the top edge */
  padding-top: 10px; /* Adjust for alignment */
  box-sizing: border-box;
}

.content-page .vertical-line {
  width: 1px;
  background-color: black;
  position: absolute;
  left: 25%; /* 1/4 from the left */
  top: 10px; /* Align with the top padding */
  bottom: 10px; /* Align with the bottom */
}

.left-side {
  width: 25%; /* Align with the vertical line */
  padding-left: 10px;
}

.right-side {
  width: 75%; /* Fill the remaining space */
  padding-right: 10px;
}

.left-side input, .right-side input {
  width: 100%;
  height: 100%;
}

.buttons {
  margin-top: 20px;
  display: flex;
  gap: 10px;
}

/* Context Menu Styles */
.context-menu {
  position: absolute;
  list-style-type: none;
  margin: 0;
  padding: 5px;
  background-color: white;
  border: 1px solid #ccc;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  z-index: 1000;
}

.context-menu li {
  padding: 8px 12px;
  cursor: pointer;
}

.context-menu li:hover {
  background-color: #eee;
}
</style>
