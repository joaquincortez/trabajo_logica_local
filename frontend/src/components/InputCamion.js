import React from 'react';

class InputCamion extends React.Component{
    render(){
        return(
            <div className="form-inline">
                <div className="form-group mb-2">
                    <input type="text" readonly className="form-control-plaintext" id="staticEmail2" value= {"Camion " + this.props.nro} />
                </div>
                <div className="form-group mx-sm-3 mb-2">
                <div className="input-group">
                        <input required min = "100" name = {"camion"+ this.props.nro} type="number" className="form-control" aria-label="Cantidad en kg" placeholder="Ingresar capacidad"></input>
                        <div className="input-group-append">
                            <span className="input-group-text">kg</span>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default InputCamion;