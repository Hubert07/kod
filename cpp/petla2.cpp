/*
 * petla2.cpp
 * 
 * Copyright 2018 Hubert <Hubert@DESKTOP-K3DV5KA>
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

int main(int argc, char **argv)
{
	int n, m, i;
    n = m = i = 0;
    
    cout << "Podaj od ktorej liczby zaczac: ";
    cin >> n;
    cout << "Podaj na ktorej liczbie skonczyc: ";
    cin >> m;
    
    for (i = n; i <= m; i++)
    {
        cout << i << " ";
    }
    
	return 0;
}

