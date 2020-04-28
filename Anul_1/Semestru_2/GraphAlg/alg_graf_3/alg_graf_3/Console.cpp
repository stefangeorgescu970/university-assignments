//
//  Console.cpp
//  alg_graf_2
//
//  Created by Georgescu Stefan on 21/04/2017.
//  Copyright © 2017 Georgescu Stefan. All rights reserved.
//

#include "Console.hpp"
#include <iostream>

Console::Console(Graph my_graph){
    this->my_graph = my_graph;
}

void Console::print_menu(){
    cout<<"1. Get shortest path between two vertices.\n";
    cout<<"2. Exit.\n\n";
}

void Console::run(){
    while (true) {
        this->print_menu();
        cout<<"Enter your option: ";
        int option;
        cin>>option;
        if(cin.fail()){
            cin.clear();
            cin.ignore();
        } else {
            if (option == 1) {
                int source, destination;
                cout<<"Input source: ";
                cin>>source;
                if(cin.fail()){
                    cout<<"No integer provided. Program terminating.\n\n";
                    cin.clear();
                    cin.ignore();
                } else {
                    cout<<"Input destination: ";
                    cin>>destination;
                    if(cin.fail()){
                        cout<<"No integer provided. Program terminating.\n\n";
                        cin.clear();
                        cin.ignore();
                    } else {
                        pair<vector<int>,int> path = this->my_graph.get_shortest_path(source, destination);
                        if (path.first.size() == 0){
                            cout<<"There is no path between the 2 vertices.\n\n";
                        } else {
                        cout<<"The path is: ";
                        for(int& vertex:path.first)
                            cout<<vertex<<" ";
                            cout<<"\nThe cost of this path is: "<<path.second;
                        cout<<"\n\n";
                        }
                    }
                }
            } else if (option == 2) {
                cout<<"End of story.\n";
                break;
            } else {
                cout<<"Option not available.\n\n";
            }
        }
    }
}
