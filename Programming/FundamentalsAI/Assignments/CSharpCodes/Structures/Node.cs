namespace Structures
{
	public class Node<T>
	{
		public struct Edge
		{
			public Node<T> dst;
			public float cost;
		}

		string id = "";
		public string Id
		{
			get
			{
				if (string.IsNullOrEmpty(id))
				{
					id = System.Guid.NewGuid().ToString();
				}
				return id;
			}
		}

		string name;
		public string Name => name;
		List<Edge> neighbours;
		public List<Edge> Neighbours { get => neighbours; set => neighbours = value; }
		T? value;
		public T? Value { get => value; }
		public Node(T v, List<Edge> neighbours, string name = "")
		{
			this.name = string.IsNullOrEmpty(name) ? Id : name;
			value = v;
			this.neighbours = neighbours;
		}

		public Node(string name)
		{
			this.name = string.IsNullOrEmpty(name) ? Id : name;
			this.neighbours = new List<Edge>();
		}

		public void AddNeighbour(Node<T> neighbour, float cost = 1)
		{
			Edge e = new Edge();
			e.dst = neighbour;
			e.cost = cost;
			Neighbours.Add(e);
		}
	}

}
