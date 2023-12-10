
# Step Guide
### Initialize Online Subsystem
```cpp
IOnlineSubsystem* subSystem = IOnlineSubsystem::Get();
IOnlineSessionPtr iSession = subSystem->GetSessionInterface();
```
All session management functions will be reside in session interface.

> Remember to register and clear corresponding callback and handlers at each stage.

### Create Session
##### Create a session
```cpp
IOnlineSession::CreateSession(const FUniqueNetId& hostingPlayerId, FName sessionName, const FOnlineSessionSettings& sessionSettings);
```
- FUniqueNetId:
	- Can be retrieved from `ULocalPlayer::GetPreferredUniqueNetId()`.
- FName:
	- A customized session name to identify the session.
- FOnlineSessionSettings:
	- Settings of the session to be created, here are some sample properties can be set:
		- bIsLANMatch
		- NumPublicConnections
		- bAllowJoinInProgress
		- bAllowJoinViaPresence
		- bShouldAdvertise
		- bUsePresence
		- bIsLANMatch
 
	- Also additional custom properties can be set using the `Set` function:
		```cpp
		// use this to filtering out session search result later on
		sessionSettings->Set(
			FName("PropOne"),
			FString("ValueOne"),
			EOnlineDataAdvertisementType inType
		);
		```


Sample code:
```cpp
// register handle and callback
createSessionCompleteDelegateHandle = sessionInterface->AddOnCreateSessionCompleteDelegate_Handle(createSessionCompleteDelegate);

// session settings, parameterize fields as needed
sessionSettings = MakeShareable(new FOnlineSessionSettings());
sessionSettings->bIsLANMatch = IOnlineSubsystem::Get()->GetSubsystemName() == "NULL";
sessionSettings->NumPublicConnections = numPublicConnections;
sessionSettings->bAllowJoinInProgress = true;
sessionSettings->bAllowJoinViaPresence = true;
sessionSettings->bShouldAdvertise = true;
sessionSettings->bUsesPresence = true;
sessionSettings->bUseLobbiesIfAvailable = true;
sessionSettings->BuildUniqueId = 1;
sessionSettings->Set(FName("MatchType"), matchType, EOnlineDataAdvertisementType::ViaOnlineServiceAndPing);

// create session
const ULocalPlayer* localPlayer{ GetWorld()->GetFirstLocalPlayerFromController() };
if (!sessionInterface->CreateSession(*(localPlayer->GetPreferredUniqueNetId()), NAME_GameSession, *sessionSettings)) {
	sessionInterface->ClearOnCreateSessionCompleteDelegate_Handle(createSessionCompleteDelegateHandle);
	OnCreateSessionComplete.Broadcast(false);
}

```

After (*the host*) successfully created a session, we can open up a new level as a lobby, travel to it as the listen server (waiting for other players to join the session).
```cpp
// can call this on OnCreateSession complete call back
GetWorld()->ServerTravel(const FString& pathToLobby);
```

### Find Sessions
```cpp
IOnlineSession::FindSessions(const FUniqueNetId &searchingPlayerId, const TSharedRef<FOnlineSessionSearch, ESPMode::ThreadSafe> &searchSettings);
```
- FUniqueNetId:
	- Similar to create session, this is the id that used to identify the player
- TSharedRef<FOnlineSessionSearch, ESPMode::ThreadSafe>:
	- Similar to create session, we also need a search setting when finding session, this will be corresponding to the settings when used in creating the session to find a match.
- Search result will be stored in `searchSettings` parameter's `SearchResults` property, and it will be ready to use in the FindSessionComplete callback.

### Join Session
The `FOnlineSessionSearch` variable contains the result and information of each available session found, after we have find the desired session to join, we can use the function on `IOnlineSessionInterface` to join the session.
OnJoinSessionComplete callback
![[joinSessionCompleteCb.png]]
After successfully join the session, we can retrieve the ip address that we need to connect to through the join session complete call back.
Once we have the ip address, we can travel to the address through `ClientTravel` function on `APlayerController` class in Unreal.
```cpp
APlayerController* pController = GetGameInstance()->GetFirstLocalPlayerController();
pController->ClientTravel(ipAddress, ETravelType::TRAVEL_Absolute);
```


### Traveling through levels
![[travelInMultiplayer.png]]