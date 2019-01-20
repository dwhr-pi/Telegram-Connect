from src.skill.i18n.language_model import LanguageModel

class NonVerboseLanguageModel(LanguageModel):
    def __init__(self, locale, non_verbose_mode):
        super().__init__(locale)

        if locale == "de-DE":
            self.set_german_language_model()
            if non_verbose_mode:
                self.set_german_non_verbose_model()
        else:
            self.set_english_language_model()
            if non_verbose_mode:
                self.set_english_non_verbose_model()
                


    def set_german_non_verbose_model(self):
        pass


    def set_english_non_verbose_model(self):
        ### SendIntent ###
        self.FIRST_NAME = "First name?"
        self.MESSAGE = "{}. Telegram?"
        self.NO_CONTACT = "I found: <break time='25ms'/> 1 <break time='75ms'/> {}, <break time='50ms'/> 2 <break time='75ms'/> {}, and <break time='50ms'/> 3 <break time='75ms'/> {}."
        self.NO_CONTACT_2 = "I found <break time='25ms'/> 1 <break time='75ms'/> {}, and <break time='50ms'/> 2 <break time='75ms'/> {}."

        ### MessageIntent ###
        self.REPLY = "<break time='50ms'/> Reply or next telegram?"
        self.NEW_TELEGRAMS = "New telegrams from: "
        self.NO_MORE_TELEGRAMS = "Done. Anything else?"
        self.NO_TELEGRAMS = "No new telegrams. Anything else?"
        self.GROUP_INTRO = "In {}: <break time='100ms'/>"
        self.GROUP_MESSAGE_INTRO = "{} wrote: <break time='50ms'/>"
        self.PERSONAL_CHAT_INTRO = "{} wrote: <break time='50ms'/>"

        ### LaunchIntent ###
        self.USER_HAS_TELEGRAMS = "Welcome. Do you want to hear your new Telegrams?"
        self.WELCOME = "Welcome"

        ### ReplyIntent ###
        self.TELEGRAM_SENT = "A Telegram was sent to {}. <break time='100ms'/>"
        self.MESSAGE_2 = "What is the Telegram?"

        ### YesIntent ###
        self.HELP_USER = "Sent Telegram or check Telegrams?"

        ## SpeedDialIntent ##
        self.SPEED_DIAL = "Number of speed dial contact?"
        self.NO_SPEED_DIAL_CONTACT ="No speed dial contact with that number. Anything else?"