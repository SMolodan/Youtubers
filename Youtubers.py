from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс від Crazy People')
main_win.resize(400, 250)

question = QLabel('Як звали першого ютуб-блогера, який набрав 100000000 підписників?')
btn_answer1 = QRadioButton('PewDiePie')
btn_answer2 = QRadioButton('Рет і Лінк')
btn_answer3 = QRadioButton('SlivkiShow')
btn_answer4 = QRadioButton('TheBrianMaps')
btn_answer5 = QRadioButton('Mister Max')
btn_answer6 = QRadioButton('EeOneGuy')


layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH4 = QHBoxLayout()
layoutH1.addWidget(question, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment=Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment=Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer5, alignment=Qt.AlignCenter)
layoutH4.addWidget(btn_answer6, alignment=Qt.AlignCenter)

layout_main = QVBoxLayout()
layout_main.addLayout(layoutH1)
layout_main.addLayout(layoutH2)
layout_main.addLayout(layoutH3)
layout_main.addLayout(layoutH4)
main_win.setLayout(layout_main)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Ви виграли зустріч з творцями каналу!')
    victory_win.exec_()

def show_lose():
    victory_win = QMessageBox()
    victory_win.setText('Пощастить іншим разом!')
    victory_win.exec_()

btn_answer3.clicked.connect(show_lose)
btn_answer1.clicked.connect(show_win)
btn_answer2.clicked.connect(show_lose)
btn_answer4.clicked.connect(show_lose)
btn_answer5.clicked.connect(show_lose)
btn_answer6.clicked.connect(show_lose)

main_win.show()
app.exec_()
