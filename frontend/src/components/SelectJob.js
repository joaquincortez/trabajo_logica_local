import React from 'react';

class SelectJob extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            datos: [],
            orden : ["primer", "segundo", "tercer", "cuarto", "quinto","sexto","septimo","octavo", "noveno", "decimo", "decimo primer",
            "decimo segundo", "decimo tercer", "decimo cuarto", "decimo quinto"],
        }
    }

    render(){
        return(
            <div>
                <select required name = {this.props.nombre} className="custom-select mr-sm-2" id="inlineFormCustomSelect">
                    <option value="">Elegir {this.state.orden[this.props.nro]} helado a producir...</option>
                    {this.props.datos.map(dato => (<option name={this.props.nombre} key = {dato.id} id={dato.id} value= {dato.id}>{dato.nombre}</option>))}
                </select>

            </div>
            
        )
    }
}

export default SelectJob;