# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .base import *  # noqa

# don't use an unicode string
localeID = 'fr_FR'
dateSep = ['\/']
timeSep = [':', 'h']
meridian = ['du matin', 'du soir']
usesMeridian = True
uses24 = True
WeekdayOffsets = {}
MonthOffsets = {}

# always lowercase any lookup values - helper code expects that
Weekdays = [
    'lundi', 'mardi', 'mercredi', 'jeudi',
    'vendredi', 'samedi', 'dimanche',
]

shortWeekdays = [
    'lun', 'mar', 'mer', 'jeu', 'ven', 'sam', 'dim',
]

Months = [
    'janvier', 'février|fevrier', 'mars', 'avril', 'mai', 'juin', 'juillet',
    'août|aout', 'septembre', 'octobre', 'novembre', 'décembre|decembre',
]

# We do not list 'mar' as a short name for 'mars' as it conflicts with
# the 'mar' of 'mardi'
shortMonths = [
    'jan', 'fév|fev', 'mars', 'avr', 'mai', 'jui',
    'juil', 'aoû|aou', 'sep', 'oct', 'nov', 'déc|dec',
]

# use the same formats as ICU by default
dateFormats = {
    'full': 'EEEE d MMMM yyyy',
    'long': 'd MMMM yyyy',
    'medium': 'd MMM yyyy',
    'short': 'd/M/yy'
}

timeFormats = {
    'full': 'h:mm:ss a z',
    'long': 'h:mm:ss a z',
    'medium': 'h:mm:ss a',
    'short': 'h:mm a',
}

dp_order = ['d', 'm', 'y']

# Used to parse expressions like "in 5 hours"
numbers = collections.OrderedDict([
    ('cinquante', 50),
    ('soixante dix', 70),
    ('quatre vingt dix', 90),
    ('quatre vingts', 80),
    ('quatre vingt', 80),
    ('zéro', 0),
    ('zero', 0),
    ('un', 1),
    ('une', 1),
    ('deux', 2),
    ('trois', 3),
    ('quatre', 4),
    ('cinq', 5),
    ('six', 6),
    ('sept', 7),
    ('huit', 8),
    ('neuf', 9),
    ('dix', 10),
    ('onze', 11),
    ('douze', 12),
    ('treize', 13),
    ('quatorze', 14),
    ('quinze', 15),
    ('seize', 16),
    ('vingt', 20),
    ('trente', 30),
    ('quarante', 40),
    ('soixante', 60),
    ('cent', 100),
])

decimal_mark = ','

# this will be added to re_values later
units = {
    'seconds': ['seconde', 'secondes', 'sec', 's'],
    'minutes': ['minute', 'minutes', 'min', 'mn'],
    'hours': ['heure', 'heures', 'h'],
    'days': ['jours', 'jour', 'journée', 'journee', 'journées', 'journees', 'j'],
    'weeks': ['semaine', 'semaines', 'sem'],
    'months': ['mois', 'm'],
    'years': ['année', 'l\'année', 'annee', 'l\'annee', 'an', 'années', 'annees', 'ans'],
}

# text constants to be used by later regular expressions
re_values = {
    'specials': 'à|a|le|la|du|de',
    'timeseparator': '(?:\:|h|\s*heures?\s*)',
    'of': None, # "eg. 3rd of march"
    'rangeseparator': '-|a|à',
    'daysuffix': 'ième|ieme|ème|eme|ère|ere|nde',
    'meridian': None,
    'qunits': 'h|m|s|j|sem|a',
    'now': ['maintenant', 'tout de suite', 'immédiatement', 'immediatement', 'à l\'instant', 'a l\'instant'],
    'after': r'après|apres|il\sy\sa|plus\stard',
    'from': r'à\spartir|a\spartir|à\spartir\sde|a\spartir\sde|à\spartir\sd\'|a\spartir\sd\'|de|d\'', # num unit from rel
    'this': 'ce|cette',
    'next': 'prochaine|prochain|prochains|prochaines',
    'last': 'dernière|derniere|dernier|dernières|dernieres|derniers',
    'in': 'dans', # "in 5 days"
    'since': 'depuis', # since time, since date, since num unit
}

