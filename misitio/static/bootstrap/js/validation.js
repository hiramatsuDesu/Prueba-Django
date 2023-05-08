function validar_campo(formulario){
    let nombre = document.forms["formulario"]["nombre"].value;
    let apellido = document.forms["formulario"]["apellido"].value;

    var valid = false;

    var num = /^[a-zA-Z\ áéíóúÁÉÍÓÚñÑ\s]*$/;

    
    if(nombre.match(num) == null){
        console.log("erroneo");
        return false;
    }
    else{
        console.log("no erroneo");

    }

    if(apellido.match(num) == null){
        console.log("erroneo");
        return false;

    }
    else{
        console.log("no erroneo");

    }
}


const alertPlaceholder = document.getElementById('liveAlertPlaceholder')
const appendAlert = (message, type) => {
  const wrapper = document.createElement('div')
  wrapper.innerHTML = [
    `<div class="alert alert-${type} alert-dismissible" role="alert">`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')

  alertPlaceholder.append(wrapper)
}

const alertTrigger = document.getElementById('liveAlertBtn')
if (alertTrigger) {
  alertTrigger.addEventListener('click', () => {
    appendAlert('Complete correctamente los campos', 'por favor')
  })
}
