#include<bits/stdc++.h>

using namespace std;

float factorial(int n) {//阶乘函数
    int p = 1;
    if (n == 0)
    {
        return 1;
    }
    else {
        for (int i = 1; i < n + 1; i++)
        {
            p = p * i;
        }
        return p;
    }
}

int main() {
    double result = 0, x = 0;
    int N = 1;

    while (N < 50)//从0加到N
    {
        while (x <= 100)
        {
            for (int i = 0; i < N; i++){//循环N遍，计算前N项和，0<=x<=N-1
                result += pow(-1 * x, i) / (factorial(i));//加上第i+1项
            }
            cout << result << "\t";
            x += 10;
            result = 0;
        }
        cout << endl;
        N++;
        x = 0;
    }
    system("pause");
    return 0;
}