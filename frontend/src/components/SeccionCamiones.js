import React from 'react';
import InputCamion from './InputCamion';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlus, faTruck } from '@fortawesome/free-solid-svg-icons'

class SeccionCamiones extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            inputCamiones:[1],
        }

    }

    AgregarCamion = () =>{
        console.log("hola")
        let nuevoInput = this.state.inputCamiones.length + 1;
        this.setState( prevState => ({inputCamiones: prevState.inputCamiones.concat([nuevoInput])}))
      }

    render(){
        return(
            <div>
                <h2><FontAwesomeIcon icon={faTruck}/> Camiones</h2>
                <p>Especificar cantidad de camiones y capacidad de cada uno.</p>
                {this.state.inputCamiones.map(input => <InputCamion key = {input} nro = {input}/> )}
                <button type="button" className="btn btn-secondary seccionCamion" id="agregarCamion" onClick={this.AgregarCamion} ><FontAwesomeIcon icon={faPlus}/> Agregar camión</button>
            </div>
                
        )
    }
}

export default SeccionCamiones;