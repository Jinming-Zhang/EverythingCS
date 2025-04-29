using System.Linq;
namespace CSP
{
  class Cryptarithmetic
  {
    List<int> Domain
    {
      get
      {
        return new List<int> { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
      }
    }

    HashSet<char> variables = new HashSet<char>();
    public Cryptarithmetic(String variables)
    {
      foreach (char c in variables)
      {
        variables.Append(c);
      }
    }

    public void Solve()
    {
      variables.Clear();
      foreach (char c in "EATTHATAPPLE")
      {
        variables.Add(c);
      }
      var result = SolveHelper(new Dictionary<char, string>());
      if (result == null)
      {
        Console.WriteLine("No solution found");
      }
      else
      {
        Console.WriteLine("Solution found:");
        foreach (var k in result.Keys)
        {
          Console.WriteLine($"\t {k} -> {result[k]}");
        }
      }
    }

    public Dictionary<char, string> SolveHelper(Dictionary<char, string> currentAssignments)
    {
      // base case
      if (currentAssignments.Keys.Count == variables.Count)
      {
        if (Solved(currentAssignments))
        {
          return currentAssignments;
        }
        else
        {
          return null;
        }
      }

      // recursion solve 
      var assigned = currentAssignments.Keys.ToList();
      foreach (char c in variables)
      {
        if (!assigned.Contains(c))
        {
          var candidates = GetDomainValues(c, currentAssignments);
          foreach (var candidate in candidates)
          {
            Dictionary<char, string> newAssignments = new Dictionary<char, string>();
            foreach (var k in currentAssignments.Keys)
            {
              newAssignments.Add(k, currentAssignments[k]);
            }
            newAssignments.Add(c, candidate);
            var result = SolveHelper(newAssignments);
            if (result != null)
            {
              return result;
            }
          }
        }
      }
      return null;
    }

    public bool Solved(Dictionary<char, string> assignments)
    {
      int n1 = int.Parse(assignments['E'] + assignments['A'] + assignments['T']);
      int n2 = int.Parse(assignments['T'] + assignments['H'] + assignments['A'] + assignments['T']);
      int result = int.Parse(assignments['A'] + assignments['P'] + assignments['P'] + assignments['L'] + assignments['E']);
      return n1 + n2 == result;
    }

    public List<string> GetDomainValues(char variable, Dictionary<char, string> currentAssignment)
    {
      List<string> d = Domain.ConvertAll<string>(i => i.ToString());
      if (variable == 'E' || variable == 'T' || variable == 'a')
      {
        d.Remove("0");
      }
      if (currentAssignment == null || currentAssignment.Keys.Count == 0)
      {
        return d;
      }

      foreach (char i in currentAssignment.Keys)
      {
        string assignment = currentAssignment[i];
        d.Remove(assignment);
      }
      return d;
    }

    public List<int> DeepCloneList(List<int> original)
    {
      return original.ConvertAll<int>(e => e);
    }
  }
  public class Constraint
  {
    List<(char, char, char)> constraint = new List<(char, char, char)>();
    public Constraint()
    {
      constraint.Add(('T', 'T', 'E'));
    }
  }
}
