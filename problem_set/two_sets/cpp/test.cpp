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
	long long N = 0, temp=0;
	cin >> N;
	long long sum_pack1 = 0, sum_pack2=0;
	long long ind_pack1 = 0, ind_pack2=0;
	long long pack1[N/2] , pack2[N/2];
	long i=0;
	if (int_sum_to_n(N)%2==0)
	{
		cout << "YES\n";
			
		temp = N;
	    	for (i=0; i<N; i++)
	    	{ 
			if (sum_pack1<=sum_pack2)
			{
				sum_pack1+=temp;
				pack1[ind_pack1]=temp;
				ind_pack1++;
			}
			else
			{
				sum_pack2+=temp;
				pack2[ind_pack2]=temp;
				ind_pack2++;
			}
			temp--;
		}

		cout << ind_pack1 << "\n";
		for (i=0;i<ind_pack1;i++)
			cout << pack1[i] << " ";
		cout << "\r\n" << ind_pack2 << "\r\n";
		for (i=0;i<ind_pack2;i++)
			cout << pack2[i] << " ";
	}
	else
	{
		cout << "NO\n";
	}
	return 0;
}
