
  var url =  window.location.hostname;
  var socket = io(url  + ":5000");

socket.on("testing", function(payload){
  // console.log(`topic: ${topic} and message: ${msg}`)
  console.log(payload)

})

socket.on("tanks/tank1", function(payload){
  console.log(payload)
})

socket.on("tanks/tank2", function(payload){
  console.log(payload)
})

socket.on("tanks/tank3", function(payload){
  console.log(payload)
})


socket.on("tanks/tank3", function(payload){
  console.log(payload)
})

socket.on("tanks/tank1/recieve/hitBy", function(payload){
  console.log(payload["id"], payload["amount"]);

  alterHealth(payload["id"], payload["amount"])
})

  function alterHealth(id, amount){
    tank = document.getElementById(id)

  current_health = parseInt(document.getElementById(id).style.width.slice(0,2))
  new_health = current_health - parseInt(amount)
    tank.setAttribute("style", `width: ${new_health}%`)
  }
