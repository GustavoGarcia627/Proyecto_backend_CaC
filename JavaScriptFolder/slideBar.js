let slider = document.querySelector(".slideBar .slideBarInn")
let lenImg = document.querySelectorAll(".slideBar .slideBarInn .imagen")

console.log(lenImg)
/*slider.style.transform = "transLateX(-100%)";*/
let index = 1

setInterval(function(){
    let porcentajes = index * -100
    slider.style.transform = "transLateX("+porcentajes+"%)";
    index++;
    if (index>lenImg.length-1){
        index = 0
    }
},5000)