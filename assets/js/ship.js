document.getElementById("submit1").onclick = shipfeee;
document.getElementById("submit2").onclick = shipfeee;
function shipfeee() {
  
    var a=((document.getElementById("total")).textContent).replace("$","").trim();
    b=parseFloat(a);
    var result, total;
    if(a>500)
    {
        result="Free Ship";
        document.getElementById("fee").innerHTML="$0";
        total=b;      
    }
    else
    {
        result="Flat Rate: $20.00";
        document.getElementById("fee").innerHTML="$20";
        total=b+20;
    } 
    document.getElementById("shipfee").innerHTML = result;
    document.getElementById("grand-total").innerHTML="$"+total.toString();
  }