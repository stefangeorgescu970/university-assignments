//
//  Graph.cpp
//  alg_graf_4
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Graph.hpp"
#include <fstream>
using namespace std;



vector<Vertex> Graph::get_problem_solution(){
    stack<Vertex> sorted_topo = this->get_sorted_topologically();
    vector<Vertex> final_solution;
    Vertex vertex = sorted_topo.top();
    sorted_topo.pop();
    final_solution.push_back(vertex);
    vertex = sorted_topo.top();
    sorted_topo.pop();
    vertex.set_earliest_start_time(0);
    vertex.set_earliest_end_time(vertex.get_execution_time());
    final_solution.push_back(vertex);
    while (!sorted_topo.empty()) {
        vertex=sorted_topo.top();
        sorted_topo.pop();
        int max = 0;
        for(Vertex predec : this->inbound_edges[vertex]){
            auto predec_needed = find(final_solution.begin(), final_solution.end(), predec);
            if ((*predec_needed).get_earliest_end_time() > max)
                max = (*predec_needed).get_earliest_end_time();
        }
        vertex.set_earliest_start_time(max);
        vertex.set_earliest_end_time(max+vertex.get_execution_time());
        final_solution.push_back(vertex);
    }
    auto it = final_solution.end()-1;
    (*it).set_latest_end_time((*it).get_earliest_end_time());
    (*it).set_latest_start_time((*it).get_latest_end_time() - (*it).get_execution_time());
    it--;
    while (it >= final_solution.begin()) {
        int min = INT_MAX;
        for(Vertex succ : this->outbound_edges[(*it)]){
            auto succ_needed = find(final_solution.begin(), final_solution.end(), succ);
            if ((*succ_needed).get_latest_start_time() < min)
                min = (*succ_needed).get_latest_start_time();
        }
        (*it).set_latest_end_time(min);
        (*it).set_latest_start_time(min - (*it).get_execution_time());
        it--;
    }
    return final_solution;
}


void Graph::visit(Vertex vertex, vector<Vertex>& did_go, vector<Vertex>& did_go_temp, stack<Vertex>& sorted_vertices){
    if(find(did_go_temp.begin(), did_go_temp.end(), vertex) != did_go_temp.end())
        throw exception(); // add my exception
    if(find(did_go.begin(), did_go.end(), vertex) == did_go.end()){
        did_go_temp.push_back(vertex);
        for(Vertex next_vert : this->outbound_edges[vertex]){
            visit(next_vert, did_go, did_go_temp, sorted_vertices);
        }
        did_go.push_back(vertex);
        did_go_temp.erase(find(did_go_temp.begin(), did_go_temp.end(), vertex));
        sorted_vertices.push(vertex);
    }
    
}

stack<Vertex> Graph::get_sorted_topologically(){
    stack<Vertex> sorted_vertices;
    vector<Vertex> my_vertices = this->get_vertices();
    vector<Vertex> did_go;
    vector<Vertex> did_go_temp;
    while(did_go.size() != my_vertices.size())
        visit(my_vertices[get_unvisited_vertex(did_go, my_vertices)], did_go, did_go_temp, sorted_vertices);
    return sorted_vertices;
}

int Graph::get_unvisited_vertex(vector<Vertex>& did_go, vector<Vertex>& my_vertices){
    for(int index = 0; index < my_vertices.size(); index++)
        if(find(did_go.begin(), did_go.end(), my_vertices[index]) == did_go.end())
            return index;
    return -1;
}

vector<Vertex> Graph::get_vertices(){
    vector<Vertex> v;
    for(auto pair : this->outbound_edges)
        v.push_back(pair.first);
    return v;
}

Graph::Graph(void){
    ifstream fin ("graph.txt");
    int no_of_vertices = 0;
    fin>>no_of_vertices;
    string activity_name;
    for(int index = 1; index <= no_of_vertices; index++){
        vector<string> prerequesities;
        string current_prereq;
        int execution_time, prerequesities_number;
        
        fin>>activity_name;
        fin>>execution_time;
        fin>>prerequesities_number;
        for(int index2 = 1; index2 <= prerequesities_number; index2++){
            fin>>current_prereq;
            prerequesities.push_back(current_prereq);
        }
        
        Vertex new_vertex{activity_name, execution_time, prerequesities};
        vector<Vertex> empty_list;
        this->inbound_edges.insert(pair<Vertex, vector<Vertex>>(new_vertex, empty_list));
        this->outbound_edges.insert(pair<Vertex, vector<Vertex>>(new_vertex, empty_list));
    }
    
    vector<Vertex> my_vertices = this->get_vertices();
    
    for(Vertex vertex : my_vertices){
        for(string prereq : vertex.get_prerequesities()){
            for (Vertex find_vertex : my_vertices) {
                if(find_vertex.get_activity() == prereq){
                    this->outbound_edges[find_vertex].push_back(vertex);
                    this->inbound_edges[vertex].push_back(find_vertex);
                    break;
                }
            }
            
        }
    }
    vector<string> empty_string_vector;
    vector<Vertex> empty_list;
    Vertex dummy_begin{"dummy_begin", 0, empty_string_vector};
    Vertex dummy_end{"dummy_end", 0, empty_string_vector};
    this->inbound_edges.insert(pair<Vertex, vector<Vertex>>(dummy_end, empty_list));
    this->outbound_edges.insert(pair<Vertex, vector<Vertex>>(dummy_end, empty_list));
    this->inbound_edges.insert(pair<Vertex, vector<Vertex>>(dummy_begin, empty_list));
    this->outbound_edges.insert(pair<Vertex, vector<Vertex>>(dummy_begin, empty_list));
    
    for(Vertex vertex:my_vertices) {
        if(get_in_degree(vertex) == 0){
            this->outbound_edges[dummy_begin].push_back(vertex);
            this->inbound_edges[vertex].push_back(dummy_begin);
        }
        if(get_out_degree(vertex) == 0) {
            this->outbound_edges[vertex].push_back(dummy_end);
            this->inbound_edges[dummy_end].push_back(vertex);
        }
    }

}

int Graph::get_out_degree(Vertex vertex){
    map<Vertex,vector<Vertex>>::iterator vertex_location = this->outbound_edges.find(vertex);
    if(vertex_location != outbound_edges.end())
        return (int)outbound_edges[vertex].size();
    return -1;
}

int Graph::get_in_degree(Vertex vertex){
   map<Vertex,vector<Vertex>>::iterator vertex_location = this->inbound_edges.find(vertex);
    if(vertex_location != inbound_edges.end())
        return (int)inbound_edges[vertex].size();
    return -1;
}

vector<Vertex> Graph::get_next_vertices(Vertex vertex){
    vector<Vertex> empty_edge_list;
    map<Vertex,vector<Vertex>>::iterator vertex_location = this->outbound_edges.find(vertex);
    if(vertex_location != outbound_edges.end())
        return outbound_edges[vertex];
    return empty_edge_list;
}

vector<Vertex> Graph::get_previous_vertices(Vertex vertex){
    vector<Vertex> empty_edge_list;
    map<Vertex,vector<Vertex>>::iterator vertex_location = this->inbound_edges.find(vertex);
    if(vertex_location != outbound_edges.end())
        return outbound_edges[vertex];
    return empty_edge_list;
}
