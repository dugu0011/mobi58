const timer = document.querySelector(".timer");
const startStopBtn = document.querySelector(".startStopBtn");
const reset = document.querySelector(".resetBtn");

let counter = 0;
let ms = 0;
let s = 0;
let m = 0;
let h = 0;
let startStopFn;

startStopBtn.addEventListener("click", () => {
  startStopBtn.classList.toggle("startBtn");
  startStopBtn.classList.toggle("stopBtn");

  if (startStopBtn.value === "Stop") {
    clearInterval(startStopFn);
    startStopBtn.value = "Start";
  } else if (startStopBtn.value === "Start") {
    startStopFn = setInterval(() => {
      ms = counter % 100;
      if (counter > 0 && ms === 0 && s < 60) {
        s++;
      }
      if (counter > 0 && s === 60 && m < 60) {
        s = 0;
        m++;
      }
      if (counter > 0 && m === 60 && h < 24) {
        m = 0;
        h++;
      }
      if (h >= 24) {
        h = 0;
      }
      counter++;

      timer.innerHTML =
        h.toLocaleString("en-US", {
          minimumIntegerDigits: 2,
          useGrouping: false
        }) +
        " : " +
        m.toLocaleString("en-US", {
          minimumIntegerDigits: 2,
          useGrouping: false
        }) +
        " : " +
        s.toLocaleString("en-US", {
          minimumIntegerDigits: 2,
          useGrouping: false
        }) +
        " : " +
        ms.toLocaleString("en-US", {
          minimumIntegerDigits: 2,
          useGrouping: false
        });
    }, 10);

    startStopBtn.value = "Stop";
  }
});

reset.addEventListener("click", () => {
  clearInterval(startStopFn);
  counter = 0;
  ms = 0;
  s = 0;
  m = 0;
  h = 0;

  timer.innerHTML =
    h.toLocaleString("en-US", { minimumIntegerDigits: 2, useGrouping: false }) +
    " : " +
    m.toLocaleString("en-US", { minimumIntegerDigits: 2, useGrouping: false }) +
    " : " +
    s.toLocaleString("en-US", { minimumIntegerDigits: 2, useGrouping: false }) +
    " : " +
    ms.toLocaleString("en-US", { minimumIntegerDigits: 2, useGrouping: false });

  startStopBtn.value = "Start";
  startStopBtn.classList.add("startBtn");
  startStopBtn.classList.remove("stopBtn");
});