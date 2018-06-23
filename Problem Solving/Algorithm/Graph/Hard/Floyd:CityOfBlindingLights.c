#include<stdio.h>
int main(){
    int n,m,i,j,k,q,a,b,w;
    scanf("%d%d",&n,&m);
    int g[n][n];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            g[i][j]=100001;
        }
    }
    for(i=0;i<m;i++){
        scanf("%d%d%d",&a,&b,&w);
        g[a-1][b-1]=w;
    }
    for(i=0;i<n;i++){
        g[i][i]=0;
    }
    for(k=0;k<n;k++){
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                if(g[i][j]>(g[i][k]+g[k][j])){
                    g[i][j]=(g[i][k]+g[k][j]);
                }
            }
        }
    }
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(g[i][j]==100001)
            g[i][j]=-1;
        }
    }
    scanf("%d",&q);
    for(i=0;i<q;i++){
        scanf("%d%d",&a,&b);
        printf("%d\n",g[a-1][b-1]);
    }
}