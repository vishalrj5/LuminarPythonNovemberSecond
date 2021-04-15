var clk=document.querySelector("#clk")
clk.addEventListener('click',()=>{
    clk.style.color="red";
    clk.textContent="Clicked"
})


var ad=document.querySelector("#dbclick")

ad.addEventListener('dblclick',()=>{
    ad.style.color="green"
})

var over=document.querySelector("#hov")
over.addEventListener("mouseover",()=>{
    over.style.color="white"
})