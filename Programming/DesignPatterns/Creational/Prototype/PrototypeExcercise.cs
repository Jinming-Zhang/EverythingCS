using System;

namespace PrototypeExcersice
{

    public interface IDeepCopy<T>
    {
        T DeepCopy();
    }
    public class Point : IDeepCopy<Point>
    {
        public int X, Y;
        public Point DeepCopy()
        {
            Point result = new Point();
            result.X = this.X;
            result.Y = this.Y;
            return result;
        }
    }

    public class Line : IDeepCopy<Line>
    {
        public Point Start, End;
        public Line()
        {

        }
        public Line DeepCopy()
        {
            Line line = new Line();
            line.Start = this.Start.DeepCopy();
            line.End = this.End.DeepCopy();
            return line;
        }
    }
}
