// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

// Driver Code
int main()
{
	long N =0, N_1=0;
	cin >> N;
	long list[N],i=0, modif =0;
	for(i =0 ; i<N;i++)
	{
		cin >> list[i];
		while (list[i]<N_1)
		{
			list[i]++;
			modif++;
			//cout << modif;
		}
		N_1=list[i];
	}

	cout << modif;
	return 0;
}

