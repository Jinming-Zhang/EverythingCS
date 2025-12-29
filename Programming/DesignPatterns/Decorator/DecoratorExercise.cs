using System;
using static System.Console;

namespace DecoratorExercise
{
	public abstract class Beverage
	{
		protected string description;
		public virtual string GetDescription()
		{
			return description;
		}
		public abstract double GetCost();
	}
	public class HomemadeCoffee : Beverage
	{
		public HomemadeCoffee(){
			description = "Home made coffee";
		}
		public override double GetCost()
		{
			return 1.1f;
		}
	}
	public class DarkRosted : Beverage
	{
		public DarkRosted(){
			description = "Dark rosted coffee";
		}
		public override double GetCost()
		{
			return 2.1f;
		}
	}
	public class BlueMountain : Beverage
	{
		public BlueMountain(){
			description = "Blue moutain coffee";
		}
		public override double GetCost()
		{
			return 1.5f;
		}
	}

	public abstract class Condiment : Beverage
	{
		protected Beverage beverage;
	}

	public class Mocha : Condiment
	{
		public Mocha(Beverage beverage)
		{
			this.beverage = beverage;
		}
		public override double GetCost()
		{
			return beverage.GetCost() + 0.5;
		}
		public override string GetDescription()
		{
			return beverage.GetDescription() + " Mocha ";
		}
	}

	public class Whip : Condiment
	{
		public Whip(Beverage beverage)
		{
			this.beverage = beverage;
		}
		public override double GetCost()
		{
			return beverage.GetCost() + 0.1;
		}
		public override string GetDescription()
		{
			return beverage.GetDescription() + " Whip ";
		}
	}

	public class Milk : Condiment
	{
		public Milk(Beverage beverage)
		{
			this.beverage = beverage;
		}
		public override double GetCost()
		{
			return beverage.GetCost() + 1;
		}
		public override string GetDescription()
		{
			return beverage.GetDescription() + " Milk ";
		}
	}

	public static class DecoratorDemo
	{
		public static void Demo()
		{
			Beverage darkrosted = new DarkRosted();
			darkrosted = new Milk(darkrosted);
			darkrosted = new Mocha(darkrosted);
			darkrosted = new Mocha(darkrosted);
			darkrosted = new Whip(darkrosted);
			WriteLine($"{darkrosted.GetDescription()}: {darkrosted.GetCost()}");
		}
	}
}