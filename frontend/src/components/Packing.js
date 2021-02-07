import React from 'react';
import Encabezado from './Encabezado';
import ResultadosPacking from './ResultadosPacking';
import SeccionCamiones from './SeccionCamiones';
import SeccionCarga from './SeccionCarga';
import {faBoxes, faCalculator} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';

class Packing extends React.Component{

    onHandleSubmit = (e)=> {
        e.persist();
    }

    render(){
        return(
            <div>
                <Encabezado titulo = "Packing" descripcion = "Optimizar el espacio." icono = {faBoxes} />
                <form action =  '/packing' method="get" onSubmit={this.onHandleSubmit} >
                    <SeccionCamiones />
                    <hr className="espacioAbajo"></hr>
                    <SeccionCarga/>
                    <hr className="espacioAbajo"></hr>
                    <button type="submit" className="btn btn-dark" ><FontAwesomeIcon icon = {faCalculator} /> Calcular</button>
                    <hr className="espacioAbajo"></hr>
                    <ResultadosPacking/>
                </form>
            </div>
        )
    }
}

export default Packing;