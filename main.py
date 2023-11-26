import io
import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

main_template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="show_btn">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>30</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Отобразить</string>
    </property>
   </widget>
   <widget class="QTableWidget" name="tableWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>100</y>
      <width>741</width>
      <height>441</height>
     </rect>
    </property>
   </widget>
   <widget class="QPushButton" name="add_btn">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>30</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Добавить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="edit_btn">
    <property name="geometry">
     <rect>
      <x>570</x>
      <y>30</y>
      <width>141</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Изменить</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''

template = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>760</width>
    <height>421</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>140</y>
      <width>41</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>id</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_7">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>260</y>
      <width>91</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Объем</string>
    </property>
   </widget>
   <widget class="QComboBox" name="comboBox">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>40</y>
      <width>171</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <item>
     <property name="text">
      <string>Добавить</string>
     </property>
    </item>
    <item>
     <property name="text">
      <string>Изменить</string>
     </property>
    </item>
   </widget>
   <widget class="QLineEdit" name="name">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>195</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>300</y>
      <width>61</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Вид</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="price">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>200</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QPushButton" name="apply_btn">
    <property name="geometry">
     <rect>
      <x>260</x>
      <y>40</y>
      <width>151</width>
      <height>51</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Применить</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="weigh">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>260</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>140</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Описание</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>400</x>
      <y>200</y>
      <width>71</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Цена</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="roasting">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>250</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="id">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>140</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>190</y>
      <width>61</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Имя</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>243</y>
      <width>131</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
    <property name="text">
     <string>Прожарка</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="description">
    <property name="geometry">
     <rect>
      <x>530</x>
      <y>140</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
   <widget class="QLineEdit" name="type">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>305</y>
      <width>171</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>20</pointsize>
     </font>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>760</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''


class Coffee(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(main_template)
        uic.loadUi(f, self)
        self.initUI()

    def initUI(self):
        db = sqlite3.connect('coffee.sqlite')
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


class addEditFormWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        f = io.StringIO(template)
        uic.loadUi(f, self)

        self.db = sqlite3.connect('coffee.sqlite')
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
