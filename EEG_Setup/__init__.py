
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'EEG'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    DURATION = 60

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # ----- REST ACTIONS ----- #
    rest_actions_eo = models.StringField(label="")
    rest_actions_ec = models.StringField(label="")
    start_time_eo_m = models.StringField(label="")
    start_time_eo_assr_attended = models.StringField(label="")
    start_time_eo_assr_ignored = models.StringField(label="")

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "duration": C.DURATION
        }


class RestEyesClosed(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "duration": C.DURATION
        }


class RestEyesOpen_Music(Page):
    form_model = 'player'
    form_fields = ['start_time_eo_m']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "playlist": getattr(player.participant, 'playlist', 'lofi.mp3'),
            "duration": C.DURATION
        }


class RestEyesOpen_ASSR_attended(Page):
    form_model = 'player'
    form_fields = ['start_time_eo_assr_attended']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "playlist": getattr(player.participant, 'playlist', 'lofi.mp3'),
            "duration": 30
        }

class RestEyesOpen_ASSR_ignored(Page):
    form_model = 'player'
    form_fields = ['start_time_eo_assr_ignored']

    @staticmethod
    def vars_for_template(player: Player):
        return {
            "playlist": getattr(player.participant, 'playlist', 'lofi.mp3'),
            "duration": 30
        }


page_sequence = [RestEyesClosed, RestEyesOpen, RestEyesOpen_Music, RestEyesOpen_ASSR_attended, RestEyesOpen_ASSR_ignored]