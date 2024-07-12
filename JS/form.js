
/*DECLARACION DE VARIABLES*/
var nombre = document.getElementById('nombre');
var apellido = document.getElementById('apellido');
var telefono = document.getElementById("telefono");
var email = document.getElementById("email");
var error = document.getElementById('error');

/*DECLARACION DE LAS FUNCIONES PARA VALIDAR*/
function enviarform(){
 
    var mensajesError = [];

    if(nombre.value === ''){
        mensajesError.push('Por favor ingrese su Nombre');
    }

    if(apellido.value === null || apellido.value === ''){
        mensajesError.push('Por favor ingrese su Apellido');
    }

    if(telefono.value === null || telefono.value === ''){
        mensajesError.push('Por favor ingrese su numero de telefono');
    }

    if(email.value === null || email.value === ''){
        mensajesError.push('Debe indicar su correo');
    }

    error.innerHTML = mensajesError.join(', ');

    return false;
}