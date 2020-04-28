//
//  Edge.cpp
//  alg_graf_3
//
//  Created by Georgescu Stefan on 25/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Edge.hpp"

Edge::Edge(int source, int destination, int cost){
    this->source = source;
    this->destination = destination;
    this->cost = cost;
}

int Edge::get_source(){
    return this->source;
}

int Edge::get_destination(){
    return this->destination;
}

int Edge::get_cost(){
    return this->cost;
}


