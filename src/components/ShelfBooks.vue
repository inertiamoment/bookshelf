<template>
  <div class="p-5">
    <div class="max-w-5xl mx-auto">
      <div
        v-if="books.length === 0"
        class="alert alert-info max-w-2xl mx-auto"
      >
        登録された本はありません。
      </div>
      <div v-else class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-5">
        <div
          v-for="{ id, title, image, memo } in books"
          :key="id"
          class="card card-compact bg-base-100 shadow"
          :aria-label="title"
        >
          <figure>
            <img :src="image" alt="" class="w-full" />
          </figure>
          <div class="card-body justify-between p-2">
            <h2 class="card-title font-semibold text-base">{{ title }}</h2>
            <!-- メモのセクションを表示 -->
            <p v-if="memo" class="text-sm text-gray-600">{{ memo }}</p>
            <div class="card-actions justify-end">
              <button
                class="btn btn-sm btn-outline btn-error pr-4"
                @click="deleteBook(id)"
              >
                <trash-icon></trash-icon>削除
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { TrashIcon } from 'vue-tabler-icons';

export default {
  components: { TrashIcon },
  props: {
    books: {
      type: Array,
      required: true,
    },
  },
  methods: {
    deleteBook(bookId) {
      // 親コンポーネントに 'delete-book' イベントを発行する
      this.$emit('delete-book', bookId);
    },
  },
};
</script>
