
#include <Servo.h>
Servo myservo;  // create servo object to control a servo
char inp;
void setup(){
      Serial.begin(74880);
      myservo.attach(5);
      // myservo.write(90);
}

void loop(){
  if (Serial.available()) 
    {

    char inp = Serial.read();

    Serial.println(inp);   
    if(inp == 'r'){
        myservo.write(0);
    }
    else if(inp == 'l'){
        myservo.write(180);
    }
    else if(inp == 'c'){
        myservo.write(90);
    }

  }
}