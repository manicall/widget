# -*- coding: utf-8 -*-
import sys
import MyWindow as win

app = win.QtWidgets.QApplication(sys.argv)
window = win.MyWindow() # Создаем окно
window.show() # Отображаем окно
sys.exit(app.exec_())