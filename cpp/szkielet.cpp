/*
 * szkielet.cpp
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
 * 
 */


#include <iostream> 

using namespace std;

/*io input/output czyli biblioteka wejścia/wyjścia w pythonie nie trzeba
 * niczego takiego importować
 * zawsze musi być main(czyli nazwa funkcji) int=integer
 * std to standard libray
 * "\n" = new line*/

int main(int argc, char **argv)
{
	int liczba; // deklaracja zmiennej liczba typu integer typ całkowitego
    liczba = 7.5;
    // std::cout << liczba; // pozwala w cpp no coś w takiego jak "wypisz" 
    cout << liczba;
    
    int a, b, c; // deklaracja zmiennej
    a = b = c = d = e = 0; // inicjalizacja zmiennych (TRZEBA TO ZROBIĆ)
    
    a = 9;
    b = 2 * c;
    c = 3 * a;
    d = c + a; // dodawanie
    e = b - a; // odejmowanie
    
    cout << "\n" << a << " " << b << " " << c << " " << d << " " e;
	return 0;
}

