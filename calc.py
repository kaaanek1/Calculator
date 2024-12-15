import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit
from PyQt5.QtGui import QFont

class Calculator(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.initUI(width, height)

    def initUI(self, width, height):
        self.setWindowTitle('Калькулятор')
        self.setGeometry(100, 100, width, height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.result_field = QLineEdit()
        self.result_field.setFixedHeight(50)  # Увеличиваем высоту текстового поля
        self.layout.addWidget(self.result_field, 0, 0, 1, 4)

        # Устанавливаем размер шрифта пропорционально высоте окна
        font_size = height // 20  # Пропорциональный размер шрифта
        font = QFont("Arial", font_size, QFont.Bold)  # Устанавливаем шрифт Arial, размер и жирность
        self.result_field.setFont(font)  # Применяем шрифт к полю ввода

        # Кнопки для цифр
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]

        # Создание кнопок в цикле
        row, col = 1, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(60, 60)  # Устанавливаем фиксированный размер кнопок
            btn.setFont(font)  # Применяем шрифт к кнопкам
            btn.clicked.connect(self.on_button_click)
            self.layout.addWidget(btn, row, col)

            col += 1
            if col > 3:  # Переход на следующую строку
                col = 0
                row += 1

        self.show()

    def on_button_click(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.result_field.clear()
        elif text == '=':
            try:
                result = eval(self.result_field.text())
                self.result_field.setText(str(result))
            except Exception as e:
                self.result_field.setText('Ошибка')
        else:
            current_text = self.result_field.text()
            new_text = current_text + text
            self.result_field.setText(new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Запрос параметров окна через консоль
    width = int(input("Введите ширину окна: "))
    height = int(input("Введите высоту окна: "))

    calculator = Calculator(width, height)
    sys.exit(app.exec_())
