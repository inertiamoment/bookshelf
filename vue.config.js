module.exports = {
  devServer: {
    proxy: { '^/books': { target: process.env.VUE_APP_HOST_DB } },
    public: process.env.C9_PID
      ? `${process.env.C9_PID}.vfs.cloud9.ap-northeast-1.amazonaws.com`
      : 'localhost:8080',
  },
  // configureWebpackは、ビルド時のバンドルサイズ設定
  // バンドルサイズが以下の指定を超えると、ビルド時にwarningで教えてくれる
  // 参考: https://webpack.js.org/configuration/performance/
  configureWebpack: {
    performance: {
      maxAssetSize: 300e3, // 300kb
      maxEntrypointSize: 500e3, // 500kb
    },
  },
};
