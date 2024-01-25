from aqt import mw

tag = mw.addonManager.addonFromModule(__name__)

def run_on_configuration_change(function):
    mw.addonManager.setConfigUpdatedAction(tag, lambda *_: function())

class Config:
    def load(self):
        self.config = mw.addonManager.getConfig(tag)
    def get(self, key):
        return self.config.get(key)

    def set(self, key, value):
        self.config[key] = value
        mw.addonManager.writeConfig(tag, self.config)

    @property
    def enable_typing_test(self):
        return self.get('enable_typing_test')

    @enable_typing_test.setter
    def enable_typing_test(self, value):
        self.set('enable_typing_test', value)
