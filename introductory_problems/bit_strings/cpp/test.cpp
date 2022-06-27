// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
#include <string.h>
using namespace std;
#define bit 2
#define nl "\r\n"
unsigned long long puis(unsigned long long pow)
{	unsigned long long n=2;
	if (pow == 0)
		return 1;
	for(unsigned long i=1; i<pow;i++)
	{
		n*=bit;
		n=n%((unsigned long long)1e9+7);
		// ajout d'un modulo sur le calcul pour éviter la saturation
	}
	return n;
}

// Driver Code
int main()
{
	unsigned long long N = 00;
	cin >> N;

	unsigned long long temp;
	temp = puis(N);
	cout << temp << nl;
	
	return 0;
}
