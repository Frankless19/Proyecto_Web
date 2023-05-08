var fontSize = 1;

var objetos = document.getElementById('objetos');

function acercar(){
    fontSize += 0.1;
    document.body.style.fontSize = fontSize + "em";
    objetos.style.fontSize = fontSize + "em";
}

function alejar(){
    fontSize -= 0.1;
    document.body.style.fontSize = fontSize + "em";
    objetos.style.fontSize = fontSize - "em";
}