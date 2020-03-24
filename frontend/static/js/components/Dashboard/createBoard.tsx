import * as React from "react";
import { Col, Row } from "reactstrap";
import axios from "axios";
import * as types from "../../types/index";

axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const createBoard = (websites: types.website[], fil: string) => {
  const [filteredWebsites, setFilteredWebsites] = React.useState<
    types.website[][]
  >([]);
  React.useEffect(() => {
    setFilteredWebsites([]);
    const newSites: types.website[] = websites.slice(0);
    const sites: types.website[] =
      fil.length === 0
        ? newSites
        : newSites.filter(
            website => website.category.toUpperCase() === fil.toUpperCase()
          );
    console.log(sites);
    while (sites.length) {
      const layOutSite = sites.splice(0, 3);
      setFilteredWebsites(prevState => [...prevState, layOutSite]);
    }
  }, [fil, websites]);
  const addClicks = (site: types.website): void => {
    axios.put(`http://127.0.0.1:8000/api/articles/${site.id}`, {
      clicks: site.clicks + 1
    });
  };
  return (
    <div>
      {filteredWebsites.map(filteredSites => {
        return (
          <Row>
            {filteredSites.map(filteredSite => {
              return (
                <Col xs="12" lg="4" className="websites">
                  <h5>{filteredSite.name}</h5>
                  <ul>
                    {filteredSite.articles.map(article => {
                      return (
                        <li className="articles">
                          <a
                            href={article.url}
                            title={article.title}
                            onClick={(
                              e: React.MouseEvent<HTMLAnchorElement>
                            ) => {
                              e.preventDefault();
                              addClicks(filteredSite);
                              window.open(article.url);
                            }}
                          >
                            {article.title}
                          </a>
                        </li>
                      );
                    })}
                  </ul>
                </Col>
              );
            })}
          </Row>
        );
      })}
    </div>
  );
};

export default createBoard;
