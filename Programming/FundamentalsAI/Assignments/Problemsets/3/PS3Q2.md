### a)
| House    | Color  | Student  | Food      | Sport      | Singer        |
|----------|--------|----------|-----------|------------|---------------|
| House 1  | Purple | Billy    | Steak     | Vollayball | Tylor Swift   |
| Houses 2 | Orange | Xiaofeng | Salad     | Basketball | Kyan West     |
| House 3  | Blue   | Jinhao   | Sushi     | Hockey     | Justine Biber |
| House 4  | Pink   | David    | Samosa    | Baseball   | Jay Zed       |
| House 5  | Red    | Sommer   | Sandwitch | Soccor     | Katy Perry    |

### b)
We can model the problem as a CSP as follows:
##### Variables and Domain
 Let X[house, color, student, food, sport, singer] be a six dimensional boolean variable with domain [0, 1], such that X is 1 if and only if it satisfys all the constraints
 
##### Constriants 1-4
1. X[**house 1**, for all colors, **Billy**, for all foods, for all sports, for all singer] = 1
2. for each house **h**:
	 X[**h**, **pink**, for all students, for all foods, for all sports, for all singers] = 1
	 if and only if
	 X[**h+1**, **red**, for all students, for all foods, for all sports, for all singers] = 1
3. for each house **h**:
	 X[**h**, for all colors, for all students, for all foods, basketball, for all singers] = 1
	 if and only if
	 X[**h+1**, for all colors, for all students, steak, for all sports, for all singers] = 1 **or** X[**h-1**, for all colors, for all students, steak, for all sports, for all singers] = 1
4. X[for all houses, for all colors, for all students, for all foods, for all sports, katy perry] = 1

#### c)
Another way to model this problem as CSP (fill each feature into corresponding house):
##### Variables
Each color, student, food, sport, singer be a variable.
##### Domains
Each variable's domain will be the number of houses.
##### Constraints 1-4
1. Billy = 1
2. Pink < Red
3. Basketball = steak +1 **or** Basketball = steak - 1
4. Katy Perry = 1-5 (can be ignored)

#### Comparision
c) is easier to understand and set up the constraints.
b) is more generalized and easy to model, but need some efforts to setup the constraints.
