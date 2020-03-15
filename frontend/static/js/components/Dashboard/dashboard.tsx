import * as React from "react";
import axios from "axios";
import * as types from "../../types/index";

const Dashboard = () => {
  const [websites, setWebsites] = React.useState<types.websites[]>([]);
  const [error, setError] = React.useState<boolean>(false);
  React.useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/articles")
      .then(response => {
        setWebsites(response.data);
      })
      .catch(err => {
        console.log(err);
        setError(true);
      });
  }, []);
  return (
    <div>
      {websites.map(website => {
        return (
          <div>
            <h3>{website.name}</h3>
            <div className="articles">
              {website.articles.map(article => {
                return (
                  <div>
                    <a style={{ color: "#000" }} href={article.url}>
                      {article.title}
                    </a>
                  </div>
                );
              })}
            </div>
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
