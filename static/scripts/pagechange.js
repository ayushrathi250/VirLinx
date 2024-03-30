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
