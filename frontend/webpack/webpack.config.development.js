const Path = require('path');
const Webpack = require('webpack');
const { merge } = require('webpack-merge');
const ESLintPlugin = require('eslint-webpack-plugin');
const StylelintPlugin = require('stylelint-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const IconFontPlugin = require('icon-font-loader').Plugin;


const common = require('./webpack.common.js');

module.exports = merge(common, {
  target: 'web',
  mode: 'development',
  devtool: 'eval',
  output: {
    chunkFilename: 'js/[name].chunk.js',
    publicPath: 'http://0.0.0.0:8080/'
  },
  devServer: {
    client: {
      logging: 'error',
    },
    hot: true,
    host: "0.0.0.0",
    port: 8080,
    allowedHosts: 'all',
    devMiddleware: {
      writeToDisk: true
    },
    headers: {
      "Access-Control-Allow-Origin": "*",
    }
  },
  watchOptions: {
    poll: true,
  },
  plugins: [
    new Webpack.DefinePlugin({
      'process.env.NODE_ENV': JSON.stringify('development'),
    }),
    new ESLintPlugin({
      extensions: 'js',
      emitWarning: true,
      files: Path.resolve(__dirname, '../src'),
      fix: true,
    }),
    new StylelintPlugin({
      files: Path.join('src', '**/*.s?(a|c)ss'),
      fix: true,
    }),
    new MiniCssExtractPlugin({
      filename: 'css/[name].css'
    }),
    new IconFontPlugin({
      filename: 'webfonts/[name].[ext]?[hash]',
    })
  ],
  module: {
    rules: [
      {
        test: /\.html$/i,
        loader: 'html-loader',
      },
      {
        test: /\.js$/,
        include: Path.resolve(__dirname, '../src'),
        loader: 'babel-loader',
      },
      {
        test: /\.s?css$/i,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              sourceMap: true,
            },
          },
          'icon-font-loader',
          'postcss-loader',
          {
            loader: 'sass-loader',
            options: {
              sassOptions: {
                quietDeps: true,
                silenceDeprecations: ['import']   // WORKAROUND FOR BOOTSTRAP INCOMPATIBILITY WITH @USE SYNTAX
              }
            }
          }
        ],
      },
    ],
  },
});
