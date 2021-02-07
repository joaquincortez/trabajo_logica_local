import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';
import SeccionDato from './SeccionDato';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import axios from "axios";


class SeccionForm extends React.Component{

  constructor(props){
    super(props)
    this.state = {
      nuevosInputs: [1,2],
      datos: [],
    }
    this.AgregarOpcion = this.AgregarOpcion.bind(this);
  }

  AgregarOpcion(){
    let nuevoInput = this.state.nuevosInputs.length;
    this.setState( prevState => ({nuevosInputs: prevState.nuevosInputs.concat([nuevoInput])}))
  }

  mostrarItems(){
    axios
    .get("http://localhost:8000/api/"+this.props.nombreAPI+ "/")
    .then(res => this.setState({ datos: res.data }))
    .catch(err => console.log(err));
  }

  componentDidMount(){
    this.mostrarItems();
  }

  render(){
      return(
          <div className="seccionForm">
              <div className="encabezado">
          <h2><FontAwesomeIcon icon = {this.props.iconoTitulo} /> {this.props.titulo}</h2>
          <div className="form-group row">
            <div className="col-9 text">
              <h4>{this.props.nombreTipo}</h4>
            </div>
            <div className="col-3">
              <h4><FontAwesomeIcon icon = {this.props.iconoCantidad} /> {this.props.nombreCantidad}</h4>
            </div>
          </div>
        </div>
        <div>
          {this.state.nuevosInputs.map(input => <SeccionDato nombre={this.props.nombreTipo.replace(/\s/g, '').toLowerCase()} key = {input.id} datos = {this.state.datos} nro = {input}/> )}
        </div>
          <button type="button" className="btn btn-secondary" id="agregarSabor" onClick = {this.AgregarOpcion}><FontAwesomeIcon icon={faPlus}/> Agregar {this.props.nombreTipo}</button>
        </div>
      )
  }
}

export default SeccionForm;