from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import math
import random
import numpy as np
from matplotlib.patches import Polygon as mPolygon
from skimage.measure import EllipseModel
from shapely.geometry.point import Point
from shapely import affinity
from numpy.polynomial.polynomial import polyfit
import vg
from copy import copy
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon
import matplotlib.patches as patches
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas






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





from gui import Ui_MainWindow

#from ui_functions import *

class Control(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.control_btn.clicked.connect(self.plot1)

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
            x[i],y[i],z[i] = np.dot(self.rotation_matrix(axis, theta), [x[i],y[i],z[i]])
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
   
    def getXYZAngles(self, x1,y1,z1,x2,y2,z2,x3,y3,z3):  

        v1 = np.array([x2-x1,y2-y1,z2-z1])
        v2 = np.array([x3-x1,y3-y1,z3-z1])
        nv = np.cross(v1, v2)
        nn = nv/ np.linalg.norm(nv)
        angles = (np.arcsin(nn))
        return angles

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
                perp_x1, perp_y1, perp_x2, perp_y2 = self.getPerpendicular(x[index],y[index],x[index-1],y[index-1], 0.3)
                perp_x3, perp_z1, perp_x4, perp_z2 = self.getPerpendicular(x[index],z[index],x[index-1],z[index-1], 0.3)

            else:
                perp_x1, perp_y1, perp_x2, perp_y2 = self.getPerpendicular(x[index],y[index],x[index+1],y[index+1], 0.3)
                perp_x3, perp_z1, perp_x4, perp_z2 = self.getPerpendicular(x[index],z[index],x[index+1],z[index+1], 0.3)

            
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

            xyz_angles = self.getXYZAngles(perp_x3,y[index],perp_z1,x[index],y[index],z[index],perp_x1,perp_y1,z[index])
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

            e_x, e_y, e_z = self.rotate(e_x,e_y,e_z,1, 0, 0, theta)
            if (type == 'skelet'):
                #e_x_1d, e_y_1d, e_z_1d = rotate(e_x_1d, e_y_1d, e_z_1d,1, 0, 0, theta)
                ed_x, ed_y, ed_z = self.rotate(ed_x,ed_y,ed_z,1, 0, 0, theta)

            #if (type == 'skelet'):
            #    ax.plot3D([perp_x1,perp_x2,perp_x3,perp_x4], [perp_y1,perp_y2, y[index], y[index]], [z[index],z[index],perp_z1,perp_z2], 'blue')

            #ax.plot_surface(np.array([perp_x1,perp_x2,perp_x3,perp_x4]), np.array([perp_y1,perp_y2, y[index], y[index]]), np.array([z[index],z[index],perp_z1,perp_z2]), color='green')

            #if (type == 'skelet'):
            #    ax.scatter([perp_x3,x[index]], [y[index],y[index]], [perp_z1,z[index]],  c='cyan', marker='o')
            #angle1 = getAnlgeBetweenVectors(perp_x3, y[index], perp_z1, x[index], y[index], z[index])
            
            #angleBetweenPointsXZ = getAngleBetweenPointsXZ(x[index],z[index],x[index],z[index+1])
            theta = -xyz_angles[2] #gay #np.radians(19) #vg_angle_y #angleBetweenPointsXZ # + 90deg
            #print("y:", theta, theta*180/np.pi)
        
            e_x, e_y, e_z = self.rotate(e_x,e_y,e_z,0, 1, 0, theta)
            if (type == 'skelet'):
                e_x_1d, e_y_1d, e_z_1d = self.rotate(e_x_1d, e_y_1d, e_z_1d,0, 1, 0, theta)
                ed_x, ed_y, ed_z = self.rotate(ed_x,ed_y,ed_z,0, 1, 0, theta)

            #print("angle1:", angle1, angle1*180/np.pi)
            angleBetweenPointsXY = self.getAngleBetweenPointsXY(x[index],0,0,0)
            theta = xyz_angles[1]#gaz #np.radians(55) #vg_angle_z#angle1#angleBetweenPointsXY
            #print("z:", theta, theta*180/np.pi)
        
            e_x, e_y, e_z = self.rotate(e_x,e_y,e_z,0, 0, 1, theta)
            if (type == 'skelet'):
                e_x_1d, e_y_1d, e_z_1d = self.rotate(e_x_1d, e_y_1d, e_z_1d,0, 0, 1, theta)
                ed_x, ed_y, ed_z = self.rotate(ed_x,ed_y,ed_z,0, 0, 1, theta)

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

        ellipses_amount = 5 if self.ui.ellipses_amount.text() == '' else int(self.ui.ellipses_amount.text())
        print("ellipses_amount:", ellipses_amount)

        r = 0.5 if self.ui.radius_inp.text() == '' else float(self.ui.radius_inp.text())
        camera = [0, 1, 5]
        laser = [0, 5, 5]

        # точки лазера для подсчета уравнения его плоскости в XYZ
        reddots_calib = [[0,0,0],[0,0.5,0.5]] if self.ui.reddot1_inp.text() =='' else [list(map(float, self.ui.reddot1_inp.text().split(","))),  list(map(float, self.ui.reddot2_inp.text().split(",")))   ] #[[0,0,0],[0,0.5,0.5]]

        radiuses_amount = 10
        reddots = []
        radiuses = []
        angle_offsets = []

        tube_centers = []
        
        k1 = (reddots_calib[1][2]-reddots_calib[0][2])/(reddots_calib[1][1]-reddots_calib[0][1])
        y1 = reddots_calib[0][1]
        z1 = reddots_calib[0][2]

        def get_z_from_laser(ty):
            return (ty-y1)*k1+z1

        for i in range(ellipses_amount):
            angle_offsets.append([])
            reddots.append([])
            radiuses.append([])
            tube_bounds_y = [random.uniform(1.9,2.1),random.uniform(2.9,3.1)]
            tube_centers.append([])
            for j in range(radiuses_amount):
                tmp_y = random.uniform(0.4,0.6)              #(y-y1)*(z2-z1))/(y2-y1) + z1
                reddots[i].append([0, tmp_y, get_z_from_laser(tmp_y)])
                #0,np.abs(tube_bounds_y[1]-tube_bounds_y[0]), r
                tube_centers[i].append([0, np.abs(tube_bounds_y[1]-tube_bounds_y[0]), get_z_from_laser(np.abs(tube_bounds_y[1]-tube_bounds_y[0]))])

                #angle_offsets[i].append(np.arctan((reddots[i][j][1][2]-r)/(reddots[i][j][1][1]-tube_centers[i][1])))
                radiuses[i].append(np.sqrt((reddots[i][j][1]-tube_centers[i][j][1])**2+(tube_centers[i][j][2]-reddots[i][j][2])**2))
            
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

        points_x = []
        points_y = []
        points = []
        tmp_counter = 0
        for i in range(ellipses_amount):
            print(i)

            points_x = []
            points_y = []
            points = []

            for j in range(radiuses_amount):
                theta = j*(360/radiuses_amount)
                theta *= np.pi/180.0
                tmp_x = 0+np.cos(theta)*radiuses[i][j]
                tmp_y = 0-np.sin(theta)*radiuses[i][j]
                
                points_x.append(tmp_x)
                points_y.append(tmp_y)
                points.append([tmp_x, tmp_y])
            
            polygons_points.append([points_x,points_y])
            poligon_patch = mPolygon(np.array([points_x,points_y]).T, color = 'tab:red', alpha = 0.5)

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

        a, b = polyfit(x_centers_curve, y_centers_curve, 1)
        c, d = polyfit(y_centers_curve, z_centers_curve, 1)
        x_centers_straight = np.array([i for i in range(len(x_centers_curve))])
        y_centers_straight = a + b * x_centers_straight
        z_centers_straight = c+d*y_centers_straight


        tmp_counter=0
        for i in range(len(x_centers_curve)):
            print(i)
            c_e = self.createEllipse(x_centers_curve,y_centers_curve,z_centers_curve,0,radiuses_axes_ellipse[tmp_counter][0],radiuses_axes_ellipse[tmp_counter][0], int(i), type='skelet', color='tab:orange')
            if (c_e != None):
                curve_e_x.append(c_e[0]); curve_e_y.append(c_e[1]); curve_e_z.append(c_e[2])
            s_e = self.createEllipse(x_centers_straight,y_centers_straight,z_centers_straight,0,0.5,0.5, int(i), type='skelet', color='tab:blue')
            if (s_e != None):
                straight_e_x.append(s_e[0]); straight_e_y.append(s_e[1]); straight_e_z.append(s_e[2])

        self.figures = []
        self.axes = []
        self.frames = []
        self.horizontalLayouts = []

        curve_e_x = copy(curve_e_y)
        straight_e_x = copy(straight_e_y)

        def checkpoint( h, k, x, y, a, b): 
            # checking the equation of ellipse with the given point 
            p = ((x - h)**2 / a**2) + ((y - k)**2 / b**2) 
            return p 

        for i in reversed(range(self.ui.horizontalLayout_10.count())): 
            self.ui.horizontalLayout_10.itemAt(i).widget().setParent(None)

        for i in range(ellipses_amount):
            print(i)
            print(self.ui.scrollAreaWidgetContents.children())
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


            #ell_patch = Ellipse((xc, yc), 2*a, 2*b, theta*180/np.pi, edgecolor='red', facecolor='none')
            #axs[i][j].add_patch(ell_patch)

            poligon_patch = mPolygon(np.array(polygons_points[i]).T, color = 'red', alpha = 0.5)
            #self.axes[i].add_patch(poligon_patch)

            ellipse1 = create_ellipse((y_centers_curve[i], z_centers_curve[i]),(radiuses_axes_ellipse[i][0],radiuses_axes_ellipse[i][1]),angles_axes_ellipse[i])
            verts1 = np.array(ellipse1.exterior.coords.xy)
            patch1 = mPolygon(verts1.T, color = 'tab:orange', alpha = 0.5)
            self.axes[i].add_patch(patch1)
            #ell_patch = Ellipse((y_centers_curve[axs_count], z_centers_curve[axs_count]), 2*radiuses_axes_ellipse[axs_count][0], 2*radiuses_axes_ellipse[axs_count][1], angles_axes_ellipse[axs_count], color='tab:orange', alpha = 0.5)
            #axs1[i][j].add_patch(ell_patch)
            dist = math.hypot(y_centers_curve[i] - y_centers_straight[i], z_centers_curve[i] - z_centers_straight[i])
            print("расстояние между центрами: ", dist, end='')
            if (dist < r*0.1):
                print(" < 0.05")
            dist = 0
            for k in range(len(polygons_points[i][0])):
                dist = math.hypot(y_centers_straight[i] - polygons_points[i][0][k], z_centers_straight[i] - polygons_points[i][1][k])-r
                
                print(" расстояние от точки", k ,"до границы окружности (r=0.5): ", dist)


            verts1 = [[verts1[0][i], verts1[1][i]] for i in range(len(verts1[0]))]
            circle1 = create_ellipse((y_centers_straight[i], z_centers_straight[i]),(r,r),0)
            verts2 = np.array(circle1.exterior.coords.xy)
    
            patch2 = mPolygon(verts2.T, color = 'tab:blue', alpha = 0.5)
            #self.axes[i].add_patch(patch2)
            verts2 = [[verts2[0][j], verts2[1][j]] for j in range(len(verts2[0]))]


            upper_limit = r*1.1
            lower_limit = r*0.9

            

            patches1 = [
                Wedge((y_centers_straight[i], z_centers_straight[i]), r, 0, 360, width=upper_limit-lower_limit, facecolor = 'tab:blue')  # Full ring
            ]

            path = patches1[0].get_path()
            transform = patches1[0].get_transform()
            # Now apply the transform to the path
            newpath = transform.transform_path(path)
            # Now you can use this
            polygon = patches.PathPatch(newpath)
            patch2 = polygon

            #patch2 = mPolygon( patches[i].get_path(), color = 'tab:pink', alpha = 0.5)
            self.axes[i].add_patch(patch2)
            

            #p = PatchCollection(patches, alpha=0.4)

            #p.set_array(np.array("tab:blue"))


            #self.axes[i].add_collection(p)



            for j in range(radiuses_amount):
                circle3 = create_ellipse((tube_centers[i][j][1], tube_centers[i][j][2]),(0.1,0.1),0)
                verts3 = np.array(circle3.exterior.coords.xy)
                patch3 = mPolygon(verts3.T, facecolor = 'black', edgecolor = 'black', alpha = 0.5)
                self.axes[i].add_patch(patch3)

            circle3 = create_ellipse((y_centers_straight[i], z_centers_straight[i]),(lower_limit,lower_limit),0)
            verts3 = np.array(circle3.exterior.coords.xy)
            patch3 = mPolygon(verts3.T, facecolor = 'none', edgecolor = 'tab:green', alpha = 0.5)
            self.axes[i].add_patch(patch3)


            circle3 = create_ellipse((y_centers_straight[i], z_centers_straight[i]),(upper_limit,upper_limit),0)
            verts3 = np.array(circle3.exterior.coords.xy)
            patch3 = mPolygon(verts3.T, facecolor = 'none', edgecolor = 'tab:green', alpha = 0.5)
            self.axes[i].add_patch(patch3)


            verts3 = [[verts3[0][i], verts3[1][i]] for i in range(len(verts3[0]))]

            io_points = []
            for k in range(len(polygons_points[i][0])):
                #print("[", axs_count, k, "] ", end = '')
                if (checkpoint(y_centers_straight[i], z_centers_straight[i], polygons_points[i][0][k], polygons_points[i][1][k], upper_limit, upper_limit) > 1): 
                    print (0, end = '') 
                    io_points.append(0)
            
                elif (checkpoint(y_centers_straight[i], z_centers_straight[i], polygons_points[i][0][k], polygons_points[i][1][k], upper_limit, upper_limit) == 1): 
                    print (1, end = '') 
                    io_points.append(1)
                elif (checkpoint(y_centers_straight[i], z_centers_straight[i], polygons_points[i][0][k], polygons_points[i][1][k], upper_limit, upper_limit) < 1 and checkpoint(y_centers_straight[i], z_centers_straight[i], polygons_points[i][0][k], polygons_points[i][1][k], lower_limit, lower_limit) == 1): 
                    print (1, end = '') 
                    io_points.append(1)
            print()
            if (sum(io_points) == len(io_points)):
                print("в допуске")
            else:
                print("не в допуске")
            #circ_patch = Circle((y_centers_straight[axs_count], z_centers_straight[axs_count]), 0.5, color='tab:blue', alpha = 0.5)
            #axs1[i][j].add_patch(circ_patch)


        

            try:
                pass
                # coords_xy_1 = sPolygon(verts1)
                # coords_xy_2 = sPolygon(patches1[0].get_path().to_polygons()[0])
                # ##the intersect will be outlined in black
                # intersect = coords_xy_1.intersection(coords_xy_2)


                # #print("intersect", intersect, intersect == "POLYGON EMPTY", intersect.length)
                # if (intersect.length == 0.0):
                #     print(i, "нет пересечений")
                #     continue
                # else: 
                #     pass
                
                # verts3 = np.array(intersect.exterior.coords.xy)
                # patch3 = mPolygon(verts3.T, facecolor = 'none', edgecolor = 'black')
                # self.axes[i].add_patch(patch3)

                # ##compute areas and ratios 
                # print('площадь эллипса1:',coords_xy_1.area)
                # print('площадь эллипса2:',coords_xy_2.area)
                # print('площадь пересечения:',intersect.area)
                # print('пересечение/эллипс1:', intersect.area/coords_xy_1.area)
                # print('пересечение/эллипс2:', intersect.area/coords_xy_2.area)



                
            except:
                print("ошибка пересечений")

            self.plotWidget = FigureCanvas(self.figures[i])

            self.horizontalLayouts[i].addWidget(self.plotWidget)
            self.ui.horizontalLayout_10.addWidget(self.frames[i])
