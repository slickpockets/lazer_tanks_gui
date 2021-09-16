## GUI for lasertanks

##authored by urs truely slickpockets

done:
  - settings page
    - tabed area to switch between the settings, checkboxes for powerups (maybe switch to multi select),
  - main page
    - only a snigle health bar for testing
  - mqtt > socketio > page completeness
    - messages published through mosquitto_pub get processed by backend,and  published ot page (testing)

todo:
  - updating health bar is currently in testing phase, and even then isnt behaving as expected.
  - create callbacks for all expected mqtt topics and messages
  - glue mqtt to socketio as needed

  TOMS NOTES:

  for the slider you need a number display/input

  for the power ups dont have none as an option. just have a none and all button that unticks/ticks all the options

  and probably rename the wifi section to wifi. and if possible have it actual change the settings on the pi not just the qr code

  last thing, it should probably be more of a setup wizard. so if there is no game running it takes you to the game mode page and then there is a next button that goes to the power up page and so on. the wifi page should probably be at a diffrent url that cant be accessed from the index. and the qr code should be on every page. just in the conner out of the way
