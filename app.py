"""Flask project for moba winrate site."""


from flask import Flask, redirect, render_template
import lolhelpers
import dotahelpers


app = Flask(__name__)


@app.route('/')
def index():
    return redirect("/league")

@app.route('/about')
def about():
    return render_template("about.html")
@app.route('/dota')
def dland():
    return render_template("dota_landing.html",
        **dotahelpers.thumbargs)

@app.route('/dota/<id>')
def dsolopage(id):
    player = dotahelpers.playerdict(id)
    items = dotahelpers.soloitems(id)
    skill = dotahelpers.soloskill(id)
    return render_template(
        'dota_solo.html', 
        pl1=player,
        id1 = id,
        items1=items, 
        skill1 = skill,
        **dotahelpers.thumbargs)


@app.route('/dota/<id>/<id2>')
def dpair(id, id2):
    return redirect("/%s/%s/foe" % (id, id2))

@app.route('/dota/<id>/<id2>/<view>')
def djoint(id, id2, view):
    if id == id2:
        return redirect("/%s" % id)
    p1 = dotahelpers.playerdict(id)
    p2 = dotahelpers.playerdict(id2)
    items1 = dotahelpers.soloitems(id)
    items2 = dotahelpers.soloitems(id2)
    skill1 = dotahelpers.soloskill(id)
    skill2 = dotahelpers.soloskill(id2)
    if view == "foe":
        other_skill1 = dotahelpers.foeskill(id, id2)
        other_skill2 = dotahelpers.foeskill(id2, id)
        other_items1 = dotahelpers.foeitems(id, id2)
        other_items2 = dotahelpers.foeitems(id2, id)
    elif view == "friend":
        other_skill1 = dotahelpers.friendskill(id, id2)
        other_skill2 = dotahelpers.friendskill(id2, id)
        other_items1 = dotahelpers.frienditems(id, id2)
        other_items2 = dotahelpers.frienditems(id2, id)
    else:
        return redirect("/%s/%s" % (id, id2))
    return render_template(
        'dota_joint.html', 
        pl1 = p1,
        pl2 = p2,
        id1 = id,
        id2 = id2,
        items1 = items1,
        items2 = items2,
        other_items1 = other_items1,
        other_items2 = other_items2,
        skill1 = skill1,
        skill2 = skill2,
        other_skill1 = other_skill1,
        other_skill2 = other_skill2,
        view = view,
        **dotahelpers.thumbargs)

@app.route('/league')
def lland():
    return render_template("lol_landing.html", thumbs=lolhelpers.thumbs)


@app.route('/league/<id>')
def lsolopage(id):
    player = lolhelpers.playerdict(id)
    items = lolhelpers.soloitems(id)
    return render_template(
        'lol_solo.html', 
        pl1=player,
        items1=items, 
        thumbs=lolhelpers.thumbs)


@app.route('/league/<id>/<id2>')
def lpair(id, id2):
    return redirect("/league/%s/%s/foe" % (id, id2))


@app.route('/league/<id>/<id2>/<view>')
def ljoint(id, id2, view):
    if id == id2:
        return redirect("/%s" % id)
    p1 = lolhelpers.playerdict(id)
    p2 = lolhelpers.playerdict(id2)
    items1 = lolhelpers.soloitems(id)
    items2 = lolhelpers.soloitems(id2)
    if view == "foe":
        other_items1 = lolhelpers.foeitems(id, id2)
        other_items2 = lolhelpers.foeitems(id2, id)
    elif view == "friend":
        other_items1 = lolhelpers.frienditems(id, id2)
        other_items2 = lolhelpers.frienditems(id2, id)
    else:
        return redirect("/league/%s/%s" % (id, id2))
    return render_template(
        'lol_joint.html', 
        pl1 = p1,
        pl2 = p2,
        items1 = items1,
        items2 = items2,
        other_items1 = other_items1,
        other_items2 = other_items2,
        view = view,
        thumbs=lolhelpers.thumbs)


if __name__ == "__main__":
    app.run(debug=True)