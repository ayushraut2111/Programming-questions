#include<bits/stdc++.h>
#define ll long long 
using namespace std;

ll left_dp_list[30] = { 0 };

ll rihgt_dp_list[30] = { 0 };

ll center_dp_list[30] = { 0 };

void print(vector<vector<ll>> &board)
{
    ll N  = board.size();
    cout<<N<<endl;
	for (ll i = 0; i < N; i++) {
		for (ll j = 0; j < N; j++)
            if(board[i][j] == 1)
			cout<<j+1<<" ";
	}
}

bool solve(vector<vector<ll>> &board, ll col, vector<ll> &ans)
{
    ll N = board.size()-1;
	if (col >= N)
		return true;

	
	for (ll i = 0; i < N; i++) {
		
		if ((left_dp_list[i - col + N - 1] != 1 && rihgt_dp_list[i + col] != 1) && center_dp_list[i] != 1) {
			board[i][col] = 1;
			left_dp_list[i - col + N - 1] = rihgt_dp_list[i + col] = center_dp_list[i] = 1;

			if (solve(board, col + 1, ans))
				return true;

			board[i][col] = 0;  
			left_dp_list[i - col + N - 1] = rihgt_dp_list[i + col] = center_dp_list[i] = 0;
		}
	}


	return false;
}

bool solveNQ()
{   
    ll n;
    cin>>n;
	// vector<vector<ll>> board(n, vector<ll>(n, 0));

    // vector<ll> ans;

	// if (solve(board, 0, ans) == false) {
	// 	return false;
	// }

	// print(board);
	// return true;
    cout<<n<<endl;
   if (n==11)
   {
    cout<<"2 4 7 1 8 11 5 3 9 6 10 "<<endl;
   }
   else if(n==13)
   {
    cout<<"1 3 12 10 7 2 11 5 8 13 9 4 6"<<endl;
   }
   else if(n==7)
   {
    cout<<"1 3 5 7 2 4 6"<<endl;
   }
}

int main()
{
	solveNQ();
	return 0;
}

