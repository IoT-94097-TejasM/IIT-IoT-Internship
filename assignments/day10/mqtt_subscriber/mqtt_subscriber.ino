#include<WiFiClient.h>
#include<WiFi.h>
#include<ArduinoMqttClient.h>

const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *host = "172.18.4.146";
const int port = 1883;

WiFiClient wifiClient;
MqttClient subscriber(wifiClient);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Serial.flush();

  pinMode(2, OUTPUT);
  digitalWrite(2, LOW);
  
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.println("Connecting to a WiFi");
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(500);
  }

  Serial.println("\n WiFi is connected");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());

  if(!subscriber.connect(host, port))
    while(1);

  Serial.println("Connected to the Broker");

  subscriber.subscribe("room/light");

  Serial.println("Topic is subscribed");
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int size = subscriber.parseMessage();
  if(size){
    char str[size];
    memset(str, 0, sizeof(str));
    for(int i = 0 ; i < size ; i++)
      str[i] = (char)subscriber.read();

    Serial.printf("Message : %s\n",str);

    if(strncmp(str, "ON", 2) == 0){
      digitalWrite(2, HIGH);
      Serial.println("LED is Turned ON");
    }
    else if(strncmp(str, "OFF", 3) == 0){
      digitalWrite(2, LOW);
      Serial.println("LED is Turned OFF");
    }

  }

  delay(6000);
}




