import React, { useEffect, useState } from "react";
import axios from "axios";

const Dashboard = () => {
  const [articles, setArticles] = useState([]);
  const [error, setError] = useState(false);
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/articles")
      .then(response => {
        setArticles(response.data);
      })
      .catch(err => {
        console.log(err);
        setError(true);
      });
  });
  return (
    <div>
      {articles.map(article => {
        return (
          <div>
            <a href={article.url}>{article.title}</a>
          </div>
        );
      })}
      {error && (
        <div>
          <h1>Error in retrieving Articles</h1>
        </div>
      )}
    </div>
  );
};

export default Dashboard;
