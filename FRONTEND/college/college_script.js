function getData() {
    // retrieving data
    var email = document.getElementById("college email").value;
    var pswd = document.getElementById("college pswd").value;

    //store data
    var em = localStorage.setItem("email",email);
    var pswd = localStorage.setItem("pswd",pswd);
    
    // retrieving stored data
    var em = localStorage.getItem("email",email);
    var pswd = localStorage.getItem("pswd",pswd);

    console.log(em);
    console.log(pswd);
    if (em == "college@gmail.com" && pswd == "college123"){
        alert("Login Successful !");

    }
    else {
        alert("Login Unsuccessful !");
    }
    
}