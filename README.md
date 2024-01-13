# ArcadeZ
## Introduction

ArcadeZ is a retro arcade style endless zombie survival game using the spyder IDE's plots pane as a user interface. This project was developed to compete in the University of Alberta's ENCMP 100 programming contest where the objective was to create a game within the content constraints of the ENCMP 100 programming course. To satisfy competition requirements ArcadeZ was built using popular python libraries such as NumPy, Matplotlib, and Keyboard (Keyboard Listener). ArcadeZ was awarded with an honorable mention in the ENCMP 100 programming contest. 

## Dependencies

* Python (3.10.9)
* Spyder IDE (5.4.3)
* Matplotlib (3.8.2)
* Numpy (1.26.2)
* Keyboard (0.13.5)

## How It Works

Check out my YouTube Channel for a demo of ArcadeZ!

* YouTube Link

ArcadeZ uses popular python libraries such as NumPy, Matplotlib, and Keyboard, as well as the Spyder IDE's plots pane as a user interface. To get started open your Spyder IDE and open the main.py file. Once the file is open in your IDE, run the program and click on the plots pane to direct your keyboards input to the game. When the user starts the game they are shown an animated start screen within the plots pane. In this animated screen the user is prompted to press space to start. Pressing space will bring the user to the Menu page, here the user is shown two options: "Play", "How To Play".

__To move the position of the cursor (Shown in the picture as the angle bracket to the left of "Play" Option) use the buttons "w" and "s" on your Keyboard.__
[![Screenshot-2024-01-13-135435.png](https://i.postimg.cc/5tYQ8pN5/Screenshot-2024-01-13-135435.png)](https://postimg.cc/2qY5DQW3)

The animated screens were made using matplotlib and plain text files (Menu.txt, HowToPlay.txt) to set the color value of pixels on the grid to illustrate a picture.

If the user selects the "How To Play" option (Hover cursor over "How To Play" option and press "k" on keyboard) it will bring them to a different screen displaying the instructions of how to play ArcadeZ.

[![Screenshot-2024-01-13-141208.png](https://i.postimg.cc/Dw95Jxqs/Screenshot-2024-01-13-141208.png)](https://postimg.cc/bZR14HVN)

If the user selects "Play" option on the main screen they will be begin the game. The blue pixel on the center of the screen is the player, while the surrounding red pixels are the "Zombie" pixels.

[![Screenshot-2024-01-13-141919.png](https://i.postimg.cc/9FTsxwJG/Screenshot-2024-01-13-141919.png)](https://postimg.cc/N5sNFFhM)

At the top of the screen the player can see information such as the current round they are on and how much time is remaining in the current round. After the timer runs out of time the round increases. With each increase in round number the game gets more difficult by increasing the time of the round as well as the number of zombies. The player moves by using the "w", "a", "s", and "d" keys. The player's objective is to survive as long as possible by avoiding the red pixels on the screen. Both the players and the zombie's locations are stored in two seperate numpy array's. As the game progresses the program will check to see if the players location in their array is the same as any of the zombie's in the zombie array. If this condition is true, the game ends and the player has lost. When the player loses they will return to the Menu screen.

To keep the game interesting, zombie spawn locations and movement patterns are randomized so the game is not deterministic. This is done through the use of the standard python library "random" which produces pseudo random numbers to determine the location of spawn locations and movement patterns.


[![Screenshot-2024-01-13-143142.png](https://i.postimg.cc/Z5f8hVqp/Screenshot-2024-01-13-143142.png)](https://postimg.cc/mPHzY3Cg)

__For more technical documentation see comments in the code files.__

