#!/usr/bin/env python2.7

import rospy
import random
from Diptera_flybase_VSLAM import MavController as Move
from std_msgs.msg import String


class DipteraAutoFly:

    def __init__(self):
        rospy.init_node("Diptera_Auto_node")
        rospy.Subscriber("/Diptera/Obstacle", String, self.cb_obst_status)
        self.pitch_heading = 0.5
        self.roll_heading = 0
        self.altitude_heading = 0.8
        self.ccwyaw = pi_2
        self.cwyaw = -1 * pi_2
        self.angul_pitch = 0
        self.angul_roll = 0

    def cb_obst_status(self, msg):
        self.path_status = str(msg)

    def flybase(self):
        if self.path_status == "MOVE":
            self.random_goto("forward")
        elif self.path_status == "BLOCKED":
            self.random_goto("turn")
            rospy.sleep(1)

    def random_goto(self, decision):
        if decision == "forward":
            #self.goto_xyz_rpy(self.pitch_heading, self.roll_heading, self.altitude_heading, self.angul_pitch,self.angul_roll, 0)
            print(decision)
        elif decision == "turn":
            direction = []
            left_dir = -1 * pi_2
            right_dir = 1 * pi_2
            back_dir = -2 * pi_2

            direction[4] = ["forward", "left", "right", "back"]
            rand_choice = random.randint(0, 4)
            if direction[rand_choice] == "forward":
                #self.goto_xyz_rpy(0, 0.0, self.altitude_heading, 0, 0, forw_dir)
                print(direction[rand_choice])
            elif direction[rand_choice] == "left":
                #self.goto_xyz_rpy(0, 0.0, self.altitude_heading, 0, 0, left_dir)
                print(direction[rand_choice])
            elif direction[rand_choice] == "right":
                #self.goto_xyz_rpy(0, 0.0, self.altitude_heading, 0, 0, right_dir)
                print(direction[rand_choice])
            elif direction[rand_choice] == "back":
                #self.goto_xyz_rpy(0, 0.0, self.altitude_heading, 0, 0, back_dir)
                print(direction[rand_choice])
            rospy.sleep(2)

    def obst_status(self):
        rospy.spin()
        self.flybase()
        print(self.path_status)


if __name__ == '__main__':
    fly = DipteraAutoFly()
    fly.obst_status()
