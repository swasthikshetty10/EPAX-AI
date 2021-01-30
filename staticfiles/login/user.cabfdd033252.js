function get_from_api() {
  var url = "/userdata";

  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      loaddata(data)
    })

}
get_from_api();

function loaddata(data) {
  document.getElementById("username").innerHTML = data.username;
  document.getElementById("userid").innerHTML = `Active | ID : ${data.userid}`;
  document.getElementById("usertodo").innerHTML = data.usertodo;
  document.getElementById("usernotes").innerHTML = data.usernotes;
}