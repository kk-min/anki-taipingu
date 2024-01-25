from aqt import mw

DEFAULT_CONFIG = {
    'enable_typing_test': False,
}

def run_on_configuration_change(function):
    mw.addonManager.setConfigUpdatedAction(__name__, lambda *_: function())

class Config:
    def load(self):
        self.config = mw.addonManager.getConfig(__name__)
        if self.config is None:
            self.config = DEFAULT_CONFIG
    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        mw.addonManager.writeConfig(__name__, self.config)

    @property
    def enable_typing_test(self):
        return self.get('enable_typing_test')

    @enable_typing_test.setter
    def enable_typing_test(self, value):
        self.set('enable_typing_test', value)
