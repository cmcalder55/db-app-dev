// Filename - "./components/Navbar.js

import React from "react";
import { Nav, NavLink, NavMenu } from "./NavbarElements";

const Navbar = () => {
    const activeStyle = { color: 'red', fontWeight: 'bold' }; // Example style object

    return (
        <>
            <Nav>
                <NavMenu>
                    <NavLink to="/" activeStyle={activeStyle}>
                        Home
                    </NavLink>
                    <NavLink to="/Arborist" activeStyle={activeStyle}>
                        Arborist
                    </NavLink>
                    <NavLink to="/Builds" activeStyle={activeStyle}>
                        Builds
                    </NavLink>
                    <NavLink to="/PriceMaster" activeStyle={activeStyle}>
                        PriceMaster
                    </NavLink>
                    <NavLink to="/Sherpa" activeStyle={activeStyle}>
                        Sherpa
                    </NavLink>
                    <NavLink to="/Wiki" activeStyle={activeStyle}>
                        Wiki
                    </NavLink>
                </NavMenu>
            </Nav>
        </>
    );
};


export default Navbar;
