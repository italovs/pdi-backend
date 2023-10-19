const socket = io()

window.onload = function() {
}

document.addEventListener('DOMContentLoaded', function() {
  socket.on("connect", () => {
    console.log("connect")
  })
  const berth = document.querySelector("input").value
  socket.emit("join", berth)
  
}, false);

socket.on('message', (msg) => {
  const section = document.querySelector(".scroll");
  const span = document.createElement("span");
  
  span.innerHTML = msg;

  section.append(span);
});