
import pandas as pd
import keyboard


from PyQt5.QtWidgets import *

from PyQt5.uic import loadUiType

from xlrd import *

from PyQt5 import QtGui

from PyQt5.QtWidgets import QApplication ,  QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout



from keras.models import load_model
from preprocessor import makesquare
from preprocessor import resize_pixel
index = 100

import cv2
import numpy as np
import math

def load_images_from_folder(folder):
    """Searches each images in a specified directory"""
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images



Main_ui, _ = loadUiType('Arabic.ui')


class Main(QMainWindow, Main_ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.center()
        self.tabWidget.setCurrentIndex(2)
        #self.setWindowFlags(
          #QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.FramelessWindowHint)
        self.Handel_UI_Changes()
        self.exit_button.clicked.connect(self.quitApplication)
        self.index_ta=0
        self.Handel_Buttons()
        self.j=30
        countes =0

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())

    def Handel_Buttons(self):
        self.Show_image_pb.clicked.connect(self.Show_image)
        self.Show_resalt_pb.clicked.connect(self.Show_resalt)
        self.pushButton_path_image.clicked.connect(self.choos)
        self.tasting_system_pb.clicked.connect(self.Testing_system)
        self.pushButton_chack_any_student.clicked.connect(self.save)
        self.pushButton_19.clicked.connect(self.save_any_staudent)
        self.pushButton_chack_all_image.clicked.connect(self.save_all_staudent)


        self.Exet_graph_pb_2.clicked.connect(self.Exet_programes)


        self.comboBox_test_model.setEnabled(False)
        self.comboBox_test_db.setEnabled(False)
        self.pushButton_19.setEnabled(False)
        self.pushButton_chack_any_student.setEnabled(False)
        self.pushButton_chack_all_image.setEnabled(False)
        self.pushButton_chack_all_image.setEnabled(False)
        self.Testing_start_pb.setEnabled(False)

    def Exet_programes(self):
        self.windows2 = Main()
        self.close()
        self.windows2.show()
        print("Separt Voctor Machine")
        global index_table, y_clome
        y_clome = 1700

        index_table = -1
        self.j=0
    def quitApplication(self):
        """shutsdown the GUI window along with removal of files"""
        userReply = QMessageBox.question(self, 'Quit Application', "Are you sure you want to quit this app?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if userReply == QMessageBox.Yes:


            keyboard.press_and_release('alt+F4')


            #clearfunc2(self.cam)
            self.close()
    def Handel_UI_Changes(self):
        # self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)
        print("d")

    def append_df_to_excel(self,df, excel_path):
        df_excel = pd.read_excel(excel_path)
        result = pd.concat([df_excel, df], ignore_index=True)
        result.to_excel(excel_path, index=False)

    def imagesfwd(self):
        """displays next images act as a gesutre viewer"""
        numberes = self.lineEdit_nuber_show.text()
        string = "".join(numberes)
        num = int(string)
        num += 100
        #print("nnnnnnnnnnn", (num))
        global index

        index += 1

        try:
            #print("index", index)
            if index < num:
                show_db = self.comboBox_databas_show.currentIndex()
                if show_db == 0:
                    self.lable_image_3.setPixmap(
                        QtGui.QPixmap("./show_image/Arabic/" + "Image{}.jpg".format(str(index))))
                if show_db == 1:
                    self.lable_image_3.setPixmap(
                        QtGui.QPixmap("./show_image/MNIST/" + "Image{}.jpg".format(str(index))))
        except:
            pass

    def toggl(self):
        """displays previous images act as a gesutre viewer"""
        numberes = self.lineEdit_nuber_show.text()
        string = "".join(numberes)
        num = int(string)
        num += 100

        global index

        index -= 1
        try:
            if index < num and index >= 100:
                show_db = self.comboBox_databas_show.currentIndex()
                if show_db == 0:
                    self.lable_image_3.setPixmap(
                        QtGui.QPixmap("./show_image/Arabic/" + "Image{}.jpg".format(str(index))))
                if show_db == 1:
                    self.lable_image_3.setPixmap(
                        QtGui.QPixmap("./show_image/MNIST/" + "Image{}.jpg".format(str(index))))
        except:
            pass

    def start_show(self):
        try:
            self.lable_image_3.setPixmap(QtGui.QPixmap("./show_image/Arabic/" + "Image101.jpg"))
            global index
            index = 100
        except:
            pass
        self.pushButton_next_pb.clicked.connect(self.imagesfwd)
        self.pushButton_prove_pb.clicked.connect(self.toggl)

    def Show_image(self):
        self.tabWidget.setCurrentIndex(0)
        self.start_show_pb.clicked.connect(self.start_show)

###################################################################
    def Start_resalt(self):
        global index_resalt
        index_resalt = 0
        Resalt_db = self.comboBox_Databas_Re.currentIndex()
        Resalt_model = self.comboBox_Resalt_model.currentIndex()
        if Resalt_db == 0:
            if Resalt_model == 0:
                self.lable_image_resalt.setPixmap(QtGui.QPixmap("./Resalt_file/ANN/" + "{}.png".format(str(1))))

        else:
            self.lable_image_resalt.setPixmap(QtGui.QPixmap("./Resalt_file/CNN/" + "{}.png".format(str(1))))


        self.pushButton_prove_resalt.clicked.connect(self.Resalt_next)
        self.pushButton_next_Resalt.clicked.connect(self.Resalt_after)

    def Resalt_next(self):
        global index_resalt

        index_resalt += 1

        try:
            if index_resalt < 10:
                Resalt_db = self.comboBox_Databas_Re.currentIndex()
                Resalt_model = self.comboBox_Resalt_model.currentIndex()
                if Resalt_db == 0 :
                    print(index_resalt)
                    if Resalt_model == 0:
                        self.lable_image_resalt.setPixmap(
                            QtGui.QPixmap("./Resalt_file/ANN/" + "{}.png".format(str(index_resalt))))

                    elif Resalt_model == 1:

                        self.lable_image_resalt.setPixmap(
                            QtGui.QPixmap("./Resalt_file/ANN/" + "{}.png".format(str(index_resalt))))



                else :
                    self.lable_image_resalt.setPixmap(
                        QtGui.QPixmap("./Resalt_file/CNN/" + "{}.png".format(str(index_resalt))))


        except:
            pass

    def Resalt_after(self):
        global index_resalt

        index_resalt -= 1
        try:
            if index_resalt < 10 and index_resalt >= 0:
                Resalt_db = self.comboBox_Databas_Re.currentIndex()
                Resalt_model = self.comboBox_Resalt_model.currentIndex()
                if Resalt_db == 0 :
                    if Resalt_model == 0:

                        self.lable_image_resalt.setPixmap(
                            QtGui.QPixmap("./Resalt_file/ANN/" + "{}.png".format(str(index_resalt))))

                    elif Resalt_model == 1:

                        self.lable_image_resalt.setPixmap(
                            QtGui.QPixmap("./Resalt_file/ANN/" + "{}.png".format(str(index_resalt))))




                else :

                    self.lable_image_resalt.setPixmap(
                        QtGui.QPixmap("./Resalt_file/CNN/" + "{}.png".format(str(index_resalt))))


        except:
            pass


    def Show_resalt(self):
        self.tabWidget.setCurrentIndex(1)
        self.pushButton_start_Resalt.clicked.connect(self.Start_resalt)




    def sater_test(self):

        global classifier
        self.Testing_start_pb.setEnabled(False)
        dd = self.comboBox_test_db.currentIndex()
        modeles = self.comboBox_test_model.currentIndex()

        global classifier_connect,classifier_acade
        classifier_connect= load_model("./model/model_of_100c_final.h5")

        classifier_acade = load_model('./model/final_model.Nh5')

        if dd == 0:


            if modeles == 0:
                classifier = load_model('./model/model_ANN_Arabic.h5')


                print("ANN")


            else:
                classifier = load_model('./model/project_Arabic_use_keras_two222.h5')



        if dd == 1:
            print("comboBox  1")
            if modeles == 0:
                classifier = load_model('./model/moedlann_endlish_finall_without_lose.h5')

                print("ANN")

            else:
                classifier = load_model('./model/final_model.Nh5')


                print("CNN")
        global filena
        filena = QFileDialog.getOpenFileName(self, "Select Excele File")[0]

        image3 = cv2.imread('rect.jpg')


        self.pushButton_chack_all_image.setEnabled(True)
        self.pushButton_chack_any_student.setEnabled(True)




    def deskew(self,img):
        m = cv2.moments(img)

        rows, cols = img.shape
        if abs(m['mu02']) < 1e-2:
            return img.copy()
        # Calculate skew based on central momemts.
        skew = m['mu11'] / m['mu02']
        # Calculate affine transform to correct skewness.
        M = np.float32([[1, skew, -0.5 * cols * skew], [0, 1, 0]])
        # Apply affine transform
        img = cv2.warpAffine(img, M, (cols, rows),
                             flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
        return img

    def choos(self):
        self.pushButton_path_image.setEnabled(False)
        img = QFileDialog.getOpenFileName(self, "OpenFile")

        image = cv2.imread(img[0])


        imagesow = cv2.resize(image, (500, 600))
        cv2.imwrite("imagesow.jpg", imagesow)
        self.lable_image_2.setPixmap(QtGui.QPixmap("imagesow.jpg"))
        print(image.shape)



        image = cv2.resize(image, (5000, 7000))
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print("gray")
        blue = cv2.GaussianBlur(gray, (25, 25), 0)
        thresh = cv2.adaptiveThreshold(blue, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 5)

        ret, thresh1 = cv2.threshold(blue, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (400, 25))
        open_h = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel_h, iterations=1)
        cnts = cv2.findContours(open_h, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        print("image2")
        image2 = gray.copy()
        image2[0:gray.shape[0], 0:gray.shape[1]] = 0

        for c in cnts:
            cv2.drawContours(image2, [c], -1, (255, 255, 255), 35)

        kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1000))
        open_v = cv2.morphologyEx(thresh1, cv2.MORPH_OPEN, kernel_v, iterations=1)
        cnts = cv2.findContours(open_v, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        print("open_v")
        for c in cnts:
            cv2.drawContours(image2, [c], -1, (255, 255, 255), 30)

        cntsf = cv2.findContours(image2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        point = []
        for cnt in cntsf:
            x, y, w, h = cv2.boundingRect(cnt)
            point.append((x, y, w, h))
        point = sorted(point, key=lambda data: math.sqrt(data[0] ** 2 + data[1] ** 2));
        print("point")
        one = point[0]
        x, y = one[0], one[1]

        last = point[-1]
        w, h = last[0] + last[2], last[1] + last[3]

        image2[y:h, x:w] = 255

        im_result = cv2.bitwise_and(image2, thresh)
        print("im_result")
        kernel_v = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 200))
        open_v = cv2.morphologyEx(im_result, cv2.MORPH_OPEN, kernel_v, iterations=1)
        cnts = cv2.findContours(open_v, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

        for c in cnts:
            cv2.drawContours(im_result, [c], -1, (0, 0, 0), 100)

        kernel_h = cv2.getStructuringElement(cv2.MORPH_RECT, (400, 4))
        open_h = cv2.morphologyEx(im_result, cv2.MORPH_OPEN, kernel_h, iterations=1)
        cnts = cv2.findContours(open_h, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        print("open_h")
        for c in cnts:
            cv2.drawContours(im_result, [c], -1, (0, 0, 0), 60)

        kernel = np.ones((5, 5), np.uint8)
        dilat = cv2.dilate(im_result, kernel)
        open_im = cv2.morphologyEx(dilat, cv2.MORPH_OPEN, kernel)

        img_table = open_im[y:h, x:w]
        print("img_table")

        img = cv2.resize(img_table, (3000, 7000))

        global image_processed
        image_processed=img


        print("preprocessing complet")
        self.Testing_start_pb.setEnabled(True)
        self.comboBox_test_model.setEnabled(True)
        self.comboBox_test_db.setEnabled(True)
        self.Testing_start_pb.clicked.connect(self.sater_test)




    def save(self):


        self.pushButton_chack_all_image.setEnabled(False)



        y = self.j

        sub_image = image_processed[y:y + 385, 0:3000]

        sub_imag = cv2.resize(sub_image, (500, 50))

        cv2.imwrite("number.png", sub_imag)
        self.label_3.setPixmap(QtGui.QPixmap("number.png"))

        i = 0
        academic_number = []
        partical = []
        middle = []
        final = []
        sums = []

        for v in range(3000, 0, -600):

            i = i + 1
            sub_v_image = sub_image[30:385, v - 600:v]


            canny = cv2.Canny(sub_v_image, 10, 255)

            contours = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

            points = []
            for cnt in contours:
                x, y, w, h = cv2.boundingRect(cnt)
                if w >= 15 and h >= 20:
                    points.append((x, y, w, h))
            points = sorted(points, key=lambda data: math.sqrt(data[0] ** 2 + data[1] ** 2));

            for c in points:

                x, y, w, h = c[0], c[1], c[2], c[3]
                area = w * h
                print("area=", area)
                if w >= 15 and h >= 60:


                    roi = sub_v_image[y:y + h, x:x + w]
                    roi = self.deskew(roi)


                    print(roi.shape)
                    image_height, image_width = roi.shape

                    print("image_height", "image_width", roi.shape)

                    if image_height >= 120 and image_width >= 150:

                        roi= cv2.bitwise_not(roi)
                        cv2.imwrite("connect_image.jpg", roi)
                        print("hhhhhhhhhhhhhhhhhh")
                        CATEGORIES = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                                      "10", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                      "24", "25", "26",

                                      "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                                      "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
                                      "53",
                                      "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66",
                                      "67",
                                      "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
                                      "81", "82",
                                      "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95",
                                      "96", "97", "98", "99"]


                        IMG_SIZE = 64  # 50 in txt-based
                        img_array = cv2.imread('connect_image.jpg', cv2.IMREAD_GRAYSCALE)
                        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                        new_array2=new_array.reshape(1, IMG_SIZE, IMG_SIZE, 1)
                        print("hhhhhhhhhhhhhhhhhh")
                        cla = load_model("model_of_100c_final.h5")
                        print("hhhhhhhhhhhhhhhhhh")
                        res = str(cla.predict_classes([new_array2])[0])

                        res = CATEGORIES[int(res)]
                        # print(CATEGORIES[int(res)])
                        print(res)


                    else:



                        dd = self.comboBox_test_db.currentIndex()
                        modeles = self.comboBox_test_model.currentIndex()

                        if dd == 0 or dd == 1:
                            print("comboBox  0")
                            if i==1:
                                roi = makesquare(roi)
                                roi = resize_pixel(28, roi)
                                roi = roi / 255
                                roi = roi.reshape(1, 28, 28, 1)
                                res = str(classifier_acade.predict_classes(roi)[0])

                            else:
                                if modeles == 0:
                                    #roi = cv2.bitwise_not(roi)
                                    roi = makesquare(roi)
                                    roi = resize_pixel(28, roi)
                                    roi = roi / 255
                                    roi = roi.reshape(1, 784)
                                    res = str(classifier.predict_classes(roi)[0])
                                    print("ANN")

                                else :

                                    roi = makesquare(roi)
                                    roi = resize_pixel(28, roi)
                                    roi = roi / 255
                                    roi = roi.reshape(1, 28, 28, 1)

                                    res = str(classifier.predict_classes(roi)[0])

                                    print("CNN")




                    if i == 1:
                        academic_number.append(res)


                    if i == 2:
                        partical.append(res)


                    if i == 3:
                        middle.append(res)

                    if i == 4:
                        final.append(res)

                    if i == 5:
                        sums.append(res)
                        print("res=",res)

        string = "".join(academic_number)


        self.lineEdit_achadimic.setText(string)

        string = "".join(partical)
        self.lineEdit_partical_dagree.setText(string)

        string = "".join(middle)
        self.lineEdit_middle_dagree.setText(string)
        print("middle=", middle)
        string = "".join(final)

        self.lineEdit_final.setText(string)
        string = "".join(sums)

        self.lineEdit_sums_dagree.setText(string)
        self.pushButton_19.setEnabled(True)
        self.pushButton_chack_any_student.setEnabled(False)



    def save_any_staudent(self):
        self.pushButton_19.setEnabled(False)

        string = "".join(self.lineEdit_achadimic.text())
        achadimic = int(string)

        string = "".join(self.lineEdit_partical_dagree.text())
        partical_dagree = int(string)

        string = "".join(self.lineEdit_middle_dagree.text())
        middle_dagree = int(string)
        print("middle_dagree  =", middle_dagree)
        string = "".join(self.lineEdit_final.text())
        final_dagree = int(string)


        string = "".join(self.lineEdit_sums_dagree.text())
        sums_degrees = int(string)
        print("sum  =", sums_degrees)

        sum_partical_middle_final = partical_dagree + middle_dagree + final_dagree
        if sum_partical_middle_final != sums_degrees:
            sums_degrees = sum_partical_middle_final

        df = pd.DataFrame({"academic_number": [achadimic], "partical": [partical_dagree], "middle": [middle_dagree],
                           "final": [final_dagree], "sums_dagree": [sum_partical_middle_final]})

        self.append_df_to_excel(df,filena)




        self.tableWidget_2.setRowCount(18)
        self.tableWidget_2.setColumnCount(5)
        print("alaaaaaaaaaa")
        print("index_table", self.index_ta)
        self.tableWidget_2.setItem(self.index_ta, 0, QTableWidgetItem(str(achadimic)))
        print("index_table", self.index_ta)
        self.tableWidget_2.setItem(self.index_ta, 1, QTableWidgetItem(str(partical_dagree)))
        self.tableWidget_2.setItem(self.index_ta, 2, QTableWidgetItem(str(middle_dagree)))
        self.tableWidget_2.setItem(self.index_ta, 3, QTableWidgetItem(str(final_dagree)))
        self.tableWidget_2.setItem(self.index_ta, 4, QTableWidgetItem(str(sums_degrees)))

        print("index_table", self.index_ta)
        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.tableWidget_2)
        self.setLayout(self.vBoxLayout)

        self.index_ta += 1

        self.j+=385

        self.pushButton_chack_any_student.setEnabled(True)



    def save_all_staudent(self):
        self.pushButton_chack_any_student.setEnabled(False)
        self.pushButton_19.setEnabled(False)


        for i in range(1,18):
            y = self.j

            sub_image = image_processed[y:y + 385, 0:3000]

            sub_imag = cv2.resize(sub_image, (500, 50))

            cv2.imwrite("number.png", sub_imag)
            self.label_3.setPixmap(QtGui.QPixmap("number.png"))

            i = 0
            academic_number = []
            partical = []
            middle = []
            final = []
            sums = []

            for v in range(3000, 0, -600):

                i = i + 1
                sub_v_image = sub_image[30:385, v - 600:v]

                canny = cv2.Canny(sub_v_image, 40, 255)

                contours = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

                points = []
                for cnt in contours:
                    x, y, w, h = cv2.boundingRect(cnt)
                    if w >= 15 and h >= 20:
                        points.append((x, y, w, h))
                points = sorted(points, key=lambda data: math.sqrt(data[0] ** 2 + data[1] ** 2));
                print("lllllllllllllllllllll")
                for c in points:
                    x, y, w, h = c[0], c[1], c[2], c[3]
                    if w >= 15 and h >= 20:
                        roi = sub_v_image[y:y + h, x:x + w]

                        print(roi.shape)
                        image_height, image_width = roi.shape

                        print("image_height", "image_width", roi.shape)

                        if image_height >= 120 and image_width >= 150:

                            roi = cv2.bitwise_not(roi)
                            cv2.imwrite("connect_image.jpg", roi)
                            print("hhhhhhhhhhhhhhhhhh")
                            CATEGORIES = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                                          "10", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23",
                                          "24", "25", "26",

                                          "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39",
                                          "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
                                          "53",
                                          "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66",
                                          "67",
                                          "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80",
                                          "81", "82",
                                          "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95",
                                          "96", "97", "98", "99"]

                            IMG_SIZE = 64  # 50 in txt-based
                            img_array = cv2.imread('connect_image.jpg', cv2.IMREAD_GRAYSCALE)
                            new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                            new_array2 = new_array.reshape(1, IMG_SIZE, IMG_SIZE, 1)
                            print("hhhhhhhhhhhhhhhhhh")
                            cla = load_model("model_of_100c_final.h5")
                            print("hhhhhhhhhhhhhhhhhh")
                            res = str(cla.predict_classes([new_array2])[0])

                            res = CATEGORIES[int(res)]
                            # print(CATEGORIES[int(res)])
                            print(res)


                        else:

                            dd = self.comboBox_test_db.currentIndex()
                            modeles = self.comboBox_test_model.currentIndex()

                            if dd == 0 or dd == 1:
                                print("comboBox  0")
                                if i == 1:
                                    roi = makesquare(roi)
                                    roi = resize_pixel(28, roi)
                                    roi = roi / 255
                                    roi = roi.reshape(1, 28, 28, 1)
                                    res = str(classifier_acade.predict_classes(roi)[0])

                                else:
                                    if modeles == 0:
                                        # roi = cv2.bitwise_not(roi)
                                        roi = makesquare(roi)
                                        roi = resize_pixel(28, roi)
                                        roi = roi / 255
                                        roi = roi.reshape(1, 784)
                                        res = str(classifier.predict_classes(roi)[0])
                                        print("ANN")

                                    else:
                                        roi = makesquare(roi)
                                        roi = resize_pixel(28, roi)
                                        roi = roi / 255
                                        roi = roi.reshape(1, 28, 28, 1)
                                        res = str(classifier.predict_classes(roi)[0])

                                        print("CNN")

                        if i == 1:
                            academic_number.append(res)

                        if i == 2:
                            partical.append(res)

                        if i == 3:
                            middle.append(res)

                        if i == 4:
                            final.append(res)

                        if i == 5:
                            sums.append(res)

            string = "".join(academic_number)

            self.lineEdit_achadimic.setText(string)

            string = "".join(partical)
            self.lineEdit_partical_dagree.setText(string)

            string = "".join(middle)
            self.lineEdit_middle_dagree.setText(string)

            string = "".join(final)

            self.lineEdit_final.setText(string)
            string = "".join(sums)

            self.lineEdit_sums_dagree.setText(string)
            self.save_any_staudent()

    def Testing_system(self):
        self.tabWidget.setCurrentIndex(2)
        self.pushButton_path_image.clicked.connect(self.choos)








def main():
    app = QApplication(sys.argv)
    window = Main()

    window.show()

    app.exec_()


if __name__ == '__main__':
    main()