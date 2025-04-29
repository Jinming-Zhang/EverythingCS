using System;
using static System.Console;
namespace SingletonExercise {
    public class SingletonTester {
        public static bool IsSingleton (Func<object> func) {
            var obj1 = func ();
            var obj2 = func ();
            return Object.ReferenceEquals (obj1, obj2);
        }
    }
    public static class SingletonExercise {
        public static void SingletonExerciseDemo () {

        }
    }
}