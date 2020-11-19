/*
iNNovation Merge 
Day 1 - #DailyCodeHub

4-Bit LIQUID CRYSTAL DISPLAY (LCD) Interface using Arduino
*/

// Load the LiquidCrystal library, which will give us
// commands to interface to the LCD:
// Library Reference : https://www.arduino.cc/en/Reference/LiquidCrystal

#include <LiquidCrystal.h>

// Initialize the library with the pins used.
// LiquidCrystal lcd(RS, E, D4, D5, D6, D7);
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
{
	lcd.begin(16, 2); //Initialize the 16x2 LCD
	lcd.clear();	//Clear any previous data displayed on the LCD
}
void loop()
{
	lcd.setCursor(0, 0); 	//Set the (invisible) cursor to column 0, row 1.
  lcd.print("iNNovation Merge"); // Display a message on the LCD!

  lcd.setCursor(1, 1);  //Set the (invisible) cursor to column 0, row 1.
  lcd.print("#DailyCodeHub"); // Display a message on the LCD!
}

