import pandas as pd

heroes = pd.read_csv('heroes.csv')
solo = pd.read_csv('solo.csv')
items = pd.read_csv('allitems.csv')
foes = pd.read_csv('opponents.csv')
friends = pd.read_csv('teammates.csv')
skills = pd.read_csv('skills.csv')
skills['id'] = pd.merge(heroes, skills, left_on=["localized_name"], right_on=["name"])['id']
skills['key'] = pd.Series(["Q", "W", "E"]*len(pd.unique(skills['id'])))


thumbs = [
    ['http://cdn.dota2.com/apps/dota2/images/heroes/earthshaker_sb.png', 
    'http://cdn.dota2.com/apps/dota2/images/heroes/sven_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tiny_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/kunkka_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/beastmaster_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/dragon_knight_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/rattletrap_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/omniknight_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/huskar_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/alchemist_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/brewmaster_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/treant_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/wisp_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/centaur_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/shredder_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/bristleback_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tusk_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/elder_titan_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/legion_commander_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/earth_spirit_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/phoenix_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/axe_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/pudge_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/sand_king_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/slardar_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tidehunter_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/skeleton_king_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/life_stealer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/night_stalker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/doom_bringer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/spirit_breaker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lycan_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/chaos_knight_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/undying_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/magnataur_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/abaddon_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/antimage_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/drow_ranger_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/juggernaut_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/mirana_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/morphling_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/phantom_lancer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/vengefulspirit_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/riki_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/sniper_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/templar_assassin_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/luna_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/bounty_hunter_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ursa_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/gyrocopter_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lone_druid_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/naga_siren_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/troll_warlord_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ember_spirit_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/bloodseeker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/nevermore_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/razor_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/venomancer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/faceless_void_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/phantom_assassin_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/viper_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/clinkz_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/broodmother_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/weaver_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/spectre_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/meepo_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/nyx_assassin_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/slark_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/medusa_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/terrorblade_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/arc_warden_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/crystal_maiden_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/puck_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/storm_spirit_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/windrunner_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/zuus_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lina_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/shadow_shaman_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/tinker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/furion_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/enchantress_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/jakiro_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/chen_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/silencer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ogre_magi_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/rubick_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/disruptor_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/keeper_of_the_light_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/skywrath_mage_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/oracle_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/techies_sb.png'], ['http://cdn.dota2.com/apps/dota2/images/heroes/bane_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lich_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/lion_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/witch_doctor_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/enigma_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/necrolyte_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/warlock_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/queenofpain_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/death_prophet_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/pugna_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/dazzle_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/leshrac_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/dark_seer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/batrider_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/ancient_apparition_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/invoker_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/obsidian_destroyer_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/shadow_demon_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/visage_sb.png', 'http://cdn.dota2.com/apps/dota2/images/heroes/winter_wyvern_sb.png']]

thumbids = [
    [7, 18, 19, 23, 38, 49, 51, 57, 59, 73, 78, 83, 91, 96, 98, 99, 100, 103, 104, 107, 110], 
    [2, 14, 16, 28, 29, 42, 54, 60, 69, 71, 77, 81, 85, 97, 102], 
    [1, 6, 8, 9, 10, 12, 20, 32, 35, 46, 48, 62, 70, 72, 80, 89, 95, 106], 
    [4, 11, 15, 40, 41, 44, 47, 56, 61, 63, 67, 82, 88, 93, 94, 109, 113], 
    [5, 13, 17, 21, 22, 25, 27, 34, 53, 58, 64, 66, 75, 84, 86, 87, 90, 101, 111, 105], 
    [3, 31, 26, 30, 33, 36, 37, 39, 43, 45, 50, 52, 55, 65, 68, 74, 76, 79, 92, 112]]

