# DesignPatternsCS

These are my personal notes while learning design patterns in C# from Udemy course created by Dmitri Nesteruk.

Also more resource on [refactoring.guru](https://refactoring.guru/design-patterns).

## SOLID Principle

- ### Single Responsibility

- ### Open/Close Principle

- ### Liskov Substitution

- ### Interface Segregation

- ### Dependency Inversion

## Design Patterns

### 1. Creational Design Patterns

- ### [Builder](https://github.com/Jinming-Zhang/DesignPatternsCS/tree/master/DesignPatterns/Builder)

  Separate component for constructing complicated objects.
  We can have multiple builders that cooperating with each other to create the object.
  Often has a fluent interface.

- ### [Factories](https://github.com/Jinming-Zhang/DesignPatternsCS/tree/master/DesignPatterns/Factories)

  When we need more expressive way to create the object other than using the default constructor.
  Facotry can be a method, a separate class or an abstract class as a base class for sub factories.

- ### [Prototype](https://github.com/Jinming-Zhang/DesignPatternsCS/tree/master/DesignPatterns/Prototype)

  Creation of object from an existing object.
  Can be done using interface, copy constructor or serialization.

- ### [Singleton](https://github.com/Jinming-Zhang/DesignPatternsCS/tree/master/DesignPatterns/Singleton)

  When we only want a single instance of the object exists.

### 2. Structural Design Patterns

- ### Adapter

  Convert an interface we get to the interface we need.

- ### Bridge

  Connects components together through abstraction to reduce the complexity of the code structure.

- ### Composite

  Allow cients to treat individual objects and collection of objects uniformly.

- ### Decorator

  Attach/add additional responsibilities/features to objects.

- ### Façade

  Provide a simpler interface over a set of complicated classes/systems.

- ### Flyweight

  Efficiently store/track very large amount of similar objects by using pointers to points to the actual object.

- ### Proxy

  Provides a replacement of the objects that forwards calls tothe real object for performing additional operations.

### 3. Behavioral Design Patterns

- ### Chain of Responsibility

  Allows component to process information/events in a chain.
  Each element in the chain can refers to the next element.

- ### Command

  Encapsulate a request into a separate object.
  Good for audit, replay and undo/redo.

- ### Interpreter

  Parse textual input into object-oriented structures.

- ### Iterator

  Provides an interface for accessing a collection of elements.

- ### Mediator

  A central place to provide services for objects.
  All objects has to refer to the mediator.
  Can be used for message passing, chat room.

- ### Memento

  Provide a read-only token that representing a system's state and allows the system to roll-back to that state.

- ### Null Object

- ### Observer

  Events

- ### State

  State machine.

- ### Strategy

  Uses composition to define an algorithm blueprint/placeholder

- ### Template Method

  Uses inheritance to define an algorithm blueprint/placeholder

- ### Visitor

  Adding functionalities to existing classes, traversal through the hierachy.
