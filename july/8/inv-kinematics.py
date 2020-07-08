# Attempt at 2D inverse kinematics with python 
from math import sin, cos, acos, sqrt, pi
import matplotlib.pyplot as plt

# JACOBIAN ALGO
# while e is too far away from g: 
#	compute the Jacobian matrix J 
#	compute the pseudoinverse of the Jacobian J+ 
# 	compute change in joint DOFs --> d-theta = J+ * d-e 
# 	apply the change in DOFs, move a small step of alpha * d-theta
# 				theta = theta + alpha * d-theta 
#

# CCD ALGO 
# start at end joint, and calculate angle from desired position to base of previous joint 
# and rotate the current joint to that desired angle. Do this for every joint, repeat
# a set number of times or when the desired position is close to the end effector 

# given number of joints, their lengths, and a target point in coordinate space,
# output the solution and plot it 

# challenge --> see if the joints can create a shape and animate the movement

# euclidean distance from 2 cartesian points
def eucldist(A, B): 
	return sqrt((abs(A[0] - B[0]))**2 + (abs(A[1] - B[1]))**2)

def norm(A): 
	return sqrt(A[0]**2 + A[1]**2)

def vecBetweenPoints(B,A):
	return [B[0] - A[0], B[1] - A[1]]

def dotProduct(A, B): 
	return (A[0] * B[0]) + (A[1] * B[1])

def angleBetweenVec(A, B):
	return (acos(dotProduct(A, B) / (norm(A) * norm(B))))

# New coords 𝑥′=𝑥 * cos(𝜃) − 𝑦 * sin(𝜃)
#            𝑦′=𝑥 * sin(𝜃) + 𝑦 & cos(𝜃)

# every joint has the same length, no DOF restrictions
# target point --> [1,2] = [x,y]
# assuming joints start in a straight line across x axis
def simpleCCD(num_joints, target_point, L, iterations):
	# starting end-first 
	joint_ends = [[L*i,0] for i in range(1, num_joints + 1)][::-1]

	ctr = 0
	while ctr < iterations and eucldist(joint_ends[0], target_point) > 1: 

		for i in range(len(joint_ends)):
			p_e = joint_ends[i]
			print("CURR JOINT END: %s" % (p_e))
			if i == len(joint_ends) - 1: 
				next_joint = [0,0]
			else: 
				next_joint = joint_ends[i + 1]
			print("NEXT JOINT END: %s" % (next_joint))
			p_c = vecBetweenPoints(p_e, next_joint)
			p_t = vecBetweenPoints(target_point, next_joint)
			theta = angleBetweenVec(p_c, p_t)
			print("ANGLE OF ROTATION: %s degrees" % (theta * 180/pi))
			# RECURSE DOWN BASE ON CURRENT POSITION IN ARRAY TO UPDATE POSITIONS OF HIGHER JOINTS
			x_prime = ((p_e[0] - next_joint[0] ) * cos(theta)) - ((p_e[1] - next_joint[1])* sin(theta)) 
			y_prime = ((p_e[0] - next_joint[0]) * sin(theta)) + ((p_e[1] - next_joint[1]) * cos(theta)) 
			joint_ends[i] = [next_joint[0] + x_prime, next_joint[1] + y_prime]

			if next_joint == [0,0]:
				joints_to_update = joint_ends[:-1]
			else: 
				joints_to_update = joint_ends[:i]

			for j in range(len(joints_to_update)):
				print("i: %s j: %s" % (i,j))
				joint = joints_to_update[j]
				print("UPDATED JOINT END: %s" % (p_e))
				print("JOINT TO ROTATE BY: %s" % (joint_ends[i]))
				x_prime = ((joint[0] - joint_ends[i][0] ) * cos(theta)) - ((joint[1] - joint_ends[i][1])* sin(theta)) 
				y_prime = ((joint[0] - joint_ends[i][0] ) * sin(theta)) - ((joint[1] - joint_ends[i][1])* cos(theta))
				joint_ends[j] = [x_prime, y_prime]
			# for 0th position, rotate based on 1st 
			# for 1st position and 0th, rotate based on 2nd 

			print("NEW JOINT POSITION: %s" % (joint_ends[i]))
			test_joint = joint_ends[::-1]
			xs = [sub[0] for sub in test_joint]
			ys = [sub[1] for sub in test_joint]
			xs.insert(0, 0)
			ys.insert(0,0)
			plt.scatter(xs,ys)
			plt.plot(xs,ys)
			plt.show()
		ctr += 1

	print(joint_ends)

# print(eucldist([2,4],[5,5]))
simpleCCD(3,[4,5], 2, 100)
