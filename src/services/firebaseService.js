import firebase from 'firebase/app';

export const postBook = async (title, image, encoded, memo) => {
  let addBook = null;
  if (!image) {
    // ファイルが選択されていないなら何もしない
    return null;
  }

  const bookTitle = title;
  const filename = image.name; // 画像ファイル名
  const bookImageLocation = `book-images/${filename}`; // 画像のアップロード先

  // Firestoreに送る書籍データ
  const bookData = {
    bookTitle,
    bookImageLocation,
    memo,
    createdAt: firebase.firestore.FieldValue.serverTimestamp(),
  };

  await firebase
    .storage()
    .ref(bookImageLocation)
    .put(image)// Storageへファイルアップロードを実行
    .then(() => {
      // Storageへのアップロードに成功したら、Firestoreに書籍データを保存する
      const docRef = firebase
        .firestore()
        .collection('books')
        .doc();

      docRef.set(bookData);
      addBook = {
        id: docRef.id,
        title: bookTitle,
        image: encoded,
        memo,
      };
    });

  return addBook;
};

export const getBooks = async () => {
  // 現在のbooksの値を取得
  const booksSnapshot = await firebase
    .firestore()
    .collection('books')
    .orderBy('createdAt')
    .get();
  const { docs } = booksSnapshot;
  const storage = firebase.storage();

  const books = [];
  for (let i = 0; i < docs.length; i += 1) {
    const doc = docs[i];
    const { bookImageLocation, bookTitle, memo } = doc.data();

    // Storageから、個々の書籍データに対応する表紙画像のURLを取得。次行のコメントは、ループ処理でawaitを使うため
    // eslint-disable-next-line no-await-in-loop
    const image = await storage.ref(bookImageLocation).getDownloadURL();

    books.push({
      id: doc.id,
      title: bookTitle,
      image,
      memo,
    });
  }
  return books;
};

export const deleteBook = async (id) => {
  // idからbookの値を取得
  const bookRef = firebase
    .firestore()
    .collection('books')
    .doc(id);
  const doc = await bookRef.get();

  // 読み込みエラー
  if (!doc.exists) {
    return false;
  }

  // 画像を削除
  const storage = firebase.storage();
  const { bookImageLocation } = doc.data();
  await storage.ref(bookImageLocation).delete();

  // データを削除
  bookRef.delete();

  return true;
};
