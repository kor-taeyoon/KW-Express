#define L_DIR 2
#define L_STEP 3
#define R_DIR 4
#define R_STEP 5

#define L_UV
#define R_UV
#define L_IR
#define R_IR

#define ULTRA_SONIC

#define STEPPER__ACCEL 8000
#define STEPPER_MAX 8000

#include <Arduino.h>
#include <AccelStepper.h>

AccelStepper stepper_l(AccelStepper::DRIVER, L_DIR, L_STEP);
AccelStepper stepper_r(AccelStepper::DRIVER, R_DIR, R_STEP);

void setup() {
    Serial.begin(9600);

    pinMode(L_DIR, OUTPUT);
    pinMode(L_STEP, OUTPUT);
    pinMode(R_DIR, OUTPUT);
    pinMode(R_STEP, OUTPUT);

    stepper_l.setMaxSpeed(STEPPER_MAX);
    stepper_l.setAcceleration(STEPPER__ACCEL);
    stepper_r.setMaxSpeed(STEPPER_MAX);
    stepper_r.setAcceleration(STEPPER__ACCEL);
}

void loop() {
    while(1){// 바코드로부터 신호 받을 때까지 대기.
        // 시리얼을 통해 바코드에 적힌 목표 주소가 어디인지 수신받으면 탈출
    }
    while(1){// 출발 버튼 눌릴 때까지 대기.
        // 버튼 눌리면 탈출
    }
    while(1){// 경비실 - 1층 현관    (UV 라인트레이싱)
        stepper_l.run();
        stepper_r.run();
        // 현관 유리에 가까워져 초음파센서 값이 상승하면 탈출
    }
    // 현관 문 열리는 신호 송신
    while(1){// 현관문 앞 대기
        // 초음파 센서 값이 확보되면 탈출
    }
    while(1){// 1층 현관 - 엘리베이터    (IR 라인트레이싱)
        stepper_l.run();
        stepper_r.run();
        // 초음파 센서 값이 상승하면 탈출
    }
    // 엘리베이터 호출 신호 발생
    while(1){// 엘리베이터 앞 대기
        // 초음파 센서 값이 확보되면 탈출
    }
    while(1){// 엘리베이터 진입
        stepper_l.run();
        stepper_r.run();
        // 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 180도 턴(내려야 하므로)
        // for loop로 직접 바퀴수 계산해서 돌리기
    }
    while(1){// 엘리베이터 문앞까지 접근
        stepper_l.run();
        stepper_r.run();
        // 직진하다가 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 엘리베이터 내릴 준비
        // 초음파 센서 값이 확보되면 탈출
    }
    while(1){// 엘리베이터 - 도착지    (IR 라인트레이싱)
        // 좌회전 우회전 구분 로직 포함, 현관문 앞까지 가기
        // 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 90도 회전

    }
    // ========================================
    // 도착 완료 !
    // ========================================
    while(1){// 짐 내려놓기

    }
    // ========================================
    // 귀가 시작 !
    // ========================================
    while(1){// 90도 회전

    }
    while(1){// 도착지 - 엘리베이터 (IR 라인트레이싱)
        stepper_l.run();
        stepper_r.run();
        // 초음파 센서 값이 확보되면 탈출
    }
    // 엘리베이터 호출 신호 발생
    while(1){// 엘리베이터 앞 대기
        // 초음파 센서 값이 확보되면 탈출
    }
    while(1){// 엘리베이터 진입
        stepper_l.run();
        stepper_r.run();
        // 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 180도 턴(내려야 하므로)
        // for loop로 직접 바퀴수 계산해서 돌리기
    }
    while(1){// 엘리베이터 문앞까지 접근
        stepper_l.run();
        stepper_r.run();
        // 직진하다가 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 엘리베이터 내릴 준비
        // 초음파 센서 값이 확보되면 탈출
    }
    while(1){// 엘리베이터 - 1층 현관    (IR 라인트레이싱)
        stepper_l.run();
        stepper_r.run();
        // 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 1층 현관 내릴 준비
        // 초음파 센서 값이 확보되면 탈출
    }
    while(1){// 1층 현관 - 경비실    (UV 라인트레이싱)
        stepper_l.run();
        stepper_r.run();
        // 초음파 센서 값이 상승하면 탈출
    }
    while(1){// 자세 정비
        // 180도 턴
    }
    // 끝났다고 알림 -> 비프음 등으로 알림 하고 루프 종료
}