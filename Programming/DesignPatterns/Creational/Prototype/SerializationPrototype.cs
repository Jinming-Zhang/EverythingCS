using System;
using System.IO;
using System.Runtime.Serialization.Formatters.Binary;
using System.Xml.Serialization;
using static System.Console;

namespace SerializationPrototype
{
    public static class Extension
    {
        /// <summary>
        /// Note if we use binary serialization, then all the class needed to be copied will need Serializable attribute
        /// </summary>
        /// <param name="obj">object to be copied</param>
        /// <typeparam name="T">generic type of the object</typeparam>
        /// <returns></returns>
        public static T DeepCopyBinSerialized<T>(this T obj)
        {
            var stream = new MemoryStream();
            var formatter = new BinaryFormatter();
            formatter.Serialize(stream, obj);
            stream.Seek(0, SeekOrigin.Begin);
            return (T)formatter.Deserialize(stream);
        }
        /// <summary>
        /// Alternatively, we can use xml serialization, then all the class needed to have a default constructor
        /// </summary>
        /// <param name="obj">object to be copied</param>
        /// <typeparam name="T">generic type of the object</typeparam>
        /// <returns></returns>
        public static T DeepCopyXMLSerialized<T>(this T obj)
        {
            MemoryStream stream = new MemoryStream();
            XmlSerializer s = new XmlSerializer(typeof(T));
            s.Serialize(stream, obj);
            stream.Position = 0; // same as stream.Seek(0, SeekOrigin.Begin);
            return (T)s.Deserialize(stream);
        }
    }
    [Serializable]
    public class Wolf
    {
        public string name, age;
        public Location location;
        public Wolf()
        {

        }
        public Wolf(string name, string age, Location l)
        {
            this.name = name;
            this.age = age;
            this.location = l;
        }

        public override string ToString()
        {
            return $"I'm {this.name}, a {this.age} old wolf live at {this.location.ToString()}";
        }

    }
    [Serializable]
    public class Location
    {
        public float longitude, latitude;
        public Location()
        {

        }
        public Location(float longitude, float latitude)
        {
            this.longitude = longitude;
            this.latitude = latitude;
        }

        public override string ToString()
        {
            return $"Longitude: {this.longitude}, Latitude: {this.latitude}.";
        }
    }
    public static class SerializationPrototype
    {
        public static void SerializationPrototypeDemo()
        {
            Wolf wolf1 = new Wolf("wolfy", "20", new Location(123, 456));
            // use binary serialization
            // Wolf wolf2 = wolf1.DeepCopyBinSerialized();
            // or use xml serialization
            Wolf wolf2 = wolf1.DeepCopyXMLSerialized();
            wolf2.name = "FluffyWolf";
            wolf2.age = "18";
            wolf2.location.longitude = 654;
            wolf2.location.latitude = 789;
            WriteLine($"Wolf 1: {wolf1.ToString()}");
            WriteLine($"Wolf 2: {wolf2.ToString()}");
        }
    }
}