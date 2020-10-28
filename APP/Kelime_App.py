import sys
import codecs
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout,QHBoxLayout,QWidget, QAction, QPlainTextEdit
from PyQt5.QtCore import *
from PyQt5.QtGui import *


qss = """
QMenuBar {
    background-color: rgb(33,33,33);
}
QMenuBar::item {
    spacing: 3px;           
    padding: 2px 10px;
    background-color: rgb(33,33,33);
    color: rgb(255,255,255);  
    border-radius: 5px;
}
QMenuBar::item:selected {    
    background-color: rgb(15,141,124);
}
QMenuBar::item:pressed {
    background: rgb(15,141,124);
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  

QMenu {
    background-color: rgb(33, 33, 33);  
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: transparent;
    color: red;
}
QMenu::item:selected { 
    background-color: rgb(15,141,124);
    color: rgb(255,255,255);
}
"""

class known_window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Known Vocabs")
        self.setGeometry(0,0, 500, 500)

        vbox = QVBoxLayout()
        text_edit = QPlainTextEdit()

        vbox.addWidget(text_edit)
        self.setLayout(vbox)
        text = codecs.open('known_vocabs.txt', encoding="utf-8").read()
        text_edit.setPlainText(text)

class dont_window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle(" Dont Known Vocabs")
        self.setGeometry(0,0, 500, 500)

        vbox = QVBoxLayout()
        text_edit = QPlainTextEdit()

        vbox.addWidget(text_edit)
        self.setLayout(vbox)
        text = codecs.open('dont_known.txt', encoding="utf-8").read()
        text_edit.setPlainText(text)


class all_window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.setWindowTitle("Known Vocabs")
        self.setGeometry(0,0, 500, 500)

        vbox = QVBoxLayout()
        text_edit = QPlainTextEdit()

        vbox.addWidget(text_edit)
        self.setLayout(vbox)
        text = codecs.open('days.txt', encoding="utf-8").read()
        text_edit.setPlainText(text)


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)
        self.Vlayout = QVBoxLayout()
        self.Hlayout1 = QHBoxLayout(centralWidget)
        self.button = QPushButton("Press for Continue", self)
        self.buttonCheck = QPushButton("Check it", self)
        self.label = QLabel("Well Come to VocApp", self)
        self.label2 = QLabel("", self)
        self.textbox = QLineEdit(self)
        self.title = "VocApp"
        self.answer = ""
        self.clicked = False
        self.menubar = self.menuBar()
        self.liste = self.menubar.addMenu("listeler")
        self.known = QAction("Known words", self)
        self.dont = QAction("dont Known words", self)
        self.all_w = QAction("All words", self)
        self.vocab_day, self.means = self.read_days()
        self.initUI()

    def initUI(self):

        self.setWindowTitle(self.title)
        self.setGeometry(500, 250, 400, 200)
        self.setStyleSheet("background-color:rgb(33, 33, 33);") 
        self.setWindowIcon(QIcon('VocApp.png'))

        self.label.resize(300, 20)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('color: rgb(60, 60, 230)')
        self.label.setFont(QFont('Arial', 14)) 

        self.label2.resize(300, 20)
        self.label2.setStyleSheet('color: white')
        self.label2.setFont(QFont('Constantia', 11))

        self.textbox.resize(300, 40)
        self.textbox.returnPressed.connect(self.check_click)
        self.textbox.setStyleSheet("color: rgb(25, 255, 170)")
        #self.textbox.setStyleSheet("background-color: rgb(70, 70, 70)")
        self.textbox.hide()

        self.button.resize(100, 30)
        self.button.setStyleSheet("background-color: rgb(255,0,0)")

        self.buttonCheck.resize(0, 0)
        self.buttonCheck.hide()
        self.buttonCheck.setStyleSheet("background-color: rgb(0,255,0)")

        self.button.clicked.connect(self.on_click)
        self.buttonCheck.clicked.connect(self.check_click)

        self.Vlayout.addWidget(self.label)
        self.Vlayout.addStretch()
        self.Vlayout.addWidget(self.label2)
        self.Vlayout.addWidget(self.textbox)
        self.Vlayout.addWidget(self.buttonCheck)
        self.Vlayout.addWidget(self.button)
        self.Vlayout.addStretch()


        self.Hlayout1.addStretch()
        self.Hlayout1.addLayout(self.Vlayout)
        self.Hlayout1.addStretch()

        self.menubar.setStyleSheet(qss)

        self.liste.addAction(self.known)
        self.liste.addAction(self.dont)
        self.liste.addAction(self.all_w)

        self.known.triggered.connect(self.known_w)
        self.dont.triggered.connect(self.dont_w)
        self.all_w.triggered.connect(self.all_words)
        self.show()

    @pyqtSlot()
    def on_click(self):
        self.button.hide()
        self.buttonCheck.show()
        self.textbox.show()
        self.ask(self.vocab_day, self.means)
        self.close()

    @pyqtSlot()
    def check_click(self):
        self.answer = self.textbox.text()
        self.clicked = True

    def known_w(self):
        self.w = known_window()
        self.w.show()

    def dont_w(self):
        self.w = dont_window()
        self.w.show()

    def all_words(self):
        self.w = all_window()
        self.w.show()

    def read_days(self):
        ff = codecs.open("days.txt", "r")
        f = codecs.open("days_meanings.txt", "r", encoding="utf-8")
        all_vocabs = ff.read()
        all_meaning = f.read()
        vocab_days = all_vocabs.split("*****")
        mean_days = all_meaning.split("*****")
        days = []
        means = []
        for i in vocab_days:
            day = i.split("\n")
            day.pop()
            days.append(day)
        days.pop()
        for i in mean_days:
            mean = i.split("\n")
            mean.pop()
            means.append(mean)
        means.pop()
        return days, means

    def ask_known(self):
        f = codecs.open("known_vocabs.txt", "r", encoding="utf-8")
        fff = codecs.open("dont_known.txt", "a", encoding="utf-8")
        known_words = f.read()
        known_words = known_words.split("\n")
        known_words.pop()
        j = 0
        for i in range(len(known_words)):
            both = known_words[j].split("->")
            self.label2.setText(f"{j + 1}. What is meaning of {both[0]}?")
            self.buttonCheck.setText("Check it")
            self.buttonCheck.setStyleSheet("background-color: rgb(255,255,0)")
            while not self.clicked:
                QCoreApplication.processEvents()

            self.clicked = False
            answer = self.answer
            if answer == both[1]:
                self.label2.setText("Correct :)")
                self.buttonCheck.setStyleSheet("background-color: rgb(0,255,0)")
            else:
                self.label2.setText(f"Wrong answer!! accurate {both[1]}")
                fff.write(both[0])
                fff.write("->")
                fff.write(both[1])
                fff.write("\n")
                del known_words[j]
                j -= 1
                self.buttonCheck.setStyleSheet("background-color: rgb(255,0,0)")
            self.buttonCheck.setText("Next")
            
            while not self.clicked:
                QCoreApplication.processEvents()

            self.clicked = False
            self.textbox.setText("")
            j += 1

        self.writeKnown(known_words)

    def writeKnown(self, known):
        f = codecs.open("known_vocabs.txt", "w", encoding="utf-8")
        f.truncate()
        for k in known:
            f.write(k)
            f.write("\n")

    def ask_didnt_known(self):
        f = codecs.open("dont_known.txt", "r", encoding="utf-8")
        ff = codecs.open("known_vocabs.txt", "a", encoding="utf-8")
        dont_known_words = f.read()
        dont_known_words = dont_known_words.split("\n")
        dont_known_words.pop()
        j = 0
        for i in range(len(dont_known_words)):
            both = dont_known_words[j].split("->")
            self.label2.setText(f"{j + 1}. vocab What is meaning of {both[0]}?")
            self.buttonCheck.setText("Check it")
            self.buttonCheck.setStyleSheet("background-color: rgb(255,255,0)")
            
            while not self.clicked:
                QCoreApplication.processEvents()

            self.clicked = False
            answer = self.answer

            if answer == both[1]:
                self.label2.setText("Correct :) you are better now")
                ff.write(both[0])
                ff.write("->")
                ff.write(answer)
                ff.write("\n")
                del dont_known_words[j]
                j -= 1
                self.buttonCheck.setStyleSheet("background-color: rgb(0,255,0)")
            else:
                self.label2.setText(f"Wrong answer!! accurate {both[1]}")
                self.buttonCheck.setStyleSheet("background-color: rgb(255,0,0)")

            self.buttonCheck.setText("Next")
            
            while not self.clicked:
                QCoreApplication.processEvents()

            self.textbox.setText("")
            self.clicked = False
            j += 1
        self.writeDintKnown(dont_known_words)

    def writeDintKnown(self, dont):
        f = codecs.open("dont_known.txt", "w", encoding="utf-8")
        f.truncate()
        for k in dont:
            f.write(k)
            f.write("\n")

    def ask(self, v, m):
        f = open("progression.txt", "r+")
        ff = codecs.open("known_vocabs.txt", "a", encoding="utf-8")
        fff = codecs.open("dont_known.txt", "a", encoding="utf-8")
        day_number = int(f.read())
        self.label.setText(f"Day number => {day_number + 1}")
        self.buttonCheck.resize(100, 30)
        self.textbox.resize(300, 30)

        if (day_number + 1) % 3 == 0:
            self.label2.setText("asking known vocabs")
            self.ask_known()
        elif ((day_number + 1) % 3 == 1 or (day_number + 1) % 3 == 2) and day_number != 0:
            self.label2.setText("Asking didn't known vocabs")
            self.ask_didnt_known()

        for i in range(len(v[day_number])):
            self.label2.setText(f"What is meaning of '{v[day_number][i]}'?")
            self.buttonCheck.setText("Check it")
            self.buttonCheck.setStyleSheet("background-color: rgb(255,255,0)")
            while not self.clicked:
                QCoreApplication.processEvents()

            self.clicked = False
            answer = self.answer
            if answer == m[day_number][i]:
                self.label2.setText(f"Correct :) => {m[day_number][i]}")
                ff.write(v[day_number][i])
                ff.write("->")
                ff.write(answer)
                ff.write("\n")
                self.buttonCheck.setStyleSheet("background-color: rgb(0,255,0)")
            else:
                self.label2.setText(f"Wrong Answer, accurate: '{m[day_number][i]}' !! Your answer is '{answer}' :(")
                fff.write(v[day_number][i])
                fff.write("->")
                fff.write(m[day_number][i])
                fff.write("\n")
                self.buttonCheck.setStyleSheet("background-color: rgb(255,0,0)")
            self.buttonCheck.setText("Next")
            while not self.clicked:
                QCoreApplication.processEvents()

            self.textbox.setText("")
            self.clicked = False
        day_number += 1
        f.seek(0)
        f.write(str(day_number))
        f.close()
        ff.close()
        fff.close()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
