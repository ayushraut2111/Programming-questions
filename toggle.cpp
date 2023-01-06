class Solution {
  public:
vector<vector<int>> roads;
vector<vector<int>> adj;
vector<int> dp;
   const int MOD = 1e9 + 7;
   void dfs(int u, int p) 
   {
    dp[u] = 1;
    for (int v : adj[u]) {
        if (v == p) continue;
        dfs(v, u);
        dp[u] = (1ll * dp[u] * (dp[v] + 1)) % MOD;
        }
    }

    
    int countGoodTrips(int n, int k, vector<vector<int> > roads) {
        roads.resize(n - 1);
    adj.resize(n);
    dp.resize(n);
    for (int i = 0; i < n - 1; i++) {
        cin >> roads[i][0] >> roads[i][1] >> roads[i][2];
        roads[i][0]--;
        roads[i][1]--;
        adj[roads[i][0]].push_back(roads[i][1]);
        adj[roads[i][1]].push_back(roads[i][0]);
    }
    dfs(0, -1);
    long long ans = 0;
    for (int i = 0; i < n - 1; i++) {
        if (roads[i][2] == 1) {
            ans = (ans + 1ll * dp[roads[i][0]] * dp[roads[i][1]]) % MOD;
        }
    }
    
    return ans;