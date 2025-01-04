
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Outro'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.StringField(blank=True)


class ThankYou(Page):
    form_model = 'player'
    form_fields = ['email']


page_sequence = [ThankYou]