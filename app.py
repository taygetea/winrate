"""Flask project for moba winrate site."""


from flask import Flask, redirect, render_template
from helpers import *


app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/1")



@app.route('/<id>')
def solopage(id):
    player = playerdict(id)
    items = soloitems(id)
    skill = soloskill(id)
    return render_template(
        'solo.html', 
        pl1=player,
        items=items, 
        skill1 = skill,
        **thumbargs)


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
    skill1 = soloskill(id)
    skill2 = soloskill(id2)
    return render_template(
        'pair.html', 
        pl1 = p1, 
        pl2 = p2, 
        items1 = items1,
        items2 = items2,
        skill1 = skill1,
        skill2 = skill2,
        **thumbargs)


@app.route('/<id>/<id2>/<view>')
def joint(id, id2, view):
    if id == id2:
        return redirect("/%s" % id)
    p1 = playerdict(id)
    p2 = playerdict(id2)
    items1 = soloitems(id)
    items2 = soloitems(id2)
    skill1 = soloskill(id)
    skill2 = soloskill(id2)
    if view == "foe":
        other_skill1 = foeskill(id, id2)
        other_skill2 = foeskill(id2, id)
        other_items1 = foeitems(id, id2)
        other_items2 = foeitems(id2, id)
    elif view == "friend":
        other_skill1 = friendskill(id, id2)
        other_skill2 = friendskill(id2, id)
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
        skill1 = skill1,
        skill2 = skill2,
        other_skill1 = other_skill1,
        other_skill2 = other_skill2,
        view = view,
        **thumbargs)


if __name__ == "__main__":
    app.run(debug=True)