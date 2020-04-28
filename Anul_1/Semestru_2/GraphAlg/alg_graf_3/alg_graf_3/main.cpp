//
//  main.cpp
//  alg_graf_2
//
//  Created by Georgescu Stefan on 21/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include <iostream>
using namespace std;
#include "Graph.hpp"
#include "Console.hpp"


int main() {
    Graph my_graph{"graph.txt"};
    Console my_console{my_graph};
    my_console.run();
    return 0;
}
