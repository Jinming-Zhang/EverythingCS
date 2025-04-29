# Singleton Design Pattern

When we have any objects that we want only have one of the instance at the time, we can make it into a singleton.
We can change our class into a singleton by:

- Make its constructor private, because we don't want people to instanciate multiple instances of our object.
- Make a static field of the instance for people to access

Though Singletons are hard to set up testcases.

## Implementation

Say we have a class that contains tons of information for different kind of wolves:

```cs
public class WolfDatabase{
    public Dictionary<string, string> data;
    public WolfDatabase{
        data = new Dictionary<string, string>();
        // retreive 1M information about different wolves
        data["BigWolf"] = "A bit wolf has blahblahblah*10000word";
    }
    public string GetWolfData(string wolf){
        return data[wolf];
    }
}
```

Because it takes tons of information to be initialized and the information is not likely chanigng frequently, So we can make it into a singleton to improve the performance and avoid people to have many duplicated copy of the class.

```cs
public class WolfDatabase{
    public Dictionary<string, string> data;
    // make the constructor private so people cant create a instance directly
    private WolfDatabase{
        data = new Dictionary<string, string>();
        // retreive 1M information about different wolves
        data["BigWolf"] = "A bit wolf has blahblahblah*10000word";
    }
    // initialze the object by ourself
    private static instance => new WolfDatabase();
    // expose our initialized object to the public
    public static Instance = this.instance;
    public string GetWolfData(string wolf){
        return data[wolf];
    }
}
```

## Dependency Inversion

## Per-Thread Singleton

## Ambient Context
