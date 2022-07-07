module.exports = {
  configureWebpack: {
    devtool: 'source-map'
  },
  pages: {
    index: {
      entry: 'src/main.js',
      template: 'public/index.html',
      filename: 'connect.html',
    },
    connect: {
      entry: 'src/pages/connect/connect.js',
      template: 'src/pages/connect/connect.html',
      filename: 'connect.html'
    },
  },
}