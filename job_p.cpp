#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;


struct Job{
    char id;
    int dead;
    int profit;

    Job(int i , int d , int p){
        this->id = i;
        this->dead = d;
        this->profit = p;
    }
};

bool comparison(Job a, Job b){
    return (a.profit > b.profit);
}

void ScheduleJob(vector<Job> arr){
    
    int n = arr.size();
    sort(arr.begin(),arr.end(),comparison);

    vector<int> result(n);
    vector<bool> slot(n,false);

    for(int i = 0 ; i<n; i++){
        for(int j = min(n,arr[i].dead)-1; j>=0;j--){
            if(){
                
            }

        }
    }
}