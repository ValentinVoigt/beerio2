const path = require('path');
const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = {
	entry: './beerio2/static/index.js',
	output: {
		path: path.resolve(__dirname, 'beerio2', 'static', 'public', 'dist'),
		filename: '[name].js'
	},
	plugins: [
		new webpack.ProvidePlugin({
			$: 'jquery',
			jQuery: 'jquery',
			'window.jQuery': 'jquery',
			Popper: ['popper.js', 'default'],
		}),
		new ExtractTextPlugin("[name].css"),
		new UglifyJsPlugin()
	],
	module: {
		loaders: [
			{
				test: /\.css$/,
				loader: ExtractTextPlugin.extract({
					use: "css-loader"
				})
			}
		]
	}
};
