#include<iostream>
#include<string>
using namespace std;
class student{
	private:
	int roll_no ;
	char student_name[15];÷
	float marks[5];
	float total;
	float gtotal[5];
public:
	void total_marks();
	void gt();
	void input_details(){
		int i;
		total=0;
		cout<<"enter roll no:"<<'\n';
		cin >> roll_no;
		cout<<"enter student name:"<<'\n';
		cin >> student_name;
		for (i=0;i<5;i++){
			cout<<"enter marks"<<'\n';
			cin>>marks[i];
		}
	}
void display_details(){
	int i;
	cout<<"student name :"<<'\n';
	cout<<"roll number :"<<'\n';
	for(i=0;i<5;i++)
	cout<<"marks :"<<marks[i]<<'\n';

	cout<<"total marks:"<<total<<'\n';

}		
};
void student::total_marks(){
	int i,j;
	for(i=0;i<5;i++)
	{
		total=0;
 for(j=0;j<5;j++)
 total= total+marks[j];
gtotal[i]=total;
}
 //cout<<"total marks :"<<'\n';

}
void student::gt()
{
	int i;
	for(i=0;i<5;i++)
	cout<<gtotal[i];
}
int main(){
	int i;
	student S[5];
	for(i=0;i<5;i++)
	{
   S[i].input_details();
	S[i].total_marks();
	S[i].gt();
	S[i].display_details();
	}
	
	
	
	

	return 0;
}
