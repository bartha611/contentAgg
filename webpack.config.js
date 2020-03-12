module.exports = {
  entry: "./frontend/src/blah.jsx",
  output: {
    path: `${__dirname}/frontend/static/frontend/`,
    filename: "bundle.js"
  },
  resolve: {
    extensions: [".js", ".jsx"]
  },
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: ["babel-loader", "eslint-loader"]
      }
    ]
  },
  watchOptions: {
    poll: true,
    ignored: /node_modules/
  }
};
