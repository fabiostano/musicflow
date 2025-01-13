
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
    name = models.StringField(blank=True)
    IBAN = models.StringField(blank=True)
    BIC = models.StringField(blank=True)

    ### --- TRAIT Q --- ###

    # ----- SDFS-2 ----- #
    sdfs1 = models.IntegerField(label="I feel I am competent enough to meet the demands of the situation",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs2 = models.IntegerField(label="I do things spontaneously and automatically without having to think.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs3 = models.IntegerField(label="I have a strong sense of what I want to do.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs4 = models.IntegerField(
        label="I have a good idea about how well I am doing while I am involved in the task/activity.",
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs5 = models.IntegerField(label="I am completely focused on the task at hand.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs6 = models.IntegerField(label="I have a feeling of total control over what I am doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs7 = models.IntegerField(label="I am not worried about what others may be thinking of me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs8 = models.IntegerField(label="The way time passes seems to be different from normal.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    sdfs9 = models.IntegerField(label="I find the experience extremely rewarding.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    ac_sdfs = models.IntegerField(
        label='This is an attention check. Please select the answer on the far right.',
        choices=[[1, ''], [2, ''], [3, ''], [4, ''], [5, '']], widget=widgets.RadioSelectHorizontal)

    # ----- Extraversion ----- #
    e1 = models.IntegerField(
        label='I would describe myself as someone who is reserved.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e2 = models.IntegerField(
        label='I would describe myself as someone who is talkative.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e3 = models.IntegerField(
        label='I would describe myself as someone who generates a lot of enthusiasm.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e4 = models.IntegerField(
        label='I would describe myself as someone who is outgoing/sociable.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)
    e5 = models.IntegerField(
        label='I would describe myself as someone who is sometimes shy/inhibited.',
        choices=[1, 2, 3, 4, 5], widget=widgets.RadioSelectHorizontal)

    # ------ Domain Expertise ------ #
    domain_exp_transcription = models.IntegerField(
        label="I am experienced in transcribing snippets of text.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    domain_exp_typing = models.IntegerField(
        label="I am a fast typer.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    domain_exp_research = models.IntegerField(
        label="I am experienced in reading and working with scientific papers.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    domain_exp_reading = models.IntegerField(
        label="I generally like reading papers or articles.",
        choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Mind Wandering Trait ----- #
    mwt01 = models.IntegerField(label="I find my thoughts wandering spontaneously.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt02 = models.IntegerField(label="My thoughts tend to be pulled from topic to topic.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt03 = models.IntegerField(label="I mind wander even when I’m supposed to be doing something else.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt04 = models.IntegerField(label="I have difficulty controlling my thoughts.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt05 = models.IntegerField(label="I find it hard to switch my thoughts off.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt06 = models.IntegerField(label="My thoughts are disorganized and `all over the place'.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt07 = models.IntegerField(label="I find it difficult to think about one thing without another thought entering my mind.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt08 = models.IntegerField(label="I find my thoughts are distracting and prevent me from focusing on what I am doing.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt09 = models.IntegerField(label="I have difficulty slowing my thoughts down and focusing on one thing at a time.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mwt10 = models.IntegerField(label="I find myself flitting back and forth between different thoughts.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    ### --- MUSIC AT WORK TYPE --- ###

    # ----- General ----- #
    mt_g_01 = models.IntegerField(label="I listen to music while working.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mt_g_02 = models.IntegerField(label="I think music can help me to achieve more in certain tasks.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mt_g_03 = models.IntegerField(label="Listening to music at work improves my overall long-term productivity.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)
    mt_g_04 = models.IntegerField(label="Listening to music at work improves my overall long-term emotional well-being.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']], widget=widgets.RadioSelectHorizontal)

    # ----- Reason ----- #
    mt_r_01 = models.IntegerField(label="I listen to music because it helps me to get into the flow state.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_02 = models.IntegerField(label="I listen to music because it helps me to stay in the flow state.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_03 = models.IntegerField(label="I listen to music because it helps me to experience more intense flow states.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_r_04 = models.IntegerField(label="I listen to music at work because it helps me to block off potential distractions from the outside.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_05 = models.IntegerField(label="I listen to music at work because it keeps unwanted inner thoughts away.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_06 = models.IntegerField(label="I listen to music at work because it motivates me to get started with my work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_07 = models.IntegerField(label="I listen to music at work because it motivates me to keep going with my work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_08 = models.IntegerField(label="I listen to music at work because it makes work more enjoyable.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_09 = models.IntegerField(label="I listen to music at work to boost my creativity.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_10 = models.IntegerField(label="I listen to music at work because it boosts my energy.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_11 = models.IntegerField(label="I listen to music at work to improve my mood.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_12 = models.IntegerField(label="I listen to music at work because it calms me down.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_13 = models.IntegerField(label="I listen to music at work because it inspires me.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_14 = models.IntegerField(label="I listen to music to make boring tasks less boring.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_15 = models.IntegerField(label="I listen to music because it creates a personal bubble in shared spaces.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_16 = models.IntegerField(label="I listen to music because it helps me to complete tasks faster.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_17 = models.IntegerField(label="Listening to music helps me maintain a high level of accuracy in my work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_18 = models.IntegerField(label="Listening to music helps me manage my workload better.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_19 = models.IntegerField(label="When listening to music, I find it easier to stay on track and avoid procrastination.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_r_20 = models.IntegerField(label="Music makes me feel more connected to my work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Source ----- #
    mt_s_01 = models.IntegerField(label="I use curated playlists or algorithms to listen to music at work.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_s_02 = models.IntegerField(label="I create my own playlists which I listen to at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_s_03 = models.IntegerField(label="I listen to the radio or similar live curated formats at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Work Tasks ----- #
    mt_w_01 = models.IntegerField(label="I listen to music mainly if tasks are rather easy for me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_02 = models.IntegerField(label="I listen to music mainly if tasks are rather hard for me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_03 = models.IntegerField(label="I listen to music for routine tasks.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_04 = models.IntegerField(label="I listen to music for tasks that are new to me.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_05 = models.IntegerField(label="I listen to music for repetitive tasks that require minimal focus.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_06 = models.IntegerField(label="I listen to music that require deep focus or high accuracy.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_w_07 = models.IntegerField(label="I listen to music for creative tasks (e.g. drafting new ideas).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_08 = models.IntegerField(label="I listen to music for graphical tasks (e.g. coming up with visualizations).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_09 = models.IntegerField(label="I listen to music for tasks that require lots of analytical thinking (e.g. programming).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_10 = models.IntegerField(label="I listen to music for tasks that require demanding writing and reading (e.g. academic work).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_w_11 = models.IntegerField(label="I listen to music for tasks that require easy writing and reading (e.g. handling e-mails).",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_w_12 = models.IntegerField(label="I listen to different types of music for different tasks.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])


    # ----- Temporal ----- #
    mt_t_01 = models.IntegerField(label="I need a constant level of background music while working.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_t_02 = models.IntegerField(label="I only use background music for certain selected periods and then turn it off again.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_t_03 = models.IntegerField(label="I find myself listening to music at work more often during the morning.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_t_04 = models.IntegerField(label="I find myself listening to music at work more often during the afternoon.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_t_05 = models.IntegerField(label="I find myself listening to music at work more often during the evening.",
                                choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_t_06 = models.IntegerField(label="I find myself listening to music at work more often during the night.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_t_07 = models.IntegerField(label="I listen to different types of music for different times of day.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Environment ---- #
    mt_e_01 = models.IntegerField(label="I like to use background music when working at home.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_02 = models.IntegerField(label="I like to use background music when working in the office.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_03 = models.IntegerField(label="I like to use background music when working in co-working spaces or public libraries.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_04 = models.IntegerField(label="I like to use background music when working in means of public transportation (e.g. train).",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_05 = models.IntegerField(label="I like to use background music when working in public places (e.g. cafes, parks).",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_06 = models.IntegerField(label="I find it easier to focus with music when I am working alone.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_07 = models.IntegerField(label="I listen to music while working in shared spaces to create a sense of privacy.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_08 = models.IntegerField(label="I listen to music while working in noisy environments.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_e_09 = models.IntegerField(label="I listen to music while working in quiet environments.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_e_10 = models.IntegerField(label="I listen to different types of music for different locations",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    # ----- Characteristics of Music ----- #
    mt_c_01 = models.IntegerField(label="I like to listen to classical music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_02 = models.IntegerField(label="I like to listen to lofi music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_03 = models.IntegerField(label="I like to listen to rap music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_04 = models.IntegerField(label="I like to listen to rock music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_05 = models.IntegerField(label="I like to listen to pop music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_06 = models.IntegerField(label="I like to listen to electronic music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_07 = models.IntegerField(label="I like to listen to jazz music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_08 = models.IntegerField(label="I like to listen to ambient music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_c_09 = models.IntegerField(label="I like to listen to music with lyrics at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_10 = models.IntegerField(label="I like to listen to instrumental music without lyrics at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_11 = models.IntegerField(label="I like to listen to fast music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])
    mt_c_12 = models.IntegerField(label="I like to listen to slow music at work.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])

    mt_c_13 = models.IntegerField(label="I like to listen to the same music at work as in my free time.",
                                  choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']])


class ThankYou(Page):
    form_model = 'player'
    form_fields = ['name', 'IBAN', 'BIC']

class TraitQuestionnaire(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        import random
        flow_fields = ['sdfs1', 'sdfs2', 'sdfs3', 'sdfs4', 'sdfs5', 'sdfs6', 'sdfs7', 'sdfs8', 'sdfs9']
        random.shuffle(flow_fields)
        all_fields = flow_fields

        ext_fields = ['e1', 'e2', 'e3', 'e4', 'e5']
        random.shuffle(ext_fields)
        all_fields += ext_fields

        domain_fields = ['domain_exp_transcription', 'domain_exp_typing', 'domain_exp_research', 'domain_exp_reading']
        random.shuffle(domain_fields)
        all_fields += domain_fields

        mwt_fields = ['mwt01', 'mwt02', 'mwt03', 'mwt04', 'mwt05', 'mwt06', 'mwt07', 'mwt08', 'mwt09', 'mwt10']
        random.shuffle(mwt_fields)
        all_fields += mwt_fields

        mt_g_fields = ['mt_g_01', 'mt_g_02', 'mt_g_03', 'mt_g_04']
        random.shuffle(mt_g_fields)
        all_fields += mt_g_fields

        return all_fields

page_sequence = [TraitQuestionnaire, ThankYou]