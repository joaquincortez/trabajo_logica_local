import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import '../css/optimizacion.css';

class OpcionRadio extends React.Component{
    render(){ //revisar value
        return(
            <div className="form-check">
                  <input className="form-check-input" type="radio" name="objetivo" value={this.props.nombre.replace(/\s/g, '').toLowerCase()} defaultChecked = {this.props.checked}></input> 
                  <label className="form-check-label">
                    {this.props.nombre}
                  </label>
            </div>
        );
    }
}

export default OpcionRadio;
