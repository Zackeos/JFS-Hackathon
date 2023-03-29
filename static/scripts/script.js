// example
var url = "https://matix.io/extract-text-from-webpage-using-beautifulsoup-and-python/"

function badwordcheck(){
    var values = document.getElementById("badword-box").value
    var xhttp = new XMLHttpRequest();
        xhttp.open("POST", "./getwords", true);
        xhttp.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhttp.send(JSON.stringify(values));
        xhttp.onload = function(){
            var badwords = JSON.parse(this.responseText);
        }
    }

