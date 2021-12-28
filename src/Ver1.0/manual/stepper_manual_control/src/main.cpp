#define L_STEP_PIN 2
#define L_DIR_PIN 3
#define R_STEP_PIN 4
#define R_DIR_PIN 5
#define L_EN_PIN 6
#define R_EN_PIN 7

#include <Arduino.h>
#include <AccelStepper.h>

AccelStepper stepper_l(AccelStepper::DRIVER, L_STEP_PIN, L_DIR_PIN);
AccelStepper stepper_r(AccelStepper::DRIVER, R_STEP_PIN, R_DIR_PIN);

int MaxSpeed = 8000;
int Accel = 8000;

void setup() {
    Serial.begin(9600);
    
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(L_STEP_PIN, OUTPUT);
    pinMode(L_DIR_PIN, OUTPUT);
    pinMode(R_STEP_PIN, OUTPUT);
    pinMode(R_DIR_PIN, OUTPUT);
    pinMode(L_EN_PIN, OUTPUT);
    pinMode(R_EN_PIN, OUTPUT);
    
    stepper_l.setMaxSpeed(MaxSpeed);
    stepper_l.setAcceleration(Accel);
    stepper_r.setMaxSpeed(MaxSpeed);
    stepper_r.setAcceleration(Accel);

    digitalWrite(LED_BUILTIN, LOW);
    digitalWrite(L_EN_PIN, LOW);
    digitalWrite(R_EN_PIN, LOW);
}

void loop() {
    stepper_l.run();
    stepper_r.run();
    if(Serial.available()){
        char tmp = Serial.read();
        if(tmp == 'w'){     // forward
            //Serial.println("forward");
            digitalWrite(LED_BUILTIN, HIGH);
            stepper_l.move(1000000000);
            stepper_r.move(-1000000000);
        }
        else if(tmp == 'x'){     // backward
            //Serial.println("backward");
            digitalWrite(LED_BUILTIN, HIGH);
            stepper_l.move(-1000000000);
            stepper_r.move(1000000000);
        }
        else if(tmp == 'a'){     // leftward
            //Serial.println("left");
            digitalWrite(LED_BUILTIN, HIGH);
            stepper_l.move(-1000000000);
            stepper_r.move(-1000000000);
        }
        else if(tmp == 'd'){     // rightward
            //Serial.println("right");
            digitalWrite(LED_BUILTIN, HIGH);
            stepper_l.move(1000000000);
            stepper_r.move(1000000000);
        }
        else if(tmp == 's'){
            //Serial.println("stop");
            digitalWrite(LED_BUILTIN, LOW);
            stepper_l.stop();
            stepper_r.stop();
        }
        else if(tmp == 'z'){
            MaxSpeed-=1000;
            stepper_l.setMaxSpeed(MaxSpeed);
            stepper_r.setMaxSpeed(MaxSpeed);
        }
        else if(tmp == 'c'){
            MaxSpeed+=1000;
            stepper_l.setMaxSpeed(MaxSpeed);
            stepper_r.setMaxSpeed(MaxSpeed);
        }
    }
}
