
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

    ### --- TRAIT Q --- ###

    # ----- SDFS-2 ----- #
    sdfs1 = models.IntegerField(label="I feel I am competent enough to meet the demands of the situation",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs2 = models.IntegerField(label="I do things spontaneously and automatically without having to think.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs3 = models.IntegerField(label="I have a strong sense of what I want to do.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs4 = models.IntegerField(
        label="I have a good idea about how well I am doing while I am involved in the task/activity.",
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs5 = models.IntegerField(label="I am completely focused on the task at hand.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs6 = models.IntegerField(label="I have a feeling of total control over what I am doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs7 = models.IntegerField(label="I am not worried about what others may be thinking of me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs8 = models.IntegerField(label="The way time passes seems to be different from normal.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdfs9 = models.IntegerField(label="I find the experience extremely rewarding.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    ac_sdfs = models.IntegerField(
        label='This is an attention check. Please select the answer on the far right.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']])

    # ----- Extraversion ----- #
    big_five_e1 = models.IntegerField(
        label='I would describe myself as someone who is reserved.',
        choices=[1, 2, 3, 4, 5])
    big_five_e2 = models.IntegerField(
        label='I would describe myself as someone who is talkative.',
        choices=[1, 2, 3, 4, 5])
    big_five_e3 = models.IntegerField(
        label='I would describe myself as someone who generates a lot of enthusiasm.',
        choices=[1, 2, 3, 4, 5])
    big_five_e4 = models.IntegerField(
        label='I would describe myself as someone who is outgoing/sociable.',
        choices=[1, 2, 3, 4, 5])
    big_five_e5 = models.IntegerField(
        label='I would describe myself as someone who is sometimes shy/inhibited.',
        choices=[1, 2, 3, 4, 5])

    # ------ Domain Expertise ------ #
    domain_exp_transcription = models.IntegerField(
        label="I am experienced in transcribing snippets of text.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']])
    domain_exp_research = models.IntegerField(
        label="I am experienced in reading and working with scientific papers.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']])
    domain_exp_reading = models.IntegerField(
        label="I generally like reading.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']])

    # ----- Mind Wandering Trait ----- #
    mwt01 = models.IntegerField(label="I find my thoughts wandering spontaneously.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt02 = models.IntegerField(label="My thoughts tend to be pulled from topic to topic.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt03 = models.IntegerField(label="I mind wander even when I’m supposed to be doing something else.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt04 = models.IntegerField(label="I have difficulty controlling my thoughts.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt05 = models.IntegerField(label="I find it hard to switch my thoughts off.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt06 = models.IntegerField(label="My thoughts are disorganized and `all over the place'.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt07 = models.IntegerField(label="I find it difficult to think about one thing without another thought entering my mind.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt08 = models.IntegerField(label="I find my thoughts are distracting and prevent me from focusing on what I am doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt09 = models.IntegerField(label="I have difficulty slowing my thoughts down and focusing on one thing at a time.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mwt10 = models.IntegerField(label="I find myself flitting back and forth between different thoughts.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    ### --- MUSIC AT WORK TYPE --- ###

    # ----- General ----- #
    mlt01 = models.IntegerField(label="I listen to music while working.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt02 = models.IntegerField(label="I think music can help me to achieve more in certain tasks.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mlt03 = models.IntegerField(label="I listen to music because it helps me to get into the flow state.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt04 = models.IntegerField(label="I listen to music because it helps me to stay in the flow state.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt05 = models.IntegerField(label="I listen to music because it helps me to experience more intense flow states.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mlt06 = models.IntegerField(label="I listen to music because it helps me to block off potential distractions from the outside.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt07 = models.IntegerField(label="I listen to music because it motivates me to get started with my work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt08 = models.IntegerField(label="I listen to music because it motivates me to keep going with my work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt09 = models.IntegerField(label="I listen to music because it makes work more enjoyable.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mlt10 = models.IntegerField(label="I listen to music to make boring tasks less boring.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt11 = models.IntegerField(label="I listen to music mainly if tasks are rather easy for me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mlt12 = models.IntegerField(label="I listen to music for creative tasks (e.g. drafting new ideas).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt13 = models.IntegerField(label="I listen to music for routine tasks (e.g. writing mails).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt14 = models.IntegerField(label="I listen to music for tasks that require lots of analytical thinking (e.g. programming).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt15 = models.IntegerField(label="I listen to music for tasks that require lots of writing and reading.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mlt16 = models.IntegerField(label="",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt17 = models.IntegerField(label="",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt18 = models.IntegerField(label="",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt19 = models.IntegerField(label="",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mlt20 = models.IntegerField(label="",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])


class ThankYou(Page):
    form_model = 'player'
    form_fields = ['email']


page_sequence = [ThankYou]