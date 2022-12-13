# GroundLight---Assessment

How to run: 
  * The game starts immediately when you run main.py. A command based prompt opens up with which you can interact
  * There are two player modes: Player V Player and Player V Bot
  * You can pick either, and for each move, the input can be given in the format of (x y) when x and y are positions of the move in a 9x9 grind with values ranging from 0-8
  * The game can be quit by entering exit at any point in time
  * The game exits on its own when the meta game is won by a player or a bot
  * Please feel free to refer to the sample output as well 
  
 Design: 
  * Class TicTacToe is a class which represents the game. All the methods which interact with the user are mostly a part of this class. We also have classes for the player and the bot as well. 
  * Has a basic driver program which creates objects for these classes and essentially allows these objects to interact and also provides the user a command based prompt to interact with
  
 What could have been done if we had more time:
  * A GUI with which a player could interact with, keeping the same methods. That is essentially having a MVC based architecture. These methods would serve as controller methods. 
  * A good development pattern. Having built interfaces, hiding more methods not needed for end user. For example facade pattern. 
  * A Bot with a better ability. A Bot instead of being purely random in nature, could have been made to make better choices at each step. 
 
