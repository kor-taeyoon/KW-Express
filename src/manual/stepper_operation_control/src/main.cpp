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

    digitalWrite(X_ENABLE_PIN    , LOW);
    digitalWrite(Y_ENABLE_PIN    , HIGH);
    digitalWrite(Z_ENABLE_PIN    , HIGH);
    digitalWrite(E_ENABLE_PIN    , HIGH);
    digitalWrite(Q_ENABLE_PIN    , HIGH);

    digitalWrite(X_DIR_PIN    , LOW);
    digitalWrite(Y_DIR_PIN    , LOW);
    digitalWrite(Z_DIR_PIN    , LOW);
    digitalWrite(E_DIR_PIN    , LOW);
    digitalWrite(Q_DIR_PIN    , LOW);
}

void loop() {
    for(int i=0;i<200;i++){
        digitalWrite(X_STEP_PIN, HIGH);
        digitalWrite(X_STEP_PIN, LOW);
        delay(1);
    }
    delay(1000);
}