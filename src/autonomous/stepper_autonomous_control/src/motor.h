#define L_DIR 2
#define L_STEP 3
#define R_DIR 4
#define R_STEP 5

#define STEPPER__ACCEL 8000
#define STEPPER_MAX 8000

void stepper_init();
void stepper_go();
void stepper_back();
void stepper_left();
void stepper_right();
void stepper_stop();
void stepper_run();
void stepper_trace(int l, int r);