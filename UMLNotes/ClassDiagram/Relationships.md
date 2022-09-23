
# Class Relationships
## Inheritance
A solid line from child class to parent class with unfilled arrowhead.<br/>

## Associations (has)
### Bi-directional association
Both classes are aware of each other and their relationship.
![[Pasted image 20220923011819.png]]
>relation is indicated at the side of target class.
>role of the targeted class is also on the side of target class.

`Flight` has 0-1 `Plane`
`Plane` has 0-many `Flights`

### Uni-directional Association
Two classes are related but only one class aware of the relationship.
> Relation is indicated as a solid line with an open arrow pointing to the known (containing) class
![[Pasted image 20220923012640.png]]

`OverdrawnAccountReport` and 0-many `BankAccount`
### Basic Aggregation (whole to its parts)
In basic aggregation the `part` class is independent of the `whole`
![[Pasted image 20220923014044.png]]
> Relationship is indicated as a solid line from parent to part class, with an unfilled diamond on the side of **parent** class.

### Composition Aggregation
In composition aggregation, the `part` class is dependent on the `parent` class.
![[Pasted image 20220923014400.png]]
> Relationship is similar to basic aggregation, but with a **filled** diamond on the side of **parent** class.
### Association Class