using System;

namespace FactoryMethodDemo
{
    /// <summary>
    /// Use a Factory Method inside the class to create the object in different ways.
    /// </summary>
    public class Point
    {
        public double x;
        public double y;
        // Factory method
        public static Point NewCartisianPoint(double x, double y)
        {
            return new Point(x, y);
        }
        // Factory method
        public static Point NewPolarPoint(double rho, double theta)
        {
            return new Point(rho * Math.Cos(theta), rho * Math.Sin(theta));
        }
        private Point(double x, double y)
        {
            this.x = x;
            this.y = y;
        }

    }
    public static class FactoryMethodDemo
    {
        public static void Demo()
        {
            Point cartisian = Point.NewCartisianPoint(12, 23);
            Point polar = Point.NewPolarPoint(1, Math.PI / 2);
            Console.WriteLine(polar.x);
        }
    }
}