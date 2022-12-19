#include <bits/stdc++.h>
using namespace std;

#define rep(i,n) for(int i=0;i<n;i++)
#define ll long long int
#define f first
#define s second
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define f first
#define s second
#define pb push_back
#define mod 1000000007
#define mp make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)

int N;
int A[1000011];
int L[1000011];
int R[1000011];
vector<int>g[1000011];
ll bt[1000011];
int maxn;
void btkit(int ind, int val) {
    while(ind <= maxn) {
        bt[ind] += val;
        ind += (ind & -ind);
    }
}
ll query(int ind) {
    ll ans = 0;
    while(ind > 0) {
        ans += bt[ind];
        ind -= (ind & -ind);
    }
    return ans;
}
vector<int>V;
int finding(int x) {
    if(V.back() <= x) return V.size();
    return upper_bound(V.begin(), V.end(), x) - V.begin();
}
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    set<int>S;
    unordered_map<int, int>M;

    for(int i = 1; i <= N; i++) {
        cin >> A[i];
        assert(A[i] >= 1 and A[i] <= 1000000000);
        S.insert(A[i]);
    }
    vector<pi>upd;
    for(int i = 1; i <= N; i++) {
        while(upd.size() > 0 and upd.back().f < A[i]) upd.pop_back();
        if(upd.size() == 0) L[i] = 1;
        else {
            L[i] = upd.back().s + 1;
        }
        upd.pb(mp(A[i], i));
    }
    upd.clear();
    for(int i = N; i >= 1; i--) {
        while(upd.size() > 0 and upd.back().f <= A[i]) upd.pop_back();
        if(upd.size() == 0) R[i] = N;
        else {
            R[i] = upd.back().s - 1;
        }
        upd.pb(mp(A[i], i));
    }

    for(int i = 1; i <= N; i++) {
        if(i - L[i] <= R[i] - i) {
            for(int j = L[i]; j < i; j++) {
                g[i - 1].pb(-A[i] / A[j]);
                g[R[i]].pb(A[i] / A[j]);
                
            }

            g[i].pb(-1);
            g[R[i]].pb(1);
        } else {

            for(int j = i + 1; j <= R[i]; j++) {
                g[L[i] - 1].pb(-A[i] / A[j]);
                g[i].pb(A[i] / A[j]);
                //S.insert(A[i]/A[j]);
            }

            g[L[i] - 1].pb(-1);
            g[i - 1].pb(1);
        }
    }
    maxn = S.size() + 2;
    int cnt = 1;
    for(set<int>::iterator it = S.begin(); it != S.end(); it++) {
        M[*it] = cnt++;
    }
    ll ans = 0;
    int r;
    V = vector<int>(S.begin(), S.end());
    for(int i = 1; i <= N; i++) {
        btkit(M[A[i]], 1);
        for(int j = 0; j < g[i].size(); j++) {
            r = finding(abs(g[i][j]));
            if(g[i][j] < 0) {
                ans -= query(r);
            } else {
                ans += query(r);
            }
        }
    }
    cout << ans;
}