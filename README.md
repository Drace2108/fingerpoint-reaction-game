# fingerpoint-reaction-game

The game has been made with the help of CVZone package developed by Murtaza Hassan. The package core is done on OpenCV and MediaPipe libraries. MediaPipe Hands high-fidelity hand and finger tracking solution employs Machine Learning pipeline to infer 21 3D landmarks of hand from single frame. By elaborating the CVZone and OpenCV I have created reaction game that allows to track hands, particularly the index finger point, and interact with object (image of apple) by “touching” the object which is calculated by tracking index finger location and if it is within the area of an object. The game has default maximum time of 10 seconds but can be changed within the code or implement new feature with setup menu in the game to change the max time value. Once the timer is done the “Game Over” text is shown, and user cannot play anymore. The player can restart game after game is over to achieve better result. Also, user can quit game anytime.

Hot Keys: “R” – restart game, “Q” – quit game.

To install CVZone package, run: pip install cvzone

I used Visual Studio Code with downloaded python package to run python file, any other alternative should work as well.

Possible future enhancements/updates: 
1)	Create User Interface with main menu and settings
2)	Implement Hand Gesture Recognition to add new features such as emotions in the game (e.g. hand gesture “piece” can “double” the scoring so other hand can double score)

Demo:

![Screen Recording 2023-12-20 at 2 26 35 PM](https://github.com/Drace2108/fingerpoint-reaction-game/assets/70643580/4f1d0181-017d-480a-9b50-44922978c6b7)

References:<br>
https://github.com/cvzone/cvzone<br>
https://www.murtazahassan.com/<br>
https://mediapipe.readthedocs.io/en/latest/solutions/hands.html<br>
https://developers.google.com/mediapipe/solutions/vision/gesture_recognizer/python
