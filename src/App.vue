<template>
  <div id="app">
    <div v-if="currentUID !== null">
        <shelf-header @add-book="onAddBook"></shelf-header>
        <shelf-message></shelf-message>
        <shelf-books
          :books="books"
          @delete-book="onDeleteBook"
        >
        </shelf-books>
        <div class="toast toast-end">
          <div
            class="alert alert-error error-alert"
            :class="{ 'show': showErrorAlert }"
          >
            <div>
              <span>{{ errorMessage }}</span>
            </div>
          </div>
        </div>
    </div>
    <div v-else>
      <shelf-login></shelf-login>
    </div>
  </div>
</template>

<script>
import firebase from 'firebase/app';
import ShelfHeader from '@/components/ShelfHeader.vue';
import ShelfMessage from '@/components/ShelfMessage.vue';
import ShelfBooks from '@/components/ShelfBooks.vue';
import ShelfLogin from '@/components/ShelfLogin.vue';
import { getBooks, postBook, deleteBook } from '@/services/firebaseService';
// import { getBooks, deleteBook } from '@/services/bookService';

export default {
  components: {
    ShelfHeader, ShelfBooks, ShelfMessage, ShelfLogin,
  },

  data() {
    return {
      books: [],
      currentUID: null,
      showErrorAlert: false,
      errorMessage: '',
    };
  },

  async created() {
    // ログイン状態の変化を監視する
    firebase.auth().onAuthStateChanged((user) => {
      if (user) {
        console.log('状態：ログイン中');
        this.currentUID = user.uid;
        this.onGetBooks();
      } else {
        console.log('状態：ログアウト');
        this.currentUID = null;
      }
    });
  },

  methods: {
    makeToast(message) {
      this.errorMessage = message;
      this.showErrorAlert = true;
      setTimeout(() => {
        this.showErrorAlert = false;
        this.errorMessage = '';
      }, 5000);
    },
    async onAddBook(book) {
      const newBook = await postBook(book.title, book.image, book.encoded, book.memo);
      if (newBook) {
        this.books.push(newBook);
      } else {
        this.makeToast('書籍を追加できませんでした。');
      }
    },
    async onGetBooks() {
      this.books = await getBooks();
    },
    async onDeleteBook(id) {
      const success = await deleteBook(id);
      if (success) {
        this.books = this.books.filter((book) => book.id !== id);
      }
    },
  },
};
</script>

<style scoped>
.error-alert {
  animation: none;
  opacity: 0;
  transition: opacity 0.25s, transform 0.25s;
  transform: translateX(50%);
}
.error-alert.show {
  opacity: 1;
  transform: translateX(0);
}
</style>
