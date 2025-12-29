using System;

namespace FluentBuilderDemo
{
    public class Wolf
    {
        public string name, gender, color;
        public int age;
        public float height, weight;

        /// <summary>
        /// Need to expose the builder, down to the level where the desired buidling components are defined.
        /// ie: only allow external builder to build up to basic info, then expose the builder as WolfInfoBuilder.
        /// if more detailed status is necessary to expose, then create the builder as WolfStatusBuilder
        /// </summary>
        public class Builder : WolfStatusBuilder<Builder>
        {

        }
        public static Builder NEW = new Builder();
        public override string ToString()
        {
            return $"My name is {name}, I am a {gender} {color} wolf of age {age}, {height} cm and {weight} kg";
        }
    }

    /// <summary>
    /// Unlike Faceted Builder, here we do not create sub-builders in the parent builder class. Instead we create a new sub-builder class that inherits the parent builder for each necessary sub-builder required.
    /// This approach is more adhere to the OPEN/CLOSE princile of software design. However, there will be some problems when we need to make a sub-sub-builder that inherits from the sub-builder. This will be resolve later in the FluentBuilderInheritant demo.
    /// </summary>
    public abstract class WolfBuilder
    {
        protected Wolf wolf;
        public Wolf Build()
        {
            return wolf;
        }
    }

    //Foo: Bar<Foo>
    public class WolfInfoBuilder<SELF> : WolfBuilder where SELF : WolfInfoBuilder<SELF>
    {
        public SELF Gender(string gender)
        {
            wolf.gender = gender;
            return (SELF)this; // this is a WolfInfoBuilder, which IS (inherit from) WolfInfoBuilder
        }

        public SELF NameIs(string name)
        {
            wolf.name = name;
            return (SELF)this;
        }
        public SELF OfColor(string color)
        {
            wolf.color = color;
            return (SELF)this;
        }
    }

    public class WolfStatusBuilder<SELF> : WolfInfoBuilder<WolfStatusBuilder<SELF>> where SELF : WolfStatusBuilder<SELF>
    {
        public SELF OfAge(int age)
        {
            wolf.age = age;
            return (SELF)this;
        }
        public SELF ofWeight(float weight)
        {
            wolf.weight = weight;
            return (SELF)this;
        }
        public SELF ofHeight(float height)
        {
            wolf.height = height;
            return (SELF)this;
        }
    }

    public class WolfFluentBuilderDemo
    {
        public void Demo()
        {
            Wolf newWolf = Wolf.NEW.Gender("Male").NameIs("Wolfy").OfColor("Blue").OfAge(20).ofHeight(174f).ofWeight(67).Build();
            Console.WriteLine(newWolf.ToString());
        }
    }
}