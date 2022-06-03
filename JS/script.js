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


