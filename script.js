let timerInterval;
let seconds = 0;

function updateTimer() {
    let hrs = String(Math.floor(seconds / 3600)).padStart(2, '0');
    let mins = String(Math.floor((seconds % 3600) / 60)).padStart(2, '0');
    let secs = String(seconds % 60).padStart(2, '0');
    document.getElementById("timer").textContent = `${hrs}:${mins}:${secs}`;
}

function startTimer() {
    if (timerInterval) return; // prevent multiple intervals
    timerInterval = setInterval(() => {
        seconds++;
        updateTimer();
    }, 1000);
}

function finishTimer() {
    clearInterval(timerInterval);
    timerInterval = null;
}

function resetTimer() {
    finishTimer();
    seconds = 0;
    updateTimer();
}

// Optional: initialize timer display on load
updateTimer();