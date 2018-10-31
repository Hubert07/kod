/*
 * anagram.cpp
 */


#include <iostream>

using namespace std;

int zlicz(char tb[]) {
    int i = 0;
    while(tb[i] != '\0') i++;
    return i;
}

void wyswietl(char tekst[], int rozmiar) {
    for(int i = 0; i < rozmiar; i++) {
        cout << tekst[i];
    }
}

void anagram(char tekst[], rozmiar) {
    //for zaczyna od ostatmniego znaku
    for (int i; i <= coś; i--) {
        
        }
    }

int main(int argc, char **argv)
{
    const int rozmiar = 50; // deklaracja stałej
    char tekst[rozmiar];
    cin.getline(tekst, rozmiar);
    wyswietl(tekst, zlicz(tekst));
    
	return 0;
}

