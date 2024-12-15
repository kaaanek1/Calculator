import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt

import csv

class TableApp(QWidget):
    def __init__(self, width, height, rows, columns):
        super().__init__()
        self.initUI(width, height, rows, columns)

    def initUI(self, width, height, rows, columns):
        self.setWindowTitle('Таблица')
        self.setGeometry(100, 100, width, height)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Создание таблицы
        self.table = QTableWidget(rows, columns)
        self.layout.addWidget(self.table)

        # Кнопки для управления таблицей
        button_layout = QHBoxLayout()

        self.add_button = QPushButton('Добавить строку')
        self.add_button.clicked.connect(self.add_row)
        button_layout.addWidget(self.add_button)

        self.delete_button = QPushButton('Удалить строку')
        self.delete_button.clicked.connect(self.delete_row)
        button_layout.addWidget(self.delete_button)

        self.edit_button = QPushButton('Редактировать ячейку')
        self.edit_button.clicked.connect(self.edit_cell)
        button_layout.addWidget(self.edit_button)

        self.save_button = QPushButton('Сохранить в файл')
        self.save_button.clicked.connect(self.save_to_file)
        button_layout.addWidget(self.save_button)

        self.layout.addLayout(button_layout)

        self.show()

    def add_row(self):
        current_row_count = self.table.rowCount()
        self.table.insertRow(current_row_count)

    def delete_row(self):
        current_row = self.table.currentRow()
        if current_row >= 0:
            self.table.removeRow(current_row)
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите строку для удаления.")

    def edit_cell(self):
        current_row = self.table.currentRow()
        current_column = self.table.currentColumn()
        if current_row >= 0 and current_column >= 0:
            item = self.table.item(current_row, current_column)
            if item is None:
                item = QTableWidgetItem("")
                self.table.setItem(current_row, current_column, item)
            item.setFlags(item.flags() | Qt.ItemIsEditable)
            self.table.editItem(item)
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите ячейку для редактирования.")

    def save_to_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить файл", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if file_name:
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        row_data.append(item.text() if item else "")
                    writer.writerow(row_data)
            QMessageBox.information(self, "Успех", "Данные успешно сохранены в файл.")


app = QApplication(sys.argv)


width = int(input("Введите ширину окна: "))
height = int(input("Введите высоту окна: "))
rows = int(input("Введите количество строк: "))
columns = int(input("Введите количество столбцов: "))

table_app = TableApp(width, height, rows, columns)
sys.exit(app.exec_())