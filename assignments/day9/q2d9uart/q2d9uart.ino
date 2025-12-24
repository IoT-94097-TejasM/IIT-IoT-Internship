void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.println("UART setup is done");
}

int count = 0;

void loop() {
  // put your main code here, to run repeatedly:
  Serial.printf("count = %d\n", count++);

  delay(2000);
}
