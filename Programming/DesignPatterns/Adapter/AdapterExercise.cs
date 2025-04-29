// Here's a very synthetic example for you to try.
// You are given an IRectangle interface and an extension method on it. Try to define a SquareToRectangleAdapter that adapts the Square to the IRectangle interface.
using System;
using static System.Console;
namespace AdapterExercise {
    public class Square {
        public int Side;
        public Square (int side) {
            this.Side = side;
        }
    }

    public interface IRectangle {
        int Width { get; }
        int Height { get; }
    }

    public class Rectangle : IRectangle {
        int width, height;
        public Rectangle (int width, int height) {
            this.width = width;
            this.height = height;
        }
        public int Width => this.width;

        public int Height => this.height;
    }
    public static class ExtensionMethods {
        public static int Area (this IRectangle rc) {
            return rc.Width * rc.Height;
        }
    }

    public class SquareToRectangleAdapter : IRectangle {
        Square square1;
        public SquareToRectangleAdapter (Square square) {
            square1 = square;
        }

        public int Width => square1.Side;

        public int Height => square1.Side;
        // todo
    }

    public static class AdapterExercise {
        public static void AdapterExerciseDemo () {
            // new we have an API that can calculate area of a rectangle
            Rectangle r1 = new Rectangle (10, 20);
            Write ($"Area of a rectangle [{r1.Width}, {r1.Height}] is: ");
            WriteLine (r1.Area ());
            // say now we have a square, and we want to use the API to also calculate the area of our square
            // however, we cannot change the original api
            // So here, we make an adapter that take our square into a rectangle that the API that can use
            Square s1 = new Square (15);
            SquareToRectangleAdapter s1Rec = new SquareToRectangleAdapter (s1);
            Write ($"Area of a square [{s1.Side}] is: ");
            WriteLine (s1Rec.Area ());

        }
    }
}