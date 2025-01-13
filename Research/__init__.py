
from otree.api import *
import random
import pandas as pd
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Research'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2
    PAPERS = [['Highlighting Strategies for Better Reading',
               'Ever wondered if highlighting fewer words could make you a better reader? This study explores how '
               'limiting highlights can boost understanding and help you remember what matters most.'],
              ['Letting Machines Handle the Small Stuff',
               'What if a machine could stimulate your muscles and move them for background tasks, while you do '
               'something else simultaneously? This paper explores how this concept can lighten your mental load.'],
              ['The Hidden Risks of Mental Health Apps',
               'Mental health apps promise help, but could they accidentally cause harm? By analyzing thousands of '
               'user reviews, this study uncovers potential risks and offers ideas for safer, smarter apps.'],
              ['Follow Your Daily Goals with Self-Voice Alarms',
               'Could hearing your own voice remind you to stick to your goals? This study tests how personalized'
               'voice alarms can improve focus and help you get more done every day.'],
              ['Voice-Based Online Dating Apps',
               'What if online dating skipped profile pictures and let your voice do the talking? This study explores '
               'a voice-first dating app that’s changing how people connect and communicate.'],
              ['TikTok and Mental Health: Laughing Through Hard Times',
               'How do young people use TikTok to share their struggles with mental health? This research dives into '
               'how humor and creativity build supportive communities on the platform.'],
              ['Gen Z and Online Information Trust',
               'How does Gen Z decide what’s true online? This study reveals how social connections shape their '
               'understanding of information in a world full of noise.'],
              ['Gaming Without Sight: How the Blind Play Mainstream Games',
               'How do blind players enjoy games designed for sighted audiences? This research explores their '
               'strategies and reveals how design can unintentionally help or hinder accessibility.']
              ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    time_start = models.StringField(blank=True)
    treatment = models.StringField(blank=True)
    notes = models.LongStringField(blank=True)
    load_time = models.IntegerField(blank=True)

    selected_paper = models.StringField(
        choices=['Highlighting Strategies for Better Reading',
                 'Letting Machines Handle the Small Stuff',
                 'The Hidden Risks of Mental Health Apps',
                 'Follow Your Daily Goals with Self-Voice Alarms',
                 'Voice-Based Online Dating Apps',
                 'TikTok and Mental Health: Laughing Through Hard Times',
                 'Gen Z and Online Information Trust',
                 'Gaming Without Sight: How the Blind Play Mainstream Games'],
        label="Select the paper you'd like to work on.",
        blank=False,
    )

    ### --- STATE Q --- ###

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
    sdb1 = models.IntegerField(label="Compared to all other activities which I partake in, this one was…",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdb2 = models.IntegerField(label="I think that my competence in this area is …",
                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdb3 = models.IntegerField(label="For me personally, the task demands were …",
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
    control_text_interest = models.IntegerField(label="I thought the paper was an interesting  read.",
                                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    control_music_liking = models.IntegerField(label="I enjoyed the background music.",
                                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6']], widget=widgets.RadioSelectHorizontal)
    control_music_turnoff = models.IntegerField(label="If it would have been possible, I would have turned off the music.",
                                               choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5'], [6, '6']], widget=widgets.RadioSelectHorizontal)



class Instructions1(Page):
    form_model = 'player'
    form_fields = ["selected_paper"]

    def is_displayed(player):
        return player.round_number == 1

    def vars_for_template(player):
        return {
            "papers": C.PAPERS,
            "round_number": player.round_number
        }

    def before_next_page(player, timeout_happened):
        player.participant.paper_r1 = player.selected_paper

        treatments = ['music', 'control']
        random.shuffle(treatments)

        player.participant.treat_order = treatments
        player.treatment = player.participant.treat_order[0]


class Instructions2(Page):
    form_model = 'player'
    form_fields = ["selected_paper"]

    def is_displayed(player):
        return player.round_number == 2


    def vars_for_template(player):
        return {
            "papers": C.PAPERS,
            "round_number": player.round_number,
            "paper_r1": player.participant.paper_r1
        }

    def before_next_page(player, timeout_happened):
        player.participant.paper_r1 = player.selected_paper

        player.treatment = player.participant.treat_order[1]




class Task(Page):
    form_model = 'player'
    form_fields = ['notes', 'load_time']

    def vars_for_template(player):
        paper_url_map = {
            "Highlighting Strategies for Better Reading": "highlighting_strategies.pdf",
            "Letting Machines Handle the Small Stuff": "ems_background.pdf",
            "The Hidden Risks of Mental Health Apps": "mental_health_apps.pdf",
            "Follow Your Daily Goals with Self-Voice Alarms": "self_voice.pdf",
            "Voice-Based Online Dating Apps": "voice_dating.pdf",
            "TikTok and Mental Health: Laughing Through Hard Times": "tik_tok_mental_health.pdf",
            "Gen Z and Online Information Trust": "genz_truth.pdf",
            "Gaming Without Sight: How the Blind Play Mainstream Games": "blind_gaming.pdf"
        }
        selected_paper = player.selected_paper
        pdf_url = paper_url_map.get(selected_paper, "blind_gaming.pdf")
        return {"pdf_url": pdf_url,
                "treatment": player.treatment,
                "playlist": player.participant.playlist,
                "trialTime": 0.1}

class TaskQuestionnaire(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = ['sfss1', 'sfss2', 'sfss3', 'sfss4', 'sfss5', 'sfss6', 'sfss7', 'sfss8', 'sfss9', 'sdb1', 'sdb2', 'sdb3']
        random.shuffle(flow_fields)
        all_fields = flow_fields

        mw_fields = ['mws1', 'mws2', 'mws3', 'mws4', 'mws5', 'mws6']
        random.shuffle(mw_fields)
        all_fields += mw_fields

        all_fields += ['tlx', 'control_text_interest', 'control_music_liking', 'control_music_turnoff']

        return all_fields

class StateQuestionnaire(Page):
    form_model = 'player'
    form_fields = ['pleasure', 'arousal', 'mf1', 'mf2', 'mf3', 'mf4']


class Done(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions1, Instructions2, Task, TaskQuestionnaire, StateQuestionnaire, Done]

