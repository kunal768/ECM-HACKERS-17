#include <iostream>
using namespace std;
#include<math.h>
int isPrime(int n)  
{  
  int i, flag=0;    
  for(i = 2; i <= sqrt(n); i++)  
  {  
      if(n % i == 0)  
      {  
          flag=1;  
          break;  
      }  
  }  
  if (flag==0)  
  return 0;
  else if(flag ==1)
    return 1;  
}  

int main() {
  int t,i;cin>>t;
  for(i = 0;i<t;i++){
    int m,n,j;cin>>m>>n;
    for(j=m;j<=n;j++){
      if(j == 1)
        continue;
      if(isPrime(j)==0)
         cout<<j<<"\n";
    }
  }
}

