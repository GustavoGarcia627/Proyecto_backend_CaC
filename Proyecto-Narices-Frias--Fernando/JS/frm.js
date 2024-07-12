/*DECLARACION DE VARIABLES*/
const   $submit = document.getElementById('submit');
        $nombre = document.getElementById('nombre');
        $apellido = document.getElementById('apellido');
        $sexo = document.getElementById('sexo');
        $telefono = document.getElementById("telefono");
        $email = document.getElementById("email");
        $asunto = document.getElementById("asunto");
        $termino = document.getElementById("termino");
        $error = document.getElementById('error');


/*DECLARACION DE LAS FUNCIONES PARA VALIDAR LOS CAMPOS*/
function validarinputs(){
/*DECLARACION EXPRESIONES REGULARES PARA LOS CAMPOS*/
    const nombreRegex = /^[a-zA-ZÀ-ÿ\s]{1,40}$/; // Letras y espacios, pueden llevar acentos.
    const apellidoRegex = /^[a-zA-ZÀ-ÿ\s]{1,40}$/; // Letras y espacios, pueden llevar acentos.
	const correoRegex = /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/;
	const telefonoRegex =  /^\d{7,14}$/; // 7 a 14 numeros.
    const asuntoRegex = /^[a-zA-ZÀ-ÿ\s]{1,300}$/; // Letras y espacios, pueden llevar acentos.


/*VALIDANDO CAMPOS*/
    if($nombre.value === null || $nombre.value === ""){
        alert("Por favor complete el campo Nombre");
        return false;
    }

    if($apellido.value === null || $apellido.value === ""){
        alert("Por favor complete el campo Apellido");
        return false;
    }

    if(!document.querySelector('input[name="sexo"]:checked')) {
        alert('Por favor indique el sexo');
        return false;
    }

    if($telefono.value === null || $telefono.value === ""){
        alert("Por favor complete el campo Telefono");
        return false;
    }

    if($email.value === null || $email.value === ""){
        alert("Por favor complete el campo Email");
        return false;
    }

    if($asunto.value === null || $asunto.value === ""){
        alert("Por favor indique la razon del contacto o un asunto.");
        return false;
    }

    if($termino.checked === false){
        alert("Por favor acepte los terminos");
        return false;
    }



/*VALIDANDO EXPRESIONES*/
    if(!nombreRegex.test($nombre.value)){
        alert("Ingrese un nombre en formato correcto");
        $nombre.style.border = "2px solid red";
        return false;
    } 

    if(!apellidoRegex.test($apellido.value)){
        alert("Ingrese su Apellido en formato correcto");
        $apellido.style.border = "2px solid red";
        return false;
    } 

    if(!telefonoRegex.test($telefono.value)){
        alert("Ingrese su Telefono en formato correcto");
        $telefono.style.border = "2px solid red";
        return false;
    } 
    
    if(!correoRegex.test($email.value)){
        alert("Ingrese el Correo/email en formato correcto");
        $email.style.border = "2px solid red";
        return false;
    } 

    if(!asuntoRegex.test($asunto.value)){
        alert("Ingrese el asunto en formato correcto");
        $asunto.style.border = "2px solid red";
        return false;
    } 

    var mensajito = "Hola, "+$nombre.value+" "+$apellido.value+" Pronto nos pondremos en contacto con vos!";
    alert(mensajito);
    console.log(mensajito);    
    formulario.reset();

    return true

}

/*VALIDANDO QUE FUNCIONE EL BOTON ENVIAR Y QUE NO SE ENVIE NADA POR DEFECTO*/
/*TAMBIEN SE LLAMA LA FUNCION PARA VALIDAR LOS IMPUTS POR CADA UNO DE LOS CAMPOS*/
document.addEventListener("click", (e)=>{
    if(e.target === $submit){
        e.preventDefault();
        validarinputs();
    }
});