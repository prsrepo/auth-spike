const { defineConfig } = require('@vue/cli-service')

const pages = {
  index: "src/main.js",
};

module.exports = defineConfig({
  publicPath: "/static/vue/",
  outputDir: "./build/static/vue/",
  indexPath: "../../templates/vue_index.html",
  transpileDependencies: true,

  pages: pages,
  devServer: {
    port: 8081
  }
})