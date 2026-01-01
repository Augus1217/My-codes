#include<iostream>
#include<vector>
#include<map>

using namespace std;

int main()
{
        short int m,n,k,a,s=0;
        string t;
        vector<vector<short int>> x;
        vector<vector<char>> c;
        cin>>m>>n>>k;
        cout<<m<<n<<k;
        for(short int i=0;i<m;++i){
                cin>>t;
                c.push_back(vector<char>(t.begin(), t.end()));
        }
        for(short int i=0;i<k;++i){
                x.push_back({});
                for(short int j=0;j<m;++j){
                        cin>>a;
                        x[i].push_back(a);
                }
        }
        for(short int i=0;i<k;++i){
                for(short int j=0;j<m;++j){
                        if(x[i].at(j)>0){
                                c[j]=c[j]+c[j].substr(0, x[i][j]);
                                c[j].erase(0,x[i][j]);
                        }
                        else if(x[i].at(j)<0){
                                c[j]=c[j].substr(x[i][j],l[j].size()-1)+c[j];
                                c[j].erase(x[i][j],c[j].size()-1);
                        }
                }
        }
        for(short int i=0;i<n;++i){
                c[i].push_back({});
                for(short int j=0;j<m;++j){
                        c[i][j].push_back(l[i][j]);
                }
        }
        for(short int i=0;i<size(c);i++){
                map<char, int> freq;
                for (char ch : c[i]) {
                        freq[ch]++;
                }
                s+=maxFreq;
        }
        cout<<s<<endl;
        return 0;
}
