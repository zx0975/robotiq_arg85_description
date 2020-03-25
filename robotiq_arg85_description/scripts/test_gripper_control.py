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
        self.r_finger_joint1='/robotiq_arg85_description/r_joint1_position_controller/command'
        self.r_finger_joint2='/robotiq_arg85_description/r_joint2_position_controller/command'
        self.r_finger_joint3='/robotiq_arg85_description/r_joint3_position_controller/command'
        self.r_finger_joint4='/robotiq_arg85_description/r_joint4_position_controller/command'
        self.r_finger_joint5='/robotiq_arg85_description/r_joint5_position_controller/command'
        self.r_finger_joint6='/robotiq_arg85_description/r_joint6_position_controller/command'

        self.l_finger_joint1='/robotiq_arg85_description/l_joint1_position_controller/command'
        self.l_finger_joint2='/robotiq_arg85_description/l_joint2_position_controller/command'
        self.l_finger_joint3='/robotiq_arg85_description/l_joint3_position_controller/command'
        self.l_finger_joint4='/robotiq_arg85_description/l_joint4_position_controller/command'
        self.l_finger_joint5='/robotiq_arg85_description/l_joint5_position_controller/command'
        self.l_finger_joint6='/robotiq_arg85_description/l_joint6_position_controller/command'

        rospy.init_node('gripper_control',anonymous=False) #初始化node    anonymous=True  在node名稱後加入亂碼    避免相同名稱的node踢掉彼此
    
    
    # def command_convert(self):
    #     direction=float(sys.argv[1])
    #     return direction

    def get_gripper_state(self,joint):
        joint_now=rospy.wait_for_message('/robotiq_arg85_description/joint_states',JointState)
        joint=joint
        return joint_now.position[joint]

    def get_ratating_state(self):
        joint_now=rospy.wait_for_message('/robotiq_arg85_description/joint_states',JointState)
        return joint_now.position[6]
###############################################
def send_finger_one(self,one,direction):
        if one=='r':
            joint1=self.r_finger_joint1
            joint2=self.r_finger_joint2
            joint3=self.r_finger_joint3
            joint4=self.r_finger_joint4
            joint5=self.r_finger_joint5
            joint6=self.r_finger_joint6
            feed_back=7
        elif one=='l':
            joint1=self.l_finger_joint1
            joint2=self.l_finger_joint2
            joint3=self.l_finger_joint3
            joint4=self.l_finger_joint4
            joint5=self.l_finger_joint5
            joint6=self.l_finger_joint6
            feed_back=0
        

        pub1=rospy.Publisher(joint1,Float64,queue_size=10)
        pub2=rospy.Publisher(joint2,Float64,queue_size=10)
        pub3=rospy.Publisher(joint3,Float64,queue_size=10)
        pub4=rospy.Publisher(joint4,Float64,queue_size=10)
        pub5=rospy.Publisher(joint5,Float64,queue_size=10)
        pub6=rospy.Publisher(joint6,Float64,queue_size=10)
        #pub:publish名稱   chatter:topic name  queue_size=緩衝區大小
        rate=rospy.Rate(self.publisher_rate)

        # direction=self.command_convert()

        if direction==1.0:
            rospy.loginfo('The gripper is closing')
            joint1_ang=self.get_gripper_state(feed_back)
            joint2_ang=self.get_gripper_state(feed_back+1)
            joint3_ang=self.get_gripper_state(feed_back+2)
            joint4_ang=self.get_gripper_state(feed_back+3)
            joint5_ang=self.get_gripper_state(feed_back+4)
            joint6_ang=self.get_gripper_state(feed_back+5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            while joint1_ang>-1.221:

                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)
                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)
                rospy.sleep(0.01)
                joint1_ang=joint1_ang-0.01
                joint3_ang=joint3_ang+0.01
            while joint2_ang>-1.57:
                pub2.publish(joint2_ang)
                rospy.sleep(0.01)
                joint2_ang=joint2_ang-0.01
        elif direction==2.0:
            rospy.loginfo('The gripper is opening')
            joint1_ang=self.get_gripper_state(feed_back)
            joint2_ang=self.get_gripper_state(feed_back+1)
            joint3_ang=self.get_gripper_state(feed_back+2)
            joint4_ang=self.get_gripper_state(feed_back+3)
            joint5_ang=self.get_gripper_state(feed_back+4)
            joint6_ang=self.get_gripper_state(feed_back+5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            
            while joint2_ang<0:
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)
                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)
                rospy.sleep(0.01)
                joint2_ang=joint2_ang+0.01
            while joint1_ang<0:
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)
                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)
                rospy.sleep(0.01)
                joint1_ang=joint1_ang+0.01
                joint3_ang=joint3_ang-0.01
