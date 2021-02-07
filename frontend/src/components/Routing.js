import React from 'react';
import Encabezado from './Encabezado';
import {faMapMarkedAlt } from '@fortawesome/free-solid-svg-icons';

class Routing extends React.Component{
    render(){
        return(
            <Encabezado titulo = "Routing" descripcion = "Optimizar el orden a la hora de utilizar maquinas para realizar tareas." icono = {faMapMarkedAlt} />
        )
    }
}

export default Routing;