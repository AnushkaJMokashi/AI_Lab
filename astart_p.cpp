#include <iostream>
#include <vector>
#include <queue>
#include <limits>
#include <cmath>
#include <functional> // Include for 'function'
using namespace std;


struct Node{
    int index;  //IIndex of the node
    int g_cost; //Cost from start node to this node
    int h_cost; //Heuristics cost 
    int f_cost;

    Node(int i,int g,int h){
        this->index = i;
        this->g_cost =g;
        this->h_cost = h;
        this->f_cost = g+h;
    }
};

int AStar(vector<vector<pair<int,int>>>& graph, vector<int>&heuristic, int start,int goal){
    int n = graph.size();

    priority_queue<Node,vector<Node>,function<bool(const Node&,const Node&)>> q(
        [](const Node& a, const Node& b){
            return a.f_cost >b.f_cost;
        }

    );

    vector<int> vis(n,0);  //int - 0

    q.push(Node(start,0,heuristic[start]));

    while(!q.empty()){
        Node current = q.top();
        q.pop();

        if(current.index == goal){
            return current.g_cost;
        }

        vis[current.index] = 1;
        
        
        for(const auto& neighbor : graph[current.index]){
            int neighborIndex = neighbor.first;
            int neighborWeight = neighbor.second;
            
            if(!vis[neighborIndex]){
                int g_cost = current.g_cost + neighborWeight;
                int h_cost = heuristic[neighborIndex];
                int f_cost = g_cost + h_cost;

                q.push(Node(neighborIndex,g_cost,h_cost));
            }
        }
    }

    return -1;

}

int main(){
    int n;
    cout << "Enter the number of nodes: ";
    cin>>n;

    vector<vector<pair<int,int>>> graph(n);
    cout << "Enter adjacency list (node index, edge weight, space-separated)" <<endl;

    for(int i = 0; i<n; ++i){
        cout<<"Enter no. neighbors of node "<<i<<":";
        int numNeighbors;
        cin>>numNeighbors;

        for(int j = 0; j<numNeighbors; ++j){
            cout<<"Enter neighbors of node "<<i<<":";
            int neighbor, weight;
            cin>>neighbor >> weight;
            graph[i].push_back({neighbor,weight});
        }
    }

    vector<int> heuristic(n,0);

    cout<<"Enter the heuristic values for each node:"<<endl;
    for(int i = 0; i<n;++i){
        cin>> heuristic[i];
    }

    int start, goal;
    cout << "Enter the start node: ";
    cin >> start;
    cout << "Enter the goal node: ";
    cin >> goal;

    int shortestPathCost = AStar(graph, heuristic, start, goal);

    if (shortestPathCost == -1) {
        cout << "No path found from node " << start << " to node " << goal << endl;
    } else {
        cout << "Shortest path cost from node " << start << " to node " << goal << " is: " << shortestPathCost << endl;
    }
}

