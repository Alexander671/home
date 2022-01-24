#include <ESP8266WiFi.h>

 
#define RELAY 0 
const char* ssid = "Belkin_Wireless";  // для SSID точки доступа

const char* password = "";  // для пароля к точке доступа

 

int ledPin = 2; // контакт GPIO2 на ESP8266

WiFiServer server(80);  //  порт веб-сервера

 

void setup() {
  
  Serial.begin(115200);

  // Переключаем контакт GPIO2 в режим вывода данных (OUTPUT):

  pinMode(ledPin, OUTPUT);


 

 

   

  // подключаемся к WiFi-сети:

  Serial.println();

  Serial.println();

  Serial.print("Connecting to ");  //  "Подключение к "

  Serial.println(ssid);

   

  WiFi.begin(ssid, password); 

   

  while (WiFi.status() != WL_CONNECTED) {

    delay(500);

    Serial.print(".");

  }

  Serial.println("");

  Serial.println("WiFi connected");  

  server.begin();

  Serial.println("Server started");  //  "Сервер запущен"

 

  // печатаем IP-адрес:

  Serial.print("Use this URL to connect: ");  

  Serial.print("http://");

  Serial.print(WiFi.localIP());

  Serial.println("/");

}

 

void loop() {

  int pin = 2;

  // проверяем, подключен ли клиент:

  WiFiClient client = server.available();

  if (!client) {

    return;
  } 

    
  // ждем, когда клиент отправит какие-нибудь данные:

  Serial.println("new client");  //  "новый клиент"

  while(!client.available()){

    delay(1);

  }

   

  // считываем первую строчку запроса:

  String request = client.readStringUntil('\r');

  Serial.println(request);

  client.flush();

   

   // обрабатываем запрос:

   int value = LOW;
   

  if (request.indexOf("/LED=OFF") != -1) {

    digitalWrite(ledPin, HIGH);

    value = HIGH;

    pinMode(RELAY,OUTPUT);                      // Указываем вывод RELAY как выход
  
    digitalWrite(RELAY, LOW);                   // Устанавливаем RELAY в LOW (0В)


  } 

  if (request.indexOf("/LED=ON") != -1){


    digitalWrite(ledPin, LOW);    // выключаем светодиод,

    Serial.println("RELAY=OFF");
  
    digitalWrite(RELAY,HIGH);


  }

 

  // выставляем значение на ledPin в соответствии с запросом:

  //digitalWrite(ledPin, value);

   

  // возвращаем ответ:

  client.println("HTTP/1.1 200 OK");

  client.println("Content-Type: text/html");  //  "Тип контента: 

                                              //  text/html "

  client.println("");  //  не забываем это...

  client.println("<!DOCTYPE HTML>");

  client.println("<html>");

   

  client.print("Led pin is now: ");  //  "Контакт светодиода теперь 

                                     //  в состоянии: "

   

  if(value == HIGH) {

    client.print("Off");   //  "Вкл"

  } else {

    client.print("On");  //  "Выкл"

  }

  client.println("<br><br>");

  client.println("Click <a href=\"/LED=ON\">here</a> turn the LED on pin 2 ON<br>");  //  "Кликните тут, чтобы включить светодиод

                 //  на контакте 2"

  client.println("Click <a href=\"/LED=OFF\">here </a> turn the LED on pin 2 OFF<br>");     //  "Кликните тут, чтобы выключить светодиод

                 //  на контакте 2"


  client.println("</html>");

 

  delay(1);

  Serial.println("Client disconnected");  //  "Клиент отключен"

  Serial.println("");

}
