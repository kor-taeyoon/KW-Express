#include <Arduino.h>
#include <AccelStepper.h>

AccelStepper stepper_l(AccelStepper::DRIVER, 2, 3);
AccelStepper stepper_r(AccelStepper::DRIVER, 4, 5);

void setup() {
    Serial.begin(9600);
    
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    stepper_l.setMaxSpeed(8000);
    stepper_l.setAcceleration(2000);
    stepper_r.setMaxSpeed(8000);
    stepper_r.setAcceleration(2000);
}

void loop() {
    stepper_l.run();
    stepper_r.run();
    if(Serial.available()){
        char tmp = Serial.read();
        if(tmp == 'w'){     // forward
            Serial.println("forward");
            stepper_l.move(1000000000);
            stepper_r.move(-1000000000);
        }
        else if(tmp == 'x'){     // backward
            Serial.println("backward");
            stepper_l.move(-1000000000);
            stepper_r.move(1000000000);
        }
        else if(tmp == 'a'){     // leftward
            Serial.println("left");
            stepper_l.move(-1000000000);
            stepper_r.move(-1000000000);
        }
        else if(tmp == 'd'){     // rightward
            Serial.println("right");
            stepper_l.move(1000000000);
            stepper_r.moveTo(1000000000);
        }
        else if(tmp == 's'){
            Serial.println("stop");
            stepper_l.stop();
            stepper_r.stop();
        }
    }
}
