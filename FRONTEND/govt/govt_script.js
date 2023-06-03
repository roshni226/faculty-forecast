function getData() {
    // retrieving data
    var email = document.getElementById("govtEmail").value;
    var pswd = document.getElementById("govtPswd").value;

    //store data
    var em = localStorage.setItem("email",email);
    var pswd = localStorage.setItem("pswd",pswd);
    
    // retrieving stored data
    var em = localStorage.getItem("email",email);
    var pswd = localStorage.getItem("pswd",pswd);

    console.log(em);
    console.log(pswd);
    if (em == "govt@gmail.com" && pswd == "govt123"){
        alert("Login Successful !");
        window.location.assign("govtpage2.html");

    }
    else {
        alert("Login Unsuccessful !");
    }
    
}