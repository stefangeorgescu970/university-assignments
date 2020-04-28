//
//  Graph.c
//  alg_graf
//
//  Created by Georgescu Stefan on 14/03/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Graph.hpp"
#include "Edge.hpp"
#include <fstream>
#include <iostream>


void Graph::add_new_edge(int source, int destination, int cost){
    Edge new_edge = Edge(source, destination, cost);
    this->outbound_edges[source].push_back(new_edge);
}

void Graph::initialise_vertices(int no_of_vertices){
    vector<Edge> empty_list;
    for(int index = 0; index < no_of_vertices; index++){
        this->outbound_edges.insert(pair<int, vector<Edge>>(index, empty_list));
    }
}
Graph::Graph(){
    
}

Graph::Graph(string file_name){
    ifstream fin (file_name);
    int no_of_vertices = 0, no_of_edges = 0;
    fin>>no_of_vertices>>no_of_edges;
    initialise_vertices(no_of_vertices);
    int source = 0, destination = 0, cost = 0;
    for(int index = 1; index <= no_of_edges; index++){
        fin>>source>>destination>>cost;
        add_new_edge(source, destination, cost);
    }
}

int Graph::get_number_of_vertices(){
    return (int)this->outbound_edges.size();
}

vector<vector<int>> Graph::initialise_matrix(vector<vector<int>>& matrix, int value, int size){
    for(int index = 0; index < size; index ++){
        vector<int> empty_vector;
        matrix.push_back(empty_vector);
        for(int index2 = 0; index2 < size; index2++)
            matrix[index].push_back(value);
    }
    return matrix;
}

pair<vector<int>, int> Graph::get_shortest_path(int source, int destination){
    vector<vector<int>> distance, next_vertex;
    int no_of_vertices = this->get_number_of_vertices();
    this->initialise_matrix(distance, INT_MAX/2, no_of_vertices);
    this->initialise_matrix(next_vertex, -1, no_of_vertices);
    for(auto& element : this->outbound_edges){
        for(Edge& edge : element.second){
            distance[edge.get_source()][edge.get_destination()] = edge.get_cost();
            next_vertex[edge.get_source()][edge.get_destination()] = edge.get_destination();
        }
    }
    for (int i=0; i<no_of_vertices; i++) {
        for (int j=0; j<no_of_vertices; j++) {
            cout<<distance[i][j]<<"         ";
        }
        cout<<endl;
    }
    cout<<endl;
    for(int interm_node = 0; interm_node < no_of_vertices; interm_node++){
        cout<<"After node "<<interm_node<<endl;
        for(int source_node = 0; source_node < no_of_vertices; source_node++)
            for(int dest_node = 0; dest_node < no_of_vertices; dest_node++){
                if(distance[source_node][dest_node] > distance[source_node][interm_node] + distance[interm_node][dest_node]){
                    distance[source_node][dest_node] = distance[source_node][interm_node] + distance[interm_node][dest_node];
                    next_vertex[source_node][dest_node] = next_vertex[source_node][interm_node];
                }
            }
        for (int i=0; i<no_of_vertices; i++) {
            for (int j=0; j<no_of_vertices; j++) {
                cout<<distance[i][j]<<"        ";
            }
            cout<<endl;
        }
    }
    vector<int> path;
    int cost = distance[source][destination];
    if (next_vertex[source][destination] == -1)
        return pair<vector<int>, int> (path, cost);
    path.push_back(source);
    while(source != destination){
        source = next_vertex[source][destination];
        path.push_back(source);
    }
    return pair<vector<int>, int> (path, cost);
}











