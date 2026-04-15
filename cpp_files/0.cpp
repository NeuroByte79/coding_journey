//Create a C++ program to manage a vehicle rental system using inheritance//
#include<iostream>
#include<string>
using namespace std;
class user_info{
public:
int id;
string name;
int age;
string address;

//USER DETAILS MODULE//

void input_info(){
cout<<"Enter name: ";
cin>>name;
cout<<"Enter age: ";
cin>>age;
cout<<"Enter ID: ";
cin>>id;
cout<<"Enter address: ";
cin>>address;
}

void display_info(){
int n;
cout<<"Name :"<<name;
cout<<"\nAge: "<<age;
cout<<"\nID: "<<id;
cout<<"\nAddress: "<<address;
}

//CHOICE MODULE//

int choice(){
int c;
cout<<"Enter 1 for 2 wheelers"<<endl;
cout<<"Enter 2 for Four wheelers"<<endl;
cout<<"Enter 3 for goods carrier"<<endl;
cout<<"Enter your choice";
cin>>c;
switch(c){
case 1:
cout<<"You have selected two wheeler."<<endl;
break;
case 2:
cout<<"You have selected four wheeler."<<endl;
break;
case 3:
cout<<"You have selected goods carrier."<<endl;
break;
default:
cout<<"Check your entry!"<<endl;
break;
    }
    return c;
  }
 };

//VEHICLE DESCRIPTION MODULE//

class vehicle{
public:
void two_wheeler(){
int p=0;
cout<<"Enter 1 for normal bike"<<endl;
cout<<"Enter 2 for long ride bike"<<endl;
cout<<"Enter 3 for super bike"<<endl;
cout<<"Enter your choice:";
cin>>p;
switch(p){
case 1:
cout<<"You have got hero splendor+\n";
break;
case 2:
cout<<"You have got himalyan\n";
break;
case 3:
cout<<"You have got Ninja H2R";
break;
 }
} 
void four_wheeler(){
int k;
cout<<"Enter 1 for sedan"<<endl;
cout<<"Enter 2 for coupe"<<endl;
cout<<"Enter 3 for suv"<<endl;
cout<<"Enter your choice: ";
cin>>k;
switch(k){
case 1:
cout<<"You have got pagani zonda\n";
break;
case 2:
cout<<"You have got TATA curvv\n";
break;
case 3:
cout<<"You have got scorpio s11";
break;
 }
} 
void goods_carrier(){
int g=0;
cout<<"Enter 1 for pickup truck"<<endl;
cout<<"Enter 2 for 12 wheeler"<<endl;
cout<<"Enter 3 for 16 wheeler"<<endl;
cout<<"Enter your choice: ";
cin>>g;
switch(g){
case 1:
cout<<"You have got Toyota hilux\n";
break;
case 2:
cout<<"You have got Ashok leyland hyva\n";
break;
case 3:
cout<<"You have got Tata signa";
break;
}
}
};

//RENTAL AGREEMENT MODULE//

class user_agreement{
public:
void instruction(){
cout<<"-----READ THE USER MANUAL CAREFULLY-----"<<'\n';
cout<<"Minimum days for aquiring any vehicle is: 7 days"<<'\n';
cout<<"Maximum days for keeping the vehicle is: 90 days"<<'\n';
cout<<"Half of total calculated payment must be paid during booking time and rest during vehicle submission"<<'\n';
cout<<"Late return of the vehicle will trigger police action right away"<<'\n';
cout<<"Required wrekage cost must be paid by user"<<'\n';
cout<<"No personal modification allowed"<<'\n';
cout<<"If caught!,using vehicle for malicious activity user will be banned forever"<<'\n';
cout<<"Check vehicle properly before taking it for your business"<<'\n';
cout<<"If any problem found while booking report it immediately for our convenience"<<'\n';
cout<<"follow traffic rules'ANY PENALTY IMPOSED WILL BE ADDED TO THE FINAL PAYMENT' "<<'\n';
cout<<"Terms and conditions applied to all type of vehicles!!!!"<<'\n';
 }
};

//BOOKING MODULE//

