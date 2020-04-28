//
//  Graph.hpp
//  alg_graf_4
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <map>
#include <vector>
#include "Vertex.hpp"
#include <stack>
#pragma once

using namespace std;

class Graph{
private:
    map<Vertex,vector<Vertex>> inbound_edges, outbound_edges;
    
    void add_new_vertex(Vertex new_vertex);
    
    void visit(Vertex vertex, vector<Vertex>& did_go, vector<Vertex>& did_go_temp, stack<Vertex>& sorted_vertices);
    
    int get_unvisited_vertex(vector<Vertex>& did_go, vector<Vertex>& my_vertices);
    
public:
    Graph(void);
    
    int get_in_degree(Vertex vertex);
    
    int get_out_degree(Vertex vertex);
    
    vector<Vertex> get_next_vertices(Vertex vertex);
    
    vector<Vertex> get_previous_vertices(Vertex vertex);
    
    stack<Vertex> get_sorted_topologically();
    
    vector<Vertex> get_vertices();
    
    vector<Vertex> get_problem_solution();
};
