#include "motor.h"
#include <AccelStepper.h>

AccelStepper stepper_l(AccelStepper::DRIVER, L_DIR, L_STEP);
AccelStepper stepper_r(AccelStepper::DRIVER, R_DIR, R_STEP);

void stepper_init(){

    pinMode(L_DIR, OUTPUT);
    pinMode(L_STEP, OUTPUT);
    pinMode(R_DIR, OUTPUT);
    pinMode(R_STEP, OUTPUT);

    stepper_l.setMaxSpeed(STEPPER_MAX);
    stepper_l.setAcceleration(STEPPER__ACCEL);
    stepper_r.setMaxSpeed(STEPPER_MAX);
    stepper_r.setAcceleration(STEPPER__ACCEL);
}

void stepper_go(){
    stepper_l.move(1000000000);
    stepper_r.move(-1000000000);
}

void stepper_back(){
    stepper_l.move(-1000000000);
    stepper_r.move(1000000000);
}

void stepper_left(){
    stepper_l.move(-1000000000);
    stepper_r.move(-1000000000);
}

void stepper_right(){
    stepper_l.move(1000000000);
    stepper_r.moveTo(1000000000);
}

void stepper_stop(){
    stepper_l.stop();
    stepper_r.stop();
}

void stepper_run(){
    stepper_l.run();
    stepper_r.run();
}

void stepper_trace(int l, int r){
    // 둘다 없으면 직진
    // 오른쪽이 잡히면 우회전
    // 왼쪽이 잡히면 좌회전
    // 둘다 잡히면 정지
}