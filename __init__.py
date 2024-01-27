from .config import Config
from .ui.typing_dialog import TypingDialog
from .ui.tools_menu import DropdownMenu
from .ui.typing_test import TypingTest

# load config object
config = Config()
config.load()

# add Taipingu menu item to Tools menu
tools_menu = DropdownMenu("Enable typing test", config)

# add typing test when showing new cards
typing_test = TypingTest(config)
