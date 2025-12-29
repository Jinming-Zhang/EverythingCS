# Factory Design Pattern

Factory is another Creational design pattern. Instead of Builder, Factory is suitable when the object can be initialized/created in many different ways and we can not use overload for constructor to achieve the purpose in a well-structured way.

An example would be a Point class. Say we need a class to create Points:

```cs
public Class Point{
    float x;
    float y;
}
```

However, a Point can be created using different systems, such as Cartesian coordinate or Polar coordinates.

Since both system use same input parameters (two floats), we can not distinguish them by only using constructor.

In this case, a Factory design pattern will provide a cleaner way for other people uses this system to create Points according to their needs.

Unlike Builder which create an object piece by piece, Factory usually create the object as a whole at once.

## Factory Method

Use a Factory Method inside the class to create the object in different ways.

```cs
public class Something{
    private Something(){

    }
    public static Something CreateSomethingWithGood(){
        // create the object depending on the need
        Something result = new Something();
        result.balabala = banana;
        return result;
    }
    public static Something CreateSomethingWithWood(){
        // create the object depending on the need
        Something result = new Something();
        result.balabala = oak;
        return result;
    }
}
```

## Asynchronous Factory Method

When we need to perform some asynchronous tasks before create the object, it could be a problem since we can not use asynchronous functions inside constructor. So people may create a separate method to initialize the object. However, it's not clear and safe becasue people can forget to call the initialization function.

```cs
public class AsyncInitClass {
        public AsyncInitClass(){
        }

        public async Task<AsyncInitClass> InitAsync(){
            AsyncInitClass result = new AsyncInitClass();
            await Task.Delay(1000);
            return result;
        }
    }
```

Factory design pattern can be a great way here to provide a cleaner API for creating such objects.

## Inner Factory

Create a separate Factory class inside the object to adhere the single responsibility principle. The Factory class can also be outside of the object, but then the object needs a public constructor for the Factory class to use. If we don't want other people to use the default constructor, it's better to use a Inner Factory Class.

```cs
public class Point
    {
        public double x, y;
        private Point(double x, double y)
        {
            this.x = x;
            this.y = y;
        }
        public static Point Origin = new Point(0, 0); // a static field
        // public static Point Origin => new Point(0,0); // a static property
        // public static Factory Factory = Factory;
        public static class Factory
        {
            public static Point NewCartisianPoint(double x, double y)
            {
                return new Point(x, y);
            }
            public static Point NewPolarPoint(double rho, double theta)
            {
                return new Point(rho * Math.Cos(theta), rho * Math.Sin(theta));
            }
        }

    }
```

## Abstract Factory

Can be used to create related objects.
Abstract Factory will give out abstract objects instead of concrete object.

In the Factory Method / Inner Factory Class we return the real constructed object. In Abstract Factory we will return the abstract class or interface.

This let us able to craete a list of Factory and loop them through.
Recall that interface contains a list of methods that every class that inherits the interface has to implement.
