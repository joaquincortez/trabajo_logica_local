import React from 'react';

class LineaCarga extends React.Component{
    render(){
        return(
            <div className="form-group row">
                <div className="col-5 text-center">
                    <select name = {"helado"+this.props.nro}  className="custom-select" id="inputGroupSelect01" required>
                        <option id="-1" value="" >Seleccionar helado</option>
                        {this.props.helados.map(dato => (<option key = {dato.id} id={dato.id} value= {dato.id}>{dato.nombre}</option>))}
                    </select>
                </div>
                <div className="col-4 text-center">
                    <select name = {"tamano"+this.props.nro}  className="custom-select" id="inputGroupSelect01" required>
                        <option id="-1" value="" >Seleccionar tamaño de cajas</option>
                        <option id="1" value="10" >Caja pequeña (10kg)</option>
                        <option id="2" value="20" >Caja mediana (20kg)</option>
                        <option id="3" value="50" >Caja grande (50kg)</option>
                    </select>
                </div>
                <div className="col-3 text-center">
                    <div className="input-group">
                        <input name = {"cantidad"+this.props.nro} type="number" className="form-control" aria-label="Cantidad de cajas" placeholder="Ingresar cantidad" required min="1"></input>
                        <div className="input-group-append">
                            <span className="input-group-text">Cajas</span>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default LineaCarga;