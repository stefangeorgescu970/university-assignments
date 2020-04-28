//
//  main.cpp
//  ppd_prep
//
//  Created by Stefan Georgescu on 22/01/2019.
//

#include <string>
#include <iostream>
#include <thread>
#include <vector>
#include <future>
#include <mutex>
#include <atomic>

std::vector<int> f;
std::vector<int> cp = f; //deep copy. All Foo copied

std::vector<int*> f_pointers;
std::vector<int*> cp_pointers = f_pointers; //deep copy (of pointers), or shallow copy (of objects).
//All pointers to Foo are copied, but not Foo themselves

using namespace std;

mutex my_mutex;
int some_shared_var=0;
atomic<int> atomic_shared_var(0);


void atomicAdd(int a) {
    atomic_shared_var += a;
}

void func(int a) {
    { //Critical section
            //cum folosim mutex
        
        std::unique_lock<std::mutex> lock(my_mutex);
        some_shared_var += a;
    } //End of critical section
}

void task1(string msg)
{
    cout << "task1 says: " << msg << "\n";
}

int task2(int a, int b) {
    return a+b;
}

//cum definim o matrice
int mat[30][30];

void backtrack(int n,int step, vector<int> currentSol) {
    if(step == n) {
        unique_lock<mutex> lock(my_mutex);
        for(int i : currentSol) {
            cout<<i<<" ";
        }
        cout<<"\n";
    } else {
        vector<int> sol1 = currentSol;
        vector<int> sol2 = currentSol;
        sol1.push_back(0);
        sol2.push_back(1);
        thread t1 = thread([n, step, sol1]{backtrack(n, step+1, sol1);});
        thread t2 = thread([n, step, sol2]{backtrack(n, step+1, sol2);});
        t1.join();
        t2.join();
    }
}

int main()
{
    vector<thread> threads;

    for(int i = 0; i < 10; i ++) {

        // cum pornim threaduri
        threads.push_back(
            thread( [i] {
                task1("hello from " + to_string(i));
            })
        );
    }

    for(int i = 0; i< threads.size(); i ++) {
        threads[i].join();
    }

    vector<future<int>> futures;

    for(int i = 0; i < 10; i++) {
        // cum pornim o functie async care returneaza future<tipul_de_return_al_metodei_apelate>
        futures.push_back(async(launch::async, task2, i, 0));
    }
    
    future<int> oneFuture = async(launch::async, task2, 1, 0);

    int result = 0;

    for(int i = 0; i < futures.size(); i++) {
        result += futures[i].get();
    }

    cout<<"\n"<<result<<"\n";


    //test despre cum folosim mutex, go to func
    vector<thread> otherThreads;

    for(int i = 0; i < 10; i++) {
        otherThreads.push_back(thread([i]{func(i);}));
    }

    for(int i = 0; i< otherThreads.size(); i ++) {
        otherThreads[i].join();
    }

    cout<<"\n"<<some_shared_var<<"\n";


    //incrementing with atomic integer
    vector<thread> someOtherThreads;

    for(int i = 0; i < 100; i++) {
        someOtherThreads.push_back(thread([i]{atomicAdd(i);}));
    }

    for(int i = 0; i< someOtherThreads.size(); i ++) {
        someOtherThreads[i].join();
    }

    cout<<"\n"<<atomic_shared_var<<"\n";
    
    vector<int> sol;
    
    backtrack(12, 0, sol);
}
