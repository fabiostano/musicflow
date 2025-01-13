from os import environ
SESSION_CONFIG_DEFAULTS = dict(real_world_currency_per_point=1, participation_fee=15)
SESSION_CONFIGS = [dict(name='full_research_first', num_demo_participants=2, app_sequence=['Intro', 'Research', 'Transcription', 'Outro']),
                   dict(name='full_transcription_first', num_demo_participants=2, app_sequence=['Intro', 'Transcription', 'Research', 'Outro']),
                   dict(name='Intro', num_demo_participants=None, app_sequence=['EEG_Setup']),
                   dict(name='outro', num_demo_participants=None, app_sequence=['Outro']),
                   dict(name='research', num_demo_participants=None, app_sequence=['Research']),
                   dict(name='transcription', num_demo_participants=None, app_sequence=['Transcription'])]
LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'EUR'
USE_POINTS = False
DEMO_PAGE_INTRO_HTML = ''
PARTICIPANT_FIELDS = ['trans_imgs_solo', 'playlist', 'treat_order']
SESSION_FIELDS = []
ROOMS = [dict(name='my_room', display_name='my_room')]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'kd2lab4ever'

SECRET_KEY = 'blahblah'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

DEBUG = True

OTREE_AUTH_LEVEL = 'STUDY'

OTREE_PRODUCTION = False