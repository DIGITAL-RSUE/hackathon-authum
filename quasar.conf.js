const { configure } = require('quasar/wrappers');
const { resolve } = require('path');
const { config } = require('dotenv');

module.exports = configure(function (ctx) {
  return {
    supportTS: {
      tsCheckerConfig: {
        eslint: {
          enabled: true,
          files: './src/**/*.{ts,tsx,js,jsx,vue}',
        },
      }
    },

    boot: [
      'axios',
    ],

    css: [
      'app.sass'
    ],

    extras: [
      'roboto-font',
      'material-icons',
    ],

    build: {
      vueRouterMode: 'history',
      env: config().parsed,
      chainWebpack(chain) {
        chain.resolve.alias
          .set('hooks', resolve(__dirname, './src/hooks/'))
          .set('images', resolve(__dirname, './src/assets/images/'))
          .set('models', resolve(__dirname, './src/models/index.ts'))
          .set('store', resolve(__dirname, './src/store/'))
      },
    },

    devServer: {
      server: {
        type: 'http'
      },
      port: 8080,
      open: true
    },

    framework: {
      config: {},
      plugins: []
    },

    animations: [],

    ssr: {
      pwa: false,

      prodPort: 3000,

      maxAge: 1000 * 60 * 60 * 24 * 30,

      chainWebpackWebserver(/* chain */) {
        //
      },

      middlewares: [
        ctx.prod ? 'compression' : '',
        'render'
      ]
    },
  }
});
