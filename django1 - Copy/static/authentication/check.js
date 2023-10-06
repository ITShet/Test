console.log("JS Loaded");

let passwordField = document.getElementsByClassName("password")[0];
let passRepField = document.getElementsByClassName("pass_rep")[0];
let button =  document.getElementsByClassName('btn-custom')[0];

function checkPasswordMatch() {
  let password = passwordField.value;
  let pass_rep = passRepField.value;
  let a = document.getElementsByClassName("test1")[0];
  let b = document.getElementsByClassName("test2")[0];

  if (password != pass_rep) {
    passwordField.classList.add("text-danger");
    passRepField.classList.add("text-danger");
    a.classList.add("text-danger");
    b.innerHTML = "* Repeat your password (Password does not match)";
    b.classList.add("text-danger");
    button.classList.add("disabled");
  } else {
    passwordField.classList.remove("text-danger");
    passRepField.classList.remove("text-danger");

    a.classList.remove("text-danger");
    b.innerHTML = "Repeat your password";
    b.classList.remove("text-danger");
    button.classList.remove("disabled");
  }
}

passwordField.addEventListener("input", checkPasswordMatch);
passRepField.addEventListener("input", checkPasswordMatch);
