#include <ros/ros.h>
#include <std_msgs/String.h>
#include <sensor_msgs/JointState.h>
#include <string>

#define MATH_PI 				3.141592653589793238463
#define MATH_TRANS  			57.2958    
#define MATH_L1 				106.6
#define MATH_L2 				13.2
#define MATH_LOWER_ARM 			142.07
#define MATH_UPPER_ARM 			158.81	
#define MATH_UPPER_LOWER 		(MATH_UPPER_ARM / MATH_LOWER_ARM)

#define LOWER_ARM_MAX_ANGLE     135.6
#define LOWER_ARM_MIN_ANGLE     0
#define UPPER_ARM_MAX_ANGLE     100.7
#define UPPER_ARM_MIN_ANGLE     0
#define LOWER_UPPER_MAX_ANGLE   151
#define LOWER_UPPER_MIN_ANGLE   10

float passive_joint_angle[6] = {0.0};

void computePassiveJoints(float active_joint_angle[3])
{
	double alpha2 = 90 - active_joint_angle[1];
	double alpha3 = active_joint_angle[2] - 3.8;
	passive_joint_angle[0] = (alpha2 + alpha3) - 176.11 + 90;
	passive_joint_angle[1] = -90 + alpha2;
	passive_joint_angle[2] = active_joint_angle[1];
	passive_joint_angle[3] = 90 - (alpha2 + alpha3 + 3.8);
	passive_joint_angle[4] = 176.11 - 180 - alpha3;
	passive_joint_angle[5] = 48.39 + alpha3 - 44.55;
}

void jointStatesCallback(const sensor_msgs::JointState& msg)
{
	if(msg.position.size() == 4)
	{
		float active_joint_angle[3];
		active_joint_angle[0] = msg.position[0]/MATH_PI*180.f;
		active_joint_angle[1] = msg.position[1]/MATH_PI*180.f;
		active_joint_angle[2] = msg.position[2]/MATH_PI*180.f;
		computePassiveJoints(active_joint_angle);
	}
}

int main(int argc, char **argv)
{	
	ros::init(argc, argv, "swiftpro_rviz_node");
	ros::NodeHandle nh("~");
	
	ros::Subscriber sub = nh.subscribe("joint_states", 1, jointStatesCallback);
	ros::Publisher 	pub = nh.advertise<sensor_msgs::JointState>("joint_states", 1);
	sensor_msgs::JointState joint_state;
	ros::Rate loop_rate(100);

	std::string ns;
	nh.getParam("namespace", ns);
	
	while (ros::ok())
	{
		joint_state.header.stamp = ros::Time::now();
		joint_state.name.resize(6);
		joint_state.position.resize(6);
		joint_state.name[0] = ns + "/passive_joint1";
		joint_state.position[0] = passive_joint_angle[0] / 57.2958;
		joint_state.name[1] = ns + "/passive_joint2";
		joint_state.position[1] = passive_joint_angle[1] / 57.2958;
		joint_state.name[2] = ns + "/passive_joint3";
		joint_state.position[2] = passive_joint_angle[2] / 57.2958;
		joint_state.name[3] = ns + "/passive_joint5";
		joint_state.position[3] = passive_joint_angle[3] / 57.2958;
		joint_state.name[4] = ns + "/passive_joint7";
		joint_state.position[4] = passive_joint_angle[4] / 57.2958;
		joint_state.name[5] = ns + "/passive_joint8";
		joint_state.position[5] = passive_joint_angle[5] / 57.2958;	
		pub.publish(joint_state);
		
		ros::spinOnce();
		loop_rate.sleep();
	}		
	return 0;
}

