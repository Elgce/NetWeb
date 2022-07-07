const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true
})

// // different screens
// const autoprefixer = require('autoprefixer');
// const pxtorem = require('postcss-pxtorem');
// module.exports = {
//   css: {
//     loaderOptions: {
//       css: {},
//       postcss: {
//         plugins:[
//           autoprefixer(),
//           pxtorem({
//             rootValue: 37.5,
//             propList: ['*'],
//             exclude: /web/i,
//             selectorBlackList: ['.a-']
//           }),
//         ]
//       }
//     }
//   }
// }