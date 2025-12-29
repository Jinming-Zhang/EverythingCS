using System;
using System.Threading.Tasks;

namespace AsyncFactoryMethodDemo
{
    /// <summary>
    /// When we need to perform some asynchronous tasks before create the object, it could be a problem since we can not use asynchronous functions inside constructor. So people may create a separate method to initialize the object. However, it's not clear and safe becasue people can forget to call the initialization function.
    ///  Factory design pattern can be a great way here to provide a cleaner API for creating such objects.
    /// </summary>
    public class AsyncInitClass
    {
        private AsyncInitClass()
        {
        }

        private async Task<AsyncInitClass> InitAsync()
        {
            await Task.Delay(1000);
            return this;
        }

        public static Task<AsyncInitClass> CreateAsync()
        {
            Console.WriteLine("Creating Asynchronous class asynchronously....");
            AsyncInitClass result = new AsyncInitClass();
            return result.InitAsync();
        }
        public override string ToString()
        {
            return "I ams an Asynchronous class!.";
        }
    }
    public static class AsyncFactoryMethodDemo
    {
        public static async Task<string> Demo()
        {
            AsyncInitClass result = await AsyncInitClass.CreateAsync();
            return (result.ToString());
        }
    }
}
