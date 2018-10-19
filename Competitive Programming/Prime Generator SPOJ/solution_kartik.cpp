#include<iostream>
#include<math.h>
using namespace std;
int main()
{
        int d,z,v;
        cin>>d;
        cout<<"\n";
        int m,n;
        int Prime(int p);
        for (int i=0;i<d;i++)
        {
                cin>>m;

                cin>>n;
                for(int j=m;j<=n;j++)
                {
                        if((Prime(j)==1)&&(j>1))
                        {
                                cout<<"\n"<<j;

                        }

                }
        }       


        return 0;
}
int Prime(int z)
        {
                int flag=1;
                for(int c=2;c<=sqrt(z);c++)
                {
                        if((z%c)==0)
                        {
                                flag=0;
                                break;
                        }

                }
                return flag;    
        }
