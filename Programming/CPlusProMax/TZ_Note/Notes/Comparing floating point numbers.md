The following function will be good enough for most cases with  
- absEpsilon = 1e-12
- relEpsilon = 1e-8
epsilon should be based on precision of floating point number that's comparing to
```cpp
bool approximatelyEqual(double a, double b, double absEpsilon, double relEpsilon){
	double diff {std::abs(a-b)};

	if(diff <= absEpsilon){
		return true;
	}

	double upperbound = std::max(std::abs(a),std::max(b);
	return diff <= upperbound * relEpsilon;
}
```