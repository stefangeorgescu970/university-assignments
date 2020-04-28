//
//  Graph.hpp
//  alg_graf_5
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#define no_of_vertices 100
#include <vector>

class Graph{
private:
    bool adjacent[no_of_vertices][no_of_vertices];
    int number_of_vertices;
    
    bool ham_cycle_util(std::vector<int>& path, int position);
    
    bool is_safe(int vertex, std::vector<int>& path, int position);
    
public:
    Graph();
    
    std::vector<int> get_hamiltonian_cycle();
    
    
};

