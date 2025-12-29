using System;
using static System.Console;

namespace SimplePrototype
{
    public interface IDeepCloneable<T>
    {
        public T DeepClone();
    }

    public class Wolf : IDeepCloneable<Wolf>
    {
        public string name, age;
        public Location location;
        public Wolf(string name, string age, Location l)
        {
            this.name = name;
            this.age = age;
            this.location = l;
        }
        // a copy constructor
        public Wolf(Wolf anotherWolf)
        {
            this.name = anotherWolf.name;
            this.age = anotherWolf.age;
            // note here, the Location is a reference typed field, so we also require a copy constructor on Location to make a deep copy of the object.
            this.location = new Location(anotherWolf.location);
        }
        public override string ToString()
        {
            return $"I'm {this.name}, a {this.age} old wolf live at {this.location.ToString()}";
        }
        /// <summary>
        /// Use the explicit genereic interface to deep copy the object.
        /// We also have the type information by using this method.
        /// </summary>
        /// <returns></returns>
        public Wolf DeepClone()
        {
            return new Wolf(this.name, this.age, this.location.DeepClone());
        }
    }
    /// <summary>
    /// However, all the reference types inside the object also have to have a deepclone method. Hence, inherit the IDeepCloneable interface.
    /// </summary>
    public class Location : IDeepCloneable<Location>
    {
        public float longitude, latitude;
        public Location(float longitude, float latitude)
        {
            this.longitude = longitude;
            this.latitude = latitude;
        }
        // a copy constructor
        public Location(Location anotherL)
        {
            this.longitude = anotherL.longitude;
            this.latitude = anotherL.latitude;
        }

        public override string ToString()
        {
            return $"Longitude: {this.longitude}, Latitude: {this.latitude}.";
        }

        public Location DeepClone()
        {
            return new Location(this.longitude, this.latitude);
        }
    }
    public static class SimplePrototype
    {
        public static void SimplePrototypeDemo()
        {
            Wolf wolf1 = new Wolf("wolfy", "20", new Location(123, 456));
            // without deep copy, we also modifies the original object when manipulating the new object
            // Wolf wolf2 = wolf1;
            // with Copy constructor, we can create deep copy of the original object and modify it independently.
            // Wolf wolf2 = new Wolf(wolf1);
            // Or with the explicit interface
            Wolf wolf2 = wolf1.DeepClone();
            wolf2.name = "FluffyWolf";
            wolf2.age = "18";
            wolf2.location.longitude = 654;
            wolf2.location.latitude = 789;
            WriteLine($"Wolf 1: {wolf1.ToString()}");
            WriteLine($"Wolf 2: {wolf2.ToString()}");
        }
    }
}