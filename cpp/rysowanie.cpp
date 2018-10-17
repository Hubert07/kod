#include <iostream>

using namespace std;

//void nie zwaraca żadnych wartosci == bez return
//w nawiasach podajemy parametry, które bd zmienne
// jeżeli po if albo for mam tylk o1 instrukcję, to można bez nawiasów
void prostokat(int x, int y, char znak) {
    
    for (int i = 1; i <= x; i++) {
        for (int j = 1; j <= y; j++)
            if (j == 1 || j == y || i == 1 || i == x)
                cout << znak;
            else
                cout << " ";
        cout << endl;
    }
}

int main(int argc, char **argv) {
    
    int a, b;
    a = b = 0;
	cout << "Podaj pierwszy bok: ";
	cout << "Podaj drugi bok: ";
    cin >> a >> b;
    char znak;
// zmienna typu char może zawierac pojedynczy znak czyli znakiem aski(127 znaków)
    cout << "Podaj znak:";
    cin >> znak;
    prostokat(a , b, znak);
    cout << "Pole prostokąta wynosi " << a * b;
	return 0;
}

