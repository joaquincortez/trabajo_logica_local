import React from 'react';
import axios from "axios";

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const respuestas = {
    "fracaso": "Se ha producido un error.",
    "opcion_no_disponible": "El objetivo de optimización indicado no está disponible.",

};

class ResultadosPacking extends React.Component{

    constructor(props){
        super(props)
        this.state = {
            datos: [],
        }
    }

    usarQuery() {
        const search = window.location.href; 
        let params =  new URLSearchParams(search)
        return params;
    }

    requestResults = (data) => {
        axios
        .post("http://localhost:8000/packing/", data)
        .then(res => {
            console.log(res);
            this.setState({ datos: res.data })})
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        
        let capacidadCamiones = []
        let helados = [];
        let tamanos = [];
        let cantCajas = []
        console.log(" parametros es ",parametros)
        parametros[0][0] = "camion1"; //porque devuelve como primero toda la url
        let i=0;
        while(i< parametros.length && "camion".localeCompare(parametros[i][0].substring(0,6)) === 0){
            capacidadCamiones.push(parametros[i][1]);
            i++;
        }
        for(i; i<parametros.length; i+=3){
            helados.push(parametros[i][1]);
            tamanos.push(parametros[i+1][1]);
            cantCajas.push(parametros[i+2][1]);
        }

        let data = { capacidades: capacidadCamiones, helados:helados, tamanos: tamanos, cantidades: cantCajas}
        console.log("data es: ",data);
        this.requestResults(data)

    }

    render(){
        const datos = this.state.datos
        return(
            <div>
                <h1>Resultados packing</h1>
                <div>
                    {this.state.datos["resultado"] === "fracaso" && 
                        <div>
                        <h3 className="text-danger">{respuestas[this.state.datos["resultado"]]}</h3>
                        <p>{respuestas[this.state.datos["razon_fracaso"]]}</p>
                        </div>}
                    {this.state.datos["resultado"] ==="exito" &&
                    <div> 
                        <h5>Se ha almacenado un valor total en los {datos.camiones.length} camiones de ${datos.valor_total}.</h5>
                        <h5>Se ha almacenado un peso total en los {datos.camiones.length} camiones de {datos.peso_total}kg.</h5>
                        {datos.camiones.map(camion =>
                            <div>
                                <h5>Camión - Capacidad {camion.capacidad}kg.</h5>
                                <ul>
                                    {camion.carga.map(carga =>
                                    <li>Se han almacenado {carga.cantidad} cajas de {carga.peso}kg de {carga.item} - Aportando un valor de ${carga.valor} y un peso de {carga.peso * carga.cantidad}kg.</li>
                                    )}
                                </ul>
                                <p>En total, el camión ha almacenado un valor total de ${camion.valor_camion} y un peso de {camion.peso_camion}kg.</p>
                            </div>    
                        )}

                    </div>}
                </div>
            </div>
        )
    }
}

export default ResultadosPacking;