// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
using namespace std;

// Driver Code
int main()
{
	long N,nombre;
	long long sum=0;

	// theoreme comme quoi la somme des entiers de 1 a N
	// n(n+1)/2
	// donc si il manque un seul nombre on peut faire la somme des nombres
	// et regarder la relation n(n+1)/2-summ
		
	cin >> N;
	
	for(int i=0;i<N-1;i++)
	{
		cin >> nombre;
		sum += nombre;
	}


	// Print output
	
	cout << (N*(N+1)>>1)-sum;

	return 0;
}

