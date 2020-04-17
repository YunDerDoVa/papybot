function add_response(responseText) {
  var zone = document.getElementById("responses_zone");
  var json = JSON.parse(responseText);

  //Leaflet
  var speak = document.getElementById("speak_template").cloneNode(true);
  speak.id = null;
  speak.classList.add('papy-speak');

  var question = speak.getElementsByClassName("user-question")[0];
  question.textContent = json.question;

  var title = speak.getElementsByClassName("papy-title")[0];
  title.textContent = json.hello;

  var maps_intro = speak.getElementsByClassName("maps-intro")[0];
  maps_intro.textContent = json.introduction_maps;

  var para = speak.getElementsByClassName("papy-para")[0];
  para.textContent = json.introduction_wiki + ' ' + json.wiki + ' ' + json.bye;

  var wiki_link = speak.getElementsByClassName("wiki-link")[0];
  wiki_link.href = json.wiki_link;

  zone.appendChild(speak);
}

function ajax_func() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {

      add_response(this.responseText);

    }
    if (this.readyState == 4 && this.status != 200) {
     document.getElementById("demo").innerHTML = "error";
    }
  };

  xhttp.open("POST", "ask/" , true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("question=" + document.getElementById('question_input').value);
}
