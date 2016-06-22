"""Flask project for moba winrate site."""


from flask import Flask, redirect, render_template
import lolhelpers as lol
import dotahelpers  as dota


app = Flask(__name__)

colnames = ["Strength", "Agility", "Intelligence"]
numerals = ["1st", "2nd", "3rd", "4th", "5th", "6th"]
@app.route('/')
def index():
    return redirect("/league")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/dota')
def dland():
    return render_template("dota_landing.html",
        colnames = ["Strength", "Agility", "Intelligence"],
        thumbargs = dota.thumbargs,
        alpha_thumbs = dota.alpha_thumbs)

@app.route('/dota/<id>')
def dsolopage(id):

    player = dota.playerdict(id)
    items = dota.soloitems(id)
    skill = dota.soloskill(id)
    rate = dota.herorate(id)
    friends, frenemies = dota.frenemies(id)
    return render_template(
        'dota_solo.html', 
        pl1=player,
        id1 = id,
        items1=items, 
        skill1 = skill,
        rate = rate,
        friends = friends,
        frenemies = frenemies,
        colnames = ["Strength", "Agility", "Intelligence"],
        numerals = ["1st", "2nd", "3rd", "4th", "5th", "6th"],
        thumbargs = dota.thumbargs,
        alpha_thumbs = dota.alpha_thumbs)


@app.route('/dota/<id>/<id2>')
def dpair(id, id2):
    if id == id2:
        return redirect("/dota/%s" % id)
    return redirect("/dota/%s/%s/foe" % (id, id2))

@app.route('/dota/<id>/<id2>/<view>')
def djoint(id, id2, view):
    if id == id2:
        return redirect("/dota/%s" % id)
    p1 = dota.playerdict(id)
    p2 = dota.playerdict(id2)
    items1 = dota.soloitems(id)
    items2 = dota.soloitems(id2)
    skill1 = dota.soloskill(id)
    skill2 = dota.soloskill(id2)
    rate1 = dota.herorate(id)
    rate2 = dota.herorate(id2)
    other_rate1 = dota.herorate(id, id2, view)
    other_rate2 = dota.herorate(id2, id, view)
    if view == "foe":
        notview = "friend"
        other_skill1 = dota.foeskill(id, id2)
        other_skill2 = dota.foeskill(id2, id)
        other_items1 = dota.foeitems(id, id2)
        other_items2 = dota.foeitems(id2, id)
    elif view == "friend":
        notview = "foe"
        other_skill1 = dota.friendskill(id, id2)
        other_skill2 = dota.friendskill(id2, id)
        other_items1 = dota.frienditems(id, id2)
        other_items2 = dota.frienditems(id2, id)
    else:
        return redirect("/dota/%s/%s" % (id, id2))
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
        notview = notview,
        rate1 = rate1,
        rate2 = rate2,
        other_rate1 = other_rate1,
        other_rate2 = other_rate2,
        colnames = ["Strength", "Agility", "Intelligence"],
        numerals = ["1st", "2nd", "3rd", "4th", "5th", "6th"],
        thumbargs = dota.thumbargs,
        alpha_thumbs = dota.alpha_thumbs)

@app.route('/league')
def lland():
    return render_template("lol_landing.html", thumbs=lol.thumbs)


@app.route('/league/<id>')
def lsolopage(id):
    player = lol.playerdict(id)
    items = lol.soloitems(id)
    rate = lol.herorate(id)
    friends, frenemies = lol.frenemies(id)
    return render_template(
        'lol_solo.html', 
        pl1=player,
        id1 = id,
        items1=items,
        rate = rate,
        friends = friends,
        frenemies = frenemies,
        numerals = ["1st", "2nd", "3rd", "4th", "5th", "6th"],
        thumbs=lol.thumbs)


@app.route('/league/<id>/<id2>')
def lpair(id, id2):
    return redirect("/league/%s/%s/foe" % (id, id2))


@app.route('/league/<id>/<id2>/<view>')
def ljoint(id, id2, view):
    if id == id2:
        return redirect("/league/%s" % id)
    p1 = lol.playerdict(id)
    p2 = lol.playerdict(id2)
    items1 = lol.soloitems(id)
    items2 = lol.soloitems(id2)
    rate1 = lol.herorate(id)
    rate2 = lol.herorate(id2)
    other_rate1 = lol.herorate(id, id2, view)
    other_rate2 = lol.herorate(id2, id, view)

    if view == "foe":
        notview = "friend"
        other_items1 = lol.foeitems(id, id2)
        other_items2 = lol.foeitems(id2, id)
    elif view == "friend":
        notview = "foe"
        other_items1 = lol.frienditems(id, id2)
        other_items2 = lol.frienditems(id2, id)
    else:
        return redirect("/league/%s/%s" % (id, id2))
    return render_template(
        'lol_joint.html', 
        pl1 = p1,
        pl2 = p2,
        id1 = id,
        id2 = id2,
        items1 = items1,
        items2 = items2,
        other_items1 = other_items1,
        other_items2 = other_items2,
        view = view,
        notview = notview,
        rate1 = rate1,
        rate2 = rate2,
        other_rate1 = other_rate1,
        other_rate2 = other_rate2,
        numerals = ["1st", "2nd", "3rd", "4th", "5th", "6th"],
        thumbs=lol.thumbs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)