let pais = document.getElementById("pais");
/* funciones para validar input*/
function validarpais() {
    let span = document.getElementById("validpais");
    const regex = /^[A-Za-z]+$/;
    if (!regex.test(pais.value)) {
        //alert("Por favor, introduce solo caracteres de texto.");
        span.style = "display:block";
        span.innerText = "Por favor, introduce solo caracteres de texto.";
        span.className = "text-danger";
        pais.className = "form-control border-input-error";
        return false;
    } else {
        span.innerText = "";
        span.style = "display:none;";
        pais.className = "form-control border-input-ok";
        return true;
    }
}
pais.addEventListener("input", validarpais);

let capital = document.getElementById("capital");

function validarcapital() {
    let span = document.getElementById("validpais");
    const regex = /^[A-Za-z]+$/;
    if (!regex.test(capital.value)) {
        //alert("Por favor, introduce solo caracteres de texto.");
        span.style = "display:block";
        span.innerText = "Por favor, introduce solo caracteres de texto.";
        span.className = "text-danger";
        capital.className = "form-control border-input-error";
        return false;
    } else {
        span.innerText = "";
        span.style = "display:none;";
        capital.className = "form-control border-input-ok";
        return true;
    }
}
capital.addEventListener("input", validarcapital);


let continente = document.getElementById("continente");

function validarcontinente() {
    let span = document.getElementById("validcontinente");
    const regex = /^[A-Za-z]+$/;
    if (!regex.test(continente.value)) {
        //alert("Por favor, introduce solo caracteres de texto.");
        span.style = "display:block";
        span.innerText = "Por favor, introduce solo caracteres de texto.";
        span.className = "text-danger";
        continente.className = "form-control border-input-error";
        return false;
    } else {
        span.innerText = "";
        span.style = "display:none;";
        continente.className = "form-control border-input-ok";
        return true;
    }
}
continente.addEventListener("input", validarcontinente);


function validaridioma() {
    let span = document.getElementById("valididioma");
    const regex = /^[A-Za-z]+$/;
    if (!regex.test(idioma.value)) {
        //alert("Por favor, introduce solo caracteres de texto.");
        span.style = "display:block";
        span.innerText = "Por favor, introduce solo caracteres de texto.";
        span.className = "text-danger";
        idioma.className = "form-control border-input-error";
        return false;
    } else {
        span.innerText = "";
        span.style = "display:none;";
        idioma.className = "form-control border-input-ok";
        return true;
    }
}
idioma.addEventListener("input", validaridioma);



let array = []; //es un array o variable global

//consumir api
function getApi() {
    const url = "https://restcountries.com/v3.1/lang/spanish";
    fetch(url)
        .then(function(response) {
            //console.log(response.status);
            return response.json();
        })
        .then(function(data) {
            //console.log(data);
            //console.table(data);
            array = [];
            data.forEach((ob) => {
                const data_api = {
                    pais: ob.name.common,
                    capital: ob.capital[0],
                    continente: ob.continents[0],
                    idioma: ob.languages.spa,
                };
                array.push(data_api);
                actualizarTablaHtml();
            });
            console.table(array);
            //addSesionStorage();
            //console.table(obtieneSesionStorage());
        })
        .catch(function(error) {
            console.log(error);
        });
}

document.addEventListener("DOMContentLoaded", getApi);

function leerForms() {
    let valid0 = validarpais();
    let valid1 = validarcapital();
    let valid2 = validarcontinente();
    let valid3 = validaridioma();
    if (valid0 && valid1 && valid2 && valid3 == true) {
        // crear un objeto en javascript
        let objeto = {
            pais: pais.value,
            capital: capital.value,
            continente: continente.value,
            idioma: idioma.value,
            estado: false,
        };
        array.push(objeto); //agregar el objeto al array
        console.table(array); // mostrar la info del array en la console

        actualizarTablaHtml();
        // console.log(objeto);
    }
    //console.log(objeto);
    //validarTexto();
    //validarCorreo();
}

function actualizarTablaHtml() {
    let datosBody = document.getElementById("datosBody");
    datosBody.innerHTML = "";
    //recorrer el array que tiene los datos
    for (let i = 0; i < array.length; i++) {
        //crear la fila
        let fila = document.createElement("tr");
        //crear la columna  pais
        let columnapais = document.createElement("td");
        columnapais.textContent = array[i].pais; //pasar el dato
        fila.appendChild(columnapais); // add columna a la fila

        //crear la columna capital
        let columnacapital = document.createElement("td");
        columnacapital.textContent = array[i].capital; //pasar el dato
        fila.appendChild(columnacapital); // add columna a la fila

        //crear la columna continente
        let columnacontinente = document.createElement("td");
        columnacontinente.textContent = array[i].continente; //pasar el dato
        fila.appendChild(columnacontinente); // add columna a la fila

        //crear la columna idioma
        let columnaIdioma = document.createElement("td");
        columnaIdioma.textContent = array[i].idioma; //pasar el dato
        fila.appendChild(columnaIdioma); // add columna a la fila

        let columnaOPciones = document.createElement("td");
        //crear boton eliminar
        let btneliminar = document.createElement("button");
        btneliminar.textContent = "Eliminar";
        btneliminar.className = "btn btn-danger me-2";
        btneliminar.addEventListener("click", function() {
            eliminar(i);
        });
        columnaOPciones.appendChild(btneliminar);
        // crear otro boton
        let btnMarcar = document.createElement("button");
        btnMarcar.textContent = "Marcar";
        btnMarcar.className = "btn btn-primary";
        btnMarcar.addEventListener("click", function() {
            cambiaEstado(i);
        });
        columnaOPciones.appendChild(btneliminar);
        columnaOPciones.appendChild(btnMarcar);

        fila.appendChild(columnaOPciones);

        if (array[i].estado) {
            fila.className = "marcar-ok";
        }
        //add fila al tbody de la tabla html
        datosBody.appendChild(fila);
    }
}

function eliminar(i) {
    array.splice(i, 1);
    actualizarTablaHtml();
}

function cambiaEstado(i) {
    array[i].estado = !array[i].estado;
    //array[i].estado= !(false)  not, and, or
    //array[i].estado= true;

    actualizarTablaHtml();
}