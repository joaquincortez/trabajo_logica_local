import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';
import OpcionRadio from './OpcionRadio';

class SeccionRadio extends React.Component{
    render(){
        return(
            <div className="seccionForm">
                <fieldset className="form-group">
                    <div className="row">
                        <legend className="col-form-label col-sm-2 pt-0">{this.props.nombre}</legend>
                        <div className="col-sm-10">
                            <OpcionRadio checked = "true" nombre='Maximizar ganancias'/>
                            <OpcionRadio nombre='Maximizar produccion'/>
                            <OpcionRadio nombre='Minimizar costos'/>
                        </div>
                    </div>
                </fieldset>
          </div>
        );
    }
}

export default SeccionRadio;
