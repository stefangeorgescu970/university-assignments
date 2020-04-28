//
//  main.cpp
//  alg_graf_4
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <iostream>
#include "Graph.hpp"


void solve_problem(Graph my_graph){
    try {
        vector<Vertex> solution = my_graph.get_problem_solution();
        for(Vertex vertex : solution){
                if(vertex.get_activity() != "dummy_begin" && vertex.get_activity() != "dummy_end"){
                cout<<"Activity name: "<<vertex.get_activity()<<"\n";
                if(vertex.get_earliest_start_time() == vertex.get_latest_start_time())
                    cout<<"This activity is a critical activity.\n";
                cout<<"Earliest start time: "<<vertex.get_earliest_start_time()<<"\n";
                cout<<"Latests start time: "<<vertex.get_latest_start_time()<<"\n\n";
            }
            cout<<"Total time: "<< (*(solution.end()-1)).get_latest_end_time();
        }
    } catch (exception& e) {
        cout<<"Graph is not a DAG, terminating.\n";
    }
}

int main() {
    Graph my_graph;
    solve_problem(my_graph);
    return 0;
}
