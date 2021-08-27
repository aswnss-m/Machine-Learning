
function increment(side,id){
    var increment_element_id = "increment_" + id.toString();
    var increment_element = document.getElementById(increment_element_id);
    if(side == "R"){
        increment_element.innerHTML = Number(increment_element.innerHTML) + 1;
    }
    else if(side == "L"){
        if(increment_element.innerHTML > 0){
            increment_element.innerHTML = Number(increment_element.innerHTML) - 1;
        }
    }
}