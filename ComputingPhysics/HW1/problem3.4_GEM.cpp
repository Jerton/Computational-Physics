#include<bits/stdc++.h>
using namespace std;

int main(){
    for (int n = 2; n <= 10; n++)//n*n+1矩阵
    {
        float H[n][n+1], x[n];
        for (int i = 0; i < n; i++)//矩阵初始化
        {
            for (int j = 0; j < n; j++)
            {
                H[i][j]=1/float(i+j+1);
            }
            H[i][n]=1;
        }
        
        for (int k = 0; k < n; k++)//此矩阵不含0对角元，直接消元
        {
            for (int i = k+1; i < n; i++)
            {
                float l = -H[i][k]/H[k][k];
                for (int j = k+1; j < n; j++)
                {
                    H[i][j] += l*H[k][j];
                }
                H[i][n] += l*H[k][n]; 
            }            
        }
        
        for (int i = n-1; i >= 0; i--)//回代法
        {
            x[i]=H[i][n];
            for (int j = n-1; j > i; j--)
            {
                x[i]=x[i]-H[i][j]*x[j];
            }
            x[i]=x[i]/H[i][i];
        }
        
        cout << "n=" << n <<",the solution vector is:" << endl << "x=(" ;//输出时为n阶矩阵
        for (int i = 0; i < n-1; i++)
        {
            cout << x[i] << "," ;
        }
        cout << x[n-1] << ")^T" << endl << endl;
    }
    system("pause");
    return 0;
}