# include <stdio.h>

int main()
{
	int x, y, a, b, r;
	printf("두 개의 정수를 입력하세요 : ");
	scanf("%d %d",&a, &b);
	if (a > b)
    {
		x = a;
		y = b;
    }
	else
    {
		x= b; 
		y= a;
    }
	while(1)
	{
		r = x % y;
		x = y;
		y = r;
		if (y == 0)
		{
			printf("최대공약수는 %d이며 프로그램을 종료합니다", x);
			break;
		}
	}
}