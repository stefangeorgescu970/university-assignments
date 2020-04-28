//
//  Graph.cpp
//  alg_graf_5
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Graph.hpp"
#include <fstream>
using namespace std;

Graph::Graph(){
    for (int index1 = 0; index1 < no_of_vertices; index1++) {
        for (int index2 = 0; index2 < no_of_vertices; index2++) {
            adjacent[index1][index2] = false;
        }
    }
    ifstream fin ("graph.txt");
    fin>>this->number_of_vertices;
    int number_of_edges;
    fin>>number_of_edges;
    int vertex1, vertex2;
    for(int index = 1; index <= number_of_edges; index++){
        fin>>vertex1>>vertex2;
        this->adjacent[vertex1][vertex2] = this->adjacent[vertex2][vertex1] = true;
    }
}

vector<int> Graph::get_hamiltonian_cycle(){
    vector<int> my_cycle, empty_list;
    my_cycle.push_back(0);
    for (int index = 0; index < this->number_of_vertices-1; index++) {
        my_cycle.push_back(-1);
    }
    if ( !ham_cycle_util(my_cycle, 1))
        return empty_list;
    return my_cycle;
}

bool Graph::is_safe(int vertex, vector<int>&path, int position){
    if ( !adjacent[path[position-1]][vertex] )
        return false;
    
    if (find(path.begin(), path.end(), vertex) != path.end())
        return false;
    
    return true;
}

bool Graph::ham_cycle_util(vector<int>& path, int position){
    if (position == this->number_of_vertices) {
        if(adjacent[path[position-1]][path[0]])
            return true;
        return false;
    }
    
    for (int vertex = 1; vertex < this->number_of_vertices; vertex++) {
        if (is_safe(vertex, path, position)){
            path[position] = vertex;
            if( ham_cycle_util(path, position+1) )
                return true;
            
            path[position] = -1;
        }
    }
    return false;
}
