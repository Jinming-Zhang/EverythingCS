using System;
using static System.Console;
// Please refactor this hierarchy, giving the base class Shape,
// a constructor that takes an interface IRenderer defined as
// interface IRenderer {
//  string WhatToRenderAs { get; } 
// }
// as well as VectorRenderer and RasterRenderer classes.
// Each implementer of the Shape abstract class should have a constructor that takes an IRenderer, such that, subsequently, each constructed object's ToString () operates correctly.
// For example,
// new Triangle (new RasterRenderer ()).ToString ()
// returns "Drawing Triangle as pixels"
namespace BridgeExercise {
    public interface IRenderer {
        string WhatToRenderAs { get; }
    }

    public abstract class Shape {
        IRenderer renderer1;
        public Shape (IRenderer renderer) {
            this.renderer1 = renderer;
        }
        public Shape () { }
        public string Name { get; set; }
        public override string ToString () {
            return $"Drawing {Name} as {renderer1.WhatToRenderAs}";
        }
    }

    public class Triangle : Shape {
        public Triangle () => Name = "Triangle";
        public Triangle (IRenderer renderer) : base (renderer) {
            Name = "Triangle";
        }
    }

    public class Square : Shape {
        public Square () => Name = "Square";
        public Square (IRenderer renderer) : base (renderer) {
            Name = "Square";
        }
    }

    public class VectorSquare : Square {
        public override string ToString () => "Drawing {Name} as lines";
    }

    public class RasterSquare : Square {
        public override string ToString () => "Drawing {Name} as pixels";
    }

    public class RasterRenderer : IRenderer {
        public string WhatToRenderAs => "pixels";
    }
    public class VectorRenderer : IRenderer {
        public string WhatToRenderAs => "lines";
    }
    // imagine VectorTriangle and RasterTriangle are here too

    public static class BridgeExercise {
        public static void BridgeExerciseDemo () {
            WriteLine (new Triangle (new RasterRenderer ()).ToString ());
        }
    }
}