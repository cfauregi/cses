// C++ program to demonstrate the
// cin object
#include <iostream>
using namespace std;
#define nl "\r\n"
int main()
{
    long long n, i;
 
    cin >> n;
    long long a[n], b[n];
    long long big, small;
    for (i=0; i<n; i++)
    {
	cin >> a[i] >> b[i];
	if (a[i]>b[i])
	{
		big=a[i];
		small=b[i];
	}
	else
	{
		big=b[i];
		small=a[i];
	}
	
	
	if( ((big + small)%3==0) && (big>0) && (small>0) && (small>=big/2) || ((big==0) && (small==0)) )
		cout << "YES" << nl;
	/*
		
	if ((((a[i]+b[i])%3==0)&&a[i]>0&&b[i]>0)  || ((a[i]==0) && (b[i]==0)))
		cout << "YES" << nl;
	*/
	else 
		cout << "NO" << nl;
    }
    
    return 0;
}
