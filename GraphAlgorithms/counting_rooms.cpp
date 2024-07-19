#include <iostream>
#include <queue>
#include <vector>
#include <array>
using namespace std;

#define i2 pair<int, int>

void bfs(vector<string>& building, vector<vector<bool> > &visited, int i, int j) {
    int n=building.size();
    int m = building[0].size();

    queue<i2> Q;
    Q.push(i2(i, j));
    visited[i][j] = true;

    while (!Q.empty()) {
        i2 p = Q.front(); Q.pop();

        if (p.first>0 && building[p.first-1][p.second]=='.' && !visited[p.first-1][p.second]) {
            Q.push(i2(p.first-1, p.second));
            visited[p.first-1][p.second] = true;
        }

        if (p.second>0 && building[p.first][p.second-1]=='.' && !visited[p.first][p.second-1]) {
            Q.push(i2(p.first, p.second-1));
            visited[p.first][p.second-1] = true;
        }

        if (p.first<n-1 && building[p.first+1][p.second]=='.' && !visited[p.first+1][p.second]) {
            Q.push(i2(p.first+1, p.second));
            visited[p.first+1][p.second] = true;
        }

        if (p.second<m-1 && building[p.first][p.second+1]=='.' && !visited[p.first][p.second+1]) {
            Q.push(i2(p.first, p.second+1));
            visited[p.first][p.second+1] = true;
        }
    }
}

int main() {
    int n, m;
    cin>>n>>m;

    vector<string> building(n);
    vector<vector<bool> > visited(n, vector<bool>(m, false));
    for (int i=0; i<n; ++i) {
        cin >> building[i];
    }

    int rooms = 0;
    for (int i=0; i<n; ++i) {
        for (int j=0; j<m; ++j) {
            if (visited[i][j] || building[i][j] == '#') continue;

            rooms++;
            bfs(building, visited, i,j );
        }
    }

    cout << rooms << endl;

    return 0;
}