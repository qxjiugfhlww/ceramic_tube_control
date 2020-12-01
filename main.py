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

from gui import Ui_MainWindow
#from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.fig, self.ax = plt.subplots(1,5)

        # verts = [
        #     (0., 0.),  # left, bottom
        #     (0., 1.),  # left, top
        #     (1., 1.),  # right, top
        #     (1., 0.),  # right, bottom
        #     (0., 0.),  # ignored
        #     ]

        # codes = [
        #     Path.MOVETO,
        #     Path.LINETO,
        #     Path.LINETO,
        #     Path.LINETO,
        #     Path.CLOSEPOLY,
        # ]

        # path = Path(verts, codes)

        # patch = patches.PathPatch(path, facecolor='orange', lw=2)

        # self.ax[0].add_patch(patch)
        
        # self.plotWidget = FigureCanvas(self.fig)
        # self.ui.scrollAreaWidgetContents.addWidget(self.plotWidget)





        

        def plot1(self): 
            curve_e_x =  []
            curve_e_y= []
            curve_e_z = []
            straight_e_x = [] 
            straight_e_y = []
            straight_e_z = []
            straight_line_angles= []

            x_centers_curve = []
            y_centers_curve = []
            z_centers_curve = []

            x_centers_straight = []
            y_centers_straight = []
            z_centers_straight = []

            ellipses_amount = 5
            print("ellipses_amount:", ellipses_amount)
            # for i in np.linspace(1,len(x),ellipses_amount):
            #     if (i == len(x)-1):
            #         break
            #     x_centers_straight.append(line_x[int(i-1)]); y_centers_straight.append(line_y[int(i-1)]); z_centers_straight.append(line_z[int(i-1)])
            #     x_centers_curve.append(x[int(i-1)]); y_centers_curve.append(y[int(i-1)]); z_centers_curve.append(z[int(i-1)])
                    
            
            self.figures = []
            self.axes = []

            self.frames = []
            self.horizontalLayouts = []



            radiuses_amount = 10
            radiuses = [[random.uniform(0.4,0.6) for i in range(radiuses_amount)] for j in range(ellipses_amount) ]
            
            radiuses_axes_ellipse = []
            angles_axes_ellipse = []
            xcy1 = []
            xcy2 = []
            polygons_points = []

            def create_ellipse(center, lengths, angle=0):
                circ = Point(center).buffer(1)
                ell = affinity.scale(circ, (lengths[0]), (lengths[1]))
                ellr = affinity.rotate(ell, np.degrees(angle))
                return ellr

            tmp_counter = 0
            for i in range(ellipses_amount):
                print(i)
                self.figures.append(0)
                self.axes.append(0)
                self.figures[i], self.axes[i] = plt.subplots(1,1)

                self.frames.append(QFrame(self.ui.scrollAreaWidgetContents))
                self.frames[i].setMinimumSize(QSize(200, 200))
                self.frames[i].setFrameShape(QFrame.StyledPanel)
                self.frames[i].setFrameShadow(QFrame.Raised)
                self.horizontalLayouts.append(QHBoxLayout(self.frames[i]))
                

                self.axes[i].set_xlim(-2, 2)
                self.axes[i].set_ylim(-2, 2)

                points_x = []
                points_y = []
                points = []
                for l in range(radiuses_amount):
                    theta = l*(360/radiuses_amount)
                    theta *= np.pi/180.0
                    #tmp_x = y_centers_curve[axis_count]+np.cos(theta)*radiuses[axis_count][l]
                    #tmp_y = z_centers_curve[axis_count]-np.sin(theta)*radiuses[axis_count][l]
                    tmp_x = 0+np.cos(theta)*radiuses[i][l]
                    tmp_y = 0-np.sin(theta)*radiuses[i][l]
                    
                    points_x.append(tmp_x)
                    points_y.append(tmp_y)
                    points.append([tmp_x, tmp_y])
                
                #ell_patch = Ellipse((xc, yc), 2*a, 2*b, theta*180/np.pi, edgecolor='red', facecolor='none')
                #axs[i][j].add_patch(ell_patch)

                polygons_points.append([points_x,points_y])
                poligon_patch = mPolygon(np.array([points_x,points_y]).T, color = 'tab:red', alpha = 0.5)
                self.axes[i].add_patch(poligon_patch)

                ellipse_model = EllipseModel()
                ellipse_model.estimate(np.array(points))
                xc, yc, a, b, theta = ellipse_model.params
                z_centers_curve.append(xc)
                y_centers_curve.append(yc)
                x_centers_curve.append(tmp_counter)
                tmp_counter += 1
                radiuses_axes_ellipse.append([a, b])
                angles_axes_ellipse.append(theta)
                print("center = ",  (xc, yc))
                print("angle of rotation = ",  theta)
                print("axes = ", (a,b))
            
                ellipse1 = create_ellipse((y_centers_curve[i], z_centers_curve[i]),(a,b),theta)
                verts1 = np.array(ellipse1.exterior.coords.xy)
                patch1 = mPolygon(verts1.T, color = 'orange', alpha = 0.5)
                self.axes[i].add_patch(patch1)
                
                #ellipse_patch = Ellipse((xc, yc), 2*a, 2*b, 0, edgecolor='tab:orange', facecolor='none')
                #axs[i][j].add_patch(ellipse_patch)

                self.plotWidget = FigureCanvas(self.figures[i])

                self.horizontalLayouts[i].addWidget(self.plotWidget)
                self.ui.horizontalLayout_10.addWidget(self.frames[i])


        plot1(self)

        
        #self.ui.canvas.compute(self)

        #self.ui.Btn_Toggle.clicked.connect(lambda: UIFunctions.toggleMenu(self, 250, True))

        self.ui.control_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.control_page))
        self.ui.calibration_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.calibration_page))
        self.ui.settings_btn.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentWidget(self.ui.settings_page))


        def Plot(self):
            f=self.FileN
            index = int(self.lineEdit.text())
            x= []
            y=[]
            with open(f, newline = '') as csv_file:
                my_file = csv.reader(csv_file, delimiter = ',',
                                    quotechar = '|')
                for row in my_file:
                    x.append(str(row[0]))
                    y.append(str(row[index]))
            self.sc.plot(x, y)



        def normalize(self, coord):
            return Coord(
                coord.x/coord.length(),
                coord.y/coord.length()
                )

        def perpendicular(self, coord):
            # Shifts the angle by pi/2 and calculate the coordinates
            # using the original vector length
            return Coord(
                coord.length()*math.cos(coord.angle()+math.pi/2),
                coord.length()*math.sin(coord.angle()+math.pi/2)
                )

        def rotation_matrix(self, axis, theta):
            """
            Return the rotation matrix associated with counterclockwise rotation about
            the given axis by theta radians.
            """
            axis = np.asarray(axis)
            axis = axis / math.sqrt(np.dot(axis, axis))
            a = math.cos(theta / 2.0)
            b, c, d = -axis * math.sin(theta / 2.0)
            aa, bb, cc, dd = a * a, b * b, c * c, d * d
            bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
            return np.array([[aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                            [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                            [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc]])

        def rotate(self, x,y,z,axis_x, axis_y, axis_z, theta):
            axis = [axis_x, axis_y, axis_z]
            theta = theta
            for i in range(len(x)):
                x[i],y[i],z[i] = np.dot(rotation_matrix(axis, theta), [x[i],y[i],z[i]])
            return x,y,z

        def getAngleBetweenPointsXY(self, x1,y1,x2,y2):
            return np.arctan2(y2-y1, x2-x1)

        def getAngleBetweenPointsXZ(self, x1,z1,x2,z2):
            return np.arctan2(z2-z1, x2-x1)

        def getAngleBetweenPointsYZ(self, y1,z1,y2,z2):
            return np.arctan2(z2-z1, y2-y1)

        def getPerpendicular(self, x1,y1,x2,y2, length):
            dx = x1-x2
            dy = y1-y2
            dist = math.sqrt(dx*dx + dy*dy)
            dx /= dist
            dy /= dist
            x3 = x1 + (length)*dy
            y3 = y1 - (length)*dx
            x4 = x1 - (length)*dy
            y4 = y1 + (length)*dx
            return x3,y3,x4,y4

        def getAngleBetweenLines(self, x1, y1, z1, x2, y2, z2, x3, y3, z3):                 
            # Find direction ratio of line AB 
            ABx = x1 - x2; 
            ABy = y1 - y2; 
            ABz = z1 - z2; 
        
            # Find direction ratio of line BC 
            BCx = x3 - x2; 
            BCy = y3 - y2; 
            BCz = z3 - z2; 
            # Find the dotProduct 
            # of lines AB & BC 
            dotProduct = (ABx * BCx + ABy * BCy + ABz * BCz); 
        
            # Find magnitude of 
            # line AB and BC 
            magnitudeAB = (ABx * ABx + ABy * ABy + ABz * ABz); 
            magnitudeBC = (BCx * BCx + BCy * BCy + BCz * BCz); 
            # Find the cosine of 
            # the angle formed 
            # by line AB and BC 
            angle = dotProduct; 
            angle /= math.sqrt(magnitudeAB * magnitudeBC); 
        
            # Find angle in radian 
            angle = (angle * 180) / 3.14; 
            # Print angle 
            return angle


        def getAnlgeBetweenVectors(self, x1, y1, z1, x2, y2, z2,x3,y3,z3,x4,y4,z4):

            vec1 = findVec([x1,y1,z1],[x2,y2,z2])
            vec2 = findVec([x3,y3,z3],[x4,y4,z4])   
            return np.arccos(np.dot(vec1 / np.linalg.norm(vec1), vec2 / np.linalg.norm(vec2)))
            #return np.arccos( (x1*x2 + y1*y2 + z1*z2) / np.sqrt( (x1*x1 + y1*y1 + z1*z1)*(x2*x2+y2*y2+z2*z2) ) )

        def getPlaneNormal(self, x1,y1,z1,x2,y2,z2,x3,y3,z3):
            v1 = [x2-x1,y2-y1,z2-z1]
            v2 = [x3-x1,y3-y1,z3-z1]
            x = 1*v1[1]*v1[2]+1*v1[2]*v2[1]
            y = 1*v1[2]*v2[0]+1*v1[0]*v2[2]
            z = 1*v1[1]*v2[0]+1*v1[0]*v2[1]
            return [x,y,z]

        def getAngle(self, x1,y1,z1,x2,y2,z2,x3,y3,z3, x4=None,y4=None,z4=None,x5=None,y5=None,z5=None,x6=None,y6=None,z6=None, ex=None, ey=None, ez=None):  

            v1 = [x2-x1,y2-y1,z2-z1]
            v2 = [x3-x1,y3-y1,z3-z1]


            if (x4 != None):
                v3 = [x5-x4,y5-y4,z5-z4]
                v4 = [x6-x4,y6-y4,z6-z4]


            nv1 = np.cross(np.array(v1), np.array(v2))
            if (x4 != None):
                nv2 = np.cross(np.array(v3), np.array(v4))
            else:
                nv2 = [ex,ey,ez]
            
            d = ( nv1[0] * nv2[0] + nv1[1] * nv2[1] + nv1[2] * nv2[2] ) 
            e1 = math.sqrt( nv1[0] * nv1[0] + nv1[1] * nv1[1] + nv1[2] * nv1[2]) 
            e2 = math.sqrt( nv2[0] * nv2[0] + nv2[1] * nv2[1] + nv2[2] * nv2[2]) 
            d = d / (e1 * e2) 
            A = math.acos(d)
            return A

        def getXYZAngles(self, x1,y1,z1,x2,y2,z2,x3,y3,z3):  

            v1 = np.array([x2-x1,y2-y1,z2-z1])
            v2 = np.array([x3-x1,y3-y1,z3-z1])
            nv = np.cross(v1, v2)
            nn = nv/ np.linalg.norm(nv)
            angles = (np.arcsin(nn))
            return angles

        def vrange(self, stops):
            """Create concatenated ranges of integers for multiple [1]/stop

            Parameters:
                starts (1-D array_like): starts for each range
                stops (1-D array_like): stops for each range (same shape as starts)

            Returns:
                numpy.ndarray: concatenated ranges
            """
            starts = np.array([1] * len(stops))
            stops = np.asarray(stops) + 1
            L_p = stops - starts
            return np.array(np.split(np.repeat(stops - L_p.cumsum(), L_p) + np.arange(L_p.sum()), np.cumsum(stops - 1)[:-1]))

        def get_points_v(self, x_v, y_v, z_v, d=None, n_p= None):
                "DESEMPACAR ARRAY DE WKT"
                x_v, y_v, z_v = np.asarray(x_v), np.asarray(y_v), np.asarray(z_v)

                "DISTANCIAS ENTRE X(n) - X(n-1), Y(n) - Y(n-1)"
                Lx, Ly = np.array(x_v[1:] - x_v[:-1]), np.array(y_v[1:] - y_v[:-1])

                "EXCLUIR LINEAS DE LONGITUD MENOR A LA DISTANCIA 'd'"
                if d and np.sum(np.asarray(((x_v[1:] - x_v[:-1]) ** 2 + (y_v[1:] - y_v[:-1]) ** 2) ** 0.5)) < d:
                    print(np.sum(Lx), np.sum(Ly))
                    pass
                else:
                    "NUMERO DE PUNTOS ENTRE VERTICES"
                    if n_p is None:
                        nx, ny = np.array(np.around(np.abs(Lx / d), decimals=0)), np.array(np.around(np.abs(Ly / d), decimals=0))
                        nx, ny = np.where(nx <= 0, 1, nx).astype(np.int), np.where(ny <= 0, 1, ny).astype(np.int)
                        n_points = np.maximum(nx, ny)
                    else:
                        n_points = np.array([1] * len(Lx)) * np.array(n_p)

                    "LONGUITUD DE SEGMENTOS ENTRE PUNTOS"
                    x_space, y_space = Lx / (n_points + 1), Ly / (n_points + 1)

                    "CREAR 2D ARRAY DE VALORES INICIALES"
                    x_init, y_init = np.array(np.split(np.repeat(x_v[:-1], n_points), np.cumsum(n_points)[:-1])), np.array(np.split(np.repeat(y_v[:-1], n_points), np.cumsum(n_points)[:-1]))

                    "CREAR RANGO DE NUMERO DE SEGMENTOS (n_points)"
                    range_n = vrange(n_points)

                    "CALCULO DE PUNTOS INTERMEDIOS ENTRE SEGMENTOS DE X_V y Y_v"
                    if n_p is None:
                        points_x, points_y = x_init + (range_n * x_space).T, y_init + (range_n * y_space).T
                    else:
                        points_x, points_y = x_init + (range_n * x_space[:, None]), y_init + (range_n * y_space[:,None])

                    "GENERAR ARRAY DE VALORES z_v"
                    points_z = np.split(np.repeat(np.array([z_v[0]] * len(points_x)), n_points), np.cumsum(n_points)[:-1])

                    return points_x, points_y, points_z

        def lin(self, z):
            x = (z - c_xz)/m_xz
            y = (z - c_yz)/m_yz
            return x,y

        def rotateX(self, y,z,cy,cz, radians):
            for i in range(len(y)):
                _y      = y[i] - cy
                _z      = z[i] - cz
                d      = math.hypot(_y, _z)
                theta  = math.atan2(_y, _z) + radians
                z[i] = cz + d * math.cos(theta)
                y[i] = cy + d * math.sin(theta)
            return y,z

        def rotateY(self, x,z,cx,cz, radians):
            for i in range(len(x)):
                _x      = x[i] - cx
                _z      = z[i] - cz
                d      = math.hypot(_x, _z)
                theta  = math.atan2(_x, _z) + radians
                z[i] = cz + d * math.cos(theta)
                x[i] = cx + d * math.sin(theta)
            return x,z

        def rotateZ(self, x,y, cx,cy, radians):   
            for i in range(len(x)):
                _x      = x[i] - cx
                _y      = y[i] - cy
                d      = math.hypot(_x, _y)
                theta  = math.atan2(_x, _y) + radians
                #y_r[i] = cy + d * math.cos(theta)
                #x_r[i] = cx + d * math.sin(theta)
                x[i] = cy + d * math.sin(theta)
                y[i] = cx + d * math.cos(theta)
            return x,y

        def createEllipse(self, x,y,z,rx,ry,rz, index, x_prev=None, y_prev=None, z_prev=None, type=None, color=None):
            index = int(index)
            #if (index == len(x)-1):
            #    return
            u = v = None
            e_x = []
            e_y = [] 
            e_z = []
            e_x_1d = []
            e_y_1d = [] 
            e_z_1d = []
            e_x_ret = None
            e_y_ret = None
            e_z_ret = None
            if (type == 'skelet'):

                u=0     #x-position of the center
                v=0    #y-position of the center
                a=ry     #radius on the x-axis
                b=rz    #radius on the y-axis

                t = np.linspace(0, 2*np.pi, 100)
                e_x = [0 for i in np.linspace(0, 2*np.pi, 100)]
                e_y = u+a*np.cos(t)
                e_z = v+b*np.sin(t)

                # e_x_ret = e_x+x[index]
                # e_y_ret = e_y+y[index]
                # #e_y_ret = e_y
                # e_z_ret = e_z+z[index]

                e_x = np.array([[e_x[i], e_x[i+1]] for i in range(len(e_x)-1)])
                e_y = np.array([[e_y[i], e_y[i+1]] for i in range(len(e_y)-1)])
                e_z = np.array([[e_z[i], e_z[i+1]] for i in range(len(e_z)-1)])

                '''
                xyz = {'x': e_x, 'y': e_y, 'z': e_z}
                # put the data into a pandas DataFrame (this is what my data looks like)
                df = pd.DataFrame(xyz, index=range(len(xyz['x']))) 

                # re-create the 2D-arrays
                y1 = np.linspace(df['y'].min(), df['y'].max(), len(df['y'].unique()))
                z1 = np.linspace(df['z'].min(), df['z'].max(), len(df['z'].unique()))
                y2, z2 = np.meshgrid(y1, z1)
                x2 = griddata((df['x'], df['y']), df['z'], (y2, z2), method='cubic')
                '''
                
                u = np.linspace(0.0, 2 * np.pi, 10)
                v = np.linspace(0.0, np.pi, 10)
                ed_x = rx * np.outer(np.cos(u), np.sin(v))
                ed_y = ry * np.outer(np.sin(u), np.sin(v))
                ed_z = rz * np.outer(np.ones_like(u), np.cos(v))
                



                #e_x, e_y, e_z = rotate(e_x,e_y,e_z,0, 1, 0, np.pi/2)
                #ax.plot_surface(e_x_ret, e_y_ret, e_z_ret,alpha=0.3, color=color)

            elif (type == 'model'):
                # u = np.linspace(0.0, 2 * np.pi, 100)
                # v = np.linspace(0.0, np.pi, 100)
                # e_x = rx * np.outer(np.cos(u), np.sin(v))
                # e_y = ry * np.outer(np.sin(u), np.sin(v))
                # e_z = rz * np.outer(np.ones_like(u), np.cos(v))

                u=0     #x-position of the center
                v=0    #y-position of the center
                a=ry     #radius on the x-axis
                b=rz    #radius on the y-axis

                t = np.linspace(0, 2*np.pi, 100)
                e_x = [0 for i in np.linspace(0, 2*np.pi, 100)]
                e_y = u+a*np.cos(t)
                e_z = v+b*np.sin(t)

                e_x = np.array([[e_x[i], e_x[i+1]] for i in range(len(e_x)-1)])
                e_y = np.array([[e_y[i], e_y[i+1]] for i in range(len(e_y)-1)])
                e_z = np.array([[e_z[i], e_z[i+1]] for i in range(len(e_z)-1)])

            if (index == len(x)-1):
                perp_x1, perp_y1, perp_x2, perp_y2 = getPerpendicular(x[index],y[index],x[index-1],y[index-1], 0.3)
                perp_x3, perp_z1, perp_x4, perp_z2 = getPerpendicular(x[index],z[index],x[index-1],z[index-1], 0.3)

            else:
                perp_x1, perp_y1, perp_x2, perp_y2 = getPerpendicular(x[index],y[index],x[index+1],y[index+1], 0.3)
                perp_x3, perp_z1, perp_x4, perp_z2 = getPerpendicular(x[index],z[index],x[index+1],z[index+1], 0.3)

            
            # gax = getAngle(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index], ex=1, ey=0,ez=0)
            # print("getAngle x:", gax)
            # gay = getAngle(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index], ex=0, ey=1,ez=0)
            # print("getAngle y:", gay)
            # gaz = getAngle(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index], ex=0, ey=0,ez=1)
            # print("getAngle z:", gaz)

            '''
            gax = getAngle(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index],    center_plane1_x[0][0],center_plane1_y[0][0],center_plane1_z[0][0],center_plane1_x[0][1],center_plane1_y[0][1],center_plane1_z[0][1],center_plane1_x[1][0],center_plane1_y[1][0],center_plane1_z[1][0])
            #print("getAngle x:", gax)
            gay = getAngle(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index],    center_plane2_x[0][0],center_plane2_y[0][0],center_plane2_z[0][0],center_plane2_x[0][1],center_plane2_y[0][1],center_plane2_z[0][1],center_plane2_x[1][0],center_plane2_y[1][0],center_plane2_z[1][0])
            #print("getAngle y:", gay)
            gaz = getAngle(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index],    center_plane3_x[0][0],center_plane3_y[0][0],center_plane3_z[0][0],center_plane3_x[0][1],center_plane3_y[0][1],center_plane3_z[0][1],center_plane3_x[1][0],center_plane3_y[1][0],center_plane3_z[1][0])
            #print("getAngle z:", gaz)
            '''
            
            #if (type == 'skelet'):
                #ax.scatter([perp_x3,perp_x1,perp_x2,perp_x4], [y[index],perp_y1,perp_y2,y[index]], [perp_z1,z[index],z[index],perp_z2],  c='cyan', marker='o')
            vg_angle_x = vg.angle(np.array([perp_x3,y[index], perp_z1]), np.array([x[index],y[index],z[index]]), look=vg.basis.x)/180*np.pi
            vg_angle_y = vg.angle(np.array([perp_x3,y[index], perp_z1]), np.array([x[index],y[index],z[index]]), look=vg.basis.y)/180*np.pi
            vg_angle_z = vg.angle(np.array([perp_x3,y[index], perp_z1]), np.array([x[index],y[index],z[index]]), look=vg.basis.z)/180*np.pi


            if (type == 'skelet'):
                pass
                #ax2.plot_surface(e_x_ret, e_y_ret, e_z_ret,alpha=0.3, color=color)

            xyz_angles = getXYZAngles(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index])
            #print("xyz_angles:", np.degrees(xyz_angles))

            # vg_angle_x = vg.angle(np.array([perp_x1,perp_y1, z[index]]), np.array([x[index],y[index],z[index]]), look=vg.basis.x)/180*np.pi
            # vg_angle_y = vg.angle(np.array([perp_x1,perp_y1, z[index]]), np.array([x[index],y[index],z[index]]), look=vg.basis.y)/180*np.pi
            # vg_angle_z = vg.angle(np.array([perp_x1,perp_y1, z[index]]), np.array([x[index],y[index],z[index]]), look=vg.basis.z)/180*np.pi
            #plot_arc3d([perp_x1,perp_y1, z[index]], [x[index],y[index],z[index]], radius=0.2, fig=ax, colour='C0')

            #print("vg.angle x", vg_angle_x, vg_angle_x*180/np.pi)
            #print("vg.angle y", vg_angle_y, vg_angle_y*180/np.pi)
            #print("vg.angle z", vg_angle_z, vg_angle_z*180/np.pi)

            x_ = np.array([[perp_x3,perp_x1 ], [perp_x2, perp_x4]])
            y_ = np.array([[y[index], perp_y1], [perp_y2, y[index]]])
            z_ = np.array([[perp_z1, z[index]], [z[index], perp_z2]])

            #ax.plot3D([perp_x1,perp_x2,perp_x3,perp_x4], [perp_y1,perp_y2, y[index], y[index]], [z[index],z[index],perp_z1,perp_z2], 'blue')

            #if (type == 'skelet'):
            #    ax.plot_surface(x_, y_, z_,alpha=0.5, color='cyan')

            #angle1 = getAngleBetweenLines(perp_x3, y[index], perp_z1, x[index], y[index], z[index],x[index+1], y[index+1],z[index+1])

            #if (type == 'skelet'):
            #    ax.plot3D([perp_x3, x[index],x[index+1]], [y[index],y[index],y[index+1]], [perp_z1,z[index],z[index+1]], 'mo-')
            #print("aaaangle1",angle1)

            #angleBetweenPointsYZ = getAngleBetweenPointsYZ(y[index],z[index],y[index+1],z[index+1])
            theta = -xyz_angles[0] #gax #np.radians(17) #vg_angle_x #angle1+np.pi/2#angleBetweenPointsYZ #+1.5708
            #print("x:", theta, theta*180/np.pi)

            e_x, e_y, e_z = rotate(e_x,e_y,e_z,1, 0, 0, theta)
            if (type == 'skelet'):
                #e_x_1d, e_y_1d, e_z_1d = rotate(e_x_1d, e_y_1d, e_z_1d,1, 0, 0, theta)
                ed_x, ed_y, ed_z = rotate(ed_x,ed_y,ed_z,1, 0, 0, theta)

            #if (type == 'skelet'):
            #    ax.plot3D([perp_x1,perp_x2,perp_x3,perp_x4], [perp_y1,perp_y2, y[index], y[index]], [z[index],z[index],perp_z1,perp_z2], 'blue')

            #ax.plot_surface(np.array([perp_x1,perp_x2,perp_x3,perp_x4]), np.array([perp_y1,perp_y2, y[index], y[index]]), np.array([z[index],z[index],perp_z1,perp_z2]), color='green')

            #if (type == 'skelet'):
            #    ax.scatter([perp_x3,x[index]], [y[index],y[index]], [perp_z1,z[index]],  c='cyan', marker='o')
            #angle1 = getAnlgeBetweenVectors(perp_x3, y[index], perp_z1, x[index], y[index], z[index])
            
            #angleBetweenPointsXZ = getAngleBetweenPointsXZ(x[index],z[index],x[index],z[index+1])
            theta = -xyz_angles[2] #gay #np.radians(19) #vg_angle_y #angleBetweenPointsXZ # + 90deg
            #print("y:", theta, theta*180/np.pi)
        
            e_x, e_y, e_z = rotate(e_x,e_y,e_z,0, 1, 0, theta)
            if (type == 'skelet'):
                e_x_1d, e_y_1d, e_z_1d = rotate(e_x_1d, e_y_1d, e_z_1d,0, 1, 0, theta)
                ed_x, ed_y, ed_z = rotate(ed_x,ed_y,ed_z,0, 1, 0, theta)

            #print("angle1:", angle1, angle1*180/np.pi)
            angleBetweenPointsXY = getAngleBetweenPointsXY(x[index],0,0,0)
            theta = xyz_angles[1]#gaz #np.radians(55) #vg_angle_z#angle1#angleBetweenPointsXY
            #print("z:", theta, theta*180/np.pi)
        
            e_x, e_y, e_z = rotate(e_x,e_y,e_z,0, 0, 1, theta)
            if (type == 'skelet'):
                e_x_1d, e_y_1d, e_z_1d = rotate(e_x_1d, e_y_1d, e_z_1d,0, 0, 1, theta)
                ed_x, ed_y, ed_z = rotate(ed_x,ed_y,ed_z,0, 0, 1, theta)

            #ax.plot_wireframe(e_x+x[index], e_y+y[index], e_z+z[index],  rstride=2, cstride=2, color='black', alpha=0.1)

            if (type == 'skelet'):

                # e_x_1d = np.reshape(e_x_1d, (len(e_x_1d)//2, len(e_y_1d)//2))
                # e_y_1d = np.reshape(e_y_1d, (len(e_x_1d)//2, len(e_y_1d)//2))
                # e_z_1d = np.reshape(e_z_1d, (len(e_x_1d)//2, len(e_y_1d)//2))
                #ax.plot_surface(e_x+x[index], e_y+y[index], e_z+z[index],alpha=0.3, color=color)   
                print("index", index) 
                #ax.plot_surface(ed_x+x[index], ed_y+y[index], ed_z+z[index],alpha=0.3, color=color)    
            elif (type == 'model'):
                pass
                #ax1.plot_wireframe(e_x+x[index], e_y+y[index], e_z+z[index],  rstride=20, cstride=20, color=color, alpha=0.8)
            #print("ret", ret)
            return e_x+x[index], e_y+y[index], e_z+z[index], x[index], y[index], z[index]

        def getAngle_BetweenLineAxisXYZ(self, x,y,z):
            deltaY = line_y[0] - line_y[len(line_y)-1]
            deltaX = line_x[0] - line_x[len(line_x)-1]
            deltaZ = line_z[0] - line_z[len(line_z)-1]
            angleX = math.atan(deltaY / deltaZ)
            angleY = math.atan(deltaX / deltaZ)
            angleZ = math.atan(deltaX / deltaY)
            return angleX, angleY, angleZ

        def compute(self):
            self.curve_e_x =  []
            self.curve_e_y= []
            self.curve_e_z = []
            self.straight_e_x = [] 
            self.straight_e_y = []
            self.straight_e_z = []
            self.straight_line_angles= []

            self.x_centers_curve = []
            self.y_centers_curve = []
            self.z_centers_curve = []

            self.x_centers_straight = []
            self.y_centers_straight = []
            self.z_centers_straight = []

            self.ellipses_amount = 5
            print("ellipses_amount:", self.ellipses_amount)

          
            self.radiuses_amount = 10
            self.radiuses = [[random.uniform(0.4,0.6) for i in range(self.radiuses_amount)] for j in range(self.ellipses_amount) ]
            
            self.axis_count = 0
            self.radiuses_axes_ellipse = []
            self.angles_axes_ellipse = []
            self.xcy1 = []
            self.xcy2 = []
            self.polygons_points = []

            def create_ellipse(center, lengths, angle=0):
                circ = Point(center).buffer(1)
                ell = affinity.scale(circ, (lengths[0]), (lengths[1]))
                ellr = affinity.rotate(ell, np.degrees(angle))
                return ellr

            self.tmp_counter = 0
            for i in range(len(self.axs)):
                for j in range(len(self.axs[i])):
                    if (self.axis_count+1 > self.ellipses_amount):
                        break
                    self.axs[i][j].set_xlim(-2, 2)
                    self.axs[i][j].set_ylim(-2, 2)

                    self.points_x = []
                    self.points_y = []
                    self.points = []
                    for l in range(self.radiuses_amount):
                        self.theta = l*(360/self.radiuses_amount)
                        self.theta *= np.pi/180.0
                        #tmp_x = y_centers_curve[axis_count]+np.cos(theta)*radiuses[axis_count][l]
                        #tmp_y = z_centers_curve[axis_count]-np.sin(theta)*radiuses[axis_count][l]
                        self.tmp_x = 0+np.cos(self.theta)*self.radiuses[self.axis_count][l]
                        self.tmp_y = 0-np.sin(self.theta)*self.radiuses[self.axis_count][l]
                        
                        self.points_x.append(self.tmp_x)
                        self.points_y.append(self.tmp_y)
                        self.points.append([self.tmp_x, self.tmp_y])
                    
                    #ell_patch = Ellipse((xc, yc), 2*a, 2*b, theta*180/np.pi, edgecolor='red', facecolor='none')
                    #axs[i][j].add_patch(ell_patch)

                    self.polygons_points.append([self.points_x,self.points_y])
                    self.poligon_patch = mPolygon(np.array([self.points_x,self.points_y]).T, color = 'tab:red', alpha = 0.5)
                    self.axs[i][j].add_patch(self.poligon_patch)

                    self.ellipse_model = EllipseModel()
                    self.ellipse_model.estimate(np.array(self.points))
                    self.xc, self.yc, self.a, self.b, self.theta = self.ellipse_model.params
                    self.z_centers_curve.append(self.xc)
                    self.y_centers_curve.append(self.yc)
                    self.x_centers_curve.append(self.tmp_counter)
                    self.tmp_counter += 1
                    self.radiuses_axes_ellipse.append([self.a, self.b])
                    self.angles_axes_ellipse.append(self.theta)
                    print("center = ",  (self.xc, self.yc))
                    print("angle of rotation = ",  self.theta)
                    print("axes = ", (self.a,self.b))
                
                    self.ellipse1 = create_ellipse((self.y_centers_curve[self.axis_count], self.z_centers_curve[self.axis_count]),(self.a,self.b),self.theta)
                    self.verts1 = np.array(self.ellipse1.exterior.coords.xy)
                    self.patch1 = mPolygon(self.verts1.T, color = 'orange', alpha = 0.5)
                    self.axs[i][j].add_patch(self.patch1)
                    
                    #ellipse_patch = Ellipse((xc, yc), 2*a, 2*b, 0, edgecolor='tab:orange', facecolor='none')
                    #axs[i][j].add_patch(ellipse_patch)
                    self.axis_count += 1



        #compute(self)

        self.show()



class myCanvas(FigureCanvas):

    def __init__(self):
        self.fig = Figure()
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)

    def plot2(self, xarray, yarray, zarray, za):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection = '3d')

        self.ax.mouse_init(rotate_btn = 1, zoom_btn = 3)

        self.ax.plot_trisurf(xarray, yarray, za, color = 'red', alpha = 0.6, edgecolor = 'red', linewidth = 0.1,
                             antialiased = True, shade = 1)

        self.ax.plot(xarray, yarray, zarray, 'ok')
        self.ax.set_xlabel('X ')
        self.ax.set_ylabel('Y ')
        self.ax.set_zlabel('Z ')
        
        self.draw()

    def plot1(self, xarray, yarray, zarray):
        self.fig.clear()
        self.ax = self.fig.add_subplot(111, projection = '3d')
        self.ax.mouse_init(rotate_btn = 1, zoom_btn = 3)
        self.ax.plot(xarray, yarray, zarray, 'ok')
        self.ax.set_xlabel('X ')
        self.ax.set_ylabel('Y ')
        self.ax.set_zlabel('Z ')
        self.draw()

    def plot2D(self, xarray, zarray):
        self.fig.clear()
        self.axe = self.fig.add_subplot(111)
        self.axe.plot(xarray, zarray, 'ok')
        self.axe.set_xlabel('X ')
        self.axe.set_ylabel('Y ')
        self.draw()

    def plot2DM(self, xarray, zarray, za):
        self.fig.clear()
        self.axe = self.fig.add_subplot(111)
        self.axe.plot(xarray, zarray, "ok")
        self.axe.plot(xarray, za, 'r-')
        self.axe.set_xlabel('X ')
        self.axe.set_ylabel('Y ')
        self.draw()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()