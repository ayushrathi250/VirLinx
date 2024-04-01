
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
  
  