
$(document).ready(function () {
    var addTimerButton = $("<button>Add new timer</button><p>Timer counter: <span class=\"count\">0</span></p>");
    var timerCount=0;
    var countSpan=addTimerButton.find(".count");
    
    $("#addtimer").append(addTimerButton);
    
    addTimerButton.click(function () {
		var timerDiv = $("<div class=\"timer\"><div class=\"hour\">End: <input type=\"text\" placeholder=\"HH:MM:SS\"><input type=\"button\" value=\"delete\"></div><div class=\"display\"></div><canvas width=\"100\" height=\"100\"></div>");
		$("#timers").append(timerDiv);

		timerCount++;
		countSpan.text(timerCount);

		var input = timerDiv.find(".hour input");
		var disp = timerDiv.find(".display");
		var close = timerDiv.find("input[type=button]");
		var h=null;
		var m=null;
		var s=null;
		var timer=null;
		var canvas = timerDiv.find("canvas")[0];
		var canvasContext = canvas.getContext("2d");

		function updateCanvas(sec,finished) {
			canvasContext.save();
			canvasContext.scale(100,100);
			canvasContext.clearRect(0,0,1,1);
			canvasContext.translate(0.5,0.5);
			canvasContext.rotate(2*Math.PI/60*sec);
			canvasContext.beginPath();
			canvasContext.arc(0,-0.4,0.1,0,2*Math.PI);
			canvasContext.fillStyle=finished?"#FF0000":"#00FF00";
			canvasContext.closePath();
			canvasContext.fill();
			canvasContext.restore();
		}

		function tryStart() {
			disp.children().remove();
			if(timer != null) {
			window.clearInterval(timer);
			timer=null;
			}
			if(h!= null && m != null && s!=null) {
			var deadline = $("<span>Expires on: "+h+":"+m+", counting:</span>");
			var countdown = $("<span></span>");
			disp.append(deadline);
			disp.append(countdown);
			if(timer == null) {
				timer = window.setInterval(function () {
					var finished=false;
					var now = new Date();
					var rH = h-now.getHours();
					var rM = m-now.getMinutes();
					var rS = s-now.getSeconds();
					if(rS<0) {
						rM--;
						rS+=60;
					}
					if(rM<0) {
						rH--;
						rM+=60;
					}
					if(rH>=0) {
						countdown.text(rH+":"+rM+":"+rS);
						timerDiv.removeClass("expired");
					} else {
						countdown.text("expired");
						timerDiv.addClass("expired");
						finished=true;
					}
					updateCanvas(60-rS, finished);
				}, 1000);
			}
			}
		}

		input.change(function () {
			var v = $(this).val();
			var match = v.match(/^(([01]?[0-9])|(2[0-3])):([0-5]?[0-9]):([0-5]?[0-9])$/);
			if(match) {
			h=parseInt(match[1]);
			m=parseInt(match[4]);
			s=parseInt(match[5]);
			} else {
			h=null;
			m=null;
			s=null;
			}
			tryStart();
		});

		close.click(function () {
			if(timer!=null) {
			window.clearInterval(timer);
			}
			timerDiv.remove();
		});

    });
});
