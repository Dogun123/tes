from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup

with open("save.txt","a",encoding="utf-8") as f:
    f.write("아이디\n비밀번호\n")

 
with open("save.txt","r",encoding="utf-8") as f:
    line = f.readlines()
    line_1 = line[0].strip()
    line_2 = line[1].strip()

with open("save2.txt","a",encoding="utf-8") as i:
    i.write("학교명\n교사성명\n생년월일\n비밀번호\n")

with open("save2.txt","r",encoding="utf-8") as i:
    rine = i.readlines()
    rine_1 = rine[0].strip()
    rine_2 = rine[1].strip()
    rine_3 = rine[2].strip()
    rine_4 = rine[3].strip()
    


class Ui_Dialog(object):
    def setupUi(self, Dialog):

        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 500)
 
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

        self.label_teacher = QtWidgets.QLabel(Dialog)
        self.label_teacher.setGeometry(QtCore.QRect(300, 10, 150, 20))
        self.label_teacher.setObjectName("label_class")
        self.label_teacher.setText("교직원 건강상태 자가진단")

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
        self.startButton.setGeometry(QtCore.QRect(40, 130, 85, 30))
        self.startButton.setObjectName("startButton")

        self.startButton_2 = QtWidgets.QPushButton(Dialog)
        self.startButton_2.setGeometry(QtCore.QRect(140, 130, 75, 30))
        self.startButton_2.setObjectName("startButton_2")

        self.startButton_3 = QtWidgets.QPushButton(Dialog)
        self.startButton_3.setGeometry(QtCore.QRect(310, 160, 120, 30))
        self.startButton_3.setObjectName("startButton_3")


        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 320, 120, 23))
        self.label_4.setObjectName("label_4")
        self.label_4.setText("등교중지 학생 명단")

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(425, 100, 100, 20))
        self.label_5.setObjectName("label_4")
        self.label_5.setText('"YYMMDD"')

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(425, 130, 100, 20))
        self.label_5.setObjectName("label_4")
        self.label_5.setText('4자리')

        self.lineEdit_SCHOOL = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_SCHOOL.setGeometry(QtCore.QRect(320, 40, 100, 20))
        self.lineEdit_SCHOOL.setText(rine_1)
        self.lineEdit_SCHOOL.setObjectName("lineEdit_SCHOOL")

        self.lineEdit_TNAME = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_TNAME.setGeometry(QtCore.QRect(320, 70, 100, 20))
        self.lineEdit_TNAME.setText(rine_2)
        self.lineEdit_TNAME.setObjectName("lineEdit_TNAME")

        self.lineEdit_BIRTH = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_BIRTH.setGeometry(QtCore.QRect(320, 100, 100, 20))
        self.lineEdit_BIRTH.setText(rine_3)
        self.lineEdit_BIRTH.setObjectName("lineEdit_BIRTH")

        self.lineEdit_TPASS = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_TPASS.setGeometry(QtCore.QRect(320, 130, 100, 20))
        self.lineEdit_TPASS.setText(rine_4)
        self.lineEdit_TPASS.setObjectName("lineEdit_TPASS")



        self.textBrowser_2 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 340, 210, 30))
        self.textBrowser_2.setObjectName("textBrowser_2")
        

        
 
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)



        

        
        
        #startButton 클릭시 autoExcute 함수 수행
        self.startButton.clicked.connect(self.autoExcute)
        self.startButton_2.clicked.connect(self.browserenter)
        self.startButton_3.clicked.connect(self.teabrowserenter)


        #콤보 선택시 학년 라벨에 표시
        self.combo_class.activated[str].connect(self.onActivated)

    

    def onActivated(self, text):
        self.text_grade = self.combo_grade.currentText()[0]
        self.text_class = self.combo_class.currentText()[0]
        
        

 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "자가진단시스템 로그인"))
        self.label.setText(_translate("Dialog", "아이디"))
        self.label_2.setText(_translate("Dialog", "비밀번호"))
        self.startButton.setText(_translate("Dialog", "명단불러오기"))
        self.startButton_2.setText(_translate("Dialog","사이트접속"))
        self.startButton_3.setText(_translate("Dialog","자가진단 참여하기"))
    
    def teabrowserenter(self):
        with open("save2.txt","w",encoding="utf-8") as f:
            f.write("{0}\n{1}\n{2}\n{3}\n".format(self.lineEdit_SCHOOL.text(),self.lineEdit_TNAME.text(),self.lineEdit_BIRTH.text(),self.lineEdit_TPASS.text()))

        school = self.lineEdit_SCHOOL.text()
        name = self.lineEdit_TNAME.text()
        birth = self.lineEdit_BIRTH.text()
        pw = self.lineEdit_TPASS.text()
        driver = webdriver.Chrome()
        driver.get('https://hcs.eduro.go.kr')
        driver.find_element_by_id('btnConfirm2').click()
        driver.find_element_by_class_name('searchBtn').click()
        driver.implicitly_wait(1)
        #시,도(충청북도)
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[1]/td/select/option[12]').click()
        #학교급(초등학교)
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[2]/td/select/option[3]').click()
        #학교명(검색)
        driver.find_element_by_class_name('searchArea').send_keys(school)
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').send_keys(Keys.ENTER)
        driver.implicitly_wait(1)
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[1]/ul/li/p/a').click()
        driver.find_element_by_xpath('//*[@id="softBoardListLayer"]/div[2]/div[2]/input').click()
        
        #성명
        driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[2]/td/input').send_keys(name)
        #생년월일
        driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr[3]/td/input').send_keys(birth)
        #추가    
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').send_keys(Keys.ENTER)
        #비밀번호
        time.sleep(2)
        driver.find_element_by_class_name('input_text_common').send_keys(pw)
        
        #추가
        driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()



    def browserenter(self):
        id = self.lineEdit_ID.text()
        pw = self.lineEdit_PW.text()

        driver = webdriver.Chrome()
        driver.implicitly_wait(1)
        driver.get('https://cbehcm.eduro.go.kr/loginFailPage.do')
        
        driver.maximize_window()
       

        driver.find_element_by_id('lusername').send_keys(id)
        driver.find_element_by_id('lpassword').send_keys(pw)
        driver.find_element_by_xpath('/html/body/div/div[1]/form/button').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="sGrade"]').click()
        driver.find_element_by_xpath('//*[@id="sGrade"]/option[{}]'.format(str(int(self.text_grade)+1))).click()
        driver.find_element_by_xpath('//*[@id="sClassCode"]/option[{}]'.format(int(self.text_class)+1)).click()
        driver.find_element_by_xpath('//*[@id="searchForm"]/ul/li[5]/input').click()
        

        
 
 #셀레니움 동작 코드 함수 autoExcute 생성
    def autoExcute(self):
        _translate = QtCore.QCoreApplication.translate
        
        options = webdriver.ChromeOptions()
        options.headless = True
        driver  = webdriver.Chrome(options=options)
        driver.implicitly_wait(1)
        driver.get('https://cbehcm.eduro.go.kr/loginFailPage.do')
        
        
        id = self.lineEdit_ID.text()
        pw = self.lineEdit_PW.text()

        
        #학년 반 조회
        driver.find_element_by_id('lusername').send_keys(id)
        driver.find_element_by_id('lpassword').send_keys(pw)
        driver.find_element_by_xpath('/html/body/div/div[1]/form/button').send_keys(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="sGrade"]').click()
        driver.find_element_by_xpath('//*[@id="sGrade"]/option[{}]'.format(int(self.text_grade)+1)).click()
        driver.find_element_by_xpath('//*[@id="sClassCode"]/option[{}]'.format(int(self.text_class)+1)).click()
        driver.find_element_by_xpath('//*[@id="searchForm"]/ul/li[5]/input').click()

        #미참여자 명단 조회
        uncheck_group = []
        stop_group = []
        text_stop = ''
        text_uncheck = ''
        soup = BeautifulSoup(driver.page_source,"lxml")
        unchecks = soup.select("#teacher_tbody > tr > td.state")
        unchecks_name = soup.select("#teacher_tbody > tr > td:nth-child(4)")
        for i,uncheck in enumerate(unchecks):
            if uncheck.text.strip() == "미참여" :
                uncheck_group.append(unchecks_name[i].text.strip())
        
        for i in uncheck_group:
            text_uncheck = text_uncheck + i + ','
        
        self.textBrowser.setText(_translate("Dialog",text_uncheck))

        #등교중지 학생 명단
        stopnums = soup.select("#teacher_tbody > tr > td:nth-child(7)")
        for i,stopnum in enumerate(stopnums):
            if stopnum.text.strip() == "0":
                stop_group.append(unchecks_name[i].text.strip())
        
        if len(stop_group) == 0:
            self.textBrowser_2.setText(_translate("Dialog","등교중지 학생 없음"))
        else:
            for i in stop_group:
                text_stop = text_stop + i + ','
            self.textBrowser_2.setText(_translate("Dialog",text_stop))

    
       
        with open("save.txt","w",encoding="utf-8") as f:
            f.write("{0}\n{1}\n".format(self.lineEdit_ID.text(),self.lineEdit_PW.text()))

        driver.implicitly_wait(1)
        driver.quit()

    
        
        
            
        
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())




