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
  span_content = `distance A: ${msg['distance']['a']} ${msg['distance']["unit"]}; `
  span_content = span_content + `distance B: ${msg['distance']['b']} ${msg['distance']["unit"]}; `
  span_content = span_content + `speed A: ${msg['velocity']['a']} ${msg["velocity"]["unit"]}; `
  span_content = span_content + `speed B: ${msg['velocity']['b']} ${msg["velocity"]["unit"]}; `
  span_content = span_content + `angle: ${msg['angle']['value']}${msg['angle']['unit']};` 
  span.innerHTML =  span_content

  section.append(span);
});