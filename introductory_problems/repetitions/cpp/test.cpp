// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

// Driver Code
int main()
{
	string S;
	char A='A', C='C', G='G', T='T', now;
	char Temoin;
	int i, count=0, max=-1;
	cin >> S;
	for(i =0 ; i<S.length();i++)
	{	now = S[i];
		if (now == Temoin)
		{
			count ++;
		}		
		else 
		{	
	        	if (now == A) 
			{
				Temoin= A;
				count =1;
			}
	        	if (now == C)
 			{
				Temoin = C;
				count = 1;
			}
	        	if (now == G) 
			{
				Temoin = G;
				count =1;
			}
	        	if (now == T) 
			{
				Temoin = T;
				count= 1;
			}
		}		
		if( max < count) 
			max = count;
		
	}	
	cout << max;
	return 0;
}

