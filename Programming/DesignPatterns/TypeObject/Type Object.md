# Type Object
## The Pattern
- Define a **typed object** (`Monster`) class and a **type object** (`Breed`) class.
- Each **typed object** instance stores a reference to the **type object** that describes its type.

The **typed object** stores instance specific data.
The **type object** stores shared data and behaviour across a set of similar objects.

## Comparision
OOP approach:
Base class of `Monster`
Each different types of monster has its own concrete class and inherit from `Monster`.

Issue:
- When there are a lot of monster types, we need a lot  of classes for similar things


- Each time the designer wants to change any attributes of a monster, we need to alter the corresponding class.

## Motivation of Type Object
- Able to change stats without recompile the code.
- Allow designers to do the changes without programmers involved.

Instead of a new class for each type of monster, we can use composition: A `Monster` has a `Breed`.
The `Breed` class will contains attributes that are shared among monsters, i.e.: attack string and health.

This way, each **Breed instance** will represent a type of breed.

## Advantage
- Good when we don't know what types we'll need for the game.
- We can now create new types of breed at run time without complicating/changing the codebase at all.

For example, we can have a database contains all the breeds needed, and have the program creating instances of `Breed` class at runtime.

If designers ever want to add/remove, or change any breed's data, all they need to do is to update the database.