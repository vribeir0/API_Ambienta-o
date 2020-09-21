//fixar reload no topo do site
$(document).ready(function () {
    $(this).scrollTop(0);
});
//carregar tela do bot
function Inicializarbot(){
    var display = document.getElementById("chat_box").style.display
    if(display == "block"){
        document.getElementById("chat_box").style.display = "none";
    }else {
        document.getElementById("chat_box").style.display = "block";
        var input = document.getElementById("message");
        input.addEventListener("keyup", function(event) {
            if (event.keyCode === 13) {
            event.preventDefault();
            EnviarMensagem()
            }
        });
    }

};

function EnviarMensagem(){
    var divOut = document.createElement('div');
    var div = document.createElement('div');

    divOut.appendChild(div)
    div.innerHTML = document.getElementById('message').value;

    divOut.style.width = "100%";
    divOut.style.height = "42px";
    
    div.classList.add("fala_pessoa");

    document.getElementById("conversation").appendChild(divOut);
    document.getElementById("message").value = ""
    console.log("Mensagem enviada!!")

    var objScrDiv = document.getElementById("conversation");
    objScrDiv.scrollTop = objScrDiv.scrollHeight;
}

function MenssagemBot(message) {
    var divOut = document.createElement('div');
    var div = document.createElement('div');

    divOut.appendChild(div)
    div.innerHTML = message

    divOut.style.width = "100%";
    divOut.style.height = "42px";
    div.classList.add("fala_bot");

    document.getElementById("conversation").appendChild(divOut);

    
    var objScrDiv = document.getElementById("conversation");
    objScrDiv.scrollTop = objScrDiv.scrollHeight;
  }

function AbrirSNP(){
    
}


//carga de senha errada
function wrongpass(){
    swal.fire({
        heightAuto: false,
        title: 'Erro no acesso',
        text: 'Senha ou usuário incorreto.',
        confirmButtonColor: '#002d41',
        confirmButtonText: 'Tentar Novamente',
        timerProgressBar: 'true'
    }
    );
}
//limpar inputs - zerar filtros
window.onload = function () {
    document.getElementById('search').value = '';
    var filter = "";
}

//tabelas dinamicas no tutoriais
$(document).ready(function () {
    var table = $('#tutoriaistable').DataTable({
        "dom": '<"panel panel-default""<"panel-heading"<"row"<"mx-auto w-auto"l><"mx-auto w-auto"f>>>t<"panel-footer"<"row"<"mx-auto w-auto"i><"mx-auto w-auto text-center"p>>>>',
        "language": {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Portuguese-Brasil.json"
        },
        "columnDefs": [{ orderable: false, targets: [3, 4] }]
    });
});

//barra de busca dentro de cards de informação
function buscadicas() {
    var input, filter, cards, cardContainer, h4, title, i;
    input = document.getElementById("search");
    filter = input.value.toUpperCase();
    cardContainer = document.getElementById("conteudos");
    cards = cardContainer.getElementsByClassName("card border-mpf");
    for (i = 0; i < cards.length; i++) {
        title = cards[i].querySelector(".card-header");
        if (title.innerText.toUpperCase().indexOf(filter) > -1) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}
/*Ativar após configuração*/
//mudar cor da navbar no scroll assim que ela passar os slides
$(document).ready(function () {
    $(window).scroll(function () { // checar se scroll foi ativado
        if ($(document).scrollTop() > document.getElementById('carouselFull').offsetHeight) { // se a descida for maior que os slides
            $("#navbarCTIC").css("background-color", "#002d41"); // neste caso preenche
        } else {
            $("#navbarCTIC").css("background-color", "transparent"); // se não fica transparente
        }
    });
});

//Alerta de tutorial nao cadastrado
function tutnaocadastrado() {
    swal.fire({
        icon: 'error',
        title: 'Tutorial Não Cadastrado',
        text: 'Este tutorial ainda não foi cadastrado em nossa base.',
        confirmButtonColor: '#e74c3c',
        confirmButtonText: 'Ok',
    }
    );
}
//detecta browser firefox
function dectfirefox() {
    var sBrowser, sUsrAg = navigator.userAgent;
    if (sUsrAg.indexOf("Firefox") > -1) {
        swal.fire({
            icon: 'success',
            title: 'Cartilha Gerada com sucesso',
            confirmButtonColor: '#18bc9c',
            confirmButtonText: 'Ok',
            timer: 3000,
            timerProgressBar: 'true'
        }
        );
    } else {
        swal.fire({
            icon: 'warning',
            title: 'Cartilha Gerada com sucesso',
            text: 'Recomendamos o Mozilla Firefox para melhor construção do pdf.',
            confirmButtonColor: '#fd7e14',
            confirmButtonText: 'Ok',
            timer: 3000,
            timerProgressBar: 'true'
        }
        );
    }
}

//gera pdf com conteudo do site (versão beta)
function funcgerarpdf() {
    dectfirefox();
    var divContents = document.querySelectorAll(".cartilha");
    var printWindow = document.implementation.createHTMLDocument('');
    var i = 0;
    var j = 0;
    printWindow.open();
    printWindow.write('<html><head><title>DIV Contents</title>');
    printWindow.write('</head><body id="conteudo">');
    while (i < divContents.length) {
        printWindow.write(divContents[i].innerHTML);
        printWindow.write('<br>');
        console.log(divContents[i].innerHTML);
        console.log("----------------");
        i++;
    }
    printWindow.write('</body></html>');
    console.log(printWindow.innerHTML);
    printWindow.close();
    var doc = new jsPDF('p', 'px', 'a4');
    var options = {
        pagesplit: true
    };
    var specialElementHandlers = {
        '#editor': function (element, renderer) {
            return true;
        }
    };
    doc.fromHTML(printWindow.getElementById("conteudo"), 15, 15, {
        'width': 410,
        'elementHandlers': specialElementHandlers,
        'pagesplit': true,
    });
    doc.save('cartilha_ambientacaotecnologica.pdf');
};
