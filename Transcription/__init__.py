
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
    time_start = models.StringField(blank=True)
    treatment = models.StringField(blank=True)
    load_time = models.IntegerField(blank=True)

    # ---- Task Actions ---- #
    trans_actions = models.LongStringField(blank=True)
    snippet_list = models.LongStringField(blank=True)

    ### --- STATE Q --- ###

    # ----- Mental Readiness ----- #
    mr1 = models.IntegerField(label="How are you feeling right now?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mr2 = models.IntegerField(label="How sleepy are you feeling right now?.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mr3 = models.IntegerField(label="How motivated are you feeling right now?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                   widget=widgets.RadioSelectHorizontal)
    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
                                  widget=widgets.RadioSelectHorizontal)

    # ----- Mental Fatigue ----- #
    mf1 = models.IntegerField(label="If I were to do someting right now, I could keep my thoughts focused on it.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mf2 = models.IntegerField(label="Right now, I could concentrate well.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mf3 = models.IntegerField(label="Currently, it would take a lot of effort to concentrate on something.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mf4 = models.IntegerField(label="My thoughts would easily wander off at the moment.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    ### --- TASK Q --- ###

    # ----- SFSS-2 ----- #
    sfss1 = models.IntegerField(label="I felt I was competent enough to meet the demands of the situation",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss2 = models.IntegerField(label="I did things spontaneously and automatically without having to think.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss3 = models.IntegerField(label="I had a strong sense of what I wanted to do.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss4 = models.IntegerField(label="I had a good idea about how well I was doing while I was involved in the task/activity.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss5 = models.IntegerField(label="I was completely focused on the task at hand.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss6 = models.IntegerField(label="I had a feeling of total control over what I was doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss7 = models.IntegerField(label="I was not worried about what others may have been thinking of me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss8 = models.IntegerField(label="The way time passed seemed to be different from normal.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sfss9 = models.IntegerField(label="I found the experience extremely rewarding.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Skill-Demand-Balance ----- #
    sdb1 = models.IntegerField(label="Compared to all other activities which I partake in, this one is…",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdb2 = models.IntegerField(label="I think that my competence in this area is …",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdb3 = models.IntegerField(label="For me personally, the current demands are …",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Mental Demand ----- #
    tlx = models.IntegerField(label="How much mental and perceptual activity was required (e.g. thinking, deciding, calculating, remembering, looking, searching, etc.?",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'],
                                       [6, '6'], [7, '7'], [8, '8'], [9, '9'], [10, '10'],
                                       [11, '11'], [12, '12'], [13, '13'], [14, '14'], [15, '15'],
                                       [16, '16'], [17, '17'], [18, '18'], [19, '19'], [20, '20'], [21, '21']], widget=widgets.RadioSelectHorizontal)

    # ----- Mind Wandering State ----- #
    mws1 = models.IntegerField(label="I thought about something, which was not related to the situation.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mws2 = models.IntegerField(label="I found myself distracted by other things in mind.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mws3 = models.IntegerField(label="I had so many things in mind.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mws4 = models.IntegerField(label="My mind wandered.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mws5 = models.IntegerField(label="I was daydreaming.",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mws6 = models.IntegerField(label="I did not concentrate on the situation.",
                              choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Misc Controls ----- #
    control_music_liking = models.IntegerField(label="I liked the background music.",
                                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6']], widget=widgets.RadioSelectHorizontal)
    control_music_turnoff = models.IntegerField(label="If it would have been possible, I would have turned off the music.",
                                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6']], widget=widgets.RadioSelectHorizontal)



class Instructions(Page):
    form_model = 'player'

    def vars_for_template(player: Player):
        return {
            "round_number": player.round_number,
        }
    def before_next_page(player, timeout_happened):
        if player.round_number == 1:
            player.treatment = player.participant.treat_order[0]
        if player.round_number == 2:
            player.treatment = player.participant.treat_order[1]


class Task(Page):
    form_model = 'player'
    form_fields = ['trans_actions', 'snippet_list', 'load_time']

    @staticmethod
    def vars_for_template(player: Player):
        imageList = player.participant.trans_imgs_solo
        random.shuffle(imageList)

        return {
            "imageList": imageList,
            "trialTime": 0.1 * 60,
            "treatment": player.treatment,
            "playlist": player.participant.playlist
        }


class TaskQuestionnaire(Page):
    form_model = 'player'
    all_fields = []

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = ['sfss1', 'sfss2', 'sfss3', 'sfss4', 'sfss5', 'sfss6', 'sfss7', 'sfss8', 'sfss9', 'sdb1', 'sdb2',
                       'sdb3']
        random.shuffle(flow_fields)
        all_fields = flow_fields

        mw_fields = ['mws1', 'mws2', 'mws3', 'mws4', 'mws5', 'mws6']
        random.shuffle(mw_fields)
        all_fields += mw_fields

        all_fields += ['tlx', 'control_music_liking', 'control_music_turnoff']

        return all_fields


class StateQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['pleasure', 'arousal', 'mf1', 'mf2', 'mf3', 'mf4']


class Done(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions, Task, TaskQuestionnaire, StateQuestionnaire, Done]