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
         "wr": round(winrate[i], 4)} for i in range(len(itemids))]
    return out
    


def soloitems(pid):
    hero = solo[solo['champ'] == int(pid)]
    return getitems(hero)


def foeitems(hero1, hero2):
    row = foes[foes['itemchamp'] == int(hero1)][foes['champcompare'] == int(hero2)]
    return getitems(row)


def frienditems(hero1, hero2):
    row = friends[friends['itemchamp'] == int(hero1)][friends['champcompare'] == int(hero2)]
    return getitems(row)


def playerdict(pid):
    player = heroes[heroes['id'] == int(pid)]
    img = pdextract(player, 'url_full_portrait')
    name = pdextract(player, 'localized_name')
    return {"img": img,
            "name" : name,
            "id": pid}