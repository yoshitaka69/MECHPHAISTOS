<template>
    <div class="bookshelf">
      <h1>My Bookshelf</h1>
      <div class="books">
        <div v-for="book in books" :key="book.id" class="book-item">
          <Book :book="book" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import Book from './Book.vue';
  
  export default {
    components: { Book },
    data() {
      return {
        books: [
          {
            id: 1,
            title: 'Book 1',
            documents: [
              { id: 101, title: 'Document 1-1', content: 'Content of Document 1-1' },
              { id: 102, title: 'Document 1-2', content: 'Content of Document 1-2' }
            ]
          },
          {
            id: 2,
            title: 'Book 2',
            documents: [
              { id: 201, title: 'Document 2-1', content: 'Content of Document 2-1' },
              { id: 202, title: 'Document 2-2', content: 'Content of Document 2-2' }
            ]
          }
        ]
      };
    }
  };
  </script>
  
  <style>
  .bookshelf {
    padding: 20px;
    background-color: #f5f5f5;
  }
  
  .books {
    display: flex;
    gap: 10px;
    align-items: flex-end;
  }
  
  .book-item {
    width: 150px;
    height: 250px;
    background-color: #8b4513;
    border-radius: 5px;
    position: relative;
    box-shadow: 3px 3px 5px rgba(0, 0, 0, 0.1);
  }
  </style>
  