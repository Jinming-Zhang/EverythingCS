![[GameModeAndState.png]]
## Game Mode
`AGameModeBase` is an unreal provided class that provides some functionalities for managing multiplayer game, such as callbacks when new player joined and exited the game.

> `GameMode` only exists on the server. So if we are in the GameMode class we are definitely the server machine.


We can create our custom game mode by inherit from this class and override functions as needed. 

Some useful functions can be override from `AGameMode` class:
```cpp
// called when a new player join the level
void AGameMode::PostLogin(APlayerController *NewPlayer);
```
## Game State
`GameState` is a variable owned by `AGameModeBase` that contains a list of players.
Some useful fields of `AGameState` class:
- List of player states
```cpp
GameState
```