#include<WiFi.h>
#include<ArduinoMqttClient.h>
#include<DHT.h>


const char *ssid = "SUNBEAM";
const char *password = "1234567890";

const char *host = "172.18.3.245";
unsigned int port = 1883;

#define DHT_PIN 4
#define DHT_TYPE  DHT11

DHT dht(DHT_PIN, DHT_TYPE);


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  dht.begin();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  Serial.print("Connecting to WiFi ");
  while(WiFi.status() != WL_CONNECTED){
    delay(500);
    Serial.print(".");
  }
  Serial.println("Connected to WiFi");
  Serial.print("IP Address : ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // put your main code here, to run repeatedly:
  float temp = dht.readTemperature();

  WiFiClient wifiClient;
  MqttClient publisher(wifiClient);

  if(publisher.connect(host, port)){
    publisher.beginMessage("reading/temp");
    publisher.print(temp);
    publisher.endMessage();
    
  }

  delay(5000);

}







