/*
 * Atmega16-AVR LED Blinking Program
 * 
 * Author :iNNovationMerge
 */ 

#include <avr/io.h>
#include<util/delay.h>

int main(void){
	/* Declare PORTB as Output*/
	DDRB=255;

    /* Make Port B pins High and low infinite times */
    while(1) 
    {

 		PORTB = 0b11111111;
		_delay_ms(1000);
		PORTB = 0b00000000;
		_delay_ms(1000);
			
    }
	return 0;
}

