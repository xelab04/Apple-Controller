int in = 13;
int in2 = 12;
int reading = 0;
int reading2 = 0;

bool v1 = false;
bool v2 = false;

float sleep = 0.75;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(in,INPUT);
  digitalWrite(in,HIGH);

  pinMode(in2,INPUT);
  digitalWrite(in2,HIGH);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  reading = digitalRead(in);
  if(reading == LOW){
    Serial.println("High1");
    //delay(sleep);
  }
  reading2 = digitalRead(in2);
  if(reading2 == LOW){
    Serial.println("High2");
    //delay(sleep);
  }
  
  int sensorValue1 = analogRead(A0);
  float voltage1 = sensorValue1 * (5.0 / 1023.0);

  int sensorValue2 = analogRead(A1);
  float voltage2 = sensorValue2 * (5.0 / 1023.0);
  
  
  if ((voltage1 < 0.6) || (voltage1 > 3)){
    Serial.println(String("Y Axis") + voltage1);
    v1 = true;
    //delay(sleep);
  }
  else if(v1 == true){
    Serial.println(String("Y Axis") + -1);
    v1 = false;
  }

  if((voltage2 < 0.6) || (voltage2 > 3)){
    Serial.println(String("X Axis") + voltage2);
    v2 = true;
    //delay(sleep);
  }
  else if(v2 == true){
    Serial.println(String("X Axis") + -1);
    v2 = false;
  }
  
  delay(75);
}
