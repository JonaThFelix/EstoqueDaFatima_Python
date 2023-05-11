let image0 = document.getElementById('img0')


function selectPicture1() {
    image0.setAttribute('src', '../produtos/imagem/0/img1.jpg')
}

function selectPicture2() {
    image0.setAttribute('src', '../produtos/imagem/0/img2.jpg')
}

function selectPicture3() {
    image0.setAttribute('src', '../produtos/imagem/0/img3.jpg')
}

function selectPicture4() {
    image0.setAttribute('src', '../produtos/imagem/0/img4.jpg')
}

let number1 = document.getElementById('number')

function minus() {
    if (number1.value > 1)  {
        number1.setAttribute('value', `${number1.value - 1}`)
        return number1.value--
    }
    else {
        alert('Quantidade não pode ser menor do que 1')
    }
}

function plus() {
    number1.value++
    number1.setAttribute('value', `${number1.value + 1}`)
    if(number1.value > 20){
        alert('Chegou na quantidade MÁXIMA do Estoque')
        alert('Escolha entre 1 a 20')
        return number1.value--
    }
}

console.log(number1.value)

