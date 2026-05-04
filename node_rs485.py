import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from manager_rs485 import Controller
import math


MAX_LINEAR_MS     = (3500/60)*2*math.pi*0.055
MAX_ANGULAR_RADS  = MAX_LINEAR_MS / (25/2)

class BLD515CDriver(Node):
   def __init__(self):
      super().__init__('bld515c_driver')

      self.bot = Controller()

      self.cmd_spd_sub = self.create_subscription(Twist, '/cmd_vel', self.move, 10)

   def move(self, msg: Twist):
      linear = msg.linear.x
      angular = msg.angular.z

      linear_norm  = linear  / MAX_LINEAR_MS
      angular_norm = angular / MAX_ANGULAR_RADS

      # Differential mixing in normalized space
      left_power  = linear_norm - angular_norm
      right_power = linear_norm + angular_norm

      # Clamp to -1/+1 in case combined values exceed range
      left_power  = max(-1.0, min(1.0, left_power))
      right_power = max(-1.0, min(1.0, right_power))
      self.bot.setPower(left_power, right_power)

def main(args=None):
    rclpy.init(args=args)
    node = BLD515CDriver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        self.bot.stop()  
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
