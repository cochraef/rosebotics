"""
  Capstone Project.  Code written by Evan Cochrane.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time
import bowmanj1


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()
    run_test_turn()


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


def run_test_turn():

    print('Test 1: Turning for 10 seconds at 50% power.')
    print()
    bowmanj1.turn(1, 100)

    print('Test 2: Turning for 4 seconds at 10% power.')
    print()
    bowmanj1.turn(4, 10)

    print('Test 3: Turning for 2 seconds at 100% power.')
    print()
    bowmanj1.turn(2, 50)


def spin_seconds(n, x):
    """ Causes the robot to spin for N seconds at duty cycle x. """
    robot = rb.Snatch3rRobot()

    robot.go(x, -x)

    start = time.time()
    while True:
        current = time.time()
        if current - start >= n:
            robot.stop(rb.StopAction.BRAKE.value)
            break


main()