# Used to adjust the returned date before/after the source
Modifiers = {
    'avant': -1,
    'il y a': -1,
    'plus tot': -1,
    'plus tôt': -1,
    'y a': -1,
    'antérieur': -1,
    'antérieurs': -1,
    'anterieur': -1,
    'anterieurs': -1,
    'dernier': -1,
    'derniers': -1,
    'dernière': -1,
    'dernières': -1,
    'derniere': -1,
    'dernieres': -1,
    'précédent': -1,
    'précedent': -1,
    'precédent': -1,
    'precedent': -1,
    'précédents': -1,
    'précedents': -1,
    'precédents': -1,
    'precedents': -1,
    'fin de': 0,
    'fin du': 0,
    'fin de la': 0,
    'fin des': 0,
    'fin d\'': 0,
    'ce': 0,
    'ces': 0,
    'cette': 0,
    'cettes': 0,
    'depuis': 1,
    'dans': 1,
    'à partir': 1,
    'a partir': 1,
    'après': 1,
    'apres': 1,
    'lendemain': 1,
    'prochain': 1,
    'prochains': 1,
    'prochaine': 1,
    'prochaines': 1,
    'suivant': 1,
    'suivante': 1,
    'plus tard': 1
}

dayOffsets = {
    'après-demain': 2,
    'apres-demain': 2,
    'après demain': 2,
    'apres demain': 2,
    'demain': 1,
    'aujourd\'hui': 0,
    'hier': -1,
    'avant-hier': -2,
    'avant hier': -2
}

# special day and/or times, i.e. lunch, noon, evening
# each element in the dictionary is a dictionary that is used
# to fill in any value to be replace - the current date/time will
# already have been populated by the method buildSources
re_sources = {
    'après-midi': {'hr': 13, 'mn': 0, 'sec': 0},
    'apres-midi': {'hr': 13, 'mn': 0, 'sec': 0},
    'après midi': {'hr': 13, 'mn': 0, 'sec': 0},
    'apres midi': {'hr': 13, 'mn': 0, 'sec': 0},
    'aprèm': {'hr': 13, 'mn': 0, 'sec': 0},
    'aprem': {'hr': 13, 'mn': 0, 'sec': 0},
    'midi': {'hr': 12, 'mn': 0, 'sec': 0},
    'déjeuner': {'hr': 12, 'mn': 0, 'sec': 0},
    'dejeuner': {'hr': 12, 'mn': 0, 'sec': 0},
    'matin': {'hr': 6, 'mn': 0, 'sec': 0},
    'petit-déjeuner': {'hr': 8, 'mn': 0, 'sec': 0},
    'petit-dejeuner': {'hr': 8, 'mn': 0, 'sec': 0},
    'petit déjeuner': {'hr': 8, 'mn': 0, 'sec': 0},
    'petit dejeuner': {'hr': 8, 'mn': 0, 'sec': 0},
    'diner': {'hr': 19, 'mn': 0, 'sec': 0},
    'dîner': {'hr': 19, 'mn': 0, 'sec': 0},
    'soir': {'hr': 18, 'mn': 0, 'sec': 0},
    'soirée': {'hr': 18, 'mn': 0, 'sec': 0},
    'soiree': {'hr': 18, 'mn': 0, 'sec': 0},
    'minuit': {'hr': 0, 'mn': 0, 'sec': 0},
    'nuit': {'hr': 21, 'mn': 0, 'sec': 0},
}

small = {
    'zéro': 0,
    'zero': 0,
    'un': 1,
    'une': 1,
    'deux': 2,
    'trois': 3,
    'quatre': 4,
    'cinq': 5,
    'six': 6,
    'sept': 7,
    'huit': 8,
    'neuf': 9,
    'dix': 10,
    'onze': 11,
    'douze': 12,
    'treize': 13,
    'quatorze': 14,
    'quinze': 15,
    'seize': 16,
    'dix-sept': 17,
    'dix sept': 17,
    'dix-huit': 18,
    'dix huit': 18,
    'dix-neuf': 19,
    'dix neuf': 19,
    'vingt': 20,
    'vingt-et-un': 21,
    'vingt et un': 21,
    'trente': 30,
    'quarante': 40,
    'cinquante': 50,
    'soixante': 60,
    'soixante-dix': 70,
    'soixante dix': 70,
    'quatre-vingt': 80,
    'quatre vingt': 80,
    'quatre-vingt-dix': 90,
    'quatre vingt dix': 90
}

magnitude = {
    'mille': 1000,
    'millier': 1000,
    'million': 1000000,
    'milliard': 1000000000,
    'trillion': 1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000,
    'décillion': 1000000000000000000000000000000000,
    'decillion': 1000000000000000000000000000000000,
}

ignore = ('et', ',', 'le', 'la', 'l\'')
