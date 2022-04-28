
#include<iostream>
using namespace std;
int main()
{
	//Array for Binary Input
	int arr[4][2] = { {0,0},
		{0,1},
		{1,0},
		{1,1}
	};

	//Target array for Binary Input
	int t[4] = {0,1,1,1};

	// Considering learning rate=1
	int alp = 1;

	// yi = input
	// yo = output
	int w1 = 0, w2 = 0, b = 0, count = 0, i, yi, yo;
	int dw1,dw2,db;

	while(1)
	{
		cout<<"x1"<<" "<<"x2"<<" "<<"b"<<" "<<"yi"<<" "<<
			"yo"<<" "<<"t"<<" "<<"dw1"<<" "<<"dw2"<<" "<<"db"<<
			" "<<"w1"<<" "<<"w2"<<" "<<"b"<<endl;

		for(i = 0; i < 4; i++)
		{
			// Calaulating Input
			yi = arr[i][0] * w1 + arr[i][1] * w2 + b;
			if(yi >= 0)
			{
				yo = 1;
			}
			else
			{
				yo = 0;
			}
			if(t[i] == yo)
			{
				count++;
				dw1 = 0;
				dw2 = 0;
				db = 0;
			}
			// Calaulating Change in Weight
			else
			{
				dw1 = alp*(t[i] - yo) * arr[i][0];
				dw2 = alp*(t[i] - yo) * arr[i][1];
				db = alp*(t[i] - yo);
			}
			w1 = w1 + dw1;
			w2 = w2 + dw2;
			b = b + db;
			cout<<arr[i][0]<<" "<<arr[i][1]<<" "<<1<<" "<<yi<<" "<<yo
				<<"	 "<<t[i]<<" "<<dw1<<" "<<dw2<<" "<<db<<" "<<w1<<" "<<w2
				<<" "<<b<<endl;
		}
		cout<<endl;
		if(count == 4)
		{
			return 0;
		}
		else
		{
			count = 0;
		}
	}
}
