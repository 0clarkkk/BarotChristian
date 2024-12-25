// DISCORD MODAL
const modal = document.getElementById("discordModal");
const discordIcon = document.getElementById("discordIcon");
const closeModal = document.getElementById("closeModal");

discordIcon.onclick = function(event) {
    event.preventDefault();
    modal.style.display = "block";
}

closeModal.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

// CLICK ME MODAL
const clickMeModal = document.getElementById("clickMeModal");
const clickMeButton = document.getElementById("clickMeButton");
const closeClickMeModal = document.getElementById("closeClickMeModal");
const meowButton = document.getElementById("meowButton");

clickMeButton.onclick = function(event) {
    event.preventDefault();
    clickMeModal.style.display = "block";
}

closeClickMeModal.onclick = function() {
    clickMeModal.style.display = "none";
}

meowButton.onclick = function() {
    clickMeModal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target === clickMeModal) {
        clickMeModal.style.display = "none";
    }
}
