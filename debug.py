from random import random

from gui import Ui_MainWindow

class Control(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    # points (for laser line on tube) with xyz in millimeters
    def generate_3d_line_points(num_points = 10):
        points =[]
        for i in range(num_points):
            x = 100 + i * 100
            y = 200 + random()*10
            z = 50 + random()*10
            points.append([x, y, z])
        return points

    # generate data for one camera picture
    def generate_frame_data(angle_of_tube_rot):
        return {'angle_of_tube' : angle_of_tube_rot, 'points' : generate_3d_line_points()}

    # generate all laser points for one tube
    # [{'angle_of_tube' : 0, 'points' : [[x, y, z],...,[x, y, z]]}]
    def generate_laser_points():
        tube_data = []
        for deg in range(0,360,60):
            tube_data.append(generate_frame_data(deg))
        return tube_data





    