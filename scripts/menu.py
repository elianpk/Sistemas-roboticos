#!/usr/bin/env python3
import rospy
import goal_navigation
import os
import time
from textformat import welcome
import activate

poses = []

def menu():
	os.system("clear")
	print(welcome("ROS"))
	print("\nChoose service you want to use : ")
	print("""
	[C] - Chamar
	[V] - Volte 
	[I] - Inicial Pose
	[S] - Sair
	""")
	opt = str(input('Escolha uma opção: ')).upper()
	if opt == 'C':
		start()
	elif opt == 'V':
		back()
	elif opt == 'I':
		print("initial Pose")
	else:
		print('bye ;)')
		time.sleep(1)
		os.system("clear")
	

def start():
	rospy.init_node('movebase_client_py')
	print("Start")
	print(poses)
	activate.start(poses)
	#goal_navigation.movebase_client(nav_x,nav_y,ang_z,ang_w)
	

def back():
	rospy.init_node('movebase_client_py')
	print("Movendo...")
	goal_navigation.movebase_client(poses[0]['nav_x'], poses[0]['nav_y'], poses[0]['ang_z'], poses[0]['ang_w'])
	print("Chegou!")	
	
	
	

if __name__ == '__main__':
	poses.append({'nav_x':0.3, 'nav_y':0.0, 'ang_z':0.0, 'ang_w':0.1})
	poses.append({'nav_x':1.9, 'nav_y':-6.1, 'ang_z':-0.7, 'ang_w':0.7})
	poses.append({'nav_x':-1.8, 'nav_y':-4.8, 'ang_z':-0.9, 'ang_w':0.05})
	menu()


