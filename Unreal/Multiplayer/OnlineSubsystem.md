# Online Subsystem
Unreal has it's Online Subsystem plug-ins for different platform services to help build a client-server mode multiplayer game. It's a layer between different platforms so we only need to write the code once.

We need to install both the **Online Subsystem** and **Online Subsystem Steam** (or other platform services) to use it in unreal project code.

- Unreal Engine Online Subsystem, plus ->
	- Steam platform
	- Epic platform
	- XBox platform
	- ...

# Session based game
Basic steps involved in creating a session based game:
- Create a session (instance)
- Wait for players to join the session
- Register players to the session
- Start the session
- Manage the particular session state throughout the game play
- End the session
- Deregister Players
- Update or destroy the session

#### Basic Session Interface Functions
- Create session
- Find sessions
- Join session
- Start session
- Destroy session


# Two Steps
## Client to create a session
1. Creating the session with configs, then (optionally go to a lobby scene) wait for others to join
## Clients to search/join a session
1. Create search configs
2. Find sessions match the config
3. Retrieve the ip and other information for the sessions that we can use to join

# Coding
We'll use the online subsystem interface provided by unreal as an abstract layer to interact with the specific online service we enabled.

Get hold of the interface instance using the following code:
```cpp
IOnlineSubsystem* onlineSubsystem = IOnlineSubsystem::Get();
IOnlineSessionPtr sessionInterface = onlineSubsystem->GetSessionInterface();
```

The interface object holds all the object/functions we'll need for creating, managing and terminating sessions through out the multiplayer game.

# Online session and delegates
Session interface uses delegates (call backs) to communicate information send back from the server

The session interface defines a set of `delegate types`, and holds a `delegate list` to iterate through and fire off events when appropriate.

We'll create an object of one of the `delegate type` that we are interested in, bind the corresponding callback function to the delegate object, then register/add the delegate object to the session interface's **delegate list**, so our call back will be called when the event happen.

## session interface delegate types sample
![[session delegate.png]]

Register needed delegates to the `IOnlineSessionInterface`:
- `FOnCreateSessionCompleteDelegate`
- `OnFindSessionsCompleted`
- etc.