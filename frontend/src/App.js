import React from 'react';
import NavBar from './components/NavBar';
import FormOptimizacion from './components/FormOptimizacion';
import Resultados from './components/Resultados';
import Scheduling from './components/Scheduling'
import Packing from './components/Packing';
import Routing from './components/Routing';
import ResultadosPacking from './components/ResultadosPacking'
import ResultadosScheduling from './components/ResultadosScheduling'
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
                  <Route path = '/resultados' exact><Resultados /></Route>
                  <Route path = '/resultadospacking' exact ><ResultadosPacking /></Route>
                  <Route path = '/resultadosscheduling' exact ><ResultadosScheduling /></Route>
                  <Route path = '/scheduling' exact><Scheduling /></Route>
                  <Route path = '/routing' exact><Routing /></Route>
                  <Route path = '/packing' exact><Packing /></Route>
                </Switch>
              </div>
            </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
