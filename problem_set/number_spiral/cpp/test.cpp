// C++ program to demonstrate the
// cin object
#include <iostream>
#include <list>
#include <string.h>
using namespace std;

// Driver Code
int main()
{
	long long N = 0;
	cin >> N;
	long long in1[N], in2[N];
	for (long i=0; i<N; i++)
		cin >> in1[i] >> in2[i];
	for (long i =0; i<N;i++)
	{	
		if (in1[i] == in2[i])
		{
			if (in1[i]==1)
				cout << 1;
			else
				cout << in1[i]*in1[i]-in1[i]-1;
		}
		else
		{
			if (in1[i]>in2[i])
			{
				//if (in2%2!=0)
					//in2 = in2*in2;
					//le top sera le carre de in2
				//if (in1%==0)
					//in1 = in1*in1;
					//la premier colone de cette ligne sera le carre de in1
				
				//le plus grand au carre -le plus petit -1
				cout << in1[i]*in1[i]-in2[i]+1<< "\n";
			}			
			else
			{
				//if (in2%2!=0)
					//in2 = in2*in2;
					//le top sera le carre de in2
				//if (in1%==0)
					//in1 = in1*in1;
					//la premier colone de cette ligne sera le carre de in1
				
				//le plus grand au carre -le plus petit -1
				cout << in2[i]*in2[i]-in1[i]+1 << "\n";
			}
		}
	}
	return 0;
}

