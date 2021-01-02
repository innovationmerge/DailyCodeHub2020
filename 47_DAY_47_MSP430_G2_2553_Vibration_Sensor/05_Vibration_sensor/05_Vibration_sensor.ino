/* iNNovationMerge 
 *  
 *  Program to Read an Vibration Sensor analog input on pin A3 and Decide weather Vibration is Detected or not
 *  
 *  Reference : https://energia.nu/guide/tutorials/basics/tutorial_analogreadserial/
 *  
 */

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600); 
}


// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin A3:
  int sensorValue = analogRead(A3);
  if (sensorValue<100){
    Serial.println("Vibration Detected");
  }
  else{
    Serial.println("Vibration Not Detected");
  }
  delay(1); // delay in between reads for stability
}
