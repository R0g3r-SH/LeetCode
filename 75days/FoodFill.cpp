#include <iostream>
#include <bits/stdc++.h>]
using namespace std;

// void BFS(vector<vector<int>> &image, vector<vector<int>> visisted, int sr, int sc, int color)
// {
// }


struct Point
{
    int x;
    int y;
};

void printMatrix(vector<vector<int>> image)
{

    for (int i = 0; i < image.size(); i++)
    {
        for (int j = 0; j < image[0].size(); j++)
        {
            cout << image[i][j] << " ";
        }
         cout <<"\n";
    }
}

void printMatrix2(vector<vector<bool>> image)
{

    for (int i = 0; i < image.size(); i++)
    {
        for (int j = 0; j < image[0].size(); j++)
        {
            cout << image[i][j] << " ";
        }
         cout <<"\n";
    }
}


bool isvisisted(vector<vector<int>> &image,vector<vector<bool>> &visited, int sr, int sc, int color ,int target, Point curp) {

//edeges of the matrix
//is the same vaule 
//is on visited

    int currx= curp.x;
    int curry = curp.y;

    if (currx >= image.size() || curry >= image[0].size() || visited[currx][curry] || image[currx][curry] == color || image[currx][curry]!= target){
        return true;
    }

    return false;
}



void BFS (vector<vector<int>> &image,vector<vector<bool>> &visited, int sr, int sc, int color){
    
    int target = image[sr][sc];

    int movx[4] = {1,-1,0,0};
    int movy[4] = {0,0,1,-1};
    
    deque<Point> nextp;

    Point curp{sr,sc};

    nextp.push_back(curp);

    while (!nextp.empty())
    {
        curp = nextp.back();
        nextp.pop_back();

        int currx= curp.x;
        int curry = curp.y;

        if (isvisisted(image,visited,sr,sc,color,target,curp)){
            continue;
        }

        visited[currx][curry] = true;
        if (image[currx][curry] == target){
            image[currx][curry] = color;
        }
        //create pore points
        for (int i =0; i<4; i++){
            Point newpoint{currx+movx[i],curry+movy[i]};
            nextp.push_back(newpoint);
        }

    }
    



}

vector<vector<int>> floodFill(vector<vector<int>> &image, int sr, int sc, int color)
{
    vector<vector<bool>> visited;
    for (int i = 0; i < image.size(); i++)
    {
        vector<bool> temp;
        for (int j = 0; j < image[0].size(); j++)
        {
            temp.push_back(false);
        }
        visited.push_back(temp);
    }
    BFS (image,visited,sr,sc,color);

    return image;
}



int main()
{
    vector<vector<int>> image ={{0,0,0},{0,0,0}};
    int sr =1, sc = 0, color=2;

    floodFill(image, sr, sc, color);
    printMatrix(image);

    return 0;
}
