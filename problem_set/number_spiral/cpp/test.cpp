// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

long long int_sum_to_n(long long n)
{
	return n*(n+1)/2;
}

// Driver Code
int main()
{
	long long N = 0;
	long long res = 0;
	long long ligne, colonne =0;
	cin >> N;
	long long in1[N], in2[N];
	for (long i=0; i<N; i++)
		cin >> in1[i] >> in2[i];
	 
	    for (long i=0; i<N; i++)
	    {
		ligne = in1[i];
		colonne = in2[i];
	     
		if (ligne >= colonne)
		{
		    if (ligne&1==1)
		    {   
		        res = (ligne-1)*(ligne-1)+colonne;
	 
		    }
		    else
		    {
		        res = ligne*ligne-colonne +1;
		    }
		}
		else 
		{
		    if (colonne &1 ==1)
		    {
		        res = colonne*colonne-ligne+1;
		    }
		    else 
		    {
		        res = (colonne -1)*(colonne -1) + ligne ;
		    }
		}
		
		cout << res << "\n";
	    }
	return 0;
}
