let player = require('play-sound')(opts = {})

player.play('alarm.mp3', (err) => {
    console.log("What is 2+2?")
    if (err) throw err
})