thumbnames = [['Earthshaker',
  'Sven',
  'Tiny',
  'Kunkka',
  'Beastmaster',
  'Dragon Knight',
  'Clockwerk',
  'Omniknight',
  'Huskar',
  'Alchemist',
  'Brewmaster',
  'Treant Protector',
  'Io',
  'Centaur Warrunner',
  'Timbersaw',
  'Bristleback',
  'Tusk',
  'Elder Titan',
  'Legion Commander',
  'Earth Spirit',
  'Phoenix'],
 ['Axe',
  'Pudge',
  'Sand King',
  'Slardar',
  'Tidehunter',
  'Wraith King',
  'Lifestealer',
  'Night Stalker',
  'Doom',
  'Spirit Breaker',
  'Lycan',
  'Chaos Knight',
  'Undying',
  'Magnus',
  'Abaddon'],
 ['Anti-Mage',
  'Drow Ranger',
  'Juggernaut',
  'Mirana',
  'Morphling',
  'Phantom Lancer',
  'Vengeful Spirit',
  'Riki',
  'Sniper',
  'Templar Assassin',
  'Luna',
  'Bounty Hunter',
  'Ursa',
  'Gyrocopter',
  'Lone Druid',
  'Naga Siren',
  'Troll Warlord',
  'Ember Spirit'],
 ['Bloodseeker',
  'Shadow Fiend',
  'Razor',
  'Venomancer',
  'Faceless Void',
  'Phantom Assassin',
  'Viper',
  'Clinkz',
  'Broodmother',
  'Weaver',
  'Spectre',
  'Meepo',
  'Nyx Assassin',
  'Slark',
  'Medusa',
  'Terrorblade',
  'Arc Warden'],
 ['Crystal Maiden',
  'Puck',
  'Storm Spirit',
  'Windranger',
  'Zeus',
  'Lina',
  'Shadow Shaman',
  'Tinker',
  "Nature's Prophet",
  'Enchantress',
  'Jakiro',
  'Chen',
  'Silencer',
  'Ogre Magi',
  'Rubick',
  'Disruptor',
  'Keeper of the Light',
  'Skywrath Mage',
  'Oracle',
  'Techies'],
 ['Bane',
  'Lich',
  'Lion',
  'Witch Doctor',
  'Enigma',
  'Necrophos',
  'Warlock',
  'Queen of Pain',
  'Death Prophet',
  'Pugna',
  'Dazzle',
  'Leshrac',
  'Dark Seer',
  'Batrider',
  'Ancient Apparition',
  'Invoker',
  'Outworld Devourer',
  'Shadow Demon',
  'Visage',
  'Winter Wyvern']]



thumbargs = {"str1": thumbs[0], 
 			"str1ids": thumbids[0],
 			"str1names": thumbnames[0],
   			"str2": thumbs[1], 
   			"str2ids": thumbids[1],
   			"str2names": thumbnames[1],
   			"agi1": thumbs[2], 
   			"agi1ids": thumbids[2],
   			"agi1names": thumbnames[2],
   			"agi2": thumbs[3], 
   			"agi2ids": thumbids[3],
   			"agi2names": thumbnames[3],
   			"int1": thumbs[4], 
   			"int1ids": thumbids[4],
   			"int1names": thumbnames[4],
   			"int2": thumbs[5], 
   			"int2ids": thumbids[5],
   			"int2names": thumbnames[5]}


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
     

def soloskill(pid):
	pid = int(pid)
	row = pd.merge(solo[['hero', 'skill', 'skill_WR']], skills[skills['id'] == pid], left_on=["hero"], right_on=["id"])
	row = row[row['key'] == row['skill']]
	name, url, key, wr = [pdextract(row, val) for val in ["skillname", "skillurl", "key", "skill_WR"]]
	return {"name": name, "url": url, "key": key, "wr": round(wr, 4)}


def foeskill(hero1, hero2):
	hero1, hero2 = int(hero1), int(hero2)
	pair = pd.merge(foes[['itemhero','herocompare', 'skill', 'skill_WR']], skills[skills['id'] == hero1], left_on=["itemhero"], right_on=["id"])
	row = pair[pair['herocompare'] == hero2][pair['key'] == pair['skill']]
	name, url, key, wr = [pdextract(row, val) for val in ["skillname", "skillurl", "key", "skill_WR"]]
	return {"name": name, "url": url, "key": key, "wr": round(wr, 4)}


def friendskill(hero1, hero2):
	hero1, hero2 = int(hero1), int(hero2)
	pair = pd.merge(friends[['itemhero','herocompare', 'skill', 'skill_WR']], skills[skills['id'] == hero1], left_on=["itemhero"], right_on=["id"])
	row = pair[pair['herocompare'] == hero2][pair['key'] == pair['skill']]
	name, url, key, wr = [pdextract(row, val) for val in ["skillname", "skillurl", "key", "skill_WR"]]
	return {"name": name, "url": url, "key": key, "wr": round(wr, 4)}


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
    player = heroes[heroes['id'] == int(pid)]
    img = pdextract(player, 'url_full_portrait')
    name = pdextract(player, 'localized_name')
    return {"img": img,
            "name" : name,
            "id": pid}