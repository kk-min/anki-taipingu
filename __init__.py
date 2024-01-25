from aqt import mw, gui_hooks
from aqt.utils import showInfo, showCritical
from aqt.qt import *

class TypingDialog(QDialog):
    def __init__(self, parent, title, ans):
        super().__init__(parent)
        self.setWindowTitle("Taipingu")
        self.setModal(False)
        self.layout = QVBoxLayout(self)
        self.ans = ans

        self.label = QLabel(self)
        self.label.setText(ans)
        self.label.move(200, 100)
        self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px;")
        self.layout.addWidget(self.label)

        self.lineedit = QLineEdit(self)
        self.label.move(200, 200)
        self.lineedit.setStyleSheet("font-size: 24px; width: 300px;")
        self.layout.addWidget(self.lineedit)

        self.b1 = QPushButton("Ok", self)
        self.label.move(200, 300)
        self.b1.setStyleSheet("font-size: 24px; width: 300px;")
        self.b1.clicked.connect(self.check)
        self.layout.addWidget(self.b1)

        self.show()

    def check(self):
        userInput = self.lineedit.text()
        if userInput == self.ans:
            self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px; color: #70C270;")
            self.label.setText(self.ans + " - Correct!")
        else:
            self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px; color: #E50000;")
            self.label.setText(self.ans + " - Incorrect!")

    def exit(self):
        self.close()

def typingTest(card):
    keyList = ['Expression', 'Key', 'Spelling']
    ans = "N/A"
    for key in keyList:
        if key in card.note():
            ans = card.note()[key]
            break
    mw.typeWidget = TypingDialog(mw, "Taipingu", ans)

gui_hooks.reviewer_did_show_question.append(typingTest)
