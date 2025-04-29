using System;
/// <summary>
/// A Builder uses facade approach, which stores a reference of the object needs to be built, and enables chaining of the building methoes. However, the object has to be a reference type. Primitives like string will not work.
/// </summary>

namespace FacetedBuilderDemo
{
    public class GameLevel
    {
        public int lvIndex, lvWidth, lvHeight, lvDifficulty;
        public string lvDescription, lvDesigner;
        public override string ToString()
        {
            return $"{nameof(lvIndex)}: {lvIndex}, {nameof(lvWidth)}: {lvWidth}, {nameof(lvHeight)}: {lvHeight}, {nameof(lvDifficulty)}: {lvDifficulty}, {nameof(lvDescription)}: {lvDescription}, {nameof(lvDesigner)}: {lvDesigner}.";
        }
    }
    /// <summary>
    /// Faceted Builder enables multiple builders and chaining builder methods.
    /// </summary>
    public class GameLevelBuilder
    {
        protected GameLevel gl = new GameLevel();
        /// <summary>
        /// Its IMPORTANT to pass the gl reference into different types of builders that we want to use, so that all the builders can build on the same object reference.!
        /// If we do not pass the reference, each builder will only build the corresponding INDEPEDENT peice of that object, and the final build result will be INCOMPLETE.
        /// </summary>
        /// <returns></returns>
        public GameLevelInfoBuilder Info => new GameLevelInfoBuilder(gl);// note the reference that passed to the constructor of the builder
        public GameLevelBaseBuilder Base => new GameLevelBaseBuilder(gl);// note the reference
        public GameLevel Build()
        {
            return gl;
        }
    }
    /// <summary>
    /// Here we enables chaing by inheritance, as we expose the sub-builder in the parent builder class, the instance of this sub-builder will also have acess to other sub-builders inside the same parent class.
    /// </summary>
    public class GameLevelBaseBuilder : GameLevelBuilder
    {
        public GameLevelBaseBuilder(GameLevel gl)
        {
            this.gl = gl;
        }
        public GameLevelBaseBuilder Lv(int index)
        {
            gl.lvIndex = index;
            return this;
        }
        public GameLevelBaseBuilder Width(int width)
        {
            gl.lvWidth = width;
            return this;
        }
        public GameLevelBaseBuilder Height(int h)
        {
            gl.lvHeight = h;
            return this;
        }
        public GameLevelBaseBuilder lvDifficulty(int d)
        {
            gl.lvDifficulty = d;
            return this;
        }
    }

    public class GameLevelInfoBuilder : GameLevelBuilder
    {
        public GameLevelInfoBuilder(GameLevel gl)
        {
            this.gl = gl;
        }
        public GameLevelInfoBuilder Description(string d)
        {
            gl.lvDescription = d;
            return this;
        }
        public GameLevelInfoBuilder DesignedBy(string d)
        {
            gl.lvDesigner = d;
            return this;
        }
    }
    public class FacetedBuilderDemo
    {
        public void Demo()
        {
            GameLevelBuilder lvBuilder = new GameLevelBuilder();
            GameLevel gameLevel = lvBuilder.Info.Description("A Level").DesignedBy("Me")
            .Base.Lv(1).lvDifficulty(10).Width(10).Height(10).Build();
            Console.WriteLine(gameLevel);
            // Though each time we call the sub-builder, the builder will return a new instance of the sub-builder, since we pass the object reference in the parent builder, it will still build (overwrite) on the same object
            lvBuilder.Info.Info.Info.DesignedBy("Me again!");
            Console.WriteLine(gameLevel);

        }
    }
}