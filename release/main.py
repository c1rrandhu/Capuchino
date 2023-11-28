import sys
import sqlite3
from main_design import Ui_MainWindow
from addEditCoffeeForm import Ui_add_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class Coffee(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        db = sqlite3.connect('release/data/coffee.sqlite')
        cur = db.cursor()
        self.res = cur.execute('SELECT * FROM main').fetchall()
        headers = ['id', 'name', 'roasting', 'type', 'description', 'price', 'weigh']

        self.tableWidget.setRowCount(len(self.res))
        self.tableWidget.setColumnCount(len(self.res[0]))
        self.tableWidget.setHorizontalHeaderLabels(headers)

        self.show_btn.clicked.connect(self.run)
        self.add_btn.clicked.connect(self.openForm)
        self.edit_btn.clicked.connect(self.openForm)

    def run(self):
        self.initUI()
        for x in range(len(self.res)):
            for y in range(len(self.res[0])):
                self.tableWidget.setItem(x, y, QTableWidgetItem(str(self.res[x][y])))

    def openForm(self):
        form = addEditFormWidget(parent=self)
        form.show()


class addEditFormWidget(QMainWindow, Ui_add_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.db = sqlite3.connect('release/data/coffee.sqlite')
        self.apply_btn.clicked.connect(self.apply_info)

    def apply_info(self):
        try:
            status = self.comboBox.currentText()
            self.statusBar().showMessage('')
            cur = self.db.cursor()
            db_id = cur.execute('SELECT id FROM main').fetchall()[-1][0]

            data = [self.id.text(), self.name.text(), self.roasting.text(), self.type.text(),
                    self.description.text(), self.price.text(), self.weigh.text()]

            if status == 'Добавить':
                cur.execute(f'''INSERT INTO main VALUES({int(db_id) + 1}, "{data[1]}", 
                                    "{data[2]}", "{data[3]}", "{data[4]}", "{data[5]}", "{data[6]}")''')
            else:
                if int(db_id) < int(data[0]) or int(data[0]) <= 0:
                    raise Exception
                cur.execute(f'''UPDATE main SET name = "{data[1]}", roasting = "{data[2]}", type = "{data[3]}", 
                        description = "{data[4]}", price = "{data[5]}", weigh = "{data[6]}" WHERE id = "{data[0]}"''')
            self.statusBar().showMessage('Запрос выполнен!')
            self.db.commit()
        except Exception:
            self.statusBar().showMessage('ERROR!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Coffee()
    ex.show()
    sys.exit(app.exec())
