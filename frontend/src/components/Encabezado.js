import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import React from 'react';;
function Encabezado(props){
    return(
        <div>
            <h1 className="display-4"><FontAwesomeIcon icon={props.icono} /> {props.titulo}</h1>
            <p className="lead">{props.descripcion}</p>
            <hr></hr>
        </div>
    )
}

export default Encabezado;