import * as React from "react";
import {
  Navbar,
  NavbarBrand,
  NavbarToggler,
  Collapse,
  NavItem,
  Nav,
  NavLink
} from "reactstrap";

interface props {
  changeFilter: (filter: string) => void;
}

const Navigation = ({ changeFilter }: props) => {
  const [open, setOpen] = React.useState<boolean>(true);
  const toggle = () => {
    setOpen(!open);
  };
  return (
    <div>
      <Navbar color="light" light expand="md">
        <NavbarBrand onClick={() => changeFilter("")}>Newsall</NavbarBrand>
        <NavbarToggler onClick={toggle} />
        <Collapse isOpen={open} navbar>
          <Nav className="mr-auto" navbar>
            <NavItem>
              <NavLink onClick={() => changeFilter("general")}>General</NavLink>
            </NavItem>
            <NavItem>
              <NavLink onClick={() => changeFilter("business")}>
                Business
              </NavLink>
            </NavItem>
            <NavItem>
              <NavLink onClick={() => changeFilter("sports")}>Sports</NavLink>
            </NavItem>
            <NavItem>
              <NavLink onClick={() => changeFilter("technology")}>
                Technology
              </NavLink>
            </NavItem>
            <NavItem>
              <NavLink onClick={() => changeFilter("Entertainment")}>
                Entertainment
              </NavLink>
            </NavItem>
            <NavItem>
              <NavLink onClick={() => changeFilter("science")}>Science</NavLink>
            </NavItem>
          </Nav>
        </Collapse>
      </Navbar>
    </div>
  );
};

export default Navigation;
