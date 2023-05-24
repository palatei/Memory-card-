
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

window.setLayout(main_v_line)

def show_answer():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn.setText('Следующий вопрос')

def show_question():
    ButtonGroup.setExclusive(False)
    r_btn_1.setChecked(False)
    r_btn_2.setChecked(False)
    r_btn_3.setChecked(False)
    r_btn_4.setChecked(False)
    ButtonGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn.setText('Ответить')


 def test():
     if btn.text() == 'Ответить':
         show_answer()
     else:
         show_question()

answers = [r_btn_1, r_btn_2, r_btn_3, r_btn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.quest)
    correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_answer()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Не правильно!')
    

btn.clicked.connect(check_answer)
ask(q)
window.show()
app.exec_()
