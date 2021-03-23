#!/usr/bin/env python3
# license removed for brevity

import rospy

# Brings in the SimpleActionClient
import actionlib
# Brings in the .action file and messages used by the move base action
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

def movebase_client(nav_x,nav_y,ang_z,ang_w):

   # Create an action client called "move_base" with action definition file "MoveBaseAction"
    client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
 
   # Waits until the action server has started up and started listening for goals.
    client.wait_for_server()

   # Creates a new goal with the MoveBaseGoal constructor
    goal = MoveBaseGoal()
    goal.target_pose.header.frame_id = "map"
    goal.target_pose.header.stamp = rospy.Time.now()
   # Move 0.5 meters forward along the x axis of the "map" coordinate frame 
    goal.target_pose.pose.position.x = nav_x
    goal.target_pose.pose.position.y = nav_y
   # No rotation of the mobile base frame w.r.t. map frame
    goal.target_pose.pose.orientation.z = ang_z
    goal.target_pose.pose.orientation.w = ang_w

   # Sends the goal to the action server.
    client.send_goal(goal)
   # Waits for the server to finish performing the action.
    wait = client.wait_for_result()
   # If the result doesn't arrive, assume the Server is not available
    if not wait:
        rospy.logerr("Action server not available!")
        rospy.signal_shutdown("Action server not available!")
    else:
    # Result of executing the action
        return client.get_result()   

def callback():
	print("oi")
# If the python node is executed as main process (sourced directly)
if __name__ == '__main__':
    try:
       # Initializes a rospy node to let the SimpleActionClient publish and subscribe
        rospy.init_node('movebase_client_py')
        nav_x = eval(input("Digite a posicao desejada no eixo X com formato 0.0: "))
        nav_y = eval(input("Digite a posicao desejada no eixo Y com formato 0.0: "))
        ang_z = eval(input("a orientação no eixo Z com formato 0.0: "))
        ang_w = eval(input("a orientação no eixo W com formato 0.0: "))
        rospy.Subscriber("next_goal", MoveBaseGoal, callback)
        result = movebase_client(nav_x,nav_y,ang_z, ang_w)
        if result:
            rospy.loginfo("Goal execution done!")
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation test finished.")

