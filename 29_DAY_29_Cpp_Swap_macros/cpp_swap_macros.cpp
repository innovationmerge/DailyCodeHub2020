// "iNNovationMerge DailyCodeHub"

// C++ program to swap two numbers using macros

#include<iostream>

#define SWAP(a,b) {int temp; temp=a; a=b; b=temp;}
using namespace std;
int main()
{
    int x,y;
    cout<<"Enter two numbers:";   
    cin>>x>>y;                   // Enter numbers
    cout<<"x="<<x<<" y="<<y;
    SWAP(x,y);
    cout<<"\nx="<<x<<" y="<<y;
    return 0;
}

/* Output
Enter two numbers:5 2
x=5 y=2
x=2 y=5
*/