###################################################
def send_finger_all(self,direction):
        pub1=rospy.Publisher(self.r_finger_joint,Float64,queue_size=10)
        pub2=rospy.Publisher(self.r_left_inner_knuckle_joint,Float64,queue_size=10)
        pub3=rospy.Publisher(self.r_left_inner_finger_joint,Float64,queue_size=10)
        pub4=rospy.Publisher(self.r_right_inner_knuckle_joint,queue_size=10)
        pub5=rospy.Publisher(self.r_right_inner_finger_joint,Float64,queue_size=10)
        pub6=rospy.Publisher(self.r_right_outer_knuckle_joint,Float64,queue_size=10)

        pub7=rospy.Publisher(self.l_finger_joint,Float64,queue_size=10)
        pub8=rospy.Publisher(self.l_left_inner_knuckle_joint,Float64,queue_size=10)
        pub9=rospy.Publisher(self.l_left_inner_finger_joint,Float64,queue_size=10)
        pub10=rospy.Publisher(self.l_right_inner_knuckle_joint,Float64,queue_size=10)
        pub11=rospy.Publisher(self.l_right_inner_finger_joint,Float64,queue_size=10)
        pub12=rospy.Publisher(self.l_right_outer_knuckle_joint,Float64,queue_size=10)
        #pub:publish名稱   chatter:topic name  queue_size=緩衝區大小
        rate=rospy.Rate(self.publisher_rate)

        if direction==1.0:
            rospy.loginfo('The gripper is closing')
            joint1_ang=self.get_gripper_state(0)
            joint2_ang=self.get_gripper_state(1)
            joint3_ang=self.get_gripper_state(2)
            joint4_ang=self.get_gripper_state(3)
            joint5_ang=self.get_gripper_state(4)
            joint6_ang=self.get_gripper_state(5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            while joint1_ang>-1.221:

                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)

                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)

                pub7.publish(joint1_ang)
                pub8.publish(joint2_ang)
                pub9.publish(joint3_ang)

                rospy.sleep(0.01)
                joint1_ang=joint1_ang-0.01
                joint3_ang=joint3_ang+0.01
            while joint2_ang>-1.57:
                pub2.publish(joint2_ang)

                pub5.publish(joint2_ang)

                pub8.publish(joint2_ang)

                rospy.sleep(0.01)
                joint2_ang=joint2_ang-0.01
        elif direction==2.0:
            rospy.loginfo('The gripper is opening')
            joint1_ang=self.get_gripper_state(0)
            joint2_ang=self.get_gripper_state(1)
            joint3_ang=self.get_gripper_state(2)
            joint4_ang=self.get_gripper_state(3)
            joint5_ang=self.get_gripper_state(4)
            joint6_ang=self.get_gripper_state(5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            
            while joint2_ang<0:
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)

                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)

                pub7.publish(joint1_ang)
                pub8.publish(joint2_ang)
                pub9.publish(joint3_ang)
                
                rospy.sleep(0.01)
                joint2_ang=joint2_ang+0.01
            while joint1_ang<0:
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)

                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)

                pub7.publish(joint1_ang)
                pub8.publish(joint2_ang)
                pub9.publish(joint3_ang)

                rospy.sleep(0.01)
                joint1_ang=joint1_ang+0.01
                joint3_ang=joint3_ang-0.01
