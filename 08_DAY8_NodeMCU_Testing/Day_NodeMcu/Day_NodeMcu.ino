/*
Author : iNNovationMerge

Testing NodeMCU with Arduino IDE - Blinking LED
*/

void setup()
{
  pinMode(D0, OUTPUT);      //Built IN LED
}

void loop()
{
  digitalWrite(D0, HIGH);   // Turn on the LED
  delay(1000);              // Wait for one second
  digitalWrite(D0, LOW);    // Turn off the LED  
  delay(1000);              // Wait for one second
}
