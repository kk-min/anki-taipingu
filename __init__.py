from aqt import mw, gui_hooks
from aqt.utils import showInfo, showCritical
from aqt.qt import *

from .config import Config, run_on_configuration_change

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

    def check(self):
        if self.correct:
            self.exit()
        userInput = self.lineedit.text()
        if userInput == self.ans:
            self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px; color: #70C270;")
            self.label.setText(self.ans + " - Correct!")
            self.correct = True
        else:
            self.label.setStyleSheet("font-size: 24px; text-align: center; width: 300px; color: #E50000;")
            self.label.setText(self.ans + " - Incorrect!")

    def exit(self):
        self.close()

# a tiny helper for menu items, since type checking is broken there
def checkable(title: str, on_click: Callable[[bool], None]) -> QAction:
    action = QAction(title, mw, checkable=True)  # noqa
    action.triggered.connect(on_click)  # noqa
    return action

def typingTest(card):
    if not config.get('enable_typing_test'):
        return
    keyList = config.get('trigger_fields')
    ans = "N/A"
    for key in keyList:
        if key in card.note():
            ans = card.note()[key]
            break
    mw.typeWidget = TypingDialog(mw, "Taipingu", ans)

# load config object
config = Config()
config.load()

# create checkbox menu item for Taipingu under 'Tools'
def set_enable_typing_test(enabled: bool) -> None:
    config.enable_typing_test = enabled

menu_enable_typing_test = checkable(title="Enable typing test", on_click=set_enable_typing_test)

def adjust_menu(old, new) -> None:
    menu_enable_typing_test.setChecked(config.enable_typing_test)

# add Taipingu menu item to Tools menu
menu_taipingu = mw.form.menuTools.addMenu("Taipingu")
menu_taipingu.addAction(menu_enable_typing_test)

gui_hooks.state_did_change.append(adjust_menu)

@run_on_configuration_change
def on_config_change() -> None:
    config.load()
    adjust_menu(None, None)

gui_hooks.reviewer_did_show_question.append(typingTest)
