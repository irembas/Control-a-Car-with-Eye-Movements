#include <SoftwareSerial.h>

SoftwareSerial bt_iletisim(6,7); // RX,TX
char a;

const uint8_t eSol = 3;
const uint8_t eSag = 5;

const uint8_t in1 = 13;
const uint8_t in2 = 12;

const uint8_t in3 = 11;
const uint8_t in4 = 10;
char user_input;

void setup() {
  // put your setup code here, to run once:

  pinMode(eSol, OUTPUT);
  pinMode(eSag, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);

  Serial.begin(9600);
  bt_iletisim.begin(9600);

}

void loop() 
{
  if (bt_iletisim.available())
  {
    a=(bt_iletisim.read());
    Serial.println(a);

    switch (a) 
    {
      case 'w':
        analogWrite(eSol, 100);
        analogWrite(eSag, 100);
        digitalWrite(in1, 1);
        digitalWrite(in2, 0);
        digitalWrite(in3, 1);
        digitalWrite(in4, 0);
        break;

      case 'a':

        analogWrite(eSol, 75);
        analogWrite(eSag, 150);
        digitalWrite(in1, 1);
        digitalWrite(in2, 0);
        digitalWrite(in3, 1);
        digitalWrite(in4, 0);
        break;

      case 'd':
        analogWrite(eSol, 150);
        analogWrite(eSag, 75);
        digitalWrite(in1, 1);
        digitalWrite(in2, 0);
        digitalWrite(in3, 1);
        digitalWrite(in4, 0);
        break;

      case 's':
        analogWrite(eSol, 100);
        analogWrite(eSag, 100);
        digitalWrite(in1, 0);
        digitalWrite(in2, 1);
        digitalWrite(in3, 0);
        digitalWrite(in4, 1);
        break;

      case 'q':
        analogWrite(eSol, 0);
        analogWrite(eSag, 0);
        digitalWrite(in1, 0);
        digitalWrite(in2, 1);
        digitalWrite(in3, 0);
        digitalWrite(in4, 1);
        break;
    }

  }
}