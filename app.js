// Simple "Hello World" routine
function hello(name) {
    // get the value of the "name" text element
    name = document.getElementById('name').value;

    // show a pop-up dialog saying hello to the user
    alert("Hello " + name + "!");
}


// Call the python "web service" to get the temperature
function FtoC() {
    // get the value of the "farenheight" text element
    farenheight = document.getElementById('farenheight').value;

    // call the FtoC url, passing the FtoCResult element to display the result text
    httpGet("/FtoC/" + farenheight, document.getElementById("FtoCResult"))

}


////////////////////////////////////////////////////////////////////////////////


// Utility function
function httpGet(url, element) {
    http = new XMLHttpRequest();
    http.onreadystatechange = function() {
        if (http.readyState == 4) {
            element.innerHTML = http.responseText;
        }
    };
    http.open("GET", url, true);
    http.send();
}
