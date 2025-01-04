
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

    # ----- DEMOGRAPHICS ----- #
    handedness = models.StringField(
        label='Which one is your dominant hand?',
        choices=["Left", "Right", "Both (Ambidextrous)"]
    )

    english = models.StringField(
        label='Please indicate the level of your English language proficiency.',
        choices=["A1 Beginner – I can understand and use familiar everyday expressions and very basic phrases.",
                 "A2 Elementary English – I can understand sentences and frequently used expressions related to areas of most immediate relevance.",
                 "B1 Intermediate English – I understand the main points of clear input on familiar matters regularly encountered in work, school, etc.",
                 "B2 Upper-Intermediate English – I understand the main ideas of complex text on concrete and abstract topics, incl. technical discussions, etc.",
                 "C1 Advanced English – I can understand a wide range of demanding, longer texts, and recognise implicit meaning.",
                 "C2 Proficiency English – I can understand with ease virtually everything I hear or read."]
    )

    age = models.IntegerField(
        label='What is your age?'
    )

    gender = models.StringField(
        label='What is your gender?',
        choices=["Male", "Female", "Diverse"]
    )

    occupation = models.StringField(
        label='What is your current occupation?',
        choices=["Apprentice", "Student", "Employee", "Entrepreneur", "Other"]
    )

    # ----- FATIGUE ----- #
    fatigue_state = models.StringField(
        label='How tired/awake are you right now?',
        choices=['Fully alert, wide awake ',
                 'Very lively, responsive, but not at peak',
                 'Okay, somewhat fresh',
                 'A little tired, less than fresh',
                 'Moderately tired, let down',
                 'Extremely tired, very difficult to concentrate',
                 'Completely exhausted, unable to function effectively']
    )

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Payout Token ----- #
    pay_tok = models.StringField(label='Please enter the token we gave you before.')


class Welcome(Page):
    form_model = 'player'


class IntroQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'handedness', 'english', 'fatigue_state', 'occupation', 'pleasure', 'arousal']


class RestEO(Page):
    form_model = 'player'
    form_fields = ['rest_actions_eo']


class RestEC(Page):
    form_model = 'player'
    form_fields = ['rest_actions_ec']


page_sequence = [Welcome, IntroQuestionnaire, RestEO, RestEC]