"""
  Capstone Project.  Code written by Jasmine Scott.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
import cochraef


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()
    #run_test_spin_seconds()
    #run_forward()


def run_test_go_stop():
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()

    robot.go(50, 25)
    time.sleep(2)
    robot.stop()

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)

    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())


def forward(x, seconds):
    """Robot goes forward for SECONDS with X duty cycle"""
    robot = rb.Snatch3rRobot
    robot.go(x, x)
    beginning = time.time()
    while True:
        ending = time.time()
        if ending - beginning >= seconds:
            robot.stop(rb.StopAction.BRAKE.value)

                       
def run_forward():
    forward(50, 7)


def run_test_spin_seconds():
    cochraef.spin_seconds(10, 50)



main()
