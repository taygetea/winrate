"""Flask project for moba winrate site."""


from flask import Flask, redirect, render_template
import pandas as pd


app = Flask(__name__)

data = pd.read_csv('heroes.csv')
solo = pd.read_csv('solo.csv')
items = pd.read_csv('allitems.csv')
foes = pd.read_csv('opponents.csv')
friends = pd.read_csv('teammates.csv')
thumbs = list(data['url_small_portrait'])
thumbids = list(data['id'])


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
    hero = solo[solo['hero'] == int(pid)]
    return getitems(hero)


def foeitems(hero1, hero2):
    row = foes[foes['itemhero'] == int(hero1)][foes['herocompare'] == int(hero2)]
    return getitems(row)


def frienditems(hero1, hero2):
    row = friends[friends['itemhero'] == int(hero1)][friends['herocompare'] == int(hero2)]
    return getitems(row)


def playerdict(pid):
    player = data[data['id'] == int(pid)]
    img = pdextract(player, 'url_full_portrait')
    name = pdextract(player, 'localized_name')
    return {"img": img,
            "name" : name,
            "id": pid}


@app.route('/')
def index():
    return redirect("/1")



@app.route('/<id>')
def solopage(id):
    player = playerdict(id)
    items = soloitems(id)
    return render_template(
        'solo.html', 
        pl1=player,
        items=items, 
        thumbs = thumbs, 
        thumbids = thumbids)


@app.route('/<id>/<id2>')
def pair(id, id2):
    if id == id2:
        return redirect("/%s" % id)
    p1 = playerdict(id)
    p2 = playerdict(id2)
    items1 = soloitems(id)
    items2 = soloitems(id2)
    foe_items1 = foeitems(id, id2)
    foe_items2 = foeitems(id2, id)
    return render_template(
        'pair.html', 
        pl1 = p1, 
        pl2 = p2, 
        items1 = items1,
        items2 = items2,
        thumbs = thumbs, 
        thumbids = thumbids)


@app.route('/<id>/<id2>/<view>')
def joint(id, id2, view):
    if id == id2:
        return redirect("/%s" % id)
    p1 = playerdict(id)
    p2 = playerdict(id2)
    items1 = soloitems(id)
    items2 = soloitems(id2)
    if view == "foe":
        other_items1 = foeitems(id, id2)
        other_items2 = foeitems(id2, id)
    elif view == "friend":
        other_items1 = frienditems(id, id2)
        other_items2 = frienditems(id2, id)
    else:
        return redirect("/%s/%s" % (id, id2))
    return render_template(
        'joint.html', 
        pl1 = p1,
        pl2 = p2,
        items1 = items1,
        items2 = items2,
        other_items1 = other_items1,
        other_items2 = other_items2,
        view = view,
        thumbs = thumbs, 
        thumbids = thumbids)


if __name__ == "__main__":
    app.run(debug=True)