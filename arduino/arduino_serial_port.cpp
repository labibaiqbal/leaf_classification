String msgPi;
int tag = 0;

void setup() {
  Serial.begin(9600);
    delay(100);
//  Serial.setTimeout(100);
}


void sendData(){
  Serial.println("cmteq channel");
  delay(5000);
}

void receiveData(){
  if(Serial.available() > 0){
    msgPi = Serial.readStringUntil('\n');
    msgPi = msgPi + " " + String(tag);
    tag++;
    Serial.println(msgPi);
  }
}

void loop() {
  // sendData();
  receiveData();
}
