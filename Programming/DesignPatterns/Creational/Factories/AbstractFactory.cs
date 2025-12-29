using System;
using System.Collections.Generic;
using static System.Console;
/// <summary>
/// Abstract Factory will give out abstract objects instead of concrete object.
/// In the Factory Method / Inner Factory Class we return the real constructed object. In Abstract Factory we will return the abstract class or interface.
/// This let us able to craete a list of Factory and loop them through.
/// Recall that interface contains a list of methods that every class that inherits the interface has to implement.
/// </summary>
namespace AbstractFactoryDemo
{
    /// <summary>
    /// Simple interface that objects inherits this has to provide a way to consume the drink
    /// </summary>
    public interface IHotDrink
    {
        void Comsume();
    }

    /// <summary>
    /// Here are two example hot drinks
    /// </summary>
    internal class Tea : IHotDrink
    {
        public void Comsume()
        {
            WriteLine("This tea is nice!");
        }
    }

    internal class Coffee : IHotDrink
    {
        public void Comsume()
        {
            WriteLine("This coffee is sensational!");
        }
    }

    /// <summary>
    /// Say we want a factory of the IHotDrink so we can make different type of teas/coffees
    /// Then for each type of Tea/Coffee (Hotdrink) we will create a Factory class that inherit from this interface.
    /// Such that they all have to implement a method to prepare/make the specific type of tea/coffee (hotdrink)
    /// </summary>
    public interface IHotDrinkFactory
    {
        IHotDrink Prepare(int amt);
    }
    /// <summary>
    /// A tea factory that makes one type of tea.
    /// We can have other type of tea factories (MilkTeaFactory:IHotDrinkFactory) depends on the need
    /// </summary>
    internal class TeaFactory : IHotDrinkFactory
    {
        public IHotDrink Prepare(int amt)
        {
            WriteLine($"Put in a tea bag, boil water, pour {amt} ml water, add lemon.");
            return new Tea();
        }
    }

    /// <summary>
    /// A coffee factory that makes one type of coffee
    /// </summary>
    internal class CoffeeFactory : IHotDrinkFactory
    {
        public IHotDrink Prepare(int amt)
        {
            WriteLine($"Grind some beans, boil water, pour {amt} ml water, add sugar and cream.");
            return new Coffee();
        }
    }

    /// <summary>
    /// This is the root class that needs all the factories.
    /// Without Factory then we may need to create classes for different types of hot drinks, or we have to create each type of HotDrinkFactory one by one.
    /// Since we have a Abstract Factory, we can initialize all the factories needed, and just use the proper one and call its interface/abstract function whereever is necessary.
    /// </summary>
    public class HotDrinkMachine
    {
        // We also could use a list representation
        public enum AvailableDrink
        {
            Coffee, Tea
        }
        // we can have a bounch of factories. Here is why we use Abstract Factories.
        // Because we will be able to make a list of such interfaces/abstract classes
        private Dictionary<AvailableDrink, IHotDrinkFactory> factories = new Dictionary<AvailableDrink, IHotDrinkFactory>();
        public HotDrinkMachine()
        {
            // initialize factories for each available drink
            foreach (AvailableDrink drink in Enum.GetValues(typeof(AvailableDrink)))
            {
                var factory = (IHotDrinkFactory)Activator.CreateInstance(Type.GetType("AbstractFactoryDemo." + Enum.GetName(typeof(AvailableDrink), drink) + "Factory"));
                factories.Add(drink, factory);
            }
        }
        /// <summary>
        /// Provide a HotDrink.
        /// We find the corresponding factory for that drink, call the function, the factory will return the object with type of the drink.
        /// Since the drink also implements the interface, we can use Liscov Subsititution to return the interface, so externals can directly consume the drink
        /// </summary>
        /// <param name="drink">Hot Drink type provided in the list</param>
        /// <param name="amount">Variable needed to make the specific hot drink</param>
        /// <returns>The Hotdrink (Interface) that can be consumed. (Liscov substitution).</returns>
        public IHotDrink MakeDrink(AvailableDrink drink, int amount)
        {
            return factories[drink].Prepare(amount);
        }
    }
    public static class AbstractFactoryDemo
    {
        public static void Demo()
        {
            HotDrinkMachine machine = new HotDrinkMachine();
            IHotDrink drink = machine.MakeDrink(HotDrinkMachine.AvailableDrink.Coffee, 10);
            drink.Comsume();
        }
    }
}