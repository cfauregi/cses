// C++ program to demonstrate the
// cin object
#include <iostream>
using namespace std;
#define nl "\r\n"
// Driver Code
unsigned long long facto (short n)
{	
	unsigned long long temp =1;
	for(short i =1; i<n+1;i++)
		temp*=i;
	return temp;
}

int main()
{
    unsigned long long n;
  
    // Take input using cin
    cin >> n;
    unsigned long long i, tampon2=1, N=0;
    for (i=1; i<n+1; i++)
    {
	tampon2*=i;
	if (tampon2%10==0)
	{
		tampon2=tampon2/10;
		N++;
	}
    }
    cout << tampon2 << nl;
    i = (long long) 1000000000000000000;
    n=0;
/*
    while(i != 1)
    {
	    if ((tampon2%i)==0)
	    {
		tampon2= tampon2/i;
		n+=1;
	    }
	    else
		i=i/10;    
    }*/
    cout << N << nl;
    //cout << n << nl;
    return 0;
}
