var webpack = require('webpack');
var path = require('path');

module.exports = {
    devtool: 'inline-source-map',
    entry: [
        // 'webpack-dev-server/client?http://127.0.0.1:8080/',
        // 'webpack/hot/only-dev-server',
        './startupfairy/static/js/category.js'
    ],
    output: {
        path: path.join(__dirname, 'startupfairy/static'),
        filename: 'bundle.js'
    },
    resolve: {
        modulesDirectories: ['node_modules', 'startupfairy/static/js'],
        extensions: ['', '.js']
    },
    module: {
        loaders: [
        {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loaders: ['babel?presets[]=react,presets[]=es2015']
        }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoErrorsPlugin()
    ],
    watch: true
};