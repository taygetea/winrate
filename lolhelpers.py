import pandas as pd

heroes = pd.read_csv('loldata/LoLherourl.csv', index_col=0)
solo = pd.read_csv('loldata/solo.csv')
items = pd.read_csv('loldata/allitems.csv')
foes = pd.read_csv('loldata/opponents.csv')
friends = pd.read_csv('loldata/teammates.csv')



thumbs = [dict(heroes.sort_values(by="localized_name").iloc[i]) for i in range(len(heroes))]


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
    
def herorate(hero1, hero2=None, view='solo'):
    # placeholder until I get the real data
    # import random
    # return round(random.gauss(0.5, 0.1)*100, 1)

    hero1 = int(hero1)
    herorow = heroes[heroes.id == hero1]
    if view == 'foe':
        hero2 = int(hero2)
        pairrow = foes[foes.champcompare == hero2]
        pairrow = pairrow[pairrow.itemchamp == hero1]
        return round(pairrow.tandem_WR.iloc[0], 3)*100
    elif view == 'friend':
        hero2 = int(hero2)
        pairrow = friends[friends.champcompare == hero2]
        pairrow = pairrow[pairrow.itemchamp == hero1]
        return round(pairrow.tandem_WR.iloc[0], 3)*100
    else:
        solorow = solo[solo.champ == hero1]
        return round(solorow.solo_WR.iloc[0], 3)*100


def soloitems(pid):
    hero = solo[solo['champ'] == int(pid)]
    return getitems(hero)


def foeitems(hero1, hero2):
    row = foes[foes['itemchamp'] == int(hero1)][foes['champcompare'] == int(hero2)]
    return getitems(row)


def frienditems(hero1, hero2):
    row = friends[friends['itemchamp'] == int(hero1)][friends['champcompare'] == int(hero2)]
    return getitems(row)

def frenemies(pid):
    row = solo[solo['champ'] == int(pid)]

    friend = [[playerdict(pdextract(row, 'friend%s' % i)) for i in range(0, 3)],
           [round(pdextract(row, 'friend_WR%s' % i)*100, 1) for i in range(0, 3)]]
    frenemy = [[playerdict(pdextract(row, 'frenemy%s' % i)) for i in range(0, 3)],
           [round(pdextract(row, 'frenemy_WR%s' % i)*100, 1) for i in range(0, 3)]]
    return friend, frenemy

def playerdict(pid):
    pid = int(pid)
    player = heroes[heroes['id'] == int(pid)]
    img = pdextract(player, 'url_full_portrait')
    name = pdextract(player, 'localized_name')
    return {"img": img,
            "name" : name,
            "id": pid}