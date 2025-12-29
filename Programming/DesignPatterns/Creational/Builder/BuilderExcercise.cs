using System;
using System.Collections.Generic;
using System.Linq;
/// <summary>
/// You are asked to implement a Builder design pattern for rendering simple chunks of code.
/// Sample use of the builder you are aksed to create:
/// var cb = new CodeBuilder("Person").AddField("Name", "string").AddField("Age", "int");
/// Console.WriteLine(cb);
/// The expected output of the above code is:
/// public class Person{
///     public string name;
///     public int Age    
/// }
/// Please observe the same placement of curly braces and use two-space indentaion.
/// </summary>
namespace BuilderExcerciseDemo
{
    public class Person
    {
        public string Name;
        public int Age;
    }
    // public class CodeStringBuilder
    // {
    //     private string className;
    //     public CodeStringBuilder(string className)
    //     {
    //         this.className = className;
    //     }

    //     public
    // }
    public class CodeBuilder
    {
        private string className;
        private List<Func<string, string>> stringBuilders = new List<Func<string, string>>();

        public CodeBuilder(string className)
        {
            this.className = className;
        }

        public CodeBuilder AddField(string fieldValue, string fieldType)
        {
            stringBuilders.Add((result) =>
            {
                result += $"  public {fieldType} {fieldValue};\n";
                return result;
            });
            return this;
        }
        public string Build()
        {
            string init = $"public class {className}\n";
            init += "{\n";
            string built = stringBuilders.Aggregate(init, (str, builder) => builder(str));
            return built + "}";
        }
        // public static implicit operator string(CodeBuilder cb) => cb.Build();
        public override string ToString()
        {
            return this.Build();
        }
    }
    public class BuilderExcerciseDemo
    {
        public void Demo()
        {
            Console.WriteLine("%%%%%%%%%     Demo for Builder Excercise...     %%%%%%%%%");
            var cb = new CodeBuilder("Person").AddField("Name", "string").AddField("Age", "int");
            Console.WriteLine(cb);
        }
    }
}