// MASCARA PARA GARANTIR QUE A ALTURA MINIMA SEJA 0 E MAIOR 999
document.getElementById('altura').addEventListener('input', function(e) {
    let value = parseInt(e.target.value);

    if (value < 0) {
        e.target.value = 0;

    } else if (value > 999) {
        e.target.value = 999;
    }
});

// MASCARA PARA GARANTIR QUE O PESO MINIMO SEJA 0 E O MAXIMO 999
document.getElementById('peso').addEventListener('input', function(e) {
    let value = parseInt(e.target.value);

    if (value < 0) {
        e.target.value = 0;

    } else if (value > 999) {
        e.target.value = 999;
    }
});

// EVENTO PARA BUSCAR OS VALORES DE ALTURA E PESO QUANDO CLICADO EM CALCULAR
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.btn-calcular').addEventListener('click', function(){
        // OBTEM VALOR DO PESO
        var peso = document.getElementById('peso').value
        
        // OBTEM VALOR DA ALTURA
        var altura = document.getElementById('altura').value

        // CASO NÃO TENHA INSERIDO NENHUM VALOR NOS CAMPOS
        if (peso.length == 0 || altura.length == 0){
            alert('Preencha todos os campos!')
        }

        // CASO TENHA INSERIDO TODOS OS VALORES
        // IRA FAZER A REQUISIÇÃO
        else{
            fetch('/calcular_imc', {
                method: 'POST',
                headers: {
                    'Content-Type':'application/json'
                },
                body: JSON.stringify({peso: peso, altura: altura})
        
            })
            .then(response=>response.json())

            .then(data=>{
                var imc = data.imc
                var grau = data.grau

                alert(`
                    Seu IMC é ${imc}
                    Seu grau é: ${grau}`)

            })
        }
    })
})