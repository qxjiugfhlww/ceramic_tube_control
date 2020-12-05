import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from mpl_toolkits.mplot3d import axis3d ,axes3d
import matplotlib.pyplot as plt


from matplotlib.path import Path
import matplotlib.patches as patches

import matplotlib
matplotlib.use('QT5Agg')

from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection


import matplotlib.pylab as plt

from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure



from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
import math
import random
from pyellipsoid import drawing

import vg

from numpy.polynomial.polynomial import polyfit

import pandas as pd

from scipy.interpolate import griddata

from itertools import chain 

from shapely.geometry.point import Point
from shapely.geometry import Polygon as sPolygon
from shapely import affinity
from matplotlib.patches import Polygon as mPolygon

from skimage.measure import EllipseModel
from matplotlib.patches import Ellipse, Circle

from copy import copy

import cv2
import numpy as np

#import stapipy as st

import qimage2ndarray

from gui import Ui_MainWindow

from control import Control


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.control = Control()


        self.ui.control_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.control_page))
        self.ui.calibration_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calibration_page))
        self.ui.settings_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.settings_page))

        self.ui.settings_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.settings_page))

        self.ui.connection_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.connection_page))
        self.ui.score_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.score_page))

        self.ui.control_btn.clicked.connect(self.control.plot1)
        
        #self.ui.calibration_btn.clicked.connect(self.camera)

        self.show()

        #self.showMaximized()







def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()