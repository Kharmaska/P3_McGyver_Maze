# Project n°3: MacGyver Maze

## Maze: help MacGyver escaping the maze

### 1. Purpose of the game

In this mini Python game, based on the Pygame library, you will have to recover the 3 items inside the maze so MacGyver can build an awesome weapon to defeat the guardian and escape the maze.
In case an item would be missing before facing the guardian, you lose!
  
### 2. Specifications of the project

This game was programmed during my OpenClassRooms Python degree course. As such, a frame was imposed while coding this exercise:

- [ ] There is only one level. The structure (starting square, the location of the walls, finish line), must be saved in a file for easy modification if necessary.
- [ ] MacGyver will be controlled by the directional keys on the keyboard.
- [ ] The objects will be randomly distributed in the labyrinth and will change location if the user closes the game and restarts it.
- [ ] The game window will be a square that can display 15 sprites lengthwise.
- [ ] MacGyver will therefore have to move from square to square.
- [ ] He will pick-up an object simply by moving over it.
- [ ] The program stops only if MacGyver has recovered all the objects and has found the exit. If he does not have all the items and he gets to the guard, he dies (a hero's life...).
- [ ] The program is a standalone game that could run on any computer.
- [ ] The code needs to be compliant with PEP 8 recommendations
- [ ] Development of the program should be done in a Virtual Environment using Python 3.X

### 3. Dependencies and installation

#### 3.1 VirtualEnv

 You will first need to install a Python Virtual Environment.
 To that matter, open a Terminal on your computer (Powershell on Windows, Bash on Mac or Linux) and proceed as follows:

##### a. Installing VirtualEnv

Open your terminal and type in:

```bash
 pip install virtualenv
```

##### b. Creating your virtualEnv

Open the terminal into the folder where you have installed the game's files and type the following:

```bash
virtualenv -p python3 env
```

if you are on Windows's PowerShell:

```powershell
 virtualenv -p $env:python3 env
```

This should have created an ENV or VENV folder in the installation folder for the game.

##### c. Activating your virtualEnv

 In order to activate the VirtualEnv then you would need to run the following command:

```bash
 source env/bin/activate
```

if VENV folder was created:

```bash
 source venv/bin/activate
```

if you are on Windows's PowerShell:

```powershell
 ./env/scripts/activate.ps1

 OR if you created a 'venv' folder and not an 'env' folder

 ./venv/scripts/activate.ps1
```

#### 3.2 Installing dependencies

In order to install the required dependencies you will have to enter the following command in your terminal

```bash
 pip install -r requirements.txt
 ```

 In case you would like to modify the version of any of the dependencies, you can do so by modifying the requirements.txt file and then by running again the command above

### 4. Launching the game

In your bash or powershell console run the following command:

```bash
python main.py
```

It should open the game GUI and display the following screen:

![Game Window MacGyver](/assets/gameCapture.jpg?raw=true "Game Window MacGyver")

If you manage to collect the 3 items that MaCGyver needs to defeat the guardian you will get the following screen:

![Game Window MacGyver Won](/assets/gameCaptureWon.jpg?raw=true "Game Window MacGyver")

Otherwise the guardian will kill you and you will have to restart the game with the command above.

![Game Window MacGyver Lost](/assets/gameCaptureLost.jpg?raw=true "Game Window MacGyver")
