#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
//#define X_MIN_PIN           3
//#define X_MAX_PIN           2
 
#define Y_STEP_PIN         60
#define Y_DIR_PIN          61
#define Y_ENABLE_PIN       56
//#define Y_MIN_PIN          14
//#define Y_MAX_PIN          15
 
#define Z_STEP_PIN         46
#define Z_DIR_PIN          48
#define Z_ENABLE_PIN       62
//#define Z_MIN_PIN          18
//#define Z_MAX_PIN          19

#define E_STEP_PIN         26
#define E_DIR_PIN          28
#define E_ENABLE_PIN       24
 
#define Q_STEP_PIN         36
#define Q_DIR_PIN          34
#define Q_ENABLE_PIN       30

#include <Arduino.h>
#include <AccelStepper.h>

AccelStepper stepper_g1(AccelStepper::DRIVER, X_STEP_PIN, X_DIR_PIN);
AccelStepper stepper_g2(AccelStepper::DRIVER, Y_STEP_PIN, Y_DIR_PIN);
AccelStepper stepper_g3(AccelStepper::DRIVER, Z_STEP_PIN, Z_DIR_PIN);
AccelStepper stepper_wl(AccelStepper::DRIVER, E_STEP_PIN, E_DIR_PIN);
AccelStepper stepper_wr(AccelStepper::DRIVER, Q_STEP_PIN, Q_DIR_PIN);

void setup() {
    pinMode(X_STEP_PIN  , OUTPUT);
    pinMode(X_DIR_PIN    , OUTPUT);
    pinMode(X_ENABLE_PIN    , OUTPUT);
    
    pinMode(Y_STEP_PIN  , OUTPUT);
    pinMode(Y_DIR_PIN    , OUTPUT);
    pinMode(Y_ENABLE_PIN    , OUTPUT);
    
    pinMode(Z_STEP_PIN  , OUTPUT);
    pinMode(Z_DIR_PIN    , OUTPUT);
    pinMode(Z_ENABLE_PIN    , OUTPUT);
    
    pinMode(E_STEP_PIN  , OUTPUT);
    pinMode(E_DIR_PIN    , OUTPUT);
    pinMode(E_ENABLE_PIN    , OUTPUT);
    
    pinMode(Q_STEP_PIN  , OUTPUT);
    pinMode(Q_DIR_PIN    , OUTPUT);
    pinMode(Q_ENABLE_PIN    , OUTPUT);


    digitalWrite(X_ENABLE_PIN    , HIGH);
    digitalWrite(Y_ENABLE_PIN    , HIGH);
    digitalWrite(Z_ENABLE_PIN    , HIGH);
    digitalWrite(E_ENABLE_PIN    , LOW);
    digitalWrite(Q_ENABLE_PIN    , LOW);

    //digitalWrite(X_DIR_PIN    , LOW);
    //digitalWrite(Y_DIR_PIN    , LOW);
    //digitalWrite(Z_DIR_PIN    , LOW);
    //digitalWrite(E_DIR_PIN    , LOW);
    //digitalWrite(Q_DIR_PIN    , LOW);

    Serial.begin(9600);

    stepper_g1.setMaxSpeed(2000);
    stepper_g1.setAcceleration(4000);
    stepper_g2.setMaxSpeed(2000);
    stepper_g2.setAcceleration(4000);
    stepper_g3.setMaxSpeed(2000);
    stepper_g3.setAcceleration(4000);
    
    stepper_wl.setMaxSpeed(1500);
    stepper_wl.setAcceleration(2000);
    stepper_wr.setMaxSpeed(1500);
    stepper_wr.setAcceleration(2000);
}

void loop() {
    stepper_g1.run();
    stepper_g2.run();
    stepper_g3.run();
    stepper_wl.run();
    stepper_wr.run();
    if(Serial.available()){
        char tmp = Serial.read();
        if(tmp == 't'){ // 1번 고리 복귀
            stepper_g1.moveTo(0);
        }
        if(tmp == 'g'){ // 1번 고리 낙하
            stepper_g1.moveTo(2400);
        }
        if(tmp == 'y'){ // 2번 고리 복귀
            stepper_g2.moveTo(0);
        }
        if(tmp == 'h'){ // 2번 고리 낙하
            stepper_g2.moveTo(2400);
        }
        if(tmp == 'u'){ // 3번 고리 복귀
            stepper_g3.moveTo(0);
        }
        if(tmp == 'j'){ // 3번 고리 낙하
            stepper_g3.moveTo(2400);
        }
        if(tmp == 'r'){ // 3번 고리 낙하
            stepper_wl.moveTo(9000);
            stepper_wr.moveTo(-9000);
        }
        if(tmp == 'f'){ // 3번 고리 낙하
            stepper_wl.moveTo(0);
            stepper_wr.moveTo(0);
        }
    }
}
