#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
	printf("Enter the coordinates: ");
	int x,y,i,res=0;
	scanf("%d%d",&x,&y);
	res = (x*(x+1))/2;
	for(i = 1;i<y;i++)
	{
		res = res + x;
		x = x+1;
	}
		printf("Result: %d",res);
	
}