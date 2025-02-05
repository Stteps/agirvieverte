const Path = require('path');
const Webpack = require('webpack');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: {
    "base": Path.resolve(__dirname, '../src/pages/base.js'),
    "index": Path.resolve(__dirname, '../src/pages/Index/index.js'),
    "about": Path.resolve(__dirname, '../src/pages/About/index.js'),
    "blog": Path.resolve(__dirname, '../src/pages/Blog/index.js'),
  },
  output: {
    path: Path.join(__dirname, '../build'),
    filename: 'js/[name].js',
    publicPath: '/static/',
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name(module) {
            // get the name. E.g. node_modules/packageName/not/this/part.js
            // or node_modules/packageName
            const packageName = module.context.match(
              /[\\/]node_modules[\\/](.*?)([\\/]|$)/
            );

            if(packageName) {
              // npm package names are URL-safe, but some servers don't like @ symbols
              return `npm.${packageName[1].replace("@", "")}`;
            } else {
              return;
            }
          }
        },
      }
    },
  },
  plugins: [
    new Webpack.ProvidePlugin({
      $: 'jquery',
      jQuery: 'jquery',
      "window.jQuery": 'jquery',
    }),
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [
        {
          from: Path.resolve(__dirname, '../src/assets/locales'),
          to: 'locales/[path][name].[hash][ext]'
        }
      ],
    }),
    new BundleTracker({ 
      path: Path.join(__dirname, '../'),
      filename: 'webpack-stats.json',
      indent: 1,
    }),
  ],
  resolve: {
    alias: {
      '~': Path.resolve(__dirname, '../src'),
    },
  },
  module: {
    rules: [
      {
        test: /\.mjs$/,
        include: /node_modules/,
        type: 'javascript/auto',
      },
      {
        test: /\.html$/i,
        loader: 'html-loader',
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|svg|webp)$/,
        type: 'asset/resource',
        generator: {
          filename: 'images/[name][ext]'
        }
      },
      {
        test: /\.(eot|otf|ttf|woff|woff2)$/,
        type: 'asset/resource',
        generator: {
          filename: 'webfonts/[name][ext]'
        }
      },
      {
        test: /\.(pdf)$/,
        type: 'asset/resource',
        generator: {
          filename: 'documents/[name][ext]'
        }
      },
    ],
  },
};
