# Enhanced Input
- Input Actions: link between Enhanced Input System and the project code. It's a layer between raw input and project code.
- Input Mapping Contexts: Maps *raw input* to *Input Actions*. These Contexts can be added through *Enhanced Input Local Player Subsystem*. These can also be prioritized to solve collisions between multiple Actions trying to consume the same raw input.
- Modifiers: Adjust the values of raw input.
- Triggers: Determine whether an *Input Action* should activate based on the modified input values and other input actions' state.
## Trigger - Combo
Ensure that for each *Action* that involves in the combo, it has a *trigger* set up that can fire the action.

## Connect Input Action using Code
We need to create an *Input Mapping Context* to connect Input Actions with the project code.
The *Input Mapping Context* can be assigned through *PlayerController* class, which can also be casted from the Controller that Pawn class has.
After we get/casted *Player Controller* class, we can access its *EnhancedInputLocalPlayerSubsystem* member and assign a *Input Mapping Context* to it with a priority.

```cpp
#include "EnhancedInputComponent.h"
#include "EnhancedInputSubsystems.h"
#include "InputAction.h"
```
- Assign an *InputMappingContext*, i.e. inside `BeginPlay`
```
```
```cpp
void APawn::BeginPlay(){
	Super::BeginPlay();
}
```