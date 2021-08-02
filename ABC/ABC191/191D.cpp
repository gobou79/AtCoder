#include <bits/stdc++.h>
using namespace std;

int main() {
    double X, Y, R;
    cin >> X >> Y >> R;
    int a, b, k;
    a = ceil(X -R);
    b = floor(X + R);
    k = 0;
    for (int x = a; x < b+1; x++) {
        int y_up, y_down;
        y_up = floor(Y + sqrt((R + x - X) * (R - x + X)));
        y_down = ceil(Y - sqrt((R + x - X) * (R - x + X)));
        k += y_up - y_down + 1;
    }
    cout << k << endl;
}