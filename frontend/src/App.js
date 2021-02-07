import React from 'react';
import NavBar from './components/NavBar';
import FormOptimizacion from './components/FormOptimizacion';
import Resultados from './components/Resultados';
import Scheduling from './components/Scheduling'
import Packing from './components/Packing'
import Routing from './components/Routing'
import './css/optimizacion.css';
import 'bootstrap/dist/css/bootstrap.css';


import {
  BrowserRouter as Router,
  Switch,
  Route,
} from "react-router-dom";


function App() {
  return (
    <Router>
      <div className="App">
        <NavBar />
        <div className = 'container'>
            <div className="jumbotron jumbotron-fluid">
              <div className="container">
                <Switch>
                  <Route path = '/' exact><FormOptimizacion /></Route>
                  <Route path = '/resultados' ><Resultados /></Route>
                  <Route path = '/scheduling' ><Scheduling /></Route>
                  <Route path = '/routing' ><Routing /></Route>
                  <Route path = '/packing' ><Packing /></Route>
                </Switch>
              </div>
            </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
