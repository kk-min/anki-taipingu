from aqt.qt import *

class TypingDialog(QDialog):
    def __init__(self, parent, title, ans):
        super().__init__(parent)
        self.setWindowTitle("Taipingu")
        self.setModal(False)
        self.layout = QVBoxLayout(self)
        self.ans = ans
        self.correct = False

        self.label = QLabel(self)
        self.label.setText(self.ans)
        self.label.move(200, 100)
        self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px;")
        self.layout.addWidget(self.label)

        self.lineedit = QLineEdit(self)
        self.label.move(200, 200)
        self.lineedit.setStyleSheet("font-size: 24px; width: 300px;")
        self.layout.addWidget(self.lineedit)
        self.lineedit.returnPressed.connect(self.check)

        self.show()

    def check(self) -> None:
        userInput = self.lineedit.text()

        if self.correct and userInput == self.ans:
            self.exit()

        if userInput == self.ans:
            self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px; color: #70C270;")
            self.label.setText(self.ans + " - Correct!")
            self.correct = True
        else:
            self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px; color: #E50000;")
            self.label.setText(self.ans + " - Incorrect!")
            self.correct = False

    def exit(self) -> None:
        self.close()
