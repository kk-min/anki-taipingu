from aqt import mw, gui_hooks

from .typing_dialog import TypingDialog

class TypingTest:
    def __init__(self, config):
        self.config = config
        gui_hooks.reviewer_did_show_question.append(self.typingTest)

    def typingTest(self, card) -> None:
        if not self.config.get('enable_typing_test'):
            return
        keyList = self.config.get('trigger_fields')
        ans = "N/A\n Card text not detected. Please check your config for Taipingu."
        for key in keyList:
            if key in card.note():
                ans = card.note()[key]
                break
        mw.typeWidget = TypingDialog(mw, "Taipingu", ans)
