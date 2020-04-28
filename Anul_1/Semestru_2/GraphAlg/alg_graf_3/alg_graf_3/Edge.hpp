//
//  Edge.hpp
//  alg_graf_3
//
//  Created by Georgescu Stefan on 25/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once

class Edge{
private:
    int source, destination, cost;
public:
    Edge(int source, int destination, int cost);
    int get_source();
    int get_destination();
    int get_cost();
};
