using System;
using System.Text;
/// <summary>
/// This demo will show the process of making a builder chainable for the subbuilders that inherited from it.
/// The problem with inheriting is that the parent-builder will not have the information of methods inside the sub-builder, and cannot chain the methods in all the builders together.
/// To solve this, we'll use recursive generic types to provide more type information when creating the parent builder, and enables the ability to call methods in its sub-builder
/// </summary>
namespace FluentBuilderInheritanceDemo
{
    /// <summary>
    /// Animal class will be a parent base class that contains several mandatory fields and optional fields.
    /// Will have a parent builder to build an Animal object
    /// </summary>
    public class Animal
    {
        public string species, gender; // mandatory
        public int age; // optional
        public float height, weight;// optional

        public class Builder : AnimalBasicBuilder<Builder, Animal>
        {
            public Builder(string species, string gender) : base(species, gender)
            {

            }
        }
        // public static Func<string, string, Builder> NEW = (string species, string gender) => new Builder(species, gender);
        public static Builder NEW(string species, string gender) => new Builder(species, gender);

        // public AnimalBasicBuilder animalBuilder;
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.Append($"Animal {gender} {species}.\n");
            if (age != default(int))
            {
                sb.Append($"Age:{age}. ");
            }
            if (height != default(float))
            {
                sb.Append($"Height :{height}. ");
            }
            if (weight != default(float))
            {
                sb.AppendLine($"Weight :{weight}. ");
            }
            return sb.ToString();
        }
    }

    /// <summary>
    /// Now say we have a wolf, that extends Animal.
    /// A Wolf also have some madatory and option fields in addition to an Animal.
    /// And we want to make a Builder for Wolf, and we want that builder to inherit from the existed Animal builder. And we want to be able to chain the methods in both builder together.
    /// </summary>
    public class Wolf : Animal
    {
        public class WB : WolfBuilder<WB>
        {
            public WB(string gender, string name, string color) : base(gender, name, color)
            {

            }
        }
        // public static Func<string, string, string, WB> NEW_WOLF = (string gender, string name, string color) => new WB(gender, name, color);
        public static WB NEW_WOLF(string gender, string name, string color) => new WB(gender, name, color);
        public string color, name; // madatory
        public bool hasPack, isSingle; // optional
        public override string ToString()
        {
            StringBuilder sb = new StringBuilder();
            sb.AppendLine($"My name is {name}. I am a {gender} {color} {species}. \n");
            if (age != default(int))
            {
                sb.Append($"Age:{age}. ");
            }
            if (height != default(float))
            {
                sb.Append($"Height :{height}. ");
            }
            if (weight != default(float))
            {
                sb.AppendLine($"Weight :{weight}. ");
            }

            if (hasPack)
            {
                sb.AppendLine($"I have already have a pack. ");
            }
            else
            {
                sb.AppendLine($"I don't have a pack yet. ");
            }

            if (isSingle)
            {
                sb.AppendLine($"I am single! ");
            }
            else
            {
                sb.AppendLine($"I am married. ");
            }
            return sb.ToString();
        }
    }

    public abstract class AnimalBuilder<T> where T : Animal, new()
    {
        protected T animal = new T();
        public T Build()
        {
            return animal;
        }
    }

    public class AnimalBasicBuilder<SELF, T> : AnimalBuilder<T> where T : Animal, new() where SELF : AnimalBasicBuilder<SELF, T>
    {
        /// <summary>
        /// Initialize Bulder for mandatory fields
        /// </summary>
        /// <param name="species">madatory species of the animal</param>
        /// <param name="gender">madatory gender of the animal (by design!)</param>
        public AnimalBasicBuilder(string species, string gender)
        {
            animal.species = species;
            animal.gender = gender;
        }

        // builder for optional parameters
        public SELF Age(int age)
        {
            animal.age = age;
            return (SELF)this;
        }

        public SELF Height(float h)
        {
            animal.height = h;
            return (SELF)this;
        }

        public SELF Weight(float w)
        {
            animal.weight = w;
            return (SELF)this;
        }
    }

    public class WolfBuilder<SELF> : AnimalBasicBuilder<WolfBuilder<SELF>, Wolf> where SELF : WolfBuilder<SELF>
    {
        public WolfBuilder(string gender, string name, string color) : base("wolf", gender)
        {
            animal.name = name;
            animal.color = color;
        }

        public SELF hasPack(bool h)
        {
            animal.hasPack = h;
            return (SELF)this;
        }

        public SELF isSingle(bool s)
        {
            animal.isSingle = s;
            return (SELF)this;
        }
    }

    public class FluentBulderInheritanceDemo
    {
        public void Demo()
        {
            Animal a = Animal.NEW("animal", "male").Age(20).Height(174).Weight(66).Build();
            Console.WriteLine(a);
            Wolf wolf = Wolf.NEW_WOLF("male", "wolfy", "blue").Age(20).hasPack(true).Height(172).Weight(77).isSingle(true).Build();
            Console.WriteLine(wolf);
        }
    }

}