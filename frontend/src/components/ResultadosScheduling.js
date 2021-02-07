import React from 'react';
import axios from "axios";
import { Chart } from "react-google-charts";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faCalendarAlt, faPlus, faCalculator } from '@fortawesome/free-solid-svg-icons';
import Encabezado from './Encabezado';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

class ResultadosScheduling extends React.Component{

    constructor(props){
        super(props)
        this.state = {
            datos: [],
            datosGrafico: [],
        }
    }

    usarQuery() {
        const search = window.location.href; // could be '?foo=bar'
        let params =  new URLSearchParams(search)
        return params;
    }

    requestResults = (hel) => {
        axios
        .post("http://localhost:8000/scheduling/", {helados: hel})
        .then(res => {
            console.log(res);
            this.setState({ datos: res.data });
            this.handleGrafico(res.data.rows);
        })
        .catch(err => {console.log(err)});
    }

    componentDidMount(){
        let query = this.usarQuery();
        let parametros = Array.from(query.entries());
        let id_helados = [];
        console.log(" parametros es ",parametros)
        if(parametros != null){
            parametros[0][0] = "sabor1"; //porque devuelve como primero toda la url
            for (let i=0; i<parametros.length; i++){
                console.log(parametros[i])
                id_helados.push(parametros[i][1])
            }
            console.log("id helados es",id_helados);
            this.requestResults(id_helados);
        }
        console.log("state aca es",this.state.datos);
        console.log("rows es",this.state.datos.rows);

    }

    handleGrafico = (filas) =>{

        console.log("state ES",this.state)

        let sumaHoras = (horas) =>{
            var dt = new Date();
            console.log("antes dt es", dt)
            dt.setHours( dt.getHours() + horas );
            console.log("despues dt es ", dt)
            return dt;
        }
    
        let corrige_horas = (rows) =>{
            for(let i =0; i < rows.length; i++){
                rows[i][3] = sumaHoras(rows[i][3]);
                rows[i][4] = sumaHoras(rows[i][4]);
            }
            return rows
        }
        
        let nuevo_filas = corrige_horas(filas);

        let datos_graph= [
            [
                { type: 'string', label: 'Task ID' },
                { type: 'string', label: 'Task Name' },
                { type: 'string', label: 'Resource' },
                { type: 'date', label: 'Start Date' },
                { type: 'date', label: 'End Date' },
                { type: 'number', label: 'Duration' },
                { type: 'number', label: 'Percent Complete' },
                { type: 'string', label: 'Dependencies' },
            ]
        ].concat(nuevo_filas);
        
        this.setState({datosGrafico: datos_graph})

        console.log("datos grafico es", this.state.datosGrafico)
    }

    render(){
        return(
            <div>
                <Encabezado titulo = "Scheduling" descripcion = "Optimizar el orden a la hora de utilizar maquinas para realizar tareas." icono = {faCalendarAlt} />
                <h5>La duración óptima es de {this.state.datos.duracion_optima} horas.</h5>
                <div style={{ display: 'flex', maxWidth: 900 }}>
                    <Chart
                        width={'100%'}
                        height={'2000px'}
                        chartType="Gantt"
                        loader={<div>Loading Chart</div>}
                        data={this.state.datosGrafico}
                        rootProps={{ 'data-testid': '3' }}
                    />
                </div>
            </div>
        )
    }
}

export default ResultadosScheduling;