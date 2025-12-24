#define MQ2_DIGITAL 26

void setup() {
  pinMode(MQ2_DIGITAL, INPUT);
  Serial.begin(115200);
}

void loop() {
  if (digitalRead(MQ2_DIGITAL) == LOW) {
    Serial.println("🚨 GAS / SMOKE DETECTED");
  }
  delay(500);
}