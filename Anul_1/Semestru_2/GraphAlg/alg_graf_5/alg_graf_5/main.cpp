#include "Graph.hpp"
#include <iostream>

using namespace std;

int main(){
    Graph my_graph;
    vector<int> my_cycle = my_graph.get_hamiltonian_cycle();
    if (my_cycle.size() == 0) {
        cout<<"The graph has no hamiltonian cycles.\n\n";
    } else {
        cout<<"One hamiltonian cycle of the graph is: ";
        for(int vertex : my_cycle)
            cout<<vertex<<", ";
        cout<<my_cycle[0]<<".\n\n";
    }
    return 0;
}
