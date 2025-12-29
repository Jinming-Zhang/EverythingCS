using System;
using System.Collections.Generic;
using System.Text;
/// <summary>
/// A simple Builder that exposes an API for building very simplified HTML elements.
/// The Builder is very simple and can not be chained in the process.
/// </summary>
namespace SimpleBuilderDemo
{
    class HTMLStringBuilder
    {
        /// <summary>
        /// Demo to build html elements using only default string/string builder
        /// </summary>
        public void Demo()
        {
            string description = "This is a demo to build html elements using only default string/ string builder, which is very cumbersome and inconvenient.\n";
            Console.WriteLine(description);
            // a <p> tag
            string hello = "hello";
            StringBuilder sb = new StringBuilder();
            sb.Append("<p>");
            sb.Append(hello);
            sb.Append("</p>");
            Console.WriteLine(sb);
            // a <ul> tag
            string words = "some random word";
            sb.Clear();
            sb.Append("<ul>\n");
            foreach (var word in words)
            {
                sb.Append($"<li>{word}</li>\n");
            }
            sb.Append("</ul>");
            Console.WriteLine(sb);
        }
    }

    class HTMLBuilder
    {
        private string rootName;
        HTMLElement root = new HTMLElement();
        public HTMLBuilder()
        {

        }
        public HTMLBuilder(string rootName)
        {
            root.Name = rootName;
            this.rootName = rootName;
        }

        public void AddChild(string name, string text)
        {
            HTMLElement newElmt = new HTMLElement(name, text);
            root.Elements.Add(newElmt);
        }

        public void Clear()
        {
            root = new HTMLElement();
            root.Name = rootName;
        }
        public override string ToString()
        {
            return root.ToString();
        }
        /// <summary>
        /// A demo on how to use the HTMLBulder, for convenience the funciton is also inside HTMLBuilder
        /// </summary>
        public void Demo()
        {
            string description = "This is a demo to build html elements using customized HTMLBuilder. With HTMLBuilder API handles formats and operations such as Add/Delete elements, other users use this API can make html more conveniently.";
            Console.WriteLine(description);
            HTMLBuilder hb = new HTMLBuilder("ul");
            hb.AddChild("li", "hello");
            hb.AddChild("li", "world");
            Console.WriteLine(hb);
        }
    }
    class HTMLElement
    {
        public string Name, Text;
        public List<HTMLElement> Elements = new List<HTMLElement>();
        private const int size = 2;
        public HTMLElement()
        {

        }
        public HTMLElement(string name, string text)
        {
            Name = name;
            Text = text;
        }

        private string ToStringImp(int lv)
        {
            StringBuilder sb = new StringBuilder();
            string indent = new string(' ', size * lv);
            sb.AppendLine($"{indent}<{Name}>");
            if (!string.IsNullOrEmpty(Text))
            {
                sb.Append($"{new string(' ', (lv + 1) * size)}{Text}\n");
            }
            foreach (HTMLElement elmt in Elements)
            {
                sb.Append(elmt.ToStringImp(lv + 1));
            }
            sb.AppendLine($"{indent}</{Name}>");
            return sb.ToString();
        }
        public override string ToString()
        {
            return ToStringImp(0);
        }
    }
    static class HTML
    {
        public static void RunDemo()
        {
            return;
        }
    }
}
