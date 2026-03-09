/*Create a class Interest that calculates simple interest
Take values using a member function.*/
#include<iostream>
using namespace std;
class interest{
private:
 float principle_amount;
 float rate_of_interest;
 float time;
public:

interest(){
	float p,r,t;
principle_amount =p;
rate_of_interest=r;
time = t;
}

void input(){
	cout<<"enter principle amount"<<'\n';
	cin>>principle_amount;
	cout<<"enter rate_of_interest:"<<'\n';
	cin>>rate_of_interest;
	cout<<"enter time"<<'\n';
	cin>>time;
}

float output(){
	input();
	float SI=(principle_amount*rate_of_interest*time)/100;
	cout<<"si is:"<<SI<<'\n';
	return SI;
}
};

int main(){
    interest m1;
    m1.output();
	return 0;
}