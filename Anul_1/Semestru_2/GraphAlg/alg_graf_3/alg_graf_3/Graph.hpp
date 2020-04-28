//
//  Graph.h
//  alg_graf
//
//  Created by Georgescu Stefan on 14/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <map>
#include <vector>
#include "Edge.hpp"
#pragma once

using namespace std;

class Graph{
private:
    map<int,vector<Edge>> outbound_edges;
    
    void add_new_edge(int source, int destination, int cost);
    
    void initialise_vertices(int no_of_vertices);
    
    vector<vector<int>> initialise_matrix(vector<vector<int>>& matrix, int value, int size);
    
public:
    Graph();
    
    Graph(string file_name);
    
    int get_number_of_vertices();
    
    pair<vector<int>, int> get_shortest_path(int source, int destination);
    
};
