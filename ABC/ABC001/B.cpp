#include <bits/stdc++.h>
using namespace std;

int main() {
    int m;
    double n;
    cin >> m;
    n += m/1000;
    cout << n << endl;
    if (n < 0.1) {
        cout << "00" << endl;
    }
    else if (0.1 <= n && n<= 5) {
        n *=10;
        if (n > 10) {
            cout << n << endl;
        }
        else {
            cout << n << endl;
        }
    }
    else if (6 <= n && n<= 30) {
        cout << n + 50 << endl;
    }
    else if (35<= n && n<= 70) {
        cout << (n-30) / 5 + 80 << endl;
    }
    else if(n > 70) {
        cout << "89" << endl;
    }

    
}