
# Replication
Replicate variable on client.

> Replication process only works from **server** to **client**, it's a **one way** process.


To have a variable replicated on client:
1. The actor needs to be a replicated actor
2. we need to give the variable a UPROPERTY
```cpp
UPROPERTY[Replicated]
	class AWeapon *overlappingWeapon;
```

Then for any class that has variables need to be replicated, we need to override a function:
```cpp
virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& outLifeTimeProps) const override;
```

Inside the function, we will register the variables that need to be replicated
```cpp
#include "Net/UnrealNetwork.h"
virtual void GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& outLifeTimeProps){
	// this will replicate the variable to all client once it's changed
	DOREPLIFETIME(ABlasterCharacter, overlappingWeapon);
	// this will only replicate the varialbe to the client that satisfy the providing condition
	DOREPLIFETIME_CONDITION(ABlasterCharacter, overlappingWeapon, COND_OwnerOnly);
} 
```

After we registered the variable, every time the value of the variable changes, it will be replicated and set all on client's `ABlasterCharacter` class.

> When we set and replicating variables, if it starts with the server, then we need to pay attention in situations that:
> 	 1. we may set the variable of the object on the server as well in addition to replicating the variable to the client objects.
> 	 2. If we trying to use the variable to do some specific action on the target client only, we need to make sure the object on the server doesn't do the same. 
> So we need to add additional condition check to see if the object is on the server or client.

### Rep Notifies
A function will be called when the replication finished on the client, the naming convention is to start the function with **OnRep_** followed by the variable name, and has a UFUNCION macro.

The function takes in an option parameter that is the value of the variable before the new value is being replicated.
```cpp
UFUNCTION()
void OnRep_OverlappingWeapon(AWeapon* lastValue);
```

To have Rep Notifier set for a variable, we'll need to adjust the UPROPERTY on that variable to the following:
```cpp
	UPROPERTY(ReplicatedUsing = OnRep_OverlappingWeapon)
	class AWeapon *overlappingWeapon;
```

### Application of RepNotifies
*One application for Rep Notifies is to shows client specific logic, such as UI.*
This is because when we setting the overlapping weapon on the server, the character object on the server first gets updated, then the value is replicated to the corresponding client.
If we have the logic directly implemented in the function code, it will be called on both server and client object. However, if we put the logic into **RepNotifies**, the the logic will only be run the client.

Another issue with this is that, the logic that depends on the RepNotifies will not be called on the server, so w