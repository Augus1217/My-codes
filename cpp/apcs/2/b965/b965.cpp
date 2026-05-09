#include<iostream>
#include<vector>
using namespace std;

int main(){
    int r, c, m;
    cin >> r >> c >> m;
    vector<vector<int>> matrix(r, vector<int>(c));
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            cin >> matrix[i][j];
        }
    }

    vector<int> ops(m);
    for(int i=0; i<m; i++){
        cin >> ops[i];
    }

    for(int i=m-1; i>=0; i--){
        int op = ops[i];
        
        if (op == 0) {
            vector<vector<int>> new_mat(c, vector<int>(r));
            for(int row=0; row<r; row++){
                for(int col=0; col<c; col++){
                    // 反向旋轉公式 (逆時針90度)
                    // 原本右上角 (row=0, col=c-1) 會變到左上角 (0, 0)
                    new_mat[c-1-col][row] = matrix[row][col];
                }
            }
            matrix = new_mat;
            swap(r, c);
        } 
        else if (op == 1) {
            vector<vector<int>> new_mat(r, vector<int>(c));
            
            for(int row=0; row<r; row++){
                for(int col=0; col<c; col++){
                    new_mat[r-1-row][col] = matrix[row][col];
                }
            }
            matrix = new_mat;
        }
    }

    cout << r << " " << c << endl;
    for(int i=0; i<r; i++){
        for(int j=0; j<c; j++){
            cout << matrix[i][j] << (j==c-1 ? "" : " ");
        }
        cout << endl;
    }
}