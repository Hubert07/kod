/*
 * znaki.cpp
 * 
 * może też być 
 * case:
 *   białe++;
 *   inne;
 * break;
 */


#include <iostream>

using namespace std;

void  licz_znaki(char tab[]) {
    int i = 0;
    int biale, inter, licz;
    biale = inter = licz = 0;
    while (tab[i] != '\0') {
/*
 *         if (tab[i] == ' ' || tab[i] == '\t')
            biale++;
        else
            cout << tab[i];
        
    }
*/
        switch (tab[i]) {
            case ' ': biale++; break;
            case '\t': biale++; break;
            case ',': inter++; break;
            case '.': inter++; break;
            default: licz++; break;
            }
        i++; // zwiększanie indeksu
        }
    cout << "\nZnaków białych " << biale << endl;
    cout << "\nZnaków interpunkcyjnych " << inter << endl;
    cout << "\nReszta " << licz << endl;
}

void ascii(char tab[]) {
    int i = 0;
    while (tab[i] != '\0') {
        cout << (int)tab[i] << " ";
        i++;
    }
}

// ASCII A-Z 65-90 a-z 97-122
void zamiana_liter(char tab[]) {
    int i = 0;
    int x;
    while (tab[i] != '\0') {
        x = (int)tab[i];
        if (x >= 65 && x <= 90) {
            x += 32;
            }
        else if (x >= 97 && x <= 122) {
            x -= 32;
            }
        cout << (char)x;
        i++;
    }
}

int main(int argc, char **argv)
{
    const int rozmiar = 50; // deklaracja stałej
    char znaki[rozmiar];
    cout << "Jak się nazywasz?" << endl;
    cin.getline(znaki, 50); // deklaracja tablicy znakowej
    cout << "Cześć " << znaki << endl;
	// licz_znaki(znaki);
    ascii(znaki);
    cout << endl;
    zamiana_liter(znaki);
	return 0;
}