class booking:public vehicle{
public:

int total_cost;
int miscellaneous_charge;

void price(){
    int choice;
    int type; //1=two wheelers,2=four wheelers,3=goods carrier//
     
    cout<<"enter choice:"<<endl;
    cin>>choice;
    cout<<"enter type:"<<endl;
    cin>>type;
    if(type == 1){
    switch(choice){
     case 1:
     cout<<"(for hero splendor)-> 1200RS/month '+' additional charge if any wrekage found"<<endl;
     break;
     case 2:
     cout<<"(for RE himalayan)-> 1800RS/month '+' additional charge if any wrekage found"<<endl;
     break;
     case 3:
     cout<<"(for NINJA h2r)-> 2700RS/month '+' additional charge if any damage found"<<endl;
     break;
     default:
     cout<<"invalid entry"<<'\n';
     }
    }

    else if(type == 2){
    switch(choice){
     case 1:
     cout<<"(for pagani zonda)-> 31000RS/month '+' additional charge if any wrekage found"<<endl;
     break;
     case 2:
     cout<<"(for TATA curvv)-> 3800RS/month '+' additional charge if any wrekage found"<<endl;
     break;
     case 3:
     cout<<"(for scorpio s11)-> 2700RS/month '+' additional charge if any damage found"<<endl;
     break;
     default:
     cout<<"invalid entry"<<'\n';
     }
    }

    else if(type == 3){
    switch(choice){
     case 1:
     cout<<"(for Toyota Hilux)-> 8200RS/month '+' additional charge if any wrekage found"<<endl;
     break;
     case 2:
     cout<<"(for Ashok Leyland hyva)-> 4800RS/month '+' additional charge if any wrekage found"<<endl;
     break;
     case 3:
     cout<<"(for TATA Signa)-> 6700RS/month '+' additional charge if any damage found"<<endl;
     break;
     default:
     cout<<"invalid entry"<<'\n';
     }
    }   
  }
  void price_calculation(){
    string gaddi[]={"splendor","himalyan","ninja h2r","pagani zonda","tata curvv","scorpio s11","toyota hilux","hyva","signa"};
    int gppm[]={1200,1800,2700,31000,3800,2700,8200,4800,6700}; //gppm->gaddi price per month//
    int time,choice;
    cout<<"enter choice(0-8)"<<'\n';
    cin>>choice;
    cout<<"enter time for booking"<<'\n';
    cin>>time;
    cout<<"enter miscellaneous charge if any"<<'\n';
    cin>>miscellaneous_charge;
    cout<<"vehicle:"<<gaddi[choice]<<endl;
    int price = (gppm[choice]*time)+(miscellaneous_charge);
    int GST=(price*0.18);
    total_cost=price+GST;
    cout<<"total cost is: "<<total_cost<<'\n';
  }
};

//payment module//

class Payment:public booking{
    public:
    int first_installment,sec_installment;
    void adv_payment(){
         first_installment= total_cost*0.4;
         cout<<"first installment is: "<<first_installment<<endl;
    cout<<"get verification document of vehicle submission after 2nd installment"<<endl;
    }
//miscellaneous charge module//

     void final_payment(){
        int d;
        cout<<"enter value of d :(if no damage enter d==0):(else d==anything)"<<endl;
        cin>>d;
        cout<<"d:"<<d<<endl;
        if(d==0){
            cout<<"no damage found"<<endl;
            miscellaneous_charge=0;
            cout<<"miscellaneous charge is: "<<miscellaneous_charge<<endl;
        }
        else if(d!=0){
            cout<<"damaged return attempted "<<endl;
            miscellaneous_charge=500;
            cout<<"miscellaneous charge is: "<<miscellaneous_charge<<endl;;
        }
        sec_installment=(total_cost-first_installment)+miscellaneous_charge;
        cout<<"second installment is: "<<sec_installment<<endl;
    }
};
// main module//

int main(){
    user_info u1;
    vehicle v1;
    user_agreement ua;
    Payment p1;

    u1.input_info();
    u1.display_info();

    ua.instruction();

    int cat = u1.choice();

    switch(cat){
        case 1: v1.two_wheeler();   break;
        case 2: v1.four_wheeler();  break;
        case 3: v1.goods_carrier(); break;
        default: cout<<"Invalid category!"<<endl; return 0;
    }

    p1.price();
    p1.price_calculation();

    p1.adv_payment();

    p1.final_payment();

    cout<<"\n--- Thank you for using our rental service! ---"<<endl;

    return 0;
}