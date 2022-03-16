const json2XML = () => {

    const val = document.getElementById("frm").type.value;
    const result = document.getElementById("result");

    if(val.trim() == ""){
        alert("Please select one field");
    }
    else if(val.trim() == "url"){
        
        console.log("URL");

        const url = document.getElementById("url").value;
        const obj = JSON.stringify({
            "url":url,
        });

        console.log(obj);

        const xhttp = new XMLHttpRequest();
        xhttp.onload = function() {

            if(this.status == 200 && this.readyState == 4){
                result.innerText = this.responseText;
            }

        }
        xhttp.open("POST", "/urljson");
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(obj);

    }
    else if(val.trim() == "text"){
        
        console.log("Text");

        const text = document.getElementById("text").value;
        const obj = JSON.stringify({
            "text":text,
        });

        console.log(obj);

        const xhttp = new XMLHttpRequest();
        xhttp.onload = function() {

            if(this.status == 200 && this.readyState == 4){
                result.innerText = this.responseText;
            }

        }
        xhttp.open("POST", "/textjson");
        xhttp.setRequestHeader("Content-type", "application/json");
        xhttp.send(obj);

    }
    else{
        alert("Please select one field");
    }

}