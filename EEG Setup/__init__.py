
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Intro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # ----- REST ACTIONS ----- #
    rest_actions_eo = models.StringField(label="")
    rest_actions_ec = models.StringField(label="")
    rest_actions_eo_m = models.StringField(label="")
    rest_actions_ec_m = models.StringField(label="")

class RestEyesOpen(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']


class RestEyesClosed(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']


class RestEyesOpen_Music(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo_m']


class RestEyesClosed_Music(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec_m']



page_sequence = [RestEyesOpen, RestEyesClosed, RestEyesOpen_Music, RestEyesClosed_Music]