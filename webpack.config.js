module.exports = {
  entry: "./frontend/src/index.jsx",
  output: {
    path: `${__dirname}/frontend/static/frontend/`,
    filename: "bundle.js"
  },
  extensions: [".js", ".jsx"],
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.jsx?/,
        exclude: /node_modules/,
        use: ["babel-loader", "eslint-loader"]
      }
    ]
  }
};
