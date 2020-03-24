const BundleTracker = require("webpack-bundle-tracker");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = {
  entry: "./frontend/static/index.tsx",
  output: {
    path: `${__dirname}/frontend/static/dist`,
    filename: "[name]-[hash].js"
  },
  resolve: {
    extensions: [".js", ".jsx", ".ts", ".tsx"]
  },
  devtool: "source-map",
  module: {
    rules: [
      {
        test: /\.tsx?/,
        exclude: /node_modules/,
        use: ["ts-loader"]
      },
      {
        test: /\.css/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },
  plugins: [
    new BundleTracker({ filename: "./webpack.stats.json" }),
    new CleanWebpackPlugin()
  ],
  watchOptions: {
    poll: true,
    ignored: /node_modules/
  }
};
