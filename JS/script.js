function validarlogin()
{
    var usuario=document.getElementById("user").value;
    var password=document.getElementById("pass").value;

    if(usuario=="user1" && password=="user1pass")
    {
        window.location="./index.html"
        //CAMBIAR AL PERFIL USUARIO 
    }
    else
    {
        alert("Datos invalidos")
    }
}

function validarRegistro()
{
    var nombre=document.getElementById("nombre").value;
    var correo=document.getElementById("correo").value;
    var contra=document.getElementById("pass2").value;
    var contra2=document.getElementById("pass3").value;
    if( nombre && correo && contra && contra2)
    {
        if(nombre.length>=4)
        {
            if(correo.includes("@gmail")||correo.includes("@hotmail")||correo.includes("@outlook")||correo.includes("@GMAIL")||correo.includes("@HOTMAIL")||correo.includes("@OUTLOOK"))
            {
                if(contra.length>=6)
                {
                    if(contra==contra2)
                    {
                        alert("Registrado correctamente");
                        window.location="./Paginalogin.html"
     

                    }
                    else{alert("Las contraseñas no son iguales.")}
                }
                else{alert("Contraseña debe tener almenos 6 caracteres");}
            }
            else{alert("Correo no contiene dominio");}
        }
        else {alert("El nombre debe tener almenos 4 caracteres");}

    }
    else{ alert("Datos invalidos")}
}


