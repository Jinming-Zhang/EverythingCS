using System;
using System.Collections.Generic;
using System.Linq;

/// <summary>
/// Since the process of using functional builder to build object can also be applied to different types of objects. We can generalize the previous functional builder using generic types so that it can be used to build more objects in general.
/// </summary>
namespace FunctionalBuilderGeneralized
{
    /// <summary>
    /// This is the root functional builder class that other functional builder will inherit from when a builder is needed for other types.
    /// </summary>
    /// <typeparam name="T">The type of the object needs to be built</typeparam>
    /// <typeparam name="TSELF">A recursive generic so that the returned builder from the 'addBuilderMethod' can be chained together when we adding building methods in our custom functional builder. </typeparam>
    public abstract class FunctionalBuilder<T, TSELF>
    where T : new()
    where TSELF : FunctionalBuilder<T, TSELF>
    {
        //
        private readonly List<Func<T, T>> builderMethods = new List<Func<T, T>>();
        public TSELF addBuilderMethod(Action<T> method)
        {
            builderMethods.Add((T objToBuld) =>
            {
                method(objToBuld);
                return objToBuld;
            });
            return (TSELF)this;
        }
        public T Build() => builderMethods.Aggregate(new T(), (objBuilding, builderMethod) => builderMethod(objBuilding));

    }
    /// <summary>
    /// Now we have a wolf to build again.
    /// </summary>
    public class Wolf
    {
        public string name, age, gender;
        public bool hasPack, isSingle;
        public override string ToString()
        {
            string packInfo = hasPack ? "have a pack" : "do not have a pack";
            string statusInfo = isSingle ? "I'm single" : "I'm married";
            return $"I'm {name}, I'm a  {age} years old {gender} wolf. I {packInfo}. {statusInfo}.";
        }
    }
    /// <summary>
    /// Here is our customized functional builder for build a Wolf. This functional builder will inherit from the generlized functional builder and then add necessary builder methods to its list of all builder methods.
    /// </summary>
    public class WolfBuilder : FunctionalBuilder<Wolf, WolfBuilder>
    {
        public WolfBuilder Name(string name) =>
            addBuilderMethod((Wolf w) =>
            {
                w.name = name;
            });

        public WolfBuilder Age(string age)
        {
            addBuilderMethod((Wolf w) =>
            {
                w.age = age;
            });
            return this;
        }

        public WolfBuilder Gender(string gender)
        {
            addBuilderMethod((Wolf w) =>
            {
                w.gender = gender;
            });
            return this;
        }

    }

    public class FunctionalBuilderGeneralizedDemo
    {
        public void Demo()
        {
            WolfBuilder wolfBuilder = new WolfBuilder();
            Wolf w = wolfBuilder.Name("wolfy").Gender("male").Age("20").Build();
            Console.WriteLine(w);
        }
    }
}