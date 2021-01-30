var clk=document.getElementById("clk")
clk.addEventListener("click",()=>{      //event,which function need to execute
    clk.style.color="red";
    clk.textContent="clicked";
})

var dbclk=document.getElementById("dbclk")
dbclk.addEventListener("dblclick",()=>{
    dbclk.style.color="green";
    dbclk.textContent="double clickedd";
})

var hover=document.getElementById("hov")
hover.addEventListener("hover",()=>{
    hover.style.color="blue";
    hover.textContent="hovered";

})