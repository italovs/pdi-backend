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
  
  span.innerHTML = `distance A: ${msg['distance_a']}; distance B: ${msg['distance_b']}; speed A: ${msg['speed_a']}; speed B: ${msg['speed_b']}; angle: ${msg['angle']};`;

  section.append(span);
});