"""Flask project for moba winrate site."""


from flask import Flask, redirect, render_template
import lolhelpers
import dotahelpers


app = Flask(__name__)

colnames = ["Strength", "Agility", "Intelligence"]
numerals = ["1st", "2nd", "3rd", "4th", "5th"]
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
        thumbargs = dotahelpers.thumbargs)

@app.route('/dota/<id>')
def dsolopage(id):

    player = dotahelpers.playerdict(id)
    items = dotahelpers.soloitems(id)
    skill = dotahelpers.soloskill(id)
    rate = dotahelpers.herorate(id)
    friends, frenemies = dotahelpers.frenemies(id)
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
        numerals = ["1st", "2nd", "3rd", "4th", "5th"],
        thumbargs = dotahelpers.thumbargs)


@app.route('/dota/<id>/<id2>')
def dpair(id, id2):
    if id == id2:
        return redirect("/dota/%s" % id)
    return redirect("/dota/%s/%s/foe" % (id, id2))

@app.route('/dota/<id>/<id2>/<view>')
def djoint(id, id2, view):
    if id == id2:
        return redirect("/dota/%s" % id)
    p1 = dotahelpers.playerdict(id)
    p2 = dotahelpers.playerdict(id2)
    items1 = dotahelpers.soloitems(id)
    items2 = dotahelpers.soloitems(id2)
    skill1 = dotahelpers.soloskill(id)
    skill2 = dotahelpers.soloskill(id2)
    rate1 = dotahelpers.herorate(id)
    rate2 = dotahelpers.herorate(id2)
    other_rate1 = dotahelpers.herorate(id, id2, view)
    other_rate2 = dotahelpers.herorate(id2, id, view)
    if view == "foe":
        notview = "friend"
        other_skill1 = dotahelpers.foeskill(id, id2)
        other_skill2 = dotahelpers.foeskill(id2, id)
        other_items1 = dotahelpers.foeitems(id, id2)
        other_items2 = dotahelpers.foeitems(id2, id)
    elif view == "friend":
        notview = "foe"
        other_skill1 = dotahelpers.friendskill(id, id2)
        other_skill2 = dotahelpers.friendskill(id2, id)
        other_items1 = dotahelpers.frienditems(id, id2)
        other_items2 = dotahelpers.frienditems(id2, id)
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
        numerals = ["1st", "2nd", "3rd", "4th", "5th"],
        thumbargs = dotahelpers.thumbargs)

@app.route('/league')
def lland():
    return render_template("lol_landing.html", thumbs=lolhelpers.thumbs)


@app.route('/league/<id>')
def lsolopage(id):
    player = lolhelpers.playerdict(id)
    items = lolhelpers.soloitems(id)
    rate = lolhelpers.herorate(id)
    friends, frenemies = lolhelpers.frenemies(id)
    return render_template(
        'lol_solo.html', 
        pl1=player,
        id1 = id,
        items1=items,
        rate = rate,
        friends = friends,
        frenemies = frenemies,
        numerals = ["1st", "2nd", "3rd", "4th", "5th"],
        thumbs=lolhelpers.thumbs)


@app.route('/league/<id>/<id2>')
def lpair(id, id2):
    return redirect("/league/%s/%s/foe" % (id, id2))


@app.route('/league/<id>/<id2>/<view>')
def ljoint(id, id2, view):
    if id == id2:
        return redirect("/league/%s" % id)
    p1 = lolhelpers.playerdict(id)
    p2 = lolhelpers.playerdict(id2)
    items1 = lolhelpers.soloitems(id)
    items2 = lolhelpers.soloitems(id2)
    rate1 = lolhelpers.herorate(id)
    rate2 = lolhelpers.herorate(id2)
    other_rate1 = lolhelpers.herorate(id, id2, view)
    other_rate2 = lolhelpers.herorate(id2, id, view)

    if view == "foe":
        notview = "friend"
        other_items1 = lolhelpers.foeitems(id, id2)
        other_items2 = lolhelpers.foeitems(id2, id)
    elif view == "friend":
        notview = "foe"
        other_items1 = lolhelpers.frienditems(id, id2)
        other_items2 = lolhelpers.frienditems(id2, id)
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
        numerals = ["1st", "2nd", "3rd", "4th", "5th"],
        thumbs=lolhelpers.thumbs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)