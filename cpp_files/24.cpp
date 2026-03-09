/*Create a class Employee with employee ID, name, and basic salary.
Write a function to calculate net salary after adding 20% HRA and 10% DA.*/
#include<iostream>
#include<string>
using namespace std;
class employee{
private:
	int ID;
	string name;
	float salary;
public:
employee(int i,string n,float s){
	ID=i;
	name=n;
	salary=s;
}	

float net_salary(){
	float HRA,DA,net_sal;
	cout<<"HRA is:"<<'\n';
	cin>>HRA;
	cout<<"DA is:"<<'\n';
	cin>>DA;
    net_sal=salary+(HRA*0.20)+(DA*0.10);
    
    return net_sal;
}

void display(){
	cout<<"name of employee:"<<name<<'\n';
	cout<<"ID of employee:"<<ID<<'\n';
	cout<<"salary of employee:"<<salary<<'\n';
	cout<<"net_salary of employee is:--"<<'\n'<<net_salary()<<'\n';
}
};

int main(){
    employee E1(101,"shyam",12000);
    E1.display();
	return 0;
}