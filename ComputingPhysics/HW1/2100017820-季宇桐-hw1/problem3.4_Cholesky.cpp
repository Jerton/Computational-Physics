#include<bits/stdc++.h>
using namespace std;

int main(){
    for (int n = 2; n <= 10; n++)//n*n+1矩阵
    {
        float H[n][n+1], x[n],y[n];
        for (int i = 0; i < n; i++)//矩阵初始化
        {
            for (int j = 0; j < n; j++)
            {
                H[i][j]=1/float(i+j+1);
            }
            H[i][n]=1;
        }
        
        for (int j = 0; j < n; j++)//Cholesky分解
        {
            for (int k = 0; k < j; k++)
            {
                H[j][j]=H[j][j]-pow(H[j][k],2);
            }
            H[j][j]=pow(H[j][j],0.5);
            for (int i = j+1; i < n; i++)
            {
                for (int k = 0; k < j; k++)
                {
                    H[i][j]=H[i][j]-H[i][k]*H[j][k];
                }
                H[i][j]=H[i][j]/H[j][j];
            }
        }
        
            for (int i = 0; i < n; i++)//前代法
        {
            y[i]=H[i][n];
            for (int j = 0; j < i; j++)
            {
                y[i]=y[i]-H[i][j]*y[j];
            }
            y[i]=y[i]/H[i][i];
        }

            for (int i = n-1; i >= 0; i--)//回代法
        {
            x[i]=y[i];
            for (int j = n-1; j > i; j--)
            {
                x[i]=x[i]-H[j][i]*x[j];
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