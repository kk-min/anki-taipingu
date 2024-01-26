from aqt import mw, gui_hooks
from aqt.qt import Callable, QAction

from .ui.typing_dialog import TypingDialog
from .config import Config, run_on_configuration_change


# load config object
config = Config()
config.load()

# a tiny helper for menu items, since type checking is broken there
def checkable(title: str, on_click: Callable[[bool], None]) -> QAction:
    action = QAction(title, mw, checkable=True)  # noqa
    action.triggered.connect(on_click)  # noqa
    return action

def typingTest(card) -> None:
    if not config.get('enable_typing_test'):
        return
    keyList = config.get('trigger_fields')
    ans = "N/A"
    for key in keyList:
        if key in card.note():
            ans = card.note()[key]
            break
    mw.typeWidget = TypingDialog(mw, "Taipingu", ans)

# create checkbox menu item for Taipingu under 'Tools'
def set_enable_typing_test(enabled: bool) -> None:
    config.enable_typing_test = enabled

def adjust_menu(old, new) -> None:
    menu_enable_typing_test.setChecked(config.enable_typing_test)

@run_on_configuration_change
def on_config_change() -> None:
    config.load()
    adjust_menu(None, None)

# add Taipingu menu item to Tools menu
menu_taipingu = mw.form.menuTools.addMenu("Taipingu")
menu_enable_typing_test = checkable(title="Enable typing test", on_click=set_enable_typing_test)
menu_taipingu.addAction(menu_enable_typing_test)

gui_hooks.state_did_change.append(adjust_menu)

gui_hooks.reviewer_did_show_question.append(typingTest)