#######################################################2finger
    def send_finger_two(self,direction):
        pub1=rospy.Publisher(self.r_finger_joint,Float64,queue_size=10)
        pub2=rospy.Publisher(self.r_left_inner_knuckle_joint,Float64,queue_size=10)
        pub3=rospy.Publisher(self.r_left_inner_finger_joint,Float64,queue_size=10)
        pub4=rospy.Publisher(self.r_right_inner_knuckle_joint,queue_size=10)
        pub5=rospy.Publisher(self.r_right_inner_finger_joint,Float64,queue_size=10)
        pub6=rospy.Publisher(self.r_right_outer_knuckle_joint,Float64,queue_size=10)

        pub7=rospy.Publisher(self.l_finger_joint,Float64,queue_size=10)
        pub8=rospy.Publisher(self.l_left_inner_knuckle_joint,Float64,queue_size=10)
        pub9=rospy.Publisher(self.l_left_inner_finger_joint,Float64,queue_size=10)
        pub10=rospy.Publisher(self.l_right_inner_knuckle_joint,Float64,queue_size=10)
        pub11=rospy.Publisher(self.l_right_inner_finger_joint,Float64,queue_size=10)
        pub12=rospy.Publisher(self.l_right_outer_knuckle_joint,Float64,queue_size=10)

        #pub:publish名稱   chatter:topic name  queue_size=緩衝區大小
        rate=rospy.Rate(self.publisher_rate)

        if direction==1.0:
            rospy.loginfo('The gripper is closing')
            joint1_ang=self.get_gripper_state(0)
            joint2_ang=self.get_gripper_state(1)
            joint3_ang=self.get_gripper_state(2)
            joint4_ang=self.get_gripper_state(3)
            joint5_ang=self.get_gripper_state(4)
            joint6_ang=self.get_gripper_state(5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            while joint1_ang>-1.221:

                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)

                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)

                rospy.sleep(0.01)
                joint1_ang=joint1_ang-0.01
                joint3_ang=joint3_ang+0.01
            while joint2_ang>-1.57:
                pub2.publish(joint2_ang)

                pub5.publish(joint2_ang)

                rospy.sleep(0.01)
                joint2_ang=joint2_ang-0.01
        elif direction==2.0:
            rospy.loginfo('The gripper is opening')
            joint1_ang=self.get_gripper_state(0)
            joint2_ang=self.get_gripper_state(1)
            joint3_ang=self.get_gripper_state(2)
            joint4_ang=self.get_gripper_state(3)
            joint5_ang=self.get_gripper_state(4)
            joint6_ang=self.get_gripper_state(5)
            rospy.loginfo('Joint angle now = [ %.2f %.2f %.2f %.2f %.2f %.2f]' ,joint1_ang,joint2_ang,joint3_ang,joint4_ang,joint5_ang,joint6_ang)
            
            while joint2_ang<0:
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)

                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)

                rospy.sleep(0.01)
                joint2_ang=joint2_ang+0.01
            while joint1_ang<0:
                pub1.publish(joint1_ang)
                pub2.publish(joint2_ang)
                pub3.publish(joint3_ang)

                pub4.publish(joint1_ang)
                pub5.publish(joint2_ang)
                pub6.publish(joint3_ang)

                rospy.sleep(0.01)
                joint1_ang=joint1_ang+0.01
                joint3_ang=joint3_ang-0.01

if __name__=='__main__':
    try:
        a=Gripper()
        #a.send_finger_one('r',1)
        #a.send_finger_one('r',2)
        #a.send_finger_one('m',1)
        #a.send_finger_one('m',2)
        a.send_rotating_command(0)
        a.send_finger_all(1)
        a.send_finger_all(2)
        a.send_rotating_command(1.57)
        a.send_finger_one('m',1)
        a.send_finger_two(1)
        a.send_finger_two(2)
        a.send_finger_one('m',2)
        a.send_rotating_command(0)
        #a.send_rotating_command(1)
        rospy.loginfo('123')
    except  rospy.ROSInterruptException:
        rospy.loginfo('end')
        pass