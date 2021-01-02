/* iNNovationMerge 
 *  
 *  Turns on an LED on for one second, then off for one second, repeatedly.
 *  
 *  Reference : https://energia.nu/guide/tutorials/basics/tutorial_blink/
 *  
 *  Demo : https://youtu.be/BZC2hu5Fisg
  */

// the setup routine runs once when you press reset:
void setup() {                
  // initialize the digital pin as an output.
  pinMode(RED_LED, OUTPUT);     
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(RED_LED, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);               // wait for a second
  digitalWrite(RED_LED, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);               // wait for a second
}
