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
    unsigned long n;
  
    // Take input using cin
    cin >> n;
    unsigned long i=1, temp=0, j=5;
    while(i>=1)
    {
	i=n/j;
	temp+=i;
	j*=5;
    }
	
    cout << temp << nl;
    return 0;
}
