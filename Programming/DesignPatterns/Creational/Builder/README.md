# Builder Design Pattern

Builder design pattern is used when the objects we want to build are kind of complecated, ie, has a lot of fields. It will be difficult and hard to read if we simply put every thing in a single constructor. The Builder design pattern will provide people a clean API to create an object piece by piece.

## Simple Builder

A simple Builder implementation where a separated class is created and provide methods for building the object.

Depending on the design, the builder methods may or may not be chainable.

using BuilderExcerciseDemo;
## Faceted Builder

A Builder uses facade approach, which stores a reference of the object needs to be built, and enables multiple builders and chaining builder methods. However, the object has to be a reference type. Primitives like string will not work.

Also, each additional sub-builder has to be created and exposed in the parent builder class.

## Fluent Builder

Unlike Faceted Builder, here we do not create sub-builders in the parent builder class. Instead we create a new sub-builder class that inherits the parent builder for each necessary sub-builder required.

This approach is more adhere to the OPEN/CLOSE princile of software design. However, there will be some problems when we need to make a sub-sub-builder that inherits from the sub-builder.

## Fluent Builder with Inheritance

The problem with inheriting in basic Fluent Builder is that the parent-builder will not have the information of the methods of their sub-builder, and so we cannot chain the methods in all the builders together.

To solve this, we can use recursive generic types to provide more type information when creating the parent builder, and enables the ability to call methods in its sub-builder.

## Functional Builder

In a functional builder, we will create a buider class to build the object.

In the class we will keep a list of functions/delegates that will be applied to build the object. Think of this list of functions as list of building methods.
The builder will allow users to register additional functions to its list of functions.
Upon build, the builder will apply all functions in its stored list and apply them to a newly created emtpy object.

The finsihed object will be returned.
To extend the bulder, we use extended methods, so that we are adhereing to the open/close principle, also without the need of inheritance.

## Generalized Functional Builder

Since the process of using functional builder to build object can also be applied to different types of objects. We can generalize the previous functional builder using generic types so that it can be used to build more objects in general.
