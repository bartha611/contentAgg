import * as React from "react";
import axios from "axios";
import { Container } from "reactstrap";
import createBoard from "./createBoard";
import * as types from "../../types/index";
import Navigation from "../Navigation/navigation";
import "./dashboard.css";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const Dashboard = () => {
  const [websites, setWebsites] = React.useState<types.website[]>([]);
  const [filter, setFilter] = React.useState<string>("");
  const [error, setError] = React.useState<boolean>(false);
  const changeFilter = (fil: string): void => {
    console.log("hello there");
    console.log(websites);
    setFilter(fil);
  };
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
      <Navigation changeFilter={changeFilter} />
      <Container>
        <div>{createBoard(websites, filter)}</div>
        {error && (
          <div>
            <h1>Error in retrieving Articles</h1>
          </div>
        )}
      </Container>
    </div>
  );
};

export default Dashboard;
