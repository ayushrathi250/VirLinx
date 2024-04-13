function myFunc(windowId, barId) {
    // Get all buttons in the sidebar
    let buttons = document.querySelectorAll('.sidebar .button');

    // Remove 'button_clicked' class from all buttons
    buttons.forEach(button => {
        button.classList.remove('button_clicked');
    });

    // Add 'button_clicked' class to the clicked button
    barId.classList.add('button_clicked');

    // Get all windows
    let windows = document.querySelectorAll('.window');

    // Hide all windows
    windows.forEach(window => {
        window.classList.remove('active');
    });

    // Show the selected window
    document.getElementById(windowId).classList.add('active');
}

document.addEventListener("DOMContentLoaded", () => {
    let but1 = document.getElementById("startVid");
    let but2 = document.getElementById("stopVid");
    let video = document.getElementById("vid");
    video.muted = true;

    but1.addEventListener("click", () => {
        // Accessing the user camera and video.
        video.src = "/video_feed"
    });

    but2.addEventListener("click", () => {
        video.src = ""

    });
});