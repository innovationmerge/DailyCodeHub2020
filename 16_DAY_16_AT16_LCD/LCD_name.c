/*
 * 16*2 LCD Interface with Atmega16-AVR
 *
 * Author : iNNovationMerge
 * 
 */

#include<avr/io.h>
#include<util/delay.h>
#include"lcd_lib.h"

int main (void)
{
	int i;
	DDRC = 255;
	LCDinit(); // Initializes LCD 
	LCDcursorOFF(); 
	LCDclr();
	_delay_ms(50);
	LCDhome();
	while(1)
	{
		LCDGotoXY(0, 0); // displays string in 1st row from 1st col
		LCDdisplay("iNNovationMerge");
		LCDGotoXY(0, 1); // displays string in 2nd row from 1st col	
		LCDdisplay("ATMEGA16 LCD");
		_delay_ms(500);
	}
	return 0;
}

