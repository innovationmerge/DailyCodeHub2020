/* iNNovationMerge 
 *  
 *  Program to read a digital input from on board Pin 5 and print  state out to the Energia Serial Monitor.
 *  
 *  Reference : https://energia.nu/guide/tutorials/basics/tutorial_digitalreadserial/
 *  
  */
// digital pin 5 has a pushbutton attached to it.
int pushButton = 5;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600); 
  // make the on-board pushbutton's pin an input pullup:
  pinMode(pushButton, INPUT_PULLUP);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input pin:
  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  Serial.print("Button State : ");
  Serial.println(buttonState);
  delay(1);        // delay in between reads for stability
}
