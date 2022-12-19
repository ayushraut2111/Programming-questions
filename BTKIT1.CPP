#include<bits/stdc++.h>
#define ll long long
using namespace std;

int main() {
    ll n;
    cin>>n;
    vector<ll> vec(n), arr;
    arr.reserve(n);
    for (ll i = 0; i < n; i++) {
        cin>>vec[i];
        vec[i] -= i;
    }
    for (ll i = 0; i < n; i++) if (vec[i] > 0) {
        ll pos = upper_bound(arr.begin(), arr.end(), vec[i]) - arr.begin();
        if (pos == arr.size()) arr.push_back(vec[i]);
        else arr[pos] = vec[i];
    }
    cout<<n-arr.size()<<endl;
    return 0;
}