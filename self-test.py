from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
from bs4 import BeautifulSoup

with open("save.txt","a",encoding="utf-8") as f:
    f.write("이름\n인증번호\n")
 
with open("save.txt","r",encoding="utf-8") as f:
    line = f.readlines()
    line_1 = line[0].strip()
    line_2 = line[1].strip()



    


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 500)
 
        self.combo_grade = QtWidgets.QComboBox(Dialog)
        self.combo_grade.addItem('선택')
        self.combo_grade.addItem('1학년')
        self.combo_grade.addItem('2학년')
        self.combo_grade.addItem('3학년')
        self.combo_grade.addItem('4학년')
        self.combo_grade.addItem('5학년')
        self.combo_grade.addItem('6학년')
        self.combo_grade.move(50,50)
        self.combo_grade.setGeometry(QtCore.QRect(180,30,60,20))
        self.combo_grade.setObjectName("grade")

        self.combo_class = QtWidgets.QComboBox(Dialog)
        self.combo_class.addItem('선택')
        self.combo_class.addItem('1반')
        self.combo_class.addItem('2반')
        self.combo_class.addItem('3반')
        self.combo_class.addItem('4반')
        self.combo_class.addItem('5반')
        self.combo_class.addItem('6반')
        self.combo_class.addItem('7반')
        self.combo_class.move(50,50)
        self.combo_class.setGeometry(QtCore.QRect(180,90,60,20))
        self.combo_class.setObjectName("grade")


        self.label_grade = QtWidgets.QLabel(Dialog)
        self.label_grade.setGeometry(QtCore.QRect(195, 10, 60, 20))
        self.label_grade.setObjectName("label_grade")
        self.label_grade.setText("학년")

        self.label_class = QtWidgets.QLabel(Dialog)
        self.label_class.setGeometry(QtCore.QRect(200, 70, 60, 20))
        self.label_class.setObjectName("label_class")
        self.label_class.setText("반")


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 10, 40, 16))
        self.label.setObjectName("label")
 
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 70, 50, 16))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(90, 165, 100, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setText("설문 미응답자")

        

        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit_ID.setText(line_1)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
 
        self.lineEdit_PW = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_PW.setGeometry(QtCore.QRect(30, 90, 113, 20))
        self.lineEdit_PW.setText(line_2)
        self.lineEdit_PW.setObjectName("lineEdit_PW")

      
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(30, 180, 210, 130))
        self.textBrowser.setObjectName("textBrowser")
        

        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.startButton.setObjectName("startButton")

        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 330, 100, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("등교중지 학생 수 : ")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(140, 330, 100, 16))
        self.label_5.setObjectName("label_5")
        

        
 
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        

        
        
        #startButton 클릭시 autoExcute 함수 수행
        self.startButton.clicked.connect(self.autoExcute)


        #콤보 선택시 학년 라벨에 표시
        self.combo_class.activated[str].connect(self.onActivated)
        

    def onActivated(self, text):
        self.text_grade = int(self.combo_grade.currentText()[0])+1
        self.text_class = int(self.combo_class.currentText()[0])+1
        
        

 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "자가진단시스템 로그인"))
        self.label.setText(_translate("Dialog", "성명"))
        self.label_2.setText(_translate("Dialog", "인증번호"))
        self.startButton.setText(_translate("Dialog", "시작"))
        
 
 #셀레니움 동작 코드 함수 autoExcute 생성
    def autoExcute(self):
        _translate = QtCore.QCoreApplication.translate
        
        driver  = webdriver.Chrome()
        driver.implicitly_wait(1)
        driver.get('https://eduro.cbe.go.kr/stv_cvd_co00_010.do')
        
        driver.maximize_window()
        id = self.lineEdit_ID.text()
        pw = self.lineEdit_PW.text()

        

        driver.find_element_by_id('pName').send_keys(id)
        driver.find_element_by_id('qstnCrtfcNo').send_keys(pw)
        driver.find_element_by_id('btnConfirm').click()
        time.sleep(1)
        #미응답자 조회
        driver.find_element_by_xpath('//*[@id="srchRspns00"]/option[3]').click()
        driver.find_element_by_xpath("//*[@id='srchGrade']/option[{}]".format(self.text_grade)).click()
        driver.find_element_by_xpath("//*[@id='srchClassCode']/option[{}]".format(self.text_class)).click()
        driver.find_element_by_xpath('//*[@id="btnDtlSearch"]').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        
        driver.implicitly_wait(2)
        name_1=[]
        text_uncheck = ""
        soup = BeautifulSoup(driver.page_source,"lxml")
        unchecks = soup.select("#qstnRsltList > tbody > tr > td.alignL > a")


        for uncheck in unchecks:
            name_1.append(uncheck.text)
        
        for i in name_1:
            text_uncheck = text_uncheck + i + ", "       

            

        

        grades = soup.select("#qstnSmupList > tbody > tr > td:nth-child(1)")
        classes = soup.select("#qstnSmupList > tbody > tr > td:nth-child(2)")


        for i,grade in enumerate(grades):
            grade = int(grade.text.strip()[0])
            clas = int(classes[i].text.strip()[0])
            if self.text_grade-1 == grade and self.text_class-1 == clas:
                selector = "#qstnSmupList > tbody > tr:nth-child(" + str(i+1) + ") > td:nth-child(7)"
                print(selector)
                stop_num = soup.select_one(selector).text + "명"
                


                   
        self.textBrowser.setText(_translate("Dialog",text_uncheck))
        self.label_5.setText(_translate("Dialog",stop_num))

    
       
        with open("save.txt","w",encoding="utf-8") as f:
            f.write("{0}\n{1}\n".format(self.lineEdit_ID.text(),self.lineEdit_PW.text()))

    
        
        
            
        
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




