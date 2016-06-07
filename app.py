"""Flask project for moba winrate site."""


from flask import Flask, redirect, render_template
import pandas as pd


app = Flask(__name__)

data = pd.read_csv('heroes.csv')
solo = pd.read_csv('solo.csv')
items = pd.read_csv('allitems.csv')
foes = pd.read_csv('opponents.csv')
friends = pd.read_csv('teammates.csv')

#thumbs = list(data['url_small_portrait'])
#thumbids = list(data['id'])

thumbs = [
    ['http://cdn.dota2.com/apps/dota2/images/heroes/earthshaker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/sven_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tiny_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/kunkka_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/beastmaster_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/dragon_knight_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/rattletrap_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/omniknight_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/huskar_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/alchemist_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/brewmaster_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/treant_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/wisp_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/centaur_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/shredder_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/bristleback_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tusk_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/elder_titan_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/legion_commander_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/earth_spirit_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/phoenix_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/axe_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/pudge_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/sand_king_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/slardar_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tidehunter_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/skeleton_king_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/life_stealer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/night_stalker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/doom_bringer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/spirit_breaker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lycan_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/chaos_knight_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/undying_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/magnataur_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/abaddon_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/antimage_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/drow_ranger_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/juggernaut_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/mirana_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/morphling_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/phantom_lancer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/vengefulspirit_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/riki_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/sniper_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/templar_assassin_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/luna_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/bounty_hunter_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ursa_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/gyrocopter_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lone_druid_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/naga_siren_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/troll_warlord_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ember_spirit_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/bloodseeker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/nevermore_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/razor_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/venomancer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/faceless_void_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/phantom_assassin_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/viper_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/clinkz_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/broodmother_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/weaver_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/spectre_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/meepo_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/nyx_assassin_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/slark_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/medusa_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/terrorblade_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/arc_warden_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/crystal_maiden_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/puck_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/storm_spirit_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/windrunner_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/zuus_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lina_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/shadow_shaman_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tinker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/furion_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/enchantress_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/jakiro_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/chen_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/silencer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ogre_magi_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/rubick_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/disruptor_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/keeper_of_the_light_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/skywrath_mage_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/oracle_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/techies_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/bane_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lich_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lion_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/witch_doctor_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/enigma_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/necrolyte_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/warlock_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/queenofpain_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/death_prophet_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/pugna_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/dazzle_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/leshrac_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/dark_seer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/batrider_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ancient_apparition_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/invoker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/obsidian_destroyer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/shadow_demon_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/visage_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/winter_wyvern_sb.png']]

thumbids = [
    [7, 18, 19, 23, 38, 49, 51, 57, 59, 73, 78, 83, 91, 96, 98, 99, 100, 103, 104, 107, 110], 
    [2, 14, 16, 28, 29, 42, 54, 60, 69, 71, 77, 81, 85, 97, 102], 
    [1, 6, 8, 9, 10, 12, 20, 32, 35, 46, 48, 62, 70, 72, 80, 89, 95, 106], 
    [4, 11, 15, 40, 41, 44, 47, 56, 61, 63, 67, 82, 88, 93, 94, 109, 113], 
    [5, 13, 17, 21, 22, 25, 27, 34, 53, 58, 64, 66, 75, 84, 86, 87, 90, 101, 111, 105], 
    [3, 31, 26, 30, 33, 36, 37, 39, 43, 45, 50, 52, 55, 65, 68, 74, 76, 79, 92, 112]]


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
        str1 = thumbs[0], 
        str1ids = thumbids[0],
        str2 = thumbs[1], 
        str2ids = thumbids[1],
        agi1 = thumbs[2], 
        agi1ids = thumbids[2],
        agi2 = thumbs[3], 
        agi2ids = thumbids[3],
        int1 = thumbs[4], 
        int1ids = thumbids[4],
        int2 = thumbs[5], 
        int2ids = thumbids[5])


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
        str1 = thumbs[0], 
        str1ids = thumbids[0],
        str2 = thumbs[1], 
        str2ids = thumbids[1],
        agi1 = thumbs[2], 
        agi1ids = thumbids[2],
        agi2 = thumbs[3], 
        agi2ids = thumbids[3],
        int1 = thumbs[4], 
        int1ids = thumbids[4],
        int2 = thumbs[5], 
        int2ids = thumbids[5])


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
        str1 = thumbs[0], 
        str1ids = thumbids[0],
        str2 = thumbs[1], 
        str2ids = thumbids[1],
        agi1 = thumbs[2], 
        agi1ids = thumbids[2],
        agi2 = thumbs[3], 
        agi2ids = thumbids[3],
        int1 = thumbs[4], 
        int1ids = thumbids[4],
        int2 = thumbs[5], 
        int2ids = thumbids[5])


if __name__ == "__main__":
    app.run(debug=True)