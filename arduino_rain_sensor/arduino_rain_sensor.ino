#define DELAY_TIME 30
#define SENSOR_ON_PIN 2
#define LED_PIN 4


void setup() {
  Serial.begin(9600);

  pinMode(SENSOR_ON_PIN, OUTPUT);
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, LOW);
  

  digitalWrite(SENSOR_ON_PIN, HIGH);
  delay(1000);
  int sensorValue = analogRead(A0);
  digitalWrite(SENSOR_ON_PIN, LOW);

  
  Serial.println(sensorValue);

  
  if(sensorValue > 200) {
    digitalWrite(LED_PIN, HIGH);  
  }

  
  delay(DELAY_TIME * 1000);
}
