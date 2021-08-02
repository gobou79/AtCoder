#include <bits/stdc++.h>
using namespace std;
using Graph = vector<vector<int> >;

vector<bool> seen;
void dfs(const Graph &G, int v) {
    seen[v] = true;

    for (auto next_v : G[v]){
        if (seen[next_v]) continue;
        dfs(G, next_v);
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    Graph G(N);
    for (int i = 0; i<M; i++) {
        int a, b;
        cin >> a >> b;
        G[a-1].push_back(b-1);
    }

    int ans = 0;

    for (int i = 0; i<N; i++) {
        seen.assign(N, false);
        dfs(G, i);
        ans += count(seen.begin(), seen.end(), true);
    }
    cout << ans << endl;
}