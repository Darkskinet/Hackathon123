const socket = io("http://localhost:1337");
// socket.emit("hello", "world");

button1 = document.getElementById("button-1");
button2 = document.getElementById("button-2");
button3 = document.getElementById("button-3");
button4 = document.getElementById("button-4");
button5 = document.getElementById("button-5");

socket.on("connect", () => {
  console.log(socket.id); 
});

socket.on("hello", (...args) => {
  console.log(args)
})

socket.on("gesture", (...args) => {
  console.log("listening")
  console.log(args);
  open = 5 - Number(args);
  switch (open) {
    case 1:
      button1.style.background = "rgba(250, 247, 247, 1)";
      window.location.href = "https://ncert.nic.in/textbook.php";
    case 2:
      button2.style.background = "rgba(250, 247, 247, 1)";
      window.location.href = "https://ict.dunesinternationalschool.com/";
    case 3:
      button3.style.background = "rgba(250, 247, 247, 1)";
      window.location.href = "https://cbseacademic.nic.in/";
    case 4:
      button4.style.background = "rgba(250, 247, 247, 1)";
      window.location.href = "/static/main/timetable.pdf";
    case 5:
      button5.style.background = "rgba(250, 247, 247, 1)";

    default:
      console.log("default");
  } // world
});

socket.on("disconnect", () => {
  console.log("disconnected");
});