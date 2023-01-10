'''
Реализации игры Крестики - Нолики
Первыми ходят Крестики
В конце игры предложится вариант переигровки

Автор: Аванесян Артём
'''

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(295, 338)
        mainWindow.setMinimumSize(QtCore.QSize(295, 338))
        mainWindow.setMaximumSize(QtCore.QSize(295, 338))
        mainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(10, 20, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_7.setCheckable(False)
        self.btn_7.setObjectName("btn_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(90, 20, 20, 271))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 20, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_8.setObjectName("btn_8")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(180, 20, 20, 271))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(190, 20, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(10, 110, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 110, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(190, 110, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_6.setObjectName("btn_6")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(10, 200, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 200, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(190, 200, 91, 91))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(26)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color:rgb(85, 85, 255);")
        self.btn_3.setObjectName("btn_3")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 100, 271, 21))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 190, 271, 21))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.btn_7.raise_()
        self.btn_8.raise_()
        self.btn_9.raise_()
        self.btn_4.raise_()
        self.btn_5.raise_()
        self.btn_6.raise_()
        self.btn_1.raise_()
        self.btn_2.raise_()
        self.btn_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 295, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        self.buttons = (self.btn_1, self.btn_2, self.btn_3, self.btn_4, self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9)
        self.add_functions()

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Крестики - Нолики"))
        self.btn_7.setText(_translate("mainWindow", ""))
        self.btn_8.setText(_translate("mainWindow", ""))
        self.btn_9.setText(_translate("mainWindow", ""))
        self.btn_4.setText(_translate("mainWindow", ""))
        self.btn_5.setText(_translate("mainWindow", ""))
        self.btn_6.setText(_translate("mainWindow", ""))
        self.btn_1.setText(_translate("mainWindow", ""))
        self.btn_2.setText(_translate("mainWindow", ""))
        self.btn_3.setText(_translate("mainWindow", ""))

    def add_functions(self):
        '''
        Добавляем функции обработки кнопок
        '''
        #
        # for i in range(len(self.buttons)):
        #    self.buttons[i].clicked.connect(lambda: self.write_symbol(self.buttons[i], i+1))
        self.btn_1.clicked.connect(lambda: self.write_symbol(self.btn_1, 1))
        self.btn_2.clicked.connect(lambda: self.write_symbol(self.btn_2, 2))
        self.btn_3.clicked.connect(lambda: self.write_symbol(self.btn_3, 3))
        self.btn_4.clicked.connect(lambda: self.write_symbol(self.btn_4, 4))
        self.btn_5.clicked.connect(lambda: self.write_symbol(self.btn_5, 5))
        self.btn_6.clicked.connect(lambda: self.write_symbol(self.btn_6, 6))
        self.btn_7.clicked.connect(lambda: self.write_symbol(self.btn_7, 7))
        self.btn_8.clicked.connect(lambda: self.write_symbol(self.btn_8, 8))
        self.btn_9.clicked.connect(lambda: self.write_symbol(self.btn_9, 9))

    # Созданы элеменьы символа, доски и флаги
    buttons=()
    symbol = 'X'
    board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    result = False
    draw = True

    def write_symbol(self, btn, index):
        '''
        Вывод символа на поле
        '''
        if self.symbol == 'X':
            btn.setText(self.symbol)
            btn.setStyleSheet("background-color:rgb(85, 85, 255);color:#FF5656")
            btn.setEnabled(False)
            self.board[index] = self.symbol
            self.result = self.check_win(self.board, self.symbol)
            # Если кто то выиграл
            if self.result:
                self.not_draw_game(self.symbol)
            else:
                self.symbol = 'O'
            self.draw = self.check_draw()
            # Если ничья
            if not self.draw:
                self.draw_game()


        else:
            btn.setText(self.symbol)
            btn.setEnabled(False)
            btn.setStyleSheet("background-color:rgb(85, 85, 255);color:#00c77b")
            self.board[index] = self.symbol
            self.result = self.check_win(self.board, self.symbol)
            # Если кто то выиграл
            if self.result:
                self.not_draw_game(self.symbol)
            else:
                self.symbol = 'X'
            self.draw = self.check_draw()
            # Если ничья
            if not self.draw:
                self.draw_game()

    def check_draw(self):
        '''
        Проверка на ничью
        '''
        for i in self.board:
            if i == " ":
                return True
        return False

    def check_win(self, board, marker):
        '''
        Проверка на выигрыш какого-либо игрока
        '''
        if (board[1] == marker and board[2] == marker and board[3] == marker) or (
                board[4] == marker and board[5] == marker and board[6] == marker) or (
                board[7] == marker and board[8] == marker and board[9] == marker) or (
                board[1] == marker and board[4] == marker and board[7] == marker) or (
                board[2] == marker and board[5] == marker and board[8] == marker) or (
                board[3] == marker and board[6] == marker and board[9] == marker) or (
                board[1] == marker and board[5] == marker and board[9] == marker) or (
                board[3] == marker and board[5] == marker and board[7] == marker):
            return True
        else:
            return False

    def not_draw_game(self, symbol):
        '''
        Функция для вызова модального окна в случае ничьи
        '''
        modal_window = QtWidgets.QMessageBox()
        modal_window.setWindowTitle('Конец игры')
        modal_window.setText(f'Игрок {symbol} выиграл! Хотите сыграть снова?')
        modal_window.setIcon(QtWidgets.QMessageBox.Information)
        button_ok = QtWidgets.QMessageBox.Ok
        button_cancel = QtWidgets.QMessageBox.Cancel

        modal_window.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        modal_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
        modal_window.buttonClicked.connect(self.choose_end_scene)

        modal_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        modal_window.exec()

    def draw_game(self):
        '''
        Функция для вызова модального окна в случае чьей-либо победы
        '''
        modal_window = QtWidgets.QMessageBox()
        modal_window.setWindowTitle('Конец игры')
        modal_window.setText('Ничья! Хотите сыграть снова?')
        modal_window.setIcon(QtWidgets.QMessageBox.Information)
        button_ok = QtWidgets.QMessageBox.Ok
        button_cancel = QtWidgets.QMessageBox.Cancel

        modal_window.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
        modal_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
        modal_window.buttonClicked.connect(self.choose_end_scene)

        modal_window.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint)
        modal_window.exec()

    def choose_end_scene(self, btn):
        if btn.text() == 'OK':
            self.btn_1.setEnabled(True)
            self.btn_2.setEnabled(True)
            self.btn_3.setEnabled(True)
            self.btn_4.setEnabled(True)
            self.btn_5.setEnabled(True)
            self.btn_6.setEnabled(True)
            self.btn_7.setEnabled(True)
            self.btn_8.setEnabled(True)
            self.btn_9.setEnabled(True)

            self.symbol = 'X'
            self.board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            self.result = False

            self.btn_7.setText('')
            self.btn_8.setText('')
            self.btn_9.setText('')
            self.btn_4.setText('')
            self.btn_5.setText('')
            self.btn_6.setText('')
            self.btn_1.setText('')
            self.btn_2.setText('')
            self.btn_3.setText('')

        else:
            mainWindow.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
