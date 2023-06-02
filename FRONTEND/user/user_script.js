function getData() {
    // Retrieving data
    var email = document.getElementById("userEmail").value;
    var pswd = document.getElementById("userPswd").value;

    // Storing data
    localStorage.setItem("email", email);
    localStorage.setItem("pswd", pswd);
    
    // Retrieving stored data
    var storedEmail = localStorage.getItem("email");
    var storedPswd = localStorage.getItem("pswd");

    if (storedEmail === "user@gmail.com" && storedPswd === "user123") {
        alert("Login Successful !");
        window.location.href = "./user_interview_form.html";
        console.log("done");
    } else {
        alert("Login Unsuccessful !");
    }
}