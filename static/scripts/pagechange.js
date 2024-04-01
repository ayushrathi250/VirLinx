// function callinfo(){
// fetch('/static/pages/info.html')
//     .then(response => response.text())
//     .then(data => {
//         var parser = new DOMParser();
//         var doc = parser.parseFromString(data, 'text/html');
//         var infopage = doc.getElementById('inf').innerHTML;
//         document.getElementsById('container').innerHTML = infopage;
//     })
//     .catch(error => console.error('Error fetching info.html:', error));
// };

// function callconnect()
// {
//     fetch('/static/pages/info.html')
//     .then(response => response.text())
//     .then(data => {
//         var parser = new DOMParser();
//         var doc = parser.parseFromString(data, 'text/html');
//         var connectpage = doc.getElementById('play').innerHTML;
//         document.getElementsById('container').innerHTML = connectpage;
//     })
//     .catch(error => console.error('Error fetching connect.html:', error));
// };

// function calldev()
// {
//     fetch('/static/pages/developers.html')
//     .then(response => response.text())
//     .then(data => {
//         var parser = new DOMParser();
//         var doc = parser.parseFromString(data, 'text/html');
//         var specificDivContent = doc.getElementsByClassName('card_container').innerHTML;
//         document.getElementsById('container').innerHTML = specificDivContent;
//     })
//     .catch(error => console.error('Error fetching developer.html:', error));
// };

// function callfaq()
// {
//     fetch('/static/pages/faq.html')
//     .then(response => response.text())
//     .then(data => {
//         var parser = new DOMParser();
//         var doc = parser.parseFromString(data, 'text/html');
//         var specificDivContent = doc.getElementById('faqs').innerHTML;
//         document.getElementsById('container').innerHTML = specificDivContent;
//     })
//     .catch(error => console.error('Error fetching faq.html:', error));
// };

// function replaceContent(sourceFile, sourceDivId, targetDivId) {
//     fetch(sourceFile)
//     .then(response => response.text())
//     .then(data => {
//         var tempElement = document.createElement('div');
//         tempElement.innerHTML = data;

//         var sourceDivContent = tempElement.querySelector('#' + sourceDivId).innerHTML;
//         document.getElementById(targetDivId).innerHTML = sourceDivContent;
//     })
//     .catch(error => console.error('Error fetching ' + sourceFile + ':', error));
// }


function callinfo(pageloc) {
  // fetch("/static/pages/info.html")
  fetch(pageloc)
    .then((response) => response.text())
    .then((data) => {
      // Replace the content of the element with id="content" with the content of file2.html
      document.getElementById("container").innerHTML = data;
    })
    .catch((error) => console.error("Error fetching info.html:", error));
}




//##############################scipts.js backup code 




// scripts.js

// function showContent(id) {
//   // Hide all content sections
//   var contents = document.getElementsByClassName("vidcontainer");
//   for (var i = 0; i < contents.length; i++) {
//       contents[i].style.display = "none";
//   }

//   // Display the selected content section
//   var selectedContent = document.getElementById(id);
//   if (selectedContent) {
//       selectedContent.style.display = "block";
//   }
// }


document.addEventListener("DOMContentLoaded", () => {
    
  // let startButton = document.getElementById("startVid");
  // let stopButton = document.getElementById("stopVid");
  // let video = document.getElementById("vid");

  
  let startButton = document.getElementById("startVid");
  let stopButton = document.getElementById("stopVid");
  let video = document.getElementById("vid");

      function startWebcam() {
          try {
              video.src = "/video_feed";
              // startButton.style.display = 'none';
              // stopButton.style.display = 'block';
          } catch (err) {
              console.error('Error accessing the webcam stream:', err);
          }
      }

      

      // Function to stop the webcam stream
      function stopWebcam() {
          video.src = '';
          // startButton.style.display = 'block';
          // stopButton.style.display = 'none';
      }

      // // Event listener for the start button
      startButton.addEventListener('click', startWebcam);

      // // Event listener for the stop button
      stopButton.addEventListener('click', stopWebcam);
      
});






// document.addEventListener('DOMContentLoaded', function () {
//   var coll = document.getElementsByClassName('collapsible');
//   var i;

//   for (i = 0; i < coll.length; i++) {
//       coll[i].addEventListener('click', function () {
//           this.classList.toggle('active');
//           var content = this.nextElementSibling;
//           if (content.style.maxHeight) {
//               content.style.maxHeight = null;
//           } else {
//               content.style.maxHeight = content.scrollHeight + 'px';
//           }
//       });
//   }
// });
