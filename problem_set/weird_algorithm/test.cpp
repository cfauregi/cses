// C++ program to demonstrate the
// cin object
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
  
// Driver Code
int main()
{
	int64_t n;
    cin >> n;
    cout << n;
	while(n>1)
	{	
		if (n & 0b1)
			n=n*3+1;
		else 
			n=n/2;
		cout << " " << n;
	}
}
