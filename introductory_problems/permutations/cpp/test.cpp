// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

// Driver Code
int main()
{
	long N =0;
	cin >> N;
	if (N <4 && N!=1)
		cout << "NO SOLUTION";
	else
	{

		long i;
		for(i=0; i< N/2; i++)
			cout << 2+i*2 << " "; 			
		if (N%2!=0)
			N+=1;
		for(i=0; i <N/2; i++)
			cout << 1+i*2 << " ";
	}
	return 0;
}

