// Filename - App.js

import React from "react";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

import Home from "./pages";
import Arborist from "./pages/Arborist";
import BuildView from "./pages/Builds";
import PriceMaster from "./pages/PriceMaster";
import Sherpa from "./pages/Sherpa";
import SiteMap from "./pages/Wiki";
// import CraftSim from "./pages/ModPredictor/CraftSimulator"
// import TimelessSim from "./pages/ModPredictor/Timeless"

import "./App.css";

function App() {
    return (
        <Router>
            <Navbar />
            <Routes>
                <Route exact path="/" element={<Home />} />
                {/* pages  */}
                <Route path="/Arborist" element={<Arborist />} />
                <Route path="/Builds" element={<BuildView />} />
                <Route path="/PriceMaster" element={<PriceMaster />} />
                <Route path="/Sherpa" element={<Sherpa />} />
                <Route path="/Wiki" element={<SiteMap />} />
            </Routes>
        </Router>
    );        
}

// function App() {
//     return (
//         <Router>
//             <div>
//                 <nav>
//                     <ul>
//                         <li><Link to="/">Home</Link></li>
//                         <li><Link to="/Arborist">Arborist</Link></li>
//                         <li><Link to="/Builds">Builds</Link></li>
//                         <li><Link to="/PriceMaster">PriceMaster</Link></li>
//                         <li><Link to="/Sherpa">Sherpa</Link></li>
//                         <li><Link to="/Wiki">Wiki</Link></li>
//                     </ul>
//                 </nav>
//                 <Routes>
//                     <Route path="/" element={<Home />} />
//                     <Route path="/Arborist" element={<Arborist />} />
//                     <Route path="/Builds" element={<BuildView />} />
//                     <Route path="/PriceMaster" element={<PriceMaster />} />
//                     <Route path="/Sherpa" element={<Sherpa />} />
//                     <Route path="/Wiki" element={<SiteMap />} />
//                 </Routes>
//             </div>
//         </Router>
//     );
// }

export default App;

