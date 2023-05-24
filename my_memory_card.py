
from random import shuffle

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QRadioButton, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QGroupBox, QPushButton, QButtonGroup)

class Question():
    def __init__(self , quest, right_answer, wrong1, wrong2, wrong3):
        self.quest = quest
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q = Question('Сколько лет городу Бухара?' , '2500' , '1200' , '3000' ,'2100' )


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(400, 200)

question = QLabel('Сколько лет Ташкенту?')

r_btn_1 = QRadioButton('2700')
r_btn_2 = QRadioButton('10600')
r_btn_3 = QRadioButton('1000')
r_btn_4 = QRadioButton('5200')

btn = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов:')
h_line_group = QHBoxLayout()
v_line_group1 = QVBoxLayout()
v_line_group2 = QVBoxLayout()

v_line_group1.addWidget(r_btn_1)
v_line_group1.addWidget(r_btn_2)
v_line_group2.addWidget(r_btn_3)
v_line_group2.addWidget(r_btn_4)
h_line_group.addLayout(v_line_group1)
h_line_group.addLayout(v_line_group2)
RadioGroupBox.setLayout(h_line_group)
###################

#Группа с ответом
AnsGroupBox = QGroupBox('Правильный ответ')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет здесь!')
ans_v_line = QVBoxLayout()
ans_v_line.addWidget(result, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
ans_v_line.addWidget(correct, alignment=Qt.AlignCenter)
AnsGroupBox.setLayout(ans_v_line)
#################

#Группа с кнопками
ButtonGroup = QButtonGroup()
ButtonGroup.addButton(r_btn_1)
ButtonGroup.addButton(r_btn_2)
ButtonGroup.addButton(r_btn_3)
ButtonGroup.addButton(r_btn_4)
##################

h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()
main_v_line = QVBoxLayout()

h_line_1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h_line_2.addWidget(RadioGroupBox)
h_line_2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
h_line_3.addWidget(btn)

main_v_line.addLayout(h_line_1)
main_v_line.addLayout(h_line_2)
main_v_line.addLayout(h_line_3)
