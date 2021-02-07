import React, {useState} from 'react';
import SeccionForm from './SeccionForm';
import SeccionRadio from './SeccionRadio';
import Encabezado from './Encabezado';
import Resultados from './Resultados';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faIceCream, faChartLine, faBox, faBoxes, faCalculator, faCode } from '@fortawesome/free-solid-svg-icons'
import { Modal, Button } from 'react-bootstrap';

function Example() {
    const [show, setShow] = useState(false);
  
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
  
    return (
      <>
        <Button variant="primary" onClick={handleShow}>
          Launch demo modal
        </Button>
  
        <Modal show={show} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Resultados de Optimización</Modal.Title>
          </Modal.Header>
          <Modal.Body><Resultados /> </Modal.Body>
          <Modal.Footer>
            <Button variant="primary" onClick={handleClose}>
              Aceptar
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
}

class FormOptimizacion extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            resultados: false,
        }
    }

    mostrarResultados = (e) =>{
        //e.preventDefault();
        this.setState({resultados: true})
    }

    ocultarResultados = () =>{
        this.setState({resultados: false})
    }


    render(){
        return(
            <div>
                <Encabezado titulo = "Optimización lineal" descripcion = "Optimización de la producción semanal de helados." icono = {faCode}/>
                <form action='/resultados' method="get" onSubmit={this.mostrarResultados}>
                    <SeccionForm titulo = "Sabores a producir" nombreTipo= "Sabor" nombreCantidad = "Demanda" iconoTitulo =  {faIceCream} iconoCantidad = {faChartLine} nombreAPI ="helados" />
                    <SeccionForm titulo = "Materias primas disponibles" nombreTipo= "Materia Prima" nombreCantidad = "Disponibilidad" iconoTitulo =  {faBox} iconoCantidad = {faBoxes} nombreAPI="materiasprima"/>
                    <SeccionRadio nombre = 'Objetivo'/>
                    <button type="submit" className="btn btn-dark" ><FontAwesomeIcon icon = {faCalculator} /> Calcular</button>
                </form>
                <Modal show={this.state.resultados} onHide={this.ocultarResultados}>
                    <Modal.Header closeButton>
                        <Modal.Title>Resultados de Optimización</Modal.Title>
                    </Modal.Header>
                    <Modal.Body><Resultados /> </Modal.Body>
                    <Modal.Footer>
                        <Button variant="primary" onClick={this.ocultarResultados}>
                        Aceptar
                        </Button>
                    </Modal.Footer>
                </Modal>
            </div>
        );
    }
}

export default FormOptimizacion;