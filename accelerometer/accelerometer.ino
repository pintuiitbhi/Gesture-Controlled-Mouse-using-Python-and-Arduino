//To plot the data on graph uncomment the commented statements
// and comment the statement from 'if' till '{Serial.println("up");}'

int x,y,z;

void setup() {
  pinMode(A0,OUTPUT);
  pinMode(A4,OUTPUT);
  digitalWrite(A4,LOW);
  digitalWrite(A0,HIGH);
  Serial.begin(500000);
// Serial.println("Monitor started:");

}

void loop() {
 x=analogRead(A1);
 y=analogRead(A2);
 z=analogRead(A3);


if(x>400)
  {Serial.println("stop");}
else if(x<340)
{Serial.println("down");}
else if(y>400)
  {Serial.println("left");}
else if(y<340)
  {Serial.println("right");}
else
  {Serial.println("up");}

//Serial.print(x);
//Serial.print(" ");
//Serial.print(y);
//Serial.print(" ");
//Serial.println(z);
 delay(500);
}
