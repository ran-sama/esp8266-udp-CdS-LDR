#include <WiFiUdp.h>
#include <ESP8266WiFi.h>

WiFiUDP Udp;
const char* ssid = "name";
const char* password = "password";
unsigned int localUdpPort = 6666;
String PinState = "";

void setup() {
  Udp.begin(localUdpPort);
  delay(200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
}

void loop() {
  PinState = analogRead(A0);
  Udp.beginPacket("10.0.0.17", 7777);
  Udp.write(&PinState[0]);
  Udp.endPacket();
  delay(60000);
}
