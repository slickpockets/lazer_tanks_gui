
  function qrgen() {
    var ssid = document.getElementById("ssid").value
    var password = document.getElementById("password").value;
    var qrcode = new QRCode(document.getElementById("qrcode"), {
    	text: `WIFI:T:WPA;S:${ssid};P:${password};;`,
      	width: 512,
    	height: 512,
    	colorDark : "#000000",
    	colorLight : "#ffffff",
    	correctLevel : QRCode.CorrectLevel.H
    });
  }



  $(document).ready(function(){
    $('.tabs').tabs();

  });
