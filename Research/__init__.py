
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
    time_start = models.StringField()
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
    form_fields = ["selected_paper"]

    def vars_for_template(player):
        return {
            "papers": C.PAPERS
        }

    def before_next_page(player, timeout_happened):
        print("test")

class Task(Page):
    form_model = 'player'

class TaskQuestionnaire(Page):
    form_model = 'player'

class StateQuestionnaire(Page):
    form_model = 'player'

class Done(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions, Task, TaskQuestionnaire, StateQuestionnaire, Done]