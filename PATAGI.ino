#include "HX711.h"
#include <ESP8266WiFi.h>
#include <PubSubClient.h>
#define MQ2pin  D1
#define Buzz    D8 

const char* ssid = "Anya Geraldine";
const char* password = "langsungmasukkok";
const char* mqtt_server = "rmq2.pptik.id"; 
const char* mqtt_user = "TMDG2022";
const char* mqtt_pass= "TMDG2022";
int sensorValue;
int wsb=0;
 
WiFiClient espClient;
PubSubClient client(espClient); 
HX711 scale(D5, D6);

float weight;
float calibration_factor = -444525; 

void setup_wifi() {
  // Connecting to a WiFi network
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}
 
void setup() 
{
  Serial.begin(115200);
  scale.set_scale();
  scale.tare();
  long zero_factor = scale.read_average(); //Get a baseline reading
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  pinMode (MQ2pin, INPUT);
  pinMode (Buzz, OUTPUT);
}
 
void loop() 
 
{
 char msg[8];
 char msg2[1];
 if (!client.connected()) {reconnect();}
 scale.set_scale(calibration_factor);
 weight = scale.get_units(5);
 sensorValue = digitalRead(MQ2pin);
 sprintf(msg,"%f",weight); 
 sprintf(msg2,"%i",sensorValue);
 client.publish("PATAGI",msg,msg2);


 unsigned long wsk = millis();
 if(wsk-wsb >= 1000)
 {
  wsb=wsk;
 if (sensorValue == HIGH) 
 {
    Serial.println("Smoke: -");
    digitalWrite(Buzz,LOW); 
  } if (sensorValue == LOW) 
  {
    Serial.println("Smoke: Detected!");
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(100);
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(100);
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(500);
    digitalWrite(Buzz,HIGH); delay(1000);
    digitalWrite(Buzz,LOW); delay(100);
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(100);
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(100);
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(100);
    digitalWrite(Buzz,HIGH); delay(100);
    digitalWrite(Buzz,LOW); delay(100);
  }
 Serial.print("Weight: ");
 Serial.print(weight);
 Serial.println(" KG");
 Serial.println();
 }
}

void reconnect() {
  // Loop until we're reconnected
  Serial.println("In reconnect...");
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("Arduino_Gas", mqtt_user, mqtt_pass)) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}
 
