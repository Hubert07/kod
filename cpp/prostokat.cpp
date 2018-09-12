/*
 * 
 */


#include <iostream>

using namespace std;

int pole(int a, int b){
    return a * b;
}
    
int obwod(int a, int b){
    return 2 * a + 2 * b;
}

int main(int argc, char **argv)
{
	int a, b;
    a = b = 0;
    
    cout << "podaj długośc pierwszego boku :";
    cin >> a;
    
    cout << "podaj długość drugiego boku :";
    cin >> b;
    
    cout << "\n" << "Pole: " << pole(a, b);
    cout << "\n" << "Obwód: " << obwod(a, b);
	return 0;
}

