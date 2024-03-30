// scripts.js

function showContent(id) {
  // Hide all content sections
  var contents = document.getElementsByClassName("content");
  for (var i = 0; i < contents.length; i++) {
      contents[i].style.display = "none";
  }

  // Display the selected content section
  var selectedContent = document.getElementById(id);
  if (selectedContent) {
      selectedContent.style.display = "block";
  }
}


document.addEventListener("DOMContentLoaded", () => {
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

        // Event listener for the start button
        startButton.addEventListener('click', startWebcam);

        // Event listener for the stop button
        stopButton.addEventListener('click', stopWebcam);
});




document.addEventListener('DOMContentLoaded', function () {
  var coll = document.getElementsByClassName('collapsible');
  var i;

  for (i = 0; i < coll.length; i++) {
      coll[i].addEventListener('click', function () {
          this.classList.toggle('active');
          var content = this.nextElementSibling;
          if (content.style.maxHeight) {
              content.style.maxHeight = null;
          } else {
              content.style.maxHeight = content.scrollHeight + 'px';
          }
      });
  }
});
