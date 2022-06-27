// C++ program to demonstrate the
// cin object
#include <iostream>
using namespace std;
#define nl "\r\n"
int main()
{
    long long n, i, temp;
 
    cin >> n;
    for(i=1;i<n+1;i++)
    {
	temp = (i-1)*(i+4)*((i*i)-(3*i)+4)/2; // p.283 non attacking chess pieces Václav Kotěšovec
	cout << temp << nl;
    }
    
    return 0;
}
