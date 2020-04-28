//
//  Console.hpp
//  alg_graf_2
//
//  Created by Georgescu Stefan on 21/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#pragma once
#include "Graph.hpp"

class Console {
private:
    Graph my_graph;
    void print_menu();
    
public:
    Console(Graph my_graph);
    
    void run();
};
