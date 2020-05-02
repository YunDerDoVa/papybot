function append_speak() {
  var zone = document.getElementById("responses_zone");

  var speak = document.getElementById("speak_template").cloneNode(true);
  speak.classList.add('papy-speak');
  speak.classList.add('empty');
  speak.id = "speak_" + String(document.getElementsByClassName("papy-speak").length);

  zone.insertBefore(speak, zone.childNodes[0]);
}

function add_response(responseText) {
  var zone = document.getElementById("responses_zone");
  var json = JSON.parse(responseText);

  if (json.error_message) {
    var message = json.error_message + " (" + String(json.errors) + ")";
    document.getElementById("error_message").textContent = message;
  }

  function setMaps() {
    var maps_intro = speak.getElementsByClassName("maps-intro")[0];
    maps_intro.textContent = json.introduction_maps;

    var maps = speak.getElementsByClassName("maps-leaflet")[0];
    maps.id = "leaflet_" + String(speak.id);
    maps.style.maxWidth = "512px";
    maps.style.width = "100%";
    maps.style.height = "256px";
    maps.style.zIndex = "0";

    var latitude = parseFloat(json.location.latitude);
    var longitude = parseFloat(json.location.longitude);
    var leaflet_map = L.map(maps, {
      center: [latitude, longitude],
      zoom: 12
    });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(leaflet_map);
    L.marker([json.location.latitude, json.location.longitude]).addTo(leaflet_map);
  }

  var speak_id = "speak_" + String(document.getElementsByClassName("papy-speak").length-1);
  var speak = document.getElementById(speak_id);

  var question = speak.getElementsByClassName("user-question")[0];
  question.textContent = json.question;

  var title = speak.getElementsByClassName("papy-title")[0];
  title.textContent = json.hello;

  setMaps();

  var para = speak.getElementsByClassName("papy-para")[0];
  para.textContent = json.introduction_wiki + ' ' + json.wiki + ' ' + json.bye;

  var wiki_link = speak.getElementsByClassName("wiki-link")[0];
  wiki_link.href = json.wiki_link;

  speak.classList.remove('empty');
}

function loading_anim(display) {

  var loading = document.getElementById("loading_anim");
  loading.style.display = display;

}

function ajax_button(disable) {

  var buttons = document.getElementsByClassName("ajax-button");
  for (var i = 0; i < buttons.length; i++) {
    buttons[i].style.disable = disable;
  }

}

function ajax_func() {
  var xhttp = new XMLHttpRequest();

  xhttp.onreadystatechange = function() {
    if (this.readyState == 1) {

      document.getElementById("error_message").textContent = null;

      loading_anim("flex");
      ajax_button("False");

      append_speak();

    }

    if (this.readyState == 4) {

      loading_anim("none");
      ajax_button("True");

    }
    if (this.readyState == 4 && this.status == 200) {

      add_response(this.responseText);

    }
    if (this.readyState == 4 && this.status != 200) {
      const papywords = "Je te prie de m'excuser, j'ai besoin de me reposer...";
      document.getElementById("error_message").textContent = papywords + " (Error " + String(this.status) + ")";
    }
  };

  xhttp.open("POST", "ask/" , true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.send("question=" + document.getElementById('question_input').value);
}
