
#include <iostream>
#include <math.h>

using namespace std;

int v(int a, int b){
    return a * a + b * b;
}

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "podaj Vy :";
    cin >> a;
    
    cout << "podaj Vx :";
    cin >> b;
    
    cout << "\n" << "Prędkość wypadkowa: " << v(a, b);
	return 0;
}

