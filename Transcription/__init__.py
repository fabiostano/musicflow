
from otree.api import *
import random
from os import walk
from os.path import join
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Transcription'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2

class Subsession(BaseSubsession):
    pass

def creating_session(subsession: Subsession):
    # Get all the snippets
    root = '_static/snippets/'
    trans_imgs = [join(path, name) for path, subdirs, files in walk(root) for name in files]
    # Remove the '_static/' part again
    trans_imgs = [s.replace('_static/', '') for s in trans_imgs]
    # Remove other files
    trans_imgs = [f for f in trans_imgs if (f.endswith('.jpg') | f.endswith('.png'))]

    # Shuffle the snippets
    random.shuffle(trans_imgs)

    for p in subsession.get_players():
        p.participant.trans_imgs_solo = trans_imgs

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    time_start = models.StringField()

    # ---- Task Actions ---- #
    trans_actions = models.LongStringField(blank=True)
    snippet_list = models.LongStringField(blank=True)

    ### --- STATE Q --- ###

    # ----- Mental Readiness ----- #
    mr1 = models.IntegerField(label="How are you feeling right now?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mr2 = models.IntegerField(label="How sleepy are you feeling right now?.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mr3 = models.IntegerField(label="How motivated are you feeling right now?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                   widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                  widget=widgets.RadioSelectHorizontal)

    # ----- Mental Fatigue ----- #
    mf1 = models.IntegerField(label="If I were to do someting right now, I could keep my thoughts focused on it.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mf2 = models.IntegerField(label="Right now, I could concentrate well.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mf3 = models.IntegerField(label="Currently, it would take a lot of effort to concentrate on something.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mf4 = models.IntegerField(label="My thoughts would easily wander off at the moment.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    ### --- TASK Q --- ###

    # ----- SFSS-2 ----- #
    sfss1 = models.IntegerField(label="I felt I was competent enough to meet the demands of the situation",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss2 = models.IntegerField(label="I did things spontaneously and automatically without having to think.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss3 = models.IntegerField(label="I had a strong sense of what I wanted to do.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss4 = models.IntegerField(label="I had a good idea about how well I was doing while I was involved in the task/activity.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss5 = models.IntegerField(label="I was completely focused on the task at hand.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss6 = models.IntegerField(label="I had a feeling of total control over what I was doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss7 = models.IntegerField(label="I was not worried about what others may have been thinking of me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss8 = models.IntegerField(label="The way time passed seemed to be different from normal.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sfss9 = models.IntegerField(label="I found the experience extremely rewarding.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Skill-Demand-Balance ----- #
    sdb1 = models.IntegerField(label="Compared to all other activities which I partake in, this one is…",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdb2 = models.IntegerField(label="I think that my competence in this area is …",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    sdb3 = models.IntegerField(label="For me personally, the current demands are …",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Mental Demand ----- #
    tlx = models.IntegerField(label="How much mental and perceptual activity was required (e.g. thinking, deciding, calculating, remembering, looking, searching, etc.?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                                       [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'],
                                       [11, '11'], [12, '12'], [13, '13'], [14, '14'], [15, '15'],
                                       [16, '16'], [17, '17'], [18, '18'], [19, '19'], [20, '20'], [21, '21']])

    # ----- Mind Wandering State ----- #
    mws1 = models.IntegerField(label="I thought about something, which was not related to the situation.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mws2 = models.IntegerField(label="I found myself distracted by other things in mind.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mws3 = models.IntegerField(label="I had so many things in mind.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mws4 = models.IntegerField(label="My mind wandered.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mws5 = models.IntegerField(label="I was daydreaming.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mws6 = models.IntegerField(label="I did not concentrate on the situation.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Misc Controls ----- #
    control_text_interest = models.IntegerField(label="I thought the paper was an interesting  read.",
                                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    control_music_liking = models.IntegerField(label="I liked the background music.",
                                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    control_music_turnoff = models.IntegerField(label="If it would have been possible, I would have turned off the music.",
                                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])



class Instructions(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == 1

    def before_next_page(player, timeout_happened):
        print("test")

class Task(Page):
    form_model = 'player'
    form_fields = ['trans_actions', 'snippet_list']

    @staticmethod
    def vars_for_template(player: Player):
        imageList = player.participant.trans_imgs_solo
        random.shuffle(imageList)

        return {
            "imageList": imageList,
            "trialTime": 10 * 60
        }

class TaskQuestionnaire(Page):
    form_model = 'player'
    all_fields = []

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = []
        random.shuffle(flow_fields)
        flow_fields += []
        all_fields = flow_fields

        tlx_fields = []
        all_fields += tlx_fields

        return all_fields

class StateQuestionnaire(Page):
    form_model = 'player'
    all_fields = []

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = []
        random.shuffle(flow_fields)
        all_fields = flow_fields

        tlx_fields = []
        all_fields += tlx_fields

        return all_fields

class Done(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions, Task, TaskQuestionnaire, StateQuestionnaire, Done]