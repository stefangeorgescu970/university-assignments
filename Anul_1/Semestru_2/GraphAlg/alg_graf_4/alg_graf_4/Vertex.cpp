//
//  Vertex.cpp
//  alg_graf_4
//
//  Created by Georgescu Stefan on 28/05/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Vertex.hpp"

using namespace std;

Vertex::Vertex(string activity, int execution_time, vector<string> prerequesities){
    this->activity = activity;
    this->execution_time = execution_time;
    this->prerequesities = prerequesities;
    this->earliest_end_time = 0;
    this->earliest_start_time = 0;
    this->latest_end_time = 0;
    this->latest_end_time = 0;
}

int Vertex::get_earliest_start_time(){
    return this->earliest_start_time;
}
void Vertex::set_earliest_start_time(int new_earliest_start_time){
    this->earliest_start_time = new_earliest_start_time;
}


int Vertex::get_latest_start_time(){
    return this->latest_start_time;
}
void Vertex::set_latest_start_time(int new_latest_start_time){
    this->latest_start_time = new_latest_start_time;
}


int Vertex::get_earliest_end_time(){
    return this->earliest_end_time;
}
void Vertex::set_earliest_end_time(int new_earliest_end_time){
    this->earliest_end_time = new_earliest_end_time;
}


int Vertex::get_latest_end_time(){
    return this->latest_end_time;
}
void Vertex::set_latest_end_time(int new_latest_end_time){
    this->latest_end_time = new_latest_end_time;
}

int Vertex::get_execution_time(){
    return this->execution_time;
}

string Vertex::get_activity(){
    return this->activity;
}

vector<string> Vertex::get_prerequesities(){
    return this->prerequesities;
}

bool Vertex::operator<(const Vertex &rhs) const {
    return this->activity < rhs.activity;
}

bool Vertex::operator== (const Vertex& rhs){
    return this->activity == rhs.activity;
}



