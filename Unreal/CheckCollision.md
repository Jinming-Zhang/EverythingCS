# Check Collision
Checking overlap by adding collision component to the object:
![[collisionComp.png]]
Accessing the collision component and register call back as appropriate:
```cpp
// register collision event call back
sphereCollision->OnComponentBeginOverlap.AddDynamic(this, &AWeapon::OnSphereOverlap);

// call back
void AWeapon::OnSphereOverlap(UPrimitiveComponent* overlappedComponent, AActor* otherActor, UPrimitiveComponent* otherComp, int32 otherBodyIndex, bool fromSweep, const FHitResult& sweepResult) { }
```