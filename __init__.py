from aqt import mw, gui_hooks

from .ui.typing_dialog import TypingDialog
from .config import Config, run_on_configuration_change
from .ui.tools_menu import DropdownMenu


# load config object
config = Config()
config.load()

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

# add Taipingu menu item to Tools menu
tools_menu = DropdownMenu("Enable typing test", config)

gui_hooks.reviewer_did_show_question.append(typingTest)
