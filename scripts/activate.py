#!/usr/bin/env python3
import rospy
from smach import State,StateMachine
from time import sleep
import smach_ros
from std_msgs.msg import Float64
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from goal_navigation import movebase_client


poses = []

class A(State):
  def __init__(self, pose):
    State.__init__(self, outcomes=['1','0'], input_keys=['input'], output_keys=[''])
    self.pose = pose
  
  def execute(self, userdata):
    #pub
    print(self.pose)
    print("Estado1")
    movebase_client(self.pose['nav_x'], self.pose['nav_y'],self.pose['ang_z'],self.pose['ang_w'])
    #sleep(3)
    if userdata.input == 1:
      return '1'
    else:
      return '0'

class B(State):
  def __init__(self, pose):
    State.__init__(self, outcomes=['1','0'], input_keys=['input'], output_keys=[''])
    self.pose = pose

  def execute(self, userdata):
    print("Estado2")
    movebase_client(self.pose['nav_x'], self.pose['nav_y'],self.pose['ang_z'],self.pose['ang_w'])
    sleep(3)
    if userdata.input == 1:
      return '1'
    else:
      return '0'

class C(State):
  def __init__(self, pose):
    State.__init__(self, outcomes=['1','0'], input_keys=['input'], output_keys=[''])
    self.pose = pose

  def execute(self, userdata):
    print("Estado3")
    movebase_client(self.pose['nav_x'], self.pose['nav_y'],self.pose['ang_z'],self.pose['ang_w'])
    sleep(3)
    if userdata.input == 1:
      return '1'
    else:
      return '0'



def start(poses_received):
  #rospy.init_node('fsm_goal', anonymous=True)
  poses = poses_received
  sm = StateMachine(outcomes=['success'])
  sm.userdata.sm_input = 1
  with sm:
    StateMachine.add('A', A(poses[0]), transitions={'1':'B','0':'A'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('B', B(poses[1]), transitions={'1':'C','0':'B'}, remapping={'input':'sm_input','output':'input'})
    StateMachine.add('C', C(poses[2]), transitions={'1':'A','0':'C'}, remapping={'input':'sm_input','output':'input'})
  sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
  sis.start()

  sm.execute()
  rospy.spin()
  sis.stop()

