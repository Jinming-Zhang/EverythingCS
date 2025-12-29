# Problem 1
### a)
##### n must be a multiple of 3
If n is not a multiple of 3, then everday there will be a team of  either 2 or 1 people.
Since for people in other group, they have to change two of their teammates everyday, this means at the end the group of 1 or 2 people will not have enough people to swap, and students won't be able to work with each of the other students exactly once.

##### d must be $\frac{n-1}{2}$
Since when (n,d) is happy, each student will be able to work with other n-1 students exactly one day, and each day the student is in a group of two, so each student works with 2 different students each day. And for the student to work with all n-1 students, it will take $\frac{n-1}{2}$ days.

##### n must be 3,9,15 if n<=20 and (n,d) is happy
When n<=20, possible values are 3,6,9,12,15,18.
Among the possible values of n, only when n = 3, 9, 15, we can get a whole number for d = 1, 4, 7.
This means when n=6, 12, 18, at the last day, there has to be people that have to work with other people that they have worked with before.

### b)
When n = 9, let A, B, C, D, E, F, G, H, I denote the 9 different students, one possible arrangement for 4 days that makes (9, 4) happy is as follows:
| day 1 | ABC | DEF | GHI |
|-------|-----|-----|-----|
| day 2 | ADG | BEH | CFI |
| day 3 | AEI | DHC | GBF |
| day 4 | GEC | DBI | AHF |
Arrange 9 students into a 3x3 matrix, then each row, col, left/right diagonals forms a team such that for every students, they worked with the other n-1 students exactly once in 4 days.

### c)
See the attached studentTeamFormation.py