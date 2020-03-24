#include <iostream>
#include <string>
#include <list>
#include <tuple>
#include <vector>

using namespace std;


vector<tuple<string,string>> subcriber_list ;            //global variable
vector<tuple<string,string>> publisher_list;            //global variable

class master{
    public:
        string topic , info;
    master(string topic,string info){
        
        for(int i=0;i<subcriber_list.size();i++){       //checking which subscriber subcribed to this topic
            if(topic == get<0>(subcriber_list[i])){
                cout<<topic+" | subscribed info:"+info<<endl;
            }
        }
        
    }
};

class subscriber{
    
    public:
        string topic,name;
        void print_info(string topic,string info){
            cout<<topic+"   "+info<<endl;
        }
        
        subscriber(string topic,string name){                   //give the name of the object as input
            subcriber_list.push_back(make_tuple(topic,name));

        }
};

class publisher{
    
    public:
    string topic,name;
        void publish(string topic,string info){
            cout<<"publish:"+info<<endl;
            master ob(topic,info);     }             //running master whenever a string is published
        
        publisher(string topic,string name){                        //give name of object as input 
            
            publisher_list.push_back(make_tuple(topic,name));      //appending topic and name of publisher to publisher_list
        }
};

int main()
{
    publisher pub("corana","pub");
    subscriber sub ("corona","sub");
    pub.publish("corona","positive");
    
    

    return 0;
}