/*program 103 extended to find the details 
  of that student with maximum total*/
#include<iostream>
#include<string>
using namespace std;
class student {
private:    
    string name;
    int roll_no;
    int marks[5];
    float total=0;
public:
    void input_details(){
     cout<<"enter name:"<<'\n';
     cin>>name;
     cout<<"enter roll no:"<<'\n';
     cin>>roll_no;
    for(int i=0;i<5;i++){
        cout<<"enter marks[i]"<<'\n';
        cin>>marks[i];
    }   
    }

    float calculate_total(){
        total=0;
for(int i=0;i<5;i++){
        total= total +marks[i];
    }
    return total;
}

    void display(){
    cout<<name<<'\n';
    cout<<roll_no<<'\n';
    cout<<"marks:"<<'\n';
    for(int i=0;i<5;i++){
        cout<<marks[i]<<'\n';
    }
    cout<<"total marks:"<<total<<endl;
    }
};

void grand_total(student S[],int n,float totals[]){   //fxn to store total of each student
    for (int i=0;i<n;i++) 
    totals[i]=S[i].calculate_total();
}

int main (){
    int i;
    float totals[3];
student S[3];
for(int i=0;i<3;i++){
S[i].input_details();
S[i].calculate_total();
S[i].display();
}
grand_total(S,3,totals);
cout<<"individual totals:"<<'\n';
for(i=0;i<3;i++)
cout<<totals[i]<<'\n';    
grand_total(S,3,totals);
int maxindex=0;
for(i=0;i<3;i++){
if(totals[i]>totals[maxindex]){
    maxindex=i;
}
}
cout<<"maxm marks :"<<totals[maxindex]<<endl;
S[maxindex].display();
return 0;
}