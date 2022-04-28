// problem link

#include <chrono>
// #include <bits/stdc++.h>
#include <iostream>
#include <vector>

#define pd push_back
#define mp make_pair
#define F first
#define S second

#define ONLINE_JUDGE

using namespace std;
using namespace std::chrono;

typedef long long int ll;
typedef vector<vector<int> > matrix;

int activate(int val, int b)
{
    int threshold = 1;
    return val + b >= threshold ? 1 : -1;
}

bool compare(matrix wOld, matrix wNew, int bOld, int bNew)
{
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
            if (wOld[i][j] != wNew[i][j])
                return false;
    }

    if (bOld != bNew)
        return false;

    return true;
}

void solve()
{
    // CREATE MATRICES
    matrix A(3, vector<int>(3, 0)), B(3, vector<int>(3, 0));

    cout << "Input A: \n";
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> A[i][j];
        }
    }
    cout << "\nInput B: \n";
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            cin >> B[i][j];
        }
    }

    int ya = 1, yb = -1;
    cout << "\nWe are considering TargetA as 1 and TargetB as -1\n";

    // initial values
    matrix w(3, vector<int>(3, 0));
    int b = 0;

    // max number of epochs
    int n = 5;
    // Apply HEBB
    while (n--)
    {
        cout << "\n\nEpoch: " << 5 - n << "\n";
        matrix wOld(w);
        int bOld = b;
        int yanet = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                yanet += w[i][j] * A[i][j];
            }
        }

        cout << "\nYnet of A: " << yanet << "\nWeights after processing A: \n";

        bool f = ya == activate(yanet, b);

        // UPDATING THE WEIGHT
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (!f)
                    w[i][j] += ya * A[i][j];
                cout << w[i][j] << " ";
            }
            cout << "\n";
        }

        // UPDATING BIAS
        b += ya;
        cout << "Bias after processing A: " << b;

        int ybnet = 0;
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                ybnet += w[i][j] * B[i][j];
            }
        }
        cout << "\nYnet of B: " << ybnet << "\nWeights after processing B: \n";

        bool f2 = yb == activate(ybnet, b);
        // UPDATING THE WEIGHT
        for (int i = 0; i < 3; i++)
        {
            for (int j = 0; j < 3; j++)
            {
                if (!f2)
                    w[i][j] += yb * B[i][j];
                cout << w[i][j] << " ";
            }
            cout << "\n";
        }

        // UPDATING BIAS
        b += yb;
        cout << "Bias after processing A: " << b;

        if (f && f2 && compare(wOld, w, bOld, b))
            break;
    }
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    // ios_base::sync_with_stdio(false);
    // cin.tie(0);
    // cout.tie(0);
    int t = 1;
    // cin >> t;
    while (t--)
    {
        auto start = high_resolution_clock::now();
        solve();
        auto stop = high_resolution_clock::now();
        auto duration = duration_cast<microseconds>(stop - start);
        cout << "\n\n"
             << duration.count() << " microseconds." << endl;
    }
    return 0;
}