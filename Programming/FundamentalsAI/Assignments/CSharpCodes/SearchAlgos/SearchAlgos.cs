using Structures;
using System.Linq;

namespace SearchAlgos
{
	public class SearchAlgos
	{
		public static List<string> BFS<T>(Node<T> start, Node<T> end)
		{
			var paths = new Dictionary<Node<T>, List<string>>();

			Queue<Node<T>> nodeQ = new Queue<Node<T>>();
			nodeQ.Enqueue(start);

			paths.Add(start, new List<string>() { start.Name });

			while (nodeQ.Count > 0)
			{
				Node<T> nodeToExpand = nodeQ.Dequeue();

				foreach (var edge in nodeToExpand.Neighbours)
				{
					var pathToCurrent = paths[nodeToExpand].ConvertAll(name => name);
					if (edge.dst.Equals(end))
					{
						pathToCurrent.Add(edge.dst.Name);
						return pathToCurrent;
					}
					else
					{
						pathToCurrent.Add(edge.dst.Name);
						paths.Add(edge.dst, pathToCurrent);
						nodeQ.Enqueue(edge.dst);
					}
				}
			}

			return new List<string>();
		}

		public static List<string> UniformSearch<T>(Node<T> start, Node<T> end)
		{

			return new List<string>();
		}
	}
}
