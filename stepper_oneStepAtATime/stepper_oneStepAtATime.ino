
/*
  Stepper Motor Control - one step at a time

  This program drives a unipolar or bipolar stepper motor.
  The motor is attached to digital pins 8 - 11 of the Arduino.

  The motor will step one step at a time, very slowly.  You can use this to
  test that you've got the four wires of your stepper wired to the correct
  pins. If wired correctly, all steps should be in the same direction.

  Use this also to count the number of steps per revolution of your motor,
  if you don't know it.  Then plug that number into the oneRevolution
  example to see if you got it right.

  Created 30 Nov. 2009
  by Tom Igoe

*/

//1  1  0  1  0
// 2  0  1  1  0
// *    3  0  1  0  1
// *    4  1  0  0  1

#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 50, 51, 52, 53);

int stepCount = 0;         // number of steps the motor has taken
int buttonState = 0;
int buttonPin = 22;
void setup() {
  // initialize the serial port:
  Serial.begin(9600);
  myStepper.setSpeed(100);


  myStepper.step(1);
  Serial.print("steps:");
  Serial.println(stepCount);
  stepCount++;

//  delay(3000);


}

void loop() {
  digitalWrite(50, 1);
  digitalWrite(51, 1);
  digitalWrite(52, 1);
  digitalWrite(53, 1);

  //    buttonState = digitalRead(buttonPin);
  //    Serial.println(buttonState);

  // check if the pushbutton is pressed. If it is, the buttonState is HIGH:
  //    if (buttonState == HIGH) {
  //      myStepper.step(1);
  //      Serial.print("steps:");
  //      Serial.println(stepCount);
  //      stepCount++;
  //
  //      delay(3000);
  //
  //  digitalrite(50, 0);
  //  digitalWrite(51, 0);
  //  digitalWrite(52, 0);
  //  digitalWrite(53, 0);

  //digitalWrite(50,0);
  //digitalWrite(50,0);
  //digitalWrite(50,0);
  //digitalWrite(50,0);
  //digitalWrite(50,0);
  //digitalWrite(50,0);
  //digitalWrite(50,0);
  //digitalWrite(50,0);


}

