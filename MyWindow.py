from PyQt5 import QtWidgets, QtCore, QtGui
import datetime
class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.SplashScreen)
        desktop = QtWidgets.QApplication.desktop()
        rect = desktop.availableGeometry()
        x = 300; y = 75
        self.setGeometry(rect.width() - x, rect.height() - y, x, y - 20)  # Минимальные размеры
        label = QtWidgets.QLabel(
            f"Дней осталось: {str(self.DaysRemain())}\nТекущая неделя: {self.CurrentWeek()}\nВсего недель: {self.Weeks()}"
            , flags=QtCore.Qt.Window)
        label.setAlignment(QtCore.Qt.AlignHCenter)
        label.setStyleSheet(r"""
            padding: 10px;
            color: white;
            border-bottom-left-radius:50px;
            border-top-left-radius:50px;
            border-width: 3;
            border-style: double;
            border-top-color: red;
            border-left-color:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 red, stop: 1 green);
            border-right-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 red, stop: 1 green);
            border-bottom-color: green;
            background-color: rgba( 0, 0, 0, 1 );      
        """)
        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(label)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

    def CurrentWeek(self):
        a = '1.2.2021'
        a = a.split('.')
        aa = datetime.date(int(a[2]), int(a[1]), int(a[0]))
        bb = datetime.date.today()
        cc = bb - aa - datetime.timedelta(days=aa.weekday())
        dd = str((cc / 7).days + 1)
        return dd.split()[0]

    def DaysRemain(self):
        a = '2021-05-22'
        a = a.split('-')
        aa = datetime.date(int(a[0]), int(a[1]), int(a[2]))
        bb = datetime.date.today()
        cc = aa - bb
        dd = str(cc)
        return dd.split()[0]

    def Weeks(self):
        a = '1.2.2021'
        a = a.split('.')
        b = '22.5.2021'
        b = b.split('.')
        aa = datetime.date(int(a[2]), int(a[1]), int(a[0]))
        bb = datetime.date(int(b[2]), int(b[1]), int(b[0]))
        cc = bb - datetime.timedelta(days=bb.weekday()) - aa + datetime.timedelta(days=aa.weekday())
        dd = str((cc / 7).days + 1)
        return dd.split()[0]

"""
DEBUG
debug1 = '1.2.2021'
debug2 = '22.5.2021'
a = debug1
a = a.split('.')
b = debug2
b = b.split('.')
aa = datetime.date(int(a[2]), int(a[1]), int(a[0]))
bb = datetime.date(int(b[2]), int(b[1]), int(b[0]))

first = aa - datetime.timedelta(days=aa.weekday())
second = bb - datetime.timedelta(days=bb.weekday())

i = 1;
while first <= second:
    print(f"{i})", first)
    first += datetime.timedelta(days=7)
    i+=1
"""