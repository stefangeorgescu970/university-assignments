//
//  Vertex.hpp
//  alg_graf_4
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include <string>
#include <vector>

class Vertex {
private:
    int earliest_start_time;
    int latest_start_time;
    int earliest_end_time;
    int latest_end_time;
    int execution_time;
    std::string activity;
    std::vector<std::string> prerequesities;
    
public:
    Vertex(std::string activity, int execution_time, std::vector<std::string> prerequesities);
    
    int get_earliest_start_time();
    void set_earliest_start_time(int new_earliest_start_time);
    
    int get_latest_start_time();
    void set_latest_start_time(int new_latest_start_time);
    
    int get_earliest_end_time();
    void set_earliest_end_time(int new_earliest_end_time);
    
    int get_latest_end_time();
    void set_latest_end_time(int new_latest_end_time);
    
    int get_execution_time();
    
    std::string get_activity();
    
    std::vector<std::string> get_prerequesities();
    
    bool operator< (const Vertex& rhs) const;
    
    bool operator== (const Vertex& rhs);
};
