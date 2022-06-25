// C++ program to demonstrate the
// cin object
#include <iostream>
using namespace std;
#define bit 2
#define nl "\r\n"
unsigned long long puis(unsigned long long pow)
{	unsigned long long n=2;
	if (pow == 0)
		return 1;
	for(unsigned long i=1; i<pow;i++)
		n*=bit;
	return n;
}
void print_binary_char(unsigned short n, unsigned short N)
{	
	short i;
	unsigned short tab[16];
	for (i=15; i>-1;i--)
		tab[i]=(n>>(15-i))&0b0000000000000001;


	for(i=16-N;i<16;i++)
	{
	    if (tab[i] & 1)
		cout << ("1");
	    else
		cout << ("0");
	    //n=n>>1;
	}
	cout << nl;
}
// Driver Code
int main()
{
    long n, a;
  
    // Take input using cin
    cin >> n;
    a = puis(n);
    unsigned short N=0;
    cout << a << nl;
    //print_binary_char(N,n);
    for (long i=0; i<n;i++)
    {	
	//cout << i << nl;
	//cout << N << nl;
	N=N|1<<i;
	print_binary_char(N,n);
    }
    for (long i=0; i<n-1;i++)
    {	
	//cout << i << nl;
	//cout << N << nl;
	N=N&0b1111111111111110<<i;
	print_binary_char(N,n);
    }
    N=N&0b1111111111111110<<i;
    print_binary_char(N,n);
    return 0;
}
