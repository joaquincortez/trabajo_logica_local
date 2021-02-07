import React from 'react';
import LineaCarga from './LineaCarga'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlus, faTruckLoading } from '@fortawesome/free-solid-svg-icons'
import axios from "axios";

class SeccionCarga extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            cargas: [1],
            helados : [],
        }

    }

    cargarHelados = () =>{
        axios
        .get("http://localhost:8000/api/helados/")
        .then(res => this.setState({ helados: res.data }))
        .catch(err => console.log(err));
      }

    AgregarCarga = () =>{
        console.log("hola")
        let nuevaCarga = this.state.cargas.length + 1;
        this.setState( prevState => ({cargas: prevState.cargas.concat([nuevaCarga])}))
        console.log(this.state.helados)
    }

    componentDidMount(){
        this.cargarHelados()
    }

    render(){
        return(
            <div>
                <h2><FontAwesomeIcon icon={faTruckLoading}/> Carga</h2>
                <p>Especificar para cada sabor de helado, cuantas cajas y de qué tamaño.</p>
                <div className="form-group row">
                    <div className="col-5 text">
                        <h4>Helado</h4>
                    </div>
                    <div className="col-4 text">
                        <h4>Tamaño</h4>
                    </div>
                    <div className="col-3">
                        <h4>Cantidad</h4>
                    </div>
                </div>
                {this.state.cargas.map(carga => <LineaCarga key = {carga} nro = {carga} helados = {this.state.helados}/> )}
                <button type="button" className="btn btn-secondary" id="agregarCarga" onClick = {this.AgregarCarga}><FontAwesomeIcon icon={faPlus}/> Agregar carga</button>

            </div>
                
        )
    }
}

export default SeccionCarga;