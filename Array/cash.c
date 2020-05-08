#include <stdio.h>
int countsetbits(int n)
{
     int count =0;
    while (n) { 
        count += n & 1; 
        n >>= 1; 
    } 
    return count; 

}
int main() {
    // your code goes here
    int t;
    scanf("%d",&t);
    while(t>0)

    {
        //printf("%d",t);
        int i,n,q,p,count1 = 0,even =0;
        scanf("%d%d",&n,&q);
        long long int a[n],r[n];

        for(i=0;i<n;i++)
        {
            scanf("%lld",&a[i]);
        }
        //for(i =0;i<q;i++)
            scanf("%d",&p);
        //printf("Suman");
        for(i =0;i<n;i++)
         {
             r[i] = p^a[i];
         }
         for( i=0;i<n;i++)
         {
            even = countsetbits(r[i]);
            if(even%2 ==0)
                count1++;
            even =0;    
        } 
        printf("%ld %ld\n",count1,n-count1);
        count1 = 0;
        t--;
        //printf("%d",t);
    }
    return 0;
}