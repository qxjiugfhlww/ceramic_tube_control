# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *

# from gui import Ui_MainWindow

# import stapipy as st
#import cv2

# class Calibration(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)
#     def camera(self):
#         number_of_images_to_grab = 1
#         try:
#             # Initialize StApi before using.
#             st.initialize()

#             # Initialize converter
#             st_converter = st.create_converter(st.EStConverterType.PixelFormat)
#             st_converter.destination_pixel_format = \
#                 st.EStPixelFormatNamingConvention.BGR8

#             # Create a system object for device scan and connection.
#             st_system = st.create_system()

#             # Connect to first detected device.
#             st_device = st_system.create_first_device()

#             # Display DisplayName of the device.
#             print('Device=', st_device.info.display_name)

#             # Create a datastream object for handling image stream data.
#             st_datastream = st_device.create_datastream()

#             do_cycle = True
#             while do_cycle:
#                 # Start the image acquisition of the host (local machine) side.
#                 st_datastream.start_acquisition(number_of_images_to_grab)

#                 # Start the image acquisition of the camera side.
#                 st_device.acquisition_start()

#                 # A while loop for acquiring data and checking status
#                 while st_datastream.is_grabbing:
#                     # Create a localized variable st_buffer using 'with'
#                     # Warning: if st_buffer is in a global scope, st_buffer must be
#                     #          assign to None to allow Garbage Collector release the buffer
#                     #          properly.
#                     image_flag = 0
#                     with st_datastream.retrieve_buffer() as st_buffer:
#                         # Check if the acquired data contains image data.
#                         if st_buffer.info.is_image_present:
#                             # Create an image object.
#                             st_image = st_buffer.get_image()

#                             # Display the information of the acquired image data.
#                             print("BlockID={0} Size={1} x {2} First Byte={3}".format(
#                                 st_buffer.info.frame_id,
#                                 st_image.width, st_image.height,
#                                 st_image.get_image_data()[0]))

#                             # Convert image and get the NumPy array.
#                             st_image = st_converter.convert(st_image)
#                             data = st_image.get_image_data()
#                             nparr = np.frombuffer(data, np.uint8)
#                             nparr = nparr.reshape(st_image.height, st_image.width, 3)
#                             frame = nparr
#                             image_flag = 1                
#                         else:
#                             # If the acquired data contains no image data.
#                             print("Image data does not exist.")

#                     if image_flag == 1:
#                         #t = time.process_time()
#                         #cv2.imshow("out", frame)

#                         # rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                         # h, w, ch = rgbImage.shape
#                         # bytesPerLine = ch * w
#                         # convertToQtFormat = QImage(rgbImage.data, w, h, bytesPerLine, QImage.Format_RGB888)
#                         # p = convertToQtFormat.scaled(640, 480, Qt.KeepAspectRatio)
#                         # self.changePixmap.emit(p)


#                         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#                         image = qimage2ndarray.array2qimage(frame)
#                         self.ui.camera_frames.setPixmap(QPixmap.fromImage(image))


#                         #label = QLabel(self)
#                         #pixmap = QPixmap(frame)
#                         #self.ui.camera_frames.setPixmap(pixmap)
                        
#                         key = cv2.waitKey(500)
#                         if (key == 27):
#                             st_device.acquisition_stop()
#                             st_datastream.stop_acquisition()
#                             do_cycle = False

#                 # Stop the image acquisition of the camera side
#                 st_device.acquisition_stop()

#                 # Stop the image acquisition of the host side
#                 st_datastream.stop_acquisition()

#         except Exception as exception:
#             print(exception)