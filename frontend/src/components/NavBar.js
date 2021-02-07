import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';


class NavBar extends React.Component{
    render(){
        return(
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <a className="navbar-brand" href="/">Panel Optimización</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
            </button>
        
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav mr-auto">
                <li className="nav-item active">
                <a className="nav-link" href="/">Optimización lineal<span className="sr-only">(current)</span></a>
                </li>
                <li className="nav-item active">
                <a className="nav-link" href="/packing" tabIndex="-1" aria-disabled="false">Packing</a>
                </li>
                <li className="nav-item active">
                <a className="nav-link" href="/scheduling" tabIndex="-1" aria-disabled="false">Scheduling</a>
                </li>
                <li className="nav-item active">
                <a className="nav-link" href="/routing" tabIndex="-1" aria-disabled="false">Routing</a>
                </li>
                <li className="nav-item active">
                <a className="nav-link" href="http://127.0.0.1:8000/admin/">Panel de administración</a>
                </li>
            </ul>
            </div>
        </nav>
        );
    }
}

export default NavBar; 