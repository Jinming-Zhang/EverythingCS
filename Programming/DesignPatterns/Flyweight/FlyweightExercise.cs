using System;
using System.Collections.Generic;
using System.Text;

/// <summary>
/// You are given a class called Sentence, which takes a string such as "hello world". You need to provide an interface such that the indexer returns a WordToken which can be used to capitalize a particular word in thes entence.
/// Typical use would be something like:
/// var sentence = new Sentence("hellow world");
/// sentence[1].Capitalize = true;
/// WriteLine(sentence);
/// </summary>
namespace FlyweightExercise {
    public class Sentence {
        List<string> words;
        List<WordTokenRange> capitalizeRanges;
        public Sentence (string plainText) {
            // todo
            capitalizeRanges = new List<WordTokenRange> ();
            this.words = new List<string> (plainText.Split (" "));
        }

        public WordToken this [int index] {
            get {
                // todo
                WordTokenRange wr = new WordTokenRange (index, index);
                capitalizeRanges.Add (wr);
                return wr.token;
            }
        }

        public override string ToString () {
            // output formatted text here
            StringBuilder sb = new StringBuilder ();
            for (int i = 0; i < this.words.Count; i++) {
                string word = this.words[i];
                foreach (WordTokenRange r in capitalizeRanges) {
                    if (r.IsInRange (i) && r.token.Capitalize) {
                        char[] chars = word.ToCharArray ();
                        word = "";
                        foreach (char c in chars) {
                            word += char.ToUpper (c);
                        }
                    }
                }
                sb.Append (word);
                if (i != this.words.Count - 1) {
                    sb.Append (" ");
                }
            }

            return sb.ToString ();
        }

        public class WordToken {
            public bool Capitalize;
        }
        public class WordTokenRange {
            int start, end;
            public WordToken token;
            public WordTokenRange (int start, int end) {
                this.start = start;
                this.end = end;
                this.token = new WordToken ();
            }
            public bool IsInRange (int index) {
                return index >= this.start && index <= this.end;
            }
        }
    }

    public static class FlyweightExercise {
        public static void FlyweightExerciseDemo () {
            Sentence s = new Sentence ("alpha beta gamma");
            s[1].Capitalize = true;
            Console.WriteLine (s);
        }
    }
}