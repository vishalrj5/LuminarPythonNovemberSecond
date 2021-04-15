circle3=document.querySelector('.circle3')
circle1=document.querySelector('.circle1')

circle2=document.querySelector('.circle2')

circle4=document.querySelector('.circle4')

const box=document.querySelector(".box")
const container=document.querySelector(".container")
const title=document.querySelector('box.h1')
let i=0;
box.addEventListener('mousemove',(e) => {

    let xAxis= (window.innerWidth / 2 - e.pageX);
    let yAxis= (window.innerHeight / 2 - e.pageY);
    console.log(xAxis,yAxis,"great")

    box.style.transform=`rotateY(${xAxis}deg) rotateX(${yAxis}deg)`
    // circle1.style.transform=`rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    // circle2.style.transform=`rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;

    // circle3.style.transform=`rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;
    // circle3.style.left=xAxis;
    // circle3.style.top=yAxis;


    // circle4.style.transform=`rotateY(${xAxis}deg) rotateX(${yAxis}deg)`;

    
});

box.addEventListener('mouseenter',(e) =>{
    box.style.transform="none";
    title.style.transform="translateZ(150px)";
})

box.addEventListener('mouseleave', (e) =>{
    box.style.transform="all 0.5s ease";
    box.style.transform=`rotateY(0deg) rotateX(0deg)`;
    title.style.transform="translateZ(0px)";
})

