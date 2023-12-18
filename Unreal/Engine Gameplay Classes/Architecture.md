# Overall Architexture
## Controller
PlayerController has Player
## Pawn
Pawn does not have a *PawnMovementComponent* attached by default, so we'll have to create one in the constructor.
*PawnMovementComponent* is not a *SceneComponent* which can be attached to a physical location, so we don't need to attach it to another component.

## InputComponent
## MovementComponent
Controllers can set input value to a *MovementComponent* by calling `SetInputVector`, then in the `Tick` function of *MovementComponent* it will consume the input and make corresponding movements.