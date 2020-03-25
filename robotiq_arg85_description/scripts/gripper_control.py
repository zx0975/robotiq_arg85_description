#!/usr/bin/env python
# encoding: utf-8   #要打中文時加這行
import rospy
import sys
import numpy as np
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
class Gripper:
    def __init__(self): 
        self.publisher_rate=100
        self.finger_joint1='/robotiq_arg85_description/r_finger_joint1_position_controller/command'
        self.finger_joint2='/robotiq_arg85_description/r_finger_joint2_position_controller/command'
        self.finger_joint3='/robotiq_arg85_description/r_finger_joint3_position_controller/command'
        self.finger_joint4='/robotiq_arg85_description/r_finger_joint4_position_controller/command'
        self.finger_joint5='/robotiq_arg85_description/r_finger_joint5_position_controller/command'
        self.finger_joint6='/robotiq_arg85_description/r_finger_joint6_position_controller/command'

        rospy.init_node('gripper_control',anonymous=False) #初始化node    anonymous=True  在node名稱後加入亂碼    避免相同名稱的node踢掉彼此
    
        
    # def command_convert(self):
    #     direction=float(sys.argv[1])
    #     return direction
    
        


    def get_gripper_state(self,joint):
        joint_now=rospy.wait_for_message('/robotiq_arg85_description/joint_states',JointState)
        bb=joint
        return joint_now.position[bb]

    def get_ratating_state(self):
        joint_now=rospy.wait_for_message('/robotiq_arg85_description/joint_states',JointState)
        return joint_now.position[6]

    def send_finger_direction(self,direction):
        pub1=rospy.Publisher(self.finger_joint1,Float64,queue_size=10)
        pub2=rospy.Publisher(self.finger_joint2,Float64,queue_size=10)
        pub3=rospy.Publisher(self.finger_joint3,Float64,queue_size=10)
        pub4=rospy.Publisher(self.finger_joint4,Float64,queue_size=10)
        pub5=rospy.Publisher(self.finger_joint5,Float64,queue_size=10)
        pub6=rospy.Publisher(self.finger_joint6,Float64,queue_size=10)

        #pub:publish名稱   chatter:topic name  queue_size=緩衝區大小
        rate=rospy.Rate(self.publisher_rate)

        if direction==1.0:
            rospy.loginfo('The gripper is opening')
            joint1_ang=self.get_gripper_state(0)
            joint2_ang=self.get_gripper_state(1)
            joint3_ang=self.get_gripper_state(2)
            joint4_ang=self.get_gripper_state(3)
            joint5_ang=self.get_gripper_state(4)
            joint6_ang=self.get_gripper_state(5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            while (joint1_ang>0):

                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)
                pub4.publish(joint4_ang)
                pub5.publish(joint5_ang)
                pub6.publish(joint6_ang)
                rospy.sleep(0.03)
                joint1_ang=joint1_ang-0.01
                joint2_ang=joint1_ang-0.01
                joint3_ang=joint1_ang-0.01
                joint4_ang=joint1_ang-0.01
                joint5_ang=joint1_ang-0.01
                joint6_ang=joint1_ang-0.01
            
        elif direction==2.0:
            rospy.loginfo('The gripper is closing')
            joint1_ang=self.get_gripper_state(0)
            joint2_ang=self.get_gripper_state(1)
            joint3_ang=self.get_gripper_state(2)
            joint4_ang=self.get_gripper_state(3)
            joint5_ang=self.get_gripper_state(4)
            joint6_ang=self.get_gripper_state(5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            
            while (joint1_ang<0.72):
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)
                pub4.publish(joint4_ang)
                pub5.publish(joint5_ang)
                pub6.publish(joint6_ang)
                rospy.sleep(0.03)
                joint1_ang=joint2_ang+0.01
                joint2_ang=joint2_ang+0.01
                joint3_ang=joint2_ang+0.01
                joint4_ang=joint2_ang+0.01
                joint5_ang=joint2_ang+0.01
                joint6_ang=joint2_ang+0.01
        

####################################################


    
if __name__ == "__main__":
    
    try:
        a = Gripper()
        rospy.loginfo('2342342342323423')
        a.send_finger_direction(1)
        a.send_finger_direction(2)
        # .send_finger_direction(1.0)
        rospy.loginfo('2342342342323423')
        #a.send_finger_direction(1.0)
        rospy.loginfo('2342342342323423')

        rospy.loginfo('123')
    except  rospy.ROSInterruptException:
        rospy.loginfo('end')
        pass


