#include <LiquidCrystal.h>
#include <Servo.h>

Servo myservo; 
const int pwmPin = 10;
byte RXBuf[2];
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int DataTampil;
int DataPWM = 0;
int DataPWM2 = 0;

void setup() {
  lcd.begin(16, 2);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
  myservo.attach(10);
}


void loop() {
  Kipas();
  if (Serial.available()){
    int nBytes = Serial.readBytes(RXBuf,sizeof(RXBuf));
    if (nBytes>=1) {
      DataPWM = int(RXBuf[0]);
      Serial.print("Data Analog : ");
      Serial.print(DataPWM2);
      Serial.print(", Pergeseran Motor Servo : ");
      Serial.println(DataPWM);
    }
  }
}

void Kipas(){
  DataTampil = analogRead(A0);
  DataPWM2 = map(DataTampil, 0, 1023, 0, 120);
  myservo.write(DataPWM);
  analogWrite(13, DataPWM2);
  lcd.print(DataPWM2);
  delay(50);
  lcd.clear();
}
