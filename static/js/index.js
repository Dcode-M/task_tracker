
var clock = document.getElementById("clock");

var ctx = clock.getContext("2d");
var radius = clock.height / 2;
ctx.translate(radius, radius);
radius = radius * 0.90
setInterval(clockAfterEachSecond, 1000);

function clockAfterEachSecond() {
  clockFace(ctx, radius);
  clockElement(ctx, radius);
  clockTime(ctx, radius);
}

function clockFace(ctx, radius) {
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, 2*Math.PI);
  ctx.fillStyle = 'yellow';
  ctx.fill();
  var gradient = ctx.createRadialGradient(0,0,radius*0.95, 0,0,radius*1.05);
  gradient.addColorStop(0, '#333');
  gradient.addColorStop(0.5, 'white');
  gradient.addColorStop(1, '#333');
  ctx.strokeStyle = gradient;
  ctx.lineWidth = radius*0.1;
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, radius*0.1, 0, 2*Math.PI);
  ctx.fillStyle = '#333';
  ctx.fill();
}

function clockElement(ctx, radius) {
  var ang;
  var num;
  ctx.font = radius*0.15 + "px arial";
  ctx.textBaseline="middle";
  ctx.textAlign="center";
  for(num = 1; num < 13; num++){
    ang = num * Math.PI / 6;
    ctx.rotate(ang);
    ctx.translate(0, -radius*0.85);
    ctx.rotate(-ang);
    ctx.fillText(num.toString(), 0, 0);
    ctx.rotate(ang);
    ctx.translate(0, radius*0.85);
    ctx.rotate(-ang);
  }
}

function clockTime(ctx, radius){
  // "2015-03-25T12:00:50"
  // clock starting point
    var startTime = new Date();
    var hour = startTime.getHours();
    var minute = startTime.getMinutes();
    var second = startTime.getSeconds();

    //hour
    hour=hour%12;
    hour=(hour*Math.PI/6)+(minute*Math.PI/(6*60))+(second*Math.PI/(360*60));
    clockHands(ctx, hour, radius*0.5, radius*0.07);

    //minute
    minute=(minute*Math.PI/30)+(second*Math.PI/(30*60));
    clockHands(ctx, minute, radius*0.8, radius*0.07);
    // second
    second=(second*Math.PI/30);
    clockHands(ctx, second, radius*0.9, radius*0.02);
}

function clockHands(ctx, pos, length, width) {
    ctx.beginPath();
    ctx.lineWidth = width;
    ctx.lineCap = "round";
    ctx.moveTo(0,0);
    ctx.rotate(pos);
    ctx.lineTo(0, -length);
    ctx.stroke();
    ctx.rotate(-pos);
}