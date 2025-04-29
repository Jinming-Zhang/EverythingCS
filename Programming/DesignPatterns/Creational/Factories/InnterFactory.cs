using System;

namespace InnerFactoryDemo
{
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

    public static class InnerFactoryDemo
    {
        public static void Demo()
        {
            Point polarPoint = Point.Factory.NewPolarPoint(1, 1.6);
        }
    }
}