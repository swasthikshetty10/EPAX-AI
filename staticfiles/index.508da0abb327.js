// const stuf_for_frontend = {
//     "response" : response,
//     "tag"  : tag,
//     "notes" : Notes,
//     "urls" : urls,
// 
// //add stackoverflow stuffs

// / --> domain

const btn = document.querySelector('.talk');
var content = document.querySelector('.content');
var date_ = new Date();

window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
//recognition.interimResults = true;
recognition.onstart = function () {
  console.log('Voice is activated');
};


function onclick_rec() {
  recognition.start();
}


recognition.addEventListener('result', e => {
  const transcript = Array.from(e.results)
    .map(result => result[0])
    .map(result => result.transcript)
    .join('')

  document.getElementById("textval").textContent = transcript;
  get_from_api(transcript);

});
// recognition.addEventListener('end' , recognition.start);


// btn.addEventListener('click') =  function()  {
//   recognition.start();
// }

//const speech = new SpeechSynthesisUtterance();

function readOutLoud(message) {
  voices = window.speechSynthesis.getVoices()
  var utterance = new SpeechSynthesisUtterance(message);
  utterance.voice = voices[1];
  window.speechSynthesis.speak(utterance);

  // var voices = window.speechSynthesis.getVoices();
  // speech.voice = voices[3];
  // speech.volume = 1;
  // speech.text = message;
  // window.speechSynthesis.speak(speech)
}

function get_from_api(message) { // getting response from ml model
  var url = `/response/${message}`;

  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      // console.log(data)
      conditions(data)
    })

}



function get_user_data() { //hhtp request for user data
  var url = "/userdata";

  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      loaddata(data)
    })

}

get_user_data();

function loaddata(data) { //load user data in main page
  // console.log(data)
  if (data.username !== "AnonymousUser") {
    document.getElementById("loginbutton").textContent = data.username;
  }
}


// take notes takes true or false to create form
function takenotes(tf) { //  hide or show notes

  if (tf) {
    document.getElementById("showbody").style.display = "block";
  } else {
    if (tf === false) {
      document.getElementById("showbody").style.display = "none";
    }


  }
}
//takenotes(true);

function sendnotes() { //send notes through url
  var title = document.getElementById("validationServerUsername").value;
  var notes = document.getElementById("exampleFormControlTextarea1").value;
  var url = `/sendnotes/${title}/${notes}`;
  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      readOutLoud(data.response)
    });
  document.getElementById("validationServerUsername").value = "";
  document.getElementById("exampleFormControlTextarea1").value = "";
  takenotes(false)

}

function rddeletenotes(title) {
  console.log(title);

  var url = `/deletenotes/${title}`;
  fetch(url)
    .then(response => {
      return response.json()
    })
    .then(data => {
      readOutLoud(data.response)
    });
  document.getElementById("response").textContent = '🚮 deleted successfully';
  document.getElementById('buttonlists').innerHTML = "";

}

function deletenotes() { //deleting notes
  //var url1 = `/deletenotes/${title}`;
  var url = '/shownotes/';

  fetch(url)
    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(data.amount)
      var key = Object.keys(data.titles)
      console.log(key)
      document.getElementById("buttonlists").innerHTML = document.getElementById("buttonlists").innerHTML = `<h4 style="color:white;">click to delete notes:</h4> <br>`
      for (i = 0; i < data.amount; i++) {
        document.getElementById("buttonlists").innerHTML = document.getElementById("buttonlists").innerHTML + `       <button type="button" class="btn btn-outline-primary" onclick ="rddeletenotes('${key[i]}')" style = "width : 100%">${key[i]}</button><br>`
      }


    });

}

function shownotes() { //deleting notes
  var url = '/shownotes/';

  fetch(url)
    .then(response => {
      return response.json()
    })
    .then(data => {
      console.log(data.amount)
      var key = Object.keys(data.titles)
      console.log(key)
      document.getElementById("buttonlists").innerHTML = document.getElementById("buttonlists").innerHTML = `<h4 style="color:white;">click to read notes:</h4> <br>`
      for (i = 0; i < data.amount; i++) {
        document.getElementById("buttonlists").innerHTML = document.getElementById("buttonlists").innerHTML + `       <button type="button" class="btn btn-outline-primary" onclick ="readnotes('${key[i]}')" style = "width : 100%">${key[i]}</button><br>`
      }


    });

}

function readnotes(title) {
  document.getElementById("buttonlists").innerHTML = "";
  var url = `/readnotes/${title}`;
  fetch(url)
    .then(response => {
      return response.json()
    })
    .then(data => {
      if (data.response !== "sorry i could not found your notes") {
        document.getElementById("meme").innerHTML = `<div class="card w-75">
      <div class="card-body">
        <h5 class="card-title">${title}</h5>
        <p class="card-text">${data.response}</p>
      </div>
    </div>`;
        readOutLoud(data.response)
      } else {
        readOutLoud(data.response)
      }

    });
}

function jokes() { // http request for jokes
  var url = '/getjoke/';
  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      document.getElementById("response").textContent = data.response;
      // console.log(data);
      readOutLoud(data.response);
    });
}

function getmeme() { // http request for meme  
  var url = '/getmeme/';
  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(data => {
      // console.log(data);
      document.getElementById("meme").innerHTML = `
                
              <div class="card">
                <div class="card-body">
                  <h5 class="card-title">${data.title}</h5>
                </div>
                <img src="${data.url}" class="card-img-top">
              </div>`;

    })
}

function iframe(url) {
  document.getElementById("iframe2").src = url;
  document.getElementById("iframes").style.display = "block";

}



// function music(tf) {
//   //   if (tf) {
//   //     document.getElementById("musicplayer").innerHTML = `<script src="https://apps.elfsight.com/p/platform.js" defer></script>
//   //     <div class="elfsight-app-382fc359-ee25-4505-8405-41a19e6b3b23"></div>`;
//   //   } else {
//   //     document.getElementById("musicplayer").innerHTML = '';
//   //   }
//   // }
var weekdays = new Array(7);
weekdays[0] = "Sunday";
weekdays[1] = "Monday";
weekdays[2] = "Tuesday";
weekdays[3] = "Wednesday";
weekdays[4] = "Thursday";
weekdays[5] = "Friday";
weekdays[6] = "Saturday";


function conditions(data) {
  //document.getElementById("meme").textContent = "";
  console.log(data);
  document.getElementById("response").textContent = data.response;
  document.getElementById("iframes").style.display = "none";
  document.getElementById("meme").innerHTML = '';
  document.getElementById('buttonlists').innerHTML = "";
  readOutLoud(data.response);
  if (data.tag === "['note-taking']") {
    takenotes(true);
  } else if (data.tag === "['delete-notes']") {
    deletenotes();

  } else if (data.tag === "['jokes']") {
    jokes();

  } else if (data.tag === "['meme']") {
    getmeme();

  } else if (data.tag === "['accountability']") {
    iframe('/todo');

  } else if (data.tag === "['news']") {
    iframe('/news');

  } else if (data.tag === "['time']") {
    readOutLoud(date_.toTimeString());
    document.getElementById("response").textContent = date_;
  } else if (data.tag === "['todays-day']") {

    readOutLoud(weekdays[date_.getDay()]);
    document.getElementById("response").textContent = date_;

  } else if (data.tag === "['todays-date']") {
    readOutLoud(date_.toDateString());
    document.getElementById("response").textContent = date_;
  } else if (data.tag === "['open-spotify']") {
    iframe('/music');

  } else if (data.tag === "['read-notes']") {
    shownotes();
    readOutLoud('click on the notes to read')
  }
}