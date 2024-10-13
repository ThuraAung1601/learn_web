function myFunction() {
    let text;
    if (confirm("Do you want Ok or Cancel?") == true) {
        text = "Ok is pressed";
    } else {
        text = "Cancel is pressed";
    }
    document.getElementById("response").innerHTML = text;
}