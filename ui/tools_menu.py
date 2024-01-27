from aqt import mw, gui_hooks
from aqt.qt import QAction, Callable
from ..config import Config, run_on_configuration_change

TITLE = "Taipingu"

class DropdownMenu:
    def __init__(self, label: str, config: Config):
        self.label = label
        self.config = config
        self.menu = mw.form.menuTools.addMenu(TITLE)
        self.menu_enable_typing_test = self.checkable()

        self.menu.addAction(self.menu_enable_typing_test)
        gui_hooks.state_did_change.append(self.adjust_menu)

    # change config to enable/disable typing test
    def set_enable_typing_test(self, enabled: bool) -> None:
        self.config.enable_typing_test = enabled

    # a tiny helper for menu items, since type checking is broken there
    def checkable(self) -> QAction:
        action = QAction(self.label, mw, checkable=True)  # noqa
        action.triggered.connect(self.set_enable_typing_test)  # noqa
        return action

    # adjust menu items when config changes
    def adjust_menu(self, old, new) -> None:
        self.menu_enable_typing_test.setChecked(self.config.enable_typing_test)

    # use decorator to run this function whenever config changes
    @run_on_configuration_change
    def on_config_change(self) -> None:
        self.config.load()
        self.adjust_menu(None, None)
