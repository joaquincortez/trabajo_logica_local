import React from 'react';
import axios from "axios";
import { faCode }  from '@fortawesome/free-solid-svg-icons';
import Encabezado from './Encabezado';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const respuestas = {
    "fracaso": "Se ha producido un error.",
    "materia_insuficiente": "No se han seleccionado materias suficientes para producir ningún helado, intente nuevamente.",
    "opcion_no_disponible": "El objetivo de optimización indicado no está disponible.",
    "maximizacion_ganancias": "Maximizar las ganancias",
    "minimizacion_costos": "Minimizar los costos",
    "maximizacion_producción": "Maximizar la producción",

};

class Resultados extends React.Component{

    constructor(props){
        super(props)
        this.state = {
          datosHelado: [],
          datosMateria: [],
          resultOpt: {},
        }
    }

    usarQuery() {
        const search = window.location.href; // could be '?foo=bar'
        let params =  new URLSearchParams(search)
        return params;
    }

    enviarRequest(sabores){
        const json = JSON.stringify(sabores);
        axios.post('http://localhost:8000/calculos/', json, {
        headers: {
            'Content-Type': 'application/json'
        }
    });

    }

    requestHelado = (info) => {
        axios
        .post("http://localhost:8000/calculoshelado/", info)
        .then(res => {
            console.log(res);
            this.setState({ datosHelado: Object.keys(res.data).map((key) => [key, res.data[key]]) })})
        .catch(err => {console.log(err)});
    }

    requestMateria = (info) => {
        axios
        .post("http://localhost:8000/calculosmateria/", info)
        .then(res => {
            console.log(res);
            this.setState({ datosMateria: Object.keys(res.data).map((key) => [key, res.data[key]]) })})
        .catch(err => {console.log(err)});
    }

    requestAmbos = (helados, materias, objetivo) => {
        axios
        .post("http://localhost:8000/calculos/", {helados, materias, "objetivo": objetivo})
        .then(res => {
            console.log(res);
            this.setState({ resultOpt: res.data })})
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        let helados = {};
        let materias = {}
        parametros[0][0] = "sabor1"; //porque devuelve como primero toda la url
        console.log("parametros son", parametros);
        let i =0;
        for(i; i<parametros.length-1; i+=2){
            console.log("sabor".localeCompare(parametros[i][0].substring(0,5)) === 0)
            if("sabor".localeCompare(parametros[i][0].substring(0,5)) === 0){
                console.log('entro');
                helados[parametros[i][1]] = parametros[i+1][1];
                console.log(parametros[i][1] + " " + parametros[i+1][1])
            }
            else
                break;
        }

        for(i; i<parametros.length -1; i+=2){
            console.log('aca');
            materias[parametros[i][1]] = parametros[i+1][1];
        }

        let objetivo = parametros[parametros.length-1][1]
        console.log("sabores son", helados);
        console.log("materias son",materias);
        const resHelado = this.requestHelado(helados);
        console.log(resHelado);
        const resMateria = this.requestMateria(materias);
        console.log(resMateria);
        const resAmbos = this.requestAmbos(helados, materias, objetivo);
        console.log("respuesta ambos es", resAmbos);
    }

    render(){ 
        console.log(this.state.datosMateria);
        return(
            <div>
                <Encabezado titulo = "Optimización lineal" descripcion = "Resultados de la consulta." icono = {faCode}/>
                <div className="seccion-result">
                    <h2>Presupuesto en helados</h2>
                    {this.state.datosHelado.map(elem => 
                        <li>Total en {elem[0]} es ${elem[1]}</li>
                        )}
                </div>
                <div className="seccion-result">
                    <h2>Presupuesto en materias primas</h2>
                    {this.state.datosMateria.map(elem => 
                        <li>Total en {elem[0]} es ${elem[1]}</li>
                        )}
                </div>
                <div className="seccion-result">
                <h2>Respuesta de Optimización</h2>
                    <div>
                        {this.state.resultOpt["resultado"] === "fracaso" && 
                            <div>
                            <h3 className="text-danger">{respuestas[this.state.resultOpt["resultado"]]}</h3>
                            <p>{respuestas[this.state.resultOpt["razon_fracaso"]]}</p>
                            </div>}
                        {this.state.resultOpt["optimizacion"] && this.state.resultOpt["optimizacion"]["resultado"] ==="fracaso" && 
                        <div>
                            <h3 className="text-warning">El problema no tiene una solución óptima.</h3>
                            <p className="text-secondary">No se pudo encontrar una solución óptima para las restricciones seleccionadas.</p>
                        </div>}
                        {this.state.resultOpt["optimizacion"] && this.state.resultOpt["optimizacion"]["resultado"] ==="exito" &&
                        <div> 
                            <h4>Objetivo: {respuestas[this.state.resultOpt["optimizacion"]["objetivo"]]}</h4>
                            <h5>Se produjeron ganancias por ${this.state.resultOpt["optimizacion"]["objective_value"]}</h5>
                            <h5>Se deben producir las siguientes cantidades de helados para {respuestas[this.state.resultOpt["optimizacion"]["objetivo"]].toLowerCase()}:</h5>
                            <ul>
                                {this.state.resultOpt.optimizacion.soluciones.map(solucion =>
                                    <li>
                                        {console.log("solucion es", solucion)}
                                        {solucion.cantidad} unidades de {solucion.nombre}
                                    </li> )}
                            </ul>
                        </div>}
                    </div>
                </div>
            </div>
        )
    }
}

export default Resultados;