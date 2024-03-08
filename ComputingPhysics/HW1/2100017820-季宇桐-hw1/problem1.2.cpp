#include<bits/stdc++.h>
using namespace std;

float S_n(float n, float x){//递归函数
    float a = 1;
    if (n == 0)
    {
        return a;
    }
    else
    {
        a = - S_n(n-1,x) * x / n;
        return a;
    }
}

int main(){
    int N = 0;
    float x = 0, result = 0;
    while (N <= 100)
    {
        while (x <= 100)
        {
            for (int i = 0; i <= N; i++)
            {
                result += S_n(i, x);//0到n求和
            }
            cout << result << "\t";
            x += 10;
            result = 0;
        }
        x = 0;
        N++;
        cout << endl;
    }
    system("pause");
    return 0;
}