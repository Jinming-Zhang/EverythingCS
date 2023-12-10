# Remote Procedure Calls
Remote Procedure Calls are functions that we can call on one machine, and have it executed on the other machine.

RPCs in Unreal have a naming convention that has a prefix of "Server"
```cpp
UFUNCTION(Server)
void ServerPickupWeapon(AWeapon* weapon);
```
And the actual implementation should have a suffix of "\_Implementation"
```cpp
void ServerPickupWeapon_Implementation(AWeapon* weapon){
	//function body
}
```

When declaring RPCs, we need to specify whether it's reliable or not.
- Reliable RPCs are guaranteed to be executed.
- Unreliable RPCs could potentially be dropped.
```cpp
UFUNCTION(Server, Reliable)
void ServerPickupWeapon(AWeapon* weapon);
```