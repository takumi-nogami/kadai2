#include <ros.h>
#include <geometry_msgs/Twist.h>
#include <geometry_msgs/Point.h>
#include <std_msgs/Float32.h>
#include <std_msgs/Int32.h>
#include <AccelStepper.h>

#define EnablePin_R 12
#define StepPin_R 8
#define DirPin_R 7

#define EnablePin_L 6
#define StepPin_L 5
#define DirPin_L 4

ros::NodeHandle node;
//std_msgs::Point stepper_msg;
//ros::Publisher stepper("cmd_stepper", &stepper_msg);

AccelStepper stepperL(1, StepPin_L, DirPin_L);
AccelStepper stepperR(1, StepPin_R, DirPin_R);

void stepper_Callback(const geometry_msgs::Point &stepper){
  //step_linear_x = is_dis.linear.x / 0.275;
  //step_angular_z = 137 * is_dis.angular.z * 3.14 / 360 / 0.275;
     stepper_run_fb(stepper.x);
     stepper_run_turn(stepper.z); //CCW
} 


void stepper_zero(){
  stepperL.setCurrentPosition(0);
  stepperR.setCurrentPosition(0);
}
void stepper_set_fb(int x, int y, int z){
  stepperR.setMaxSpeed(x);
  stepperR.setAcceleration(y);
  stepperR.moveTo(z);
  stepperL.setMaxSpeed(x);
  stepperL.setAcceleration(y);
  stepperL.moveTo(-z);
}
void stepper_set_turn(int x, int y, int z){
  stepperR.setMaxSpeed(x);
  stepperR.setAcceleration(y);
  stepperR.moveTo(z);
  stepperL.setMaxSpeed(x);
  stepperL.setAcceleration(y);
  stepperL.moveTo(z);
}

void stepper_run_fb(float x){
  int step_x = x / 0.275;
  stepper_set_fb(1846, 3692, step_x);
  while( (stepperL.distanceToGo() != 0) && (stepperR.distanceToGo() != 0) ){
      stepperL.run();
      stepperR.run();
    }  
  stepper_zero();
  delay(1000);
}
void stepper_run_turn(float z){
  int step_angular_z = 137 * z * 3.14 / 360 / 0.275;
  stepper_set_turn(1200, 3692, step_angular_z);
  while( (stepperL.distanceToGo() != 0) && (stepperR.distanceToGo() != 0) ){
      stepperL.run();
      stepperR.run();
    }  
  stepper_zero();
  delay(1000);
}

ros::Subscriber<geometry_msgs::Point>stepper("cmd_stepper", &stepper_Callback);

void setup() { 
  pinMode(EnablePin_L,OUTPUT); // Enable
  pinMode(EnablePin_R,OUTPUT); // Enable
  
  pinMode(11,OUTPUT); 
  pinMode(10,OUTPUT);  //HowStep
  pinMode(9,OUTPUT);  
  
  digitalWrite(EnablePin_L,LOW); // Set Enable low　→　Low状態でEnable
  digitalWrite(EnablePin_R,LOW); // Set Enable low　→　Low状態でEnable
  
  digitalWrite(11,HIGH);
  digitalWrite(10,LOW); //FULLSTEP
  digitalWrite(9,LOW);

  node.initNode();
  node.subscribe(stepper);
}

void loop() {
  node.spinOnce();
  delay(1);
}

