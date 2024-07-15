int x = 0;
int c1 = 7;

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  pinMode(c1, OUTPUT);

  digitalWrite(c1, LOW);
  
}

void loop() {
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.print(x + 1);
  if(x == 13) {
    digitalWrite(c1, HIGH);
    }
  else {
    digitalWrite(c1, LOW);
  }
}
