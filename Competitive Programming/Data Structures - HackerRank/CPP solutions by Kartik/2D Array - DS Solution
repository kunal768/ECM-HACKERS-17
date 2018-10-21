#include<iostream>
using namespace std;
int main()
{
    int i,j,arr[6][6],sumarr[4][4];
    for(i=0;i<6;i++)
    {
        for(j=0;j<6;j++)
        {
            cin>>arr[i][j];
            if((arr[i][j]<-9)&&(arr[i][j]>9))
            return(0);
            //cout<<"Not allowed!";            
        }
    }
    sumarr[0][0]=arr[0][0]+arr[0][1]+arr[0][2]+arr[1][1]+arr[2][0]+arr[2][1]+arr[2][2];
    sumarr[0][1]=arr[0][1]+arr[0][2]+arr[0][3]+arr[1][2]+arr[2][1]+arr[2][2]+arr[2][3];
    sumarr[0][2]=arr[0][2]+arr[0][3]+arr[0][4]+arr[1][3]+arr[2][2]+arr[2][3]+arr[2][4];
    sumarr[0][3]=arr[0][3]+arr[0][4]+arr[0][5]+arr[1][4]+arr[2][3]+arr[2][4]+arr[2][5];
    
    sumarr[1][0]=arr[1][0]+arr[1][1]+arr[1][2]+arr[2][1]+arr[3][0]+arr[3][1]+arr[3][2];
    sumarr[1][1]=arr[1][1]+arr[1][2]+arr[1][3]+arr[2][2]+arr[3][1]+arr[3][2]+arr[3][3];
    sumarr[1][2]=arr[1][2]+arr[1][3]+arr[1][4]+arr[2][3]+arr[3][2]+arr[3][3]+arr[3][4];
    sumarr[1][3]=arr[1][3]+arr[1][4]+arr[1][5]+arr[2][4]+arr[3][3]+arr[3][4]+arr[3][5];

    sumarr[2][0]=arr[2][0]+arr[2][1]+arr[2][2]+arr[3][1]+arr[4][0]+arr[4][1]+arr[4][2];
    sumarr[2][1]=arr[2][1]+arr[2][2]+arr[2][3]+arr[3][2]+arr[4][1]+arr[4][2]+arr[4][3];
    sumarr[2][2]=arr[2][2]+arr[2][3]+arr[2][4]+arr[3][3]+arr[4][2]+arr[4][3]+arr[4][4];
    sumarr[2][3]=arr[2][3]+arr[2][4]+arr[2][5]+arr[3][4]+arr[4][3]+arr[4][4]+arr[4][5];
    
    sumarr[3][0]=arr[3][0]+arr[3][1]+arr[3][2]+arr[4][1]+arr[5][0]+arr[5][1]+arr[5][2];
    sumarr[3][1]=arr[3][1]+arr[3][2]+arr[3][3]+arr[4][2]+arr[5][1]+arr[5][2]+arr[5][3];
    sumarr[3][2]=arr[3][2]+arr[3][3]+arr[3][4]+arr[4][3]+arr[5][2]+arr[5][3]+arr[5][4];
    sumarr[3][3]=arr[3][3]+arr[3][4]+arr[3][5]+arr[4][4]+arr[5][3]+arr[5][4]+arr[5][5];
    
    int max = sumarr[0][0]; 
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
            if(sumarr[i][j]>max)
            {
                max = sumarr[i][j];
            }
        }
    }
    cout<<max;    
}
