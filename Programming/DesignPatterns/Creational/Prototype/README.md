# Prototype Design Pattern

Prototype design pattern is about object copying.

Sometimes we may need to copy a relatively complicated object and make modifications on that object. In this case we will need a deep copy of the object so that the modifications doesn't affect the original one.

## Why Not use C# built-in ICloneable interface

> It's not consistant, sometimes its shallow copy sometimes its deep copy.

---

> Its return is Object type, which is too general and users have to mannually cast the result.

## Copy Constructor and Explicit Interface

### Copy Constructor

We can make an additional constructor for the object, which will takes another object of the same type that need to be copied, and return a deep copied object.

However, we need to make sure that these fields are also deep copied. If the Object has fields that are reference type, we need to make deep copy of that reference type. So it may also need a Copy constructor.

```cs
public class Wolf{
    // normal constructor
    public Wolf(){

    }
    // Copy constructor
    public Wolf(Wolf wolf2){
        this.name = anotherWolf.name;
        this.age = anotherWolf.age;
        // note here, the Location is a reference typed field, so we also require a copy constructor on Location to make a deep copy of the object.
        this.location = new Location(anotherWolf.location);
    }
}
```

### Explicit Interface

Use the explicit genereic interface to deep copy the object.

We also have the type information by using this method.

```cs
public interface IDeepCloneable<T>
    {
        public T DeepClone();
    }
```

However, all the reference types inside the object also have to have a deepclone method. Hence, inherit the IDeepCloneable interface.

```cs
public Wolf DeepClone()
{
    return new Wolf(this.name, this.age, this.location.DeepClone());
}
```

```cs
public Location DeepClone()
{
     return new Location(this.longitude, this.latitude);
}
```

## Copy through Serialization

The idea is to deserialize the object into memory stream first, so all its field are actually deserialized. Then we create the new object from the serialized stream, hence we will get a deep copied new object.

We can acheive this by adding an generic typed Extension method to all objects.

```cs
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
```
