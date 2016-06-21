import pandas as pd
from thumbnails import thumbs as thumbargs

heroes = pd.read_csv('dotadata/heroes.csv')
solo = pd.read_csv('dotadata/solo.csv')
items = pd.read_csv('dotadata/allitems.csv')
foes = pd.read_csv('dotadata/opponents.csv')
friends = pd.read_csv('dotadata/teammates.csv')
# skills = pd.read_csv('dotadata/skills.csv')
# skills['id'] = pd.merge(heroes, skills, left_on=["localized_name"], right_on=["name"])['id']
# skills['key'] = pd.Series(["Q", "W", "E"]*len(pd.unique(skills['id'])))



def pdextract(row, col):
    """Helper function to get the value at a row and column."""
    return row[col].values[0]


def getitems(row):
    itemnames = [pdextract(row, 'item_name%s' % i) for i in range(0, 5)]
    itemids = [pdextract(row, 'item%s' % i) for i in range(0, 5)]
    winrate = [pdextract(row, 'item_WR%s' % i) for i in range(0, 5)]
    urls = [pdextract(items[items['id'] == i], 'url_image') for i in itemids]
    out = [
        {"id": itemids[i],
         "name": itemnames[i],
         "url": urls[i],
         "wr": round(winrate[i], 3)*100} for i in range(len(itemids))]
    return out
     
def soloskill(pid):
    pid = int(pid)
    herorow = heroes[heroes.id == pid]
    solorow = solo[solo.hero == pid]
    skill = solorow['skill'].iloc[0]
    wr = solorow['skill_WR'].iloc[0]
    name = herorow[skill+"_name"].iloc[0]
    url = herorow[skill+"_url"].iloc[0]
    return {"name": name, "url": url, "wr": round(wr, 3)*100}

def herorate(hero1, hero2=None, view='solo'):
    hero1 = int(hero1)
    herorow = heroes[heroes.id == hero1]
    if view == 'foe':
        hero2 = int(hero2)
        pairrow = foes[foes.herocompare == hero2]
        pairrow = pairrow[pairrow.itemhero == hero1]
        return round(pairrow.tandem_WR.iloc[0], 3)*100
    elif view == 'friend':
        hero2 = int(hero2)
        pairrow = friends[friends.herocompare == hero2]
        pairrow = pairrow[pairrow.itemhero == hero1]
        return round(pairrow.tandem_WR.iloc[0], 3)*100
    else:
        solorow = solo[solo.hero == hero1]
        return round(solorow.solo_WR.iloc[0], 3)*100

def foeskill(hero1, hero2):
    hero1, hero2 = int(hero1), int(hero2)
    herorow = heroes[heroes.id == hero1]
    pairrow = foes[foes.herocompare == hero2]
    pairrow = pairrow[pairrow.itemhero == hero1]
    skill = pairrow['skill'].iloc[0]
    wr = pairrow['skill_WR'].iloc[0]
    name = herorow[skill+"_name"].iloc[0]
    url = herorow[skill+"_url"].iloc[0]
    return {"name": name, "url": url, "wr": round(wr, 3)*100}


def friendskill(hero1, hero2):
    hero1, hero2 = int(hero1), int(hero2)
    herorow = heroes[heroes.id == hero1]
    pairrow = friends[friends.herocompare == hero2]
    pairrow = pairrow[pairrow.itemhero == hero1]
    skill = pairrow['skill'].iloc[0]
    wr = pairrow['skill_WR'].iloc[0]
    name = herorow[skill+"_name"].iloc[0]
    url = herorow[skill+"_url"].iloc[0]
    return {"name": name, "url": url, "wr": round(wr, 3)*100}


def soloitems(pid):
    hero = solo[solo['hero'] == int(pid)]
    return getitems(hero)


def foeitems(hero1, hero2):
    row = foes[foes['itemhero'] == int(hero1)][foes['herocompare'] == int(hero2)]
    return getitems(row)


def frienditems(hero1, hero2):
    row = friends[friends['itemhero'] == int(hero1)][friends['herocompare'] == int(hero2)]
    return getitems(row)

def frenemies(pid):
    row = solo[solo['hero'] == int(pid)]

    friend = [[playerdict(pdextract(row, 'friend%s' % i)) for i in range(0, 3)],
           [round(pdextract(row, 'friend_WR%s' % i)*100, 1) for i in range(0, 3)]]
    for f in friend[0]:
        f['img'] = f['img'].replace("_full.png", "_vert.jpg")
    frenemy = [[playerdict(pdextract(row, 'frenemy%s' % i)) for i in range(3, 6)],
           [round(pdextract(row, 'frenemy_WR%s' % i)*100, 1) for i in range(3, 6)]]
    for f in frenemy[0]:
        f['img'] = f['img'].replace("_full.png", "_vert.jpg")
    return friend, frenemy

def playerdict(pid):
    player = heroes[heroes['id'] == int(pid)]
    img = pdextract(player, 'url_full_portrait')
    name = pdextract(player, 'localized_name')
    return {"img": img,
            "name" : name,
            "id": pid}