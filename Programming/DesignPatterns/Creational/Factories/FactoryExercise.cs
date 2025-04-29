using System;
using static System.Console;
/// <summary>
/// Given a class called Person. The person has two fields: Id, and Name.
/// Implement a non-static PersonFactory that has a CreatePerson() method that takes a person's name.
/// The Id of the person should be set as a 0-based index of teh object created. So, the first person the factory makes should have Id=0. Second Id=1.
/// </summary>
namespace FactoryPractice
{
    public class Person
    {
        public int Id { get; set; }
        public string Name { get; set; }
    }
    public class PersonFactory
    {
        public int index;
        public PersonFactory()
        {
            this.index = 0;
        }
        public Person CreatePerson(string name)
        {
            Person newPerson = new Person();
            newPerson.Id = this.index;
            newPerson.Name = name;
            this.index++;
            return newPerson;
        }
    }
    public static class FactoryPractice
    {
        public static void FactoryPracticeDemo()
        {

        }
    }
}