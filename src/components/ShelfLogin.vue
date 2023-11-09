<template>
  <div class="max-w-sm mx-auto mt-10">
    <h2 class="font-bold text-3xl text-center">ログイン</h2>
    <form
      @submit.prevent="onSubmitLogIn"
    >
      <div class="form-control w-full mt-3">
        <label class="label" for="usermail">
          <span class="label-text text-lg">メールアドレス</span>
        </label>
        <input
          id="usermail"
          type="email"
          placeholder=""
          class="input input-bordered w-full"
          v-model="usermail"
        />
      </div>
      <div class="form-control w-full mt-3">
        <label class="label" for="userpass">
          <span class="label-text text-lg">パスワード</span>
        </label>
        <input
          id="userpass"
          type="password"
          placeholder=""
          class="input input-bordered w-full"
          v-model="userpass"
        />
      </div>
      <p
        v-if="isFailed"
        class="text-red-600 px-3 py-2 w-full rounded bg-red-100 border-red-500 mt-5"
        role="alert"
      >
        ログインに失敗しました。
      </p>
      <button
        type="submit"
        class="btn btn-outline btn-success w-full mt-7"
        :class="{'btn-disabled': isPosting}"
      >
        ログイン
      </button>
    </form>
  </div>
</template>

<script>
import firebase from 'firebase/app';

// 状態の定数
const IS_DEFAULT = 'IS_DEFAULT';
const IS_POSTING = 'IS_POSTING'; // データを送信中
const IS_FAILED = 'IS_FAILED'; // ログインに失敗した

export default {
  data() {
    return {
      usermail: '',
      userpass: '',
      currentState: IS_DEFAULT,
    };
  },
  computed: {
    isPosting() {
      return this.currentState === IS_POSTING;
    },
    isFailed() {
      return this.currentState === IS_FAILED;
    },
  },
  methods: {
    // 状態を変更する
    toDefault() {
      this.currentState = IS_DEFAULT;
    },
    toPosting() {
      this.currentState = IS_POSTING;
    },
    toFailed() {
      this.currentState = IS_FAILED;
    },
    onSubmitLogIn() {
      firebase
        .auth()
        .signInWithEmailAndPassword(this.usermail, this.userpass)
        .then(() => {
          // ログインに成功したときの処理
          console.log('ログインしました');
          this.toDefault();
        })
        .catch((error) => {
          // ログインに失敗したときの処理
          console.error('ログインエラー', error);
          this.toFailed();
        });
    },
  },
};
</script>

<style>
</style>
