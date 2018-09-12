/*
 * wejscie_wyjscie.cpp
 *
 * Copyright 2018  <>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 *
 *  endl = koniec lini "cout << endl << a;"
 * floating point expection błąd jak podaje się 0 do dzielenia
 * void = nie zwracam wartości
 */


#include <iostream>

using namespace std;

int suma(int a, int b){
    return a + b;
}

int roznica(int a, int b){
    return a - b;
}
    
int iloczyn(int a, int b){
    return a * b;
}

int iloraz(int a, int b){
    return a / b;
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;

    cout << "podaj liczbę:";
    cin >> a;
    cout << "podaj drugą liczbę:";
    cin >> b;
    cout << "\n" << "Suma: " << suma(a, b);
    cout << "\n" << "Różnica: " << roznica(a, b);
    cout << "\n" << "Iloczyn: " << iloczyn(a, b);
    cout << "\n" << "Iloraz: " << iloraz(a, b);

	return 0;
}

