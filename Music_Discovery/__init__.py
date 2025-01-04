
from otree.api import *
import random
import pandas as pd
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Music_Discovery'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 40

    allsongs = [
        '90Seconds.mp3',
        'ABadDream.mp3',
        'ACertainRatioHolySmoke.mp3',
        'ACertainRatioTier3.mp3',
        'AKLEMMEFINDOUT.mp3',
        'aldnheadstronggunner.mp3',
        'ArlissaHardToBe.mp3',
        'ArtSchoolGirlfriendCloseToTheClouds.mp3',
        'AshleySinghYouCanThinkOfHim.mp3',
        'BarrieEmpty.mp3',
        'BarrieGhostWorld.mp3',
        'BarrieNocturneInterlude.mp3',
        'BarrieUnholyAppetite.mp3',
        'BBYGOYARDCUDDLEFISH.mp3',
        'BIGBABYGUCCISILVER.mp3',
        'BuzzyLeeInternalAffairs.mp3',
        'BuzzyLeeWhenCanI.mp3',
        'CarolineRose_EverywhereIGoIBringTheRain.mp3',
        'CarolineRose_LoveSongForMyself.mp3',
        'CarolineRose_StockholmSyndrome.mp3',
        'CarolineRose_TheKiss.mp3',
        'Change.mp3',
        'ChiiildBonVoyage.mp3',
        'ChiiildSurfingTheSilverLinings.mp3',
        'CitizenQueenSoSpecial.mp3',
        'CityatEleven.mp3',
        'COLOR.mp3',
        'Come2Brazil.mp3',
        'CrawlersThatTimeOfYearAlways.mp3',
        'CrownLandsDreamerOfTheDawn.mp3',
        'CrownLandsReflections.mp3',
        'CrownLandsTheShadow.mp3',
        'DevLemonsDizzyVision.mp3',
        'EllaVosSuperglue.mp3',
        'FarAway.mp3',
        'FazerdazeFloodInto.mp3',
        'forestpartii_.mp3',
        'FrostChildrenALLIGOT.mp3',
        'FrostChildrenFLATLINE.mp3',
        'Grudge.mp3',
        'guardinitliveswhereilive.mp3',
        'HalfSilvered.mp3',
        'HardFeelings.mp3',
        'ICECOLDBISHOPDARE.mp3',
        'ICECOLDBISHOPFOCUSED.mp3',
        'ImInHell.mp3',
        'JaeSkeeseBonneville.mp3',
        'JaeSkeeseBurnerPhone.mp3',
        'junosininsideadress.mp3',
        'LandandSky.mp3',
        'LikeMike.mp3',
        'LimeGreen.mp3',
        'LindseyLomisThisTime.mp3',
        'LosingBattle.mp3',
        'MarujaBlindSpot.mp3',
        'MindsEye.mp3',
        'Movies.mp3',
        'NavyBlueTheMedium_Pillars.mp3',
        'NavyBlueTheOne.mp3',
        'NobodyKnows.mp3',
        'NowUnitedDabke.mp3',
        'PearlyDropsKissAwayThePearlyDrops.mp3',
        'RavMyBag.mp3',
        'ready2go.mp3',
        'renforshortbebe.mp3',
        'RiseandFall.mp3',
        'ROA.mp3',
        'RockBottom.mp3',
        'RXKNephewAllIHadWasABeanProdByBrainstorm.mp3',
        'Saturn.mp3',
        'SleepingNightandDay.mp3',
        'SoftcultDress.mp3',
        'SoftcultSpoiled.mp3',
        'SongofConsolation.mp3',
        'SophiePowersNosebleed.mp3',
        'spilltabWindow.mp3',
        'Tanukichan_LikeYou.mp3',
        'TeiShiGRIP.mp3',
        'TeiShiMONALISA.mp3',
        'TheBeths_WatchingTheCredits.mp3',
        'THEBLSSM_WHOSTOSAY.mp3',
        'TheLathumsLuckyBean.mp3',
        'TheLemonTwigsInMyHead.mp3',
        'TheRamonaFlowersHeyYou.mp3',
        'TheSkiniLiveIn.mp3',
        'TheWash.mp3',
        'ThomasHeadonilovedaboy.mp3',
        'TransvioletDevils.mp3',
        'TransvioletHowLucky.mp3',
        'TransvioletNaive.mp3',
        'TransvioletRunTowardsTheMonster.mp3',
        'Unabomber.mp3',
        'UnabomberII.mp3',
        'Understudies.mp3',
        'Undeserving.mp3',
        'VETTESUM.mp3',
        'WeDontGetHighLikeWeUsedTo.mp3',
        'WevalIsThatHowYouFeelIt.mp3',
        'WevalLosingDays.mp3',
        'WhenTheWorldEnds.mp3',
    ]

    songs = [
        'UnabomberII.mp3',
        'Unabomber.mp3',
        'CitizenQueenSoSpecial.mp3',
        'SophiePowersNosebleed.mp3',
        'Saturn.mp3',
        'aldnheadstronggunner.mp3',
        'JaeSkeeseBonneville.mp3',
        'FrostChildrenFLATLINE.mp3',
        'ChiiildBonVoyage.mp3',
        'ThomasHeadonilovedaboy.mp3',
        'ICECOLDBISHOPFOCUSED.mp3',
        'TheLemonTwigsInMyHead.mp3',
        'TheBeths_WatchingTheCredits.mp3',
        'EllaVosSuperglue.mp3',
        'renforshortbebe.mp3',
        'RiseandFall.mp3',
        'junosininsideadress.mp3',
        'WhenTheWorldEnds.mp3',
        'WevalIsThatHowYouFeelIt.mp3',
        'COLOR.mp3',
        'CrawlersThatTimeOfYearAlways.mp3',
        'TransvioletDevils.mp3',
        'CarolineRose_LoveSongForMyself.mp3',
        'WevalLosingDays.mp3',
        'JaeSkeeseBurnerPhone.mp3',
        'NobodyKnows.mp3',
        'forestpartii_.mp3',
        'HardFeelings.mp3',
        'MindsEye.mp3',
        'BuzzyLeeWhenCanI.mp3',
        'Change.mp3',
        'ROA.mp3',
        'TheRamonaFlowersHeyYou.mp3',
        'Movies.mp3',
        'LosingBattle.mp3',
        'LimeGreen.mp3',
        'LikeMike.mp3',
        'TheWash.mp3',
        'SleepingNightandDay.mp3',
        'ACertainRatioHolySmoke.mp3'
    ]

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # ----- Likes ----- #
    likes = models.StringField()
    added_to_playlist = models.BooleanField(initial=False)
    time_start = models.StringField()
    time_add = models.StringField()
    current_song = models.StringField()

    preference = models.IntegerField(
        label="Please rate the song.",
        choices=[[1, 'Very Bad'], [2, 'Bad'], [3, 'Rather Bad'], [4, 'Average'], [5, 'Rather Good'], [6, 'Good'],
                 [7, 'Very Good']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- Pleasure & Arousal ----- #
    pleasure = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']],
                                   widget=widgets.RadioSelectHorizontal)

    arousal = models.IntegerField(label="test", choices=[[1, '1'], [2, '2'], [3, '4'], [4, '4'], [5, '5']],
                                  widget=widgets.RadioSelectHorizontal)

    # ----- FKS Absorption ----- #

    fks1 = models.IntegerField(
        label="My thoughts/activities ran fluidly and smoothly.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'], [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks2 = models.IntegerField(
        label="I didn't notice time passing.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks3 = models.IntegerField(
        label="I had no difficulty concentrating on the music.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks4 = models.IntegerField(
        label="My mind was completely clear.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks5 = models.IntegerField(
        label="I was totally absorbed in what I am doing.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks6 = models.IntegerField(
        label="I was completely lost in thought.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks7 = models.IntegerField(
        label="I was concerned with what others may have been thinking of me.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    fks8 = models.IntegerField(
        label="I really enjoyed the experience.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    # ----- TAS Absorption ----- #

    tas1 = models.IntegerField(
        label="I found it impossible to keep my thoughts from wandering to things unrelated to the music.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    tas2 = models.IntegerField(
        label="I was greatly moved by the eloquent or poetic qualities of the sounds.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    tas3 = models.IntegerField(
        label="I found myself wanting to sing or whistle along quietly.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    tas4 = models.IntegerField(
        label="I sometimes felt as if I 'stepped outside' myself and experienced the music as if from an outside perspective.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    tas5 = models.IntegerField(
        label="I found myself being absorbed as if I were part of the music itself.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    tas6 = models.IntegerField(
        label="I was so involved that I forgot where I was and felt as if I were part of the music's story.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

    tas7 = models.IntegerField(
        label="Certain parts of the music produced powerful images or feelings in me.",
        choices=[[1, 'Strongly Disagree'], [2, 'Disagree'], [3, 'Somewhat Disagree'], [4, 'Average'],
                 [5, 'Somewhat Agree'], [6, 'Agree'],
                 [7, 'Strongly Agree']],
        widget=widgets.RadioSelectHorizontal
    )

class Instructions(Page):
    form_model = 'player'

    def is_displayed(player):
        return player.round_number == 1

    def before_next_page(player, timeout_happened):
        # Randomly sample 50 songs_full from the available 100
        playlist = C.songs.copy()

        random.shuffle(playlist)
        # Store the playlist in participant vars
        player.participant.vars['playlist'] = playlist
        player.participant.likes = ['start']

class Rating(Page):
    form_model = 'player'
    form_fields = ['added_to_playlist', 'preference', 'time_start', 'time_add', 'pleasure', 'arousal']

    def vars_for_template(player):
        # Ensure the song for the current round is fetched from the playlist
        current_song = player.participant.vars['playlist'][player.round_number]

        player.current_song = current_song

        return dict(
            round=player.round_number,
            song_src="/static/songs_chorus/" + current_song
        )

    def before_next_page(player, timeout_happened):
        if player.added_to_playlist == 1:
            player.participant.likes.append(player.current_song)

    def is_displayed(player):
        return player.round_number % 2 != 0


class Rating_Full(Page):
    form_model = 'player'
    form_fields = ['added_to_playlist', 'preference', 'time_start', 'time_add', 'pleasure', 'arousal', 'fks2',
                   'fks3', 'fks7', 'tas1', 'tas5']

    def vars_for_template(player):
        # Ensure the song for the current round is fetched from the playlist
        current_song = player.participant.vars['playlist'][player.round_number-1]

        player.current_song = current_song

        return dict(
            round=player.round_number,
            song_src="/static/songs_chorus/" + current_song
        )

    def before_next_page(player, timeout_happened):
        if player.added_to_playlist == 1:
            player.participant.likes.append(player.current_song)


class Done(Page):
    form_model = 'player'

    def vars_for_template(player):

        # Load the matched songs_full data
        df = pd.read_csv('matched_songs.csv')

        # Extract liked songs_full from participant vars
        likes = player.participant.vars.get('likes', [])

        # Filter out the 'start' entry if present
        if 'start' in likes:
            likes.remove('start')

        # Find the artist and title for each liked song
        liked_songs_data = []
        for filename in likes:
            song_data = df[df['matched_filename'] == filename]
            if not song_data.empty:
                artist = song_data.iloc[0]['artist']
                song = song_data.iloc[0]['Song']
                liked_songs_data.append({'artist': artist, 'song': song})

        return {'liked_songs': liked_songs_data}

    def is_displayed(player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [Instructions, Rating_Full, Done]