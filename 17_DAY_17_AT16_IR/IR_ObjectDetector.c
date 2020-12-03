/*
 * Infrared object detection with Atmega16-AVR
 * Author : iNNovationMerge
 */ 
#define F_CPU 16000000UL
#include <avr/io.h>
#include "lcd_lib.h"
#include <util/delay.h>
#include <stdio.h>
#include "adc_lib.h"

int x;
char a[15];
int main(void )
{
	LCDinit();
	LCDclr( );
	ADCinit();// Initializes ADC in 10 bit mode
	DDRB = 0xff; // make port B as output 
	while (1)
	{
		x = read_adc(0);// returns the digital value of the analog i/p connected to pin 0 of port A
		
		LCDGotoXY(0,0);				// displays string in 1st row from 1st col
		LCDdisplay("Object Detector:");
		_delay_ms(100);
		
		if(x <= 100)
		{
		LCDGotoXY(0,1);				// displays string in 2nd row from 1st col
		LCDdisplay("Not Detected         ");
		PORTB = 0x00;
		_delay_ms(300);
		}
		else
		{
		LCDGotoXY(0,1);				// displays string in 2nd row from 2nd col
		LCDdisplay("Detected          ");
		PORTB = 0xff;
		_delay_ms(300);
		}
	}
	return 0;
}
