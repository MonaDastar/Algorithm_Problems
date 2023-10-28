class Robot:
    """An imaginary robot that accepts commands for various actions.

    This class represents a simple robot capable of performing actions based on
    commands received as sequences of words and numbers. The robot can beep, rotate
    its neck, and control LEDs based on the provided commands.

    Attributes:
        leds (dict): A dictionary that maps LED identifiers to LED components for
            controlling the robot's LEDs.

    """
    def __init__(self):
        self.Leds={}
    
    def handle_command(self, message):
        """Handle a command message and execute the corresponding action.

        Args:
            message (list): A list representing a command message. The format of
                the message should be a sequence of words and numbers.

        Raises:
            InvalidCommand: If the provided command message does not match any
                known pattern, this exception is raised.

        Examples:
            Usage example:
            >>> robot = Robot()
            >>> robot.handle_command(['BEEPER', 440, 3])
            >>> robot.handle_command(['NECK', 90])
            >>> robot.handle_command(['LED', 1, 50])
            >>> robot.handle_command(['LED', 2, 255, 0, 0])

        """
        
        match message:
            case['BEEPER', frequency, times]:
                self.beep(frequency,times)
            case['NECK', angel]:
                self.rotate_neck(angel)
            case['LED', ident, intensity]:
                self.leds([ident].set_brightnes(ident, intensity))
            case['LED', ident, red, blue, green]:
                self.leds([ident].set_color(red, blue, green))
            
    def beep(self, frequency, times):
        pass
    
    def rotate_neck(self, angel):
        pass
    
class InvalidCommand(Exception):
    """Exception raised when an invalid command is received by the robot.

    This exception is raised when the `handle_command` method encounters a command
    message that does not match any known pattern.

    Attributes:
        message (list): The invalid command message that triggered the exception.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(f"invalid command : {message}")           
    
    
# usage:
robot = Robot()

try:
    robot.handle_command(['BEEPER',110,10])
    robot.handle_command(['LED',10,50,2])
    robot.handle_command(['LED',20])
    robot.handle_command(['NECK',45])
    robot.handle_command(['INVALID','command'])
    
    
except InvalidCommand as e:
    print(e)