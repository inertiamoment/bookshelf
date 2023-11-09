import axios from 'axios';

const dbAccessor = axios.create({
  // baseURLは、Cloud9で単体テストをするための設定
  baseURL: process.env.NODE_ENV === 'test' ? process.env.VUE_APP_HOST_DB : '',
});

export const getBooks = async () => {
  const { data } = await dbAccessor.get('/books');
  return data;
};
export const postBook = (title, image, memo) => dbAccessor.post('/books', { title, image, memo });
export const deleteBook = (id) => dbAccessor.delete(`/books/${id}`);
