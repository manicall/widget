from PyQt5 import QtWidgets, QtCore, QtGui
import datetime
from DialogDate import DialogDate


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.desktop = QtWidgets.QApplication.desktop()
        self.settings = QtCore.QSettings("settings\config.ini", QtCore.QSettings.IniFormat)
        self.label = QtWidgets.QLabel("", flags=QtCore.Qt.Window)
        self.first_date = None
        self.second_date = None

        if not (self.settings.contains('firstDate') and self.settings.contains('secondDate')):
            self.set_date_range()
        else:
            self.first_date = str(self.settings.value("firstDate"))
            self.second_date = str(self.settings.value("secondDate"))

        self.set_window_size()
        self.set_label()

        vbox = QtWidgets.QVBoxLayout()

        vbox.addWidget(self.label)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

    def current_week(self):
        rebuilt_first_date = self.rebuild_date(self.first_date)
        day = datetime.date.today() - rebuilt_first_date - datetime.timedelta(days=rebuilt_first_date.weekday())
        current_week = str((day / 7).days + 1)
        return current_week.split()[0]

    def days_remain(self):
        rebuilt_second_date = self.rebuild_date(self.second_date)
        different = rebuilt_second_date - datetime.date.today()
        return str(different).split()[0]

    def weeks(self):
        rebuilt_first_date = self.rebuild_date(self.first_date)
        rebuilt_second_date = self.rebuild_date(self.second_date)

        range_of_days = rebuilt_second_date - datetime.timedelta(days=rebuilt_second_date.weekday()) - rebuilt_first_date + datetime.timedelta(days=rebuilt_first_date.weekday())

        num_of_weeks = str((range_of_days / 7).days + 1)
        return num_of_weeks.split()[0]

    def rebuild_date(self, date):
        split_date = date.split('-')
        return datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))

    def contextMenuEvent(self, event):
        # действия
        acts = [QtWidgets.QAction('закрыть', self), QtWidgets.QAction('сменить даты', self)]

        # функции
        funcs = [lambda event: self.close(), lambda event: self.change_date_range()]

        # соединить функцию и действия
        for i in range(len(acts)):
            acts[i].triggered.connect(funcs[i])
        # вызвать меню
        QtWidgets.QMenu.exec(acts, event.globalPos(), acts[0], self)

    def set_window_size(self):
        rect = self.desktop.availableGeometry()
        x = rect.width() / 8;
        y = rect.height() / 16
        self.setGeometry(rect.width() - x, rect.height() - y, x, y)  # Минимальные размеры

    def set_label(self):
        self.label.setText(f"Дней осталось: {str(self.days_remain())}\n"
                           f"Текущая неделя: {self.current_week()}\n"
                           f"Всего недель: {self.weeks()}")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.label.setStyleSheet(r"""
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

    def change_date_range(self):
        self.set_date_range()
        self.set_label()

    def set_date_range(self):
        dialog = DialogDate()
        result = dialog.exec()
        if result == QtWidgets.QDialog.Accepted:
            self.settings.setValue('firstDate', dialog.first_date)
            self.settings.setValue('secondDate', dialog.last_date)
            self.settings.sync()

            self.first_date = str(self.settings.value('firstDate'))
            self.second_date = str(self.settings.value('secondDate'))
        else:
            exit(0)
