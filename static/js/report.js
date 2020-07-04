const scanDetails = document.querySelector(".scan-details");
const payloadsTried = document.querySelector(".payloads-tried");
const scanLogs = document.querySelectorAll(".scan-logs");
const payloads = document.querySelectorAll(".payloads");
const testLogs = document.querySelectorAll(".test-logs");
const scanDetails1 = document.querySelector(".scan-details1");
const risk = document.querySelectorAll(".risk");

risk.forEach((e) => {
  if (e.innerText == "High") {
    e.style.color = "red";
  } else {
    e.style.color = "#008000";
  }
});

scanDetails.addEventListener("click", reveal);

function reveal() {
  scanLogs.forEach((e) => {
    if (e.style.visibility == "hidden") {
      e.style.visibility = "visible";
    } else {
      e.style.visibility = "hidden";
    }
  });
}

payloadsTried.addEventListener("click", show);

function show() {
  payloads.forEach((e) => {
    if (e.style.visibility == "hidden") {
      e.style.visibility = "visible";
    } else {
      e.style.visibility = "hidden";
    }
  });
}

scanDetails1.addEventListener("click", opened);

function opened() {
  testLogs.forEach((e) => {
    if (e.style.visibility == "hidden") {
      e.style.visibility = "visible";
    } else {
      e.style.visibility = "hidden";
    }
  });
}
