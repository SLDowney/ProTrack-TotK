from models import *
from thesite.application_v2 import app, db

def armor_percent():
    total_armor = Armors.query.count()
    completed_armor = Armors.query.filter_by(done=1).count()

    if total_armor == 0:
        return 0

    return completed_armor


def korok_percent():
    total_koroks = Koroks.query.count()
    completed_koroks = Koroks.query.filter_by(korok_done=1).count()

    if total_koroks == 0:
        return 0

    return completed_koroks

def compendium_percent():
    total_items = Compendium.query.count()
    completed_items = Compendium.query.filter_by(done=1).count()

    if total_items == 0:
        return 0

    return completed_items


def caves_percent():
    total_caves = Caves.query.count()
    completed_caves = Caves.query.filter_by(done=2).count()

    if total_caves == 0:
        return 0

    return completed_caves


def chests_percent():
    total_chests = Chests.query.count()
    completed_chests = Chests.query.filter_by(chest_done=1).count()

    if total_chests == 0:
        return 0

    return completed_chests


def lightroots_percent():
    total_lightroots = Lightroots.query.count()
    completed_lightroots = Lightroots.query.filter_by(root_done=1).count()

    if total_lightroots == 0:
        return 0

    return completed_lightroots


def shrines_percent():
    total_shrines = Shrines.query.count()
    completed_shrines = Shrines.query.filter_by(done=2).count()

    if total_shrines == 0:
        return 0

    return completed_shrines


def overall_percent():
    total_items = sum([
        Armors.query.count(),
        Koroks.query.count(),
        Compendium.query.count(),
        Caves.query.count(),
        Chests.query.count(),
        Lightroots.query.count(),
        Shrines.query.count(),
    ])

    completed_items = sum([
        Armors.query.filter_by(done=1).count(),
        Koroks.query.filter_by(korok_done=1).count(),
        Compendium.query.filter_by(done=1).count(),
        Caves.query.filter_by(done=1).count(),
        Chests.query.filter_by(chest_done=1).count(),
        Lightroots.query.filter_by(root_done=1).count(),
        Shrines.query.filter_by(done=1).count(),
    ])

    if total_items == 0:
        return 0

    return round((completed_items / total_items) * 100)