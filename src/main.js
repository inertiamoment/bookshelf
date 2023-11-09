import Vue from 'vue';
import firebase from 'firebase/app';
import App from './App.vue';
import './app.css';
import 'firebase/auth';
import 'firebase/firestore';
import 'firebase/storage';

Vue.config.productionTip = false;

const firebaseConfig = {
  apiKey: 'AIzaSyAJ1y3gXwnLrUrXrVwRoH2jFlddnQY_ARg',
  authDomain: 'bookshelf2-8dda9.firebaseapp.com',
  projectId: 'bookshelf2-8dda9',
  storageBucket: 'bookshelf2-8dda9.appspot.com',
  messagingSenderId: '98110608737',
  appId: '1:98110608737:web:26a99dd71f44c81dd6e120',
};

firebase.initializeApp(firebaseConfig);

new Vue({
  render: (h) => h(App),
}).$mount('#app');
