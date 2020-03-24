import * as React from "react";
import { render } from "react-dom";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";

import Dashboard from "./js/components/Dashboard/dashboard";

const App = () => {
  return (
    <Router>
      <Route path="/">
        <Dashboard />
      </Route>
    </Router>
  );
};

render(<App />, document.getElementById("root"));
