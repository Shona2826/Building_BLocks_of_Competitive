#include<iostream>
#include<stdio.h>
#include<math.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	while(t>0)
	{
		int n,q,steps = 0;
		scanf("%d%d",&n,&q);
		int f[q],d[n];
		for(int i =0;i<q;i++)
		{
			scanf("%d%d",&f[i],&d[i]);
		}
		for(int i =0;i<q;i++)
		{
			if(i == 0)
			{
				steps += f[i];
				
			}
			else if(i>0)
			{
				steps = steps + abs(f[i] - d[i-1]);
				//steps = steps + 
			}
			steps = steps + abs(d[i] - f[i]);
		}
		printf("%d\n",steps);
		t--;
		}
}
