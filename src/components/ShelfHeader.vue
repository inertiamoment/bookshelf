<template>
  <div class="navbar bg-base-100 justify-between">
    <a href="./index.html" class="btn btn-ghost">
      <img src="@/assets/logo.png" alt="Bookshelf"/>
    </a>
     <div class="flex gap-3">
    <shelf-modal
      @add-book="onAddBook"
    >
    </shelf-modal>
    <button
        @click="onClickLogOut"
        class="btn btn-sm btn-outline"
      >
        ログアウト
      </button>
      </div>
  </div>
</template>

<script>
import firebase from 'firebase/app';
import ShelfModal from '@/components/ShelfModal.vue';

export default {
  components: { ShelfModal },
  methods: {
    onAddBook(book) {
      this.$emit('add-book', book);
    },
    onClickLogOut() {
      firebase
        .auth()
        .signOut() // ログアウト実行
        .then(() => {
          // ログアウトに成功したときの処理
          console.log('ログアウトしました');
        })
        .catch((error) => {
          // ログアウトに失敗したときの処理
          console.error('ログアウトエラー', error);
        });
    },
  },
};
</script>
