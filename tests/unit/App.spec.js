import { randomBytes } from 'crypto';
import {
  getByText,
  render,
  screen,
  waitFor,
  waitForElementToBeRemoved,
} from '@testing-library/vue';
import userEvent from '@testing-library/user-event';
import App from '@/App.vue';
import { getBooks } from '@/services/bookService';

// 書籍を登録して削除する結合テスト
test('①書籍を登録できる。②登録した書籍を一覧画面に表示できる。③登録した書籍を削除できる', async () => {
  render(App);

  // DBに保存された書籍データを取得する
  const booksBeforePost = await getBooks();

  // 新たな書籍データを登録する
  await userEvent.click(screen.getByText(/書籍の登録/));

  const inputTitleElm = screen.getByLabelText('タイトル');
  const inputImageElm = screen.getByLabelText('表紙画像');

  // 初期は画像サムネイルは非表示
  expect(screen.queryByAltText('アップロード画像')).toBeNull();

  // フォームにタイトルを入力する。入力値は一意であれば良いので、randomBytesメソッドの引数（24）に意味はない
  const title = randomBytes(24).toString('hex');
  userEvent.type(inputTitleElm, title);
  expect(inputTitleElm).toHaveValue(title);

  // フォームに画像をアップロードする
  const file = new File(['book'], 'book.png', { type: 'image/png' });
  userEvent.upload(inputImageElm, file);
  expect(inputImageElm.files.item(0)).toStrictEqual(file);
  expect(inputImageElm.files).toHaveLength(1);

  // アップロードした画像のサムネイルを表示する
  let uploadImage = '';
  await waitFor(() => {
    // 画像サムネイルが表示されること
    const previewImageElm = screen.getByAltText('アップロード画像');
    uploadImage = previewImageElm.getAttribute('src');
    expect(uploadImage).toMatch(/^data:image\/png;base64/);
  });

  // DBに書籍データを保存する
  userEvent.click(screen.getByText(/保存する/));

  // 登録した書籍が、一覧画面に表示されるまで待つ
  await waitFor(() => {
    expect(screen.getByLabelText(title)).toBeInTheDocument();
  });

  // 一覧画面に表示された書籍の削除ボタンをクリックする
  const deleteBtnElm = getByText(screen.getByLabelText(title), /削除/);
  userEvent.click(deleteBtnElm);

  await waitForElementToBeRemoved(() => screen.getByLabelText(title));
  expect(screen.queryByLabelText(title)).not.toBeInTheDocument();

  // 書籍の登録前と、登録→削除後で、DBのデータが一致している
  const booksAfterPost = await getBooks();
  expect(booksBeforePost.length).toBe(booksAfterPost.length);
  expect(booksBeforePost).toEqual(booksAfterPost);
});
