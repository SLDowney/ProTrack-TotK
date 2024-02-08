import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from .models import Armors, Koroks, Compendium, Caves, Chests, Lightroots, Shrines, ShrinesChests, Fabrics, Locations, Armor_sets, Dragontears
from sqlalchemy.sql import func

db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# Replace 'mysql://username:password@localhost/db_name' with your MySQL connection details
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:BlackFlame!1@localhost/totk_v2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def armor_percent():
    total_armor = Armors.query.count()
    completed_armor = Armors.query.filter_by(done=1).count()

    if total_armor == 0:
        return 0

    return completed_armor


def korok_percent():
    total_koroks = Koroks.query.count()
    completed_koroks = Koroks.query.filter_by(korok_done=1).count()

    if total_koroks == 0:
        return 0

    return completed_koroks

def compendium_percent():
    total_items = Compendium.query.count()
    completed_items = Compendium.query.filter_by(done=1).count()

    if total_items == 0:
        return 0

    return completed_items


def caves_percent():
    total_caves = Caves.query.count()
    completed_caves = Caves.query.filter_by(done=2).count()

    if total_caves == 0:
        return 0

    return completed_caves


def chests_percent():
    total_chests = Chests.query.count()
    completed_chests = Chests.query.filter_by(chest_done=1).count()

    if total_chests == 0:
        return 0

    return completed_chests


def lightroots_percent():
    total_lightroots = Lightroots.query.count()
    completed_lightroots = Lightroots.query.filter_by(root_done=1).count()

    if total_lightroots == 0:
        return 0

    return completed_lightroots


def shrines_percent():
    total_shrines = Shrines.query.count()
    completed_shrines = Shrines.query.filter_by(done=2).count()

    if total_shrines == 0:
        return 0

    return completed_shrines


def overall_percent():
    total_items = sum([
        Armors.query.count(),
        Koroks.query.count(),
        Compendium.query.count(),
        Caves.query.count(),
        Chests.query.count(),
        Lightroots.query.count(),
        Shrines.query.count(),
    ])

    completed_items = sum([
        Armors.query.filter_by(done=1).count(),
        Koroks.query.filter_by(korok_done=1).count(),
        Compendium.query.filter_by(done=1).count(),
        Caves.query.filter_by(done=1).count(),
        Chests.query.filter_by(chest_done=1).count(),
        Lightroots.query.filter_by(root_done=1).count(),
        Shrines.query.filter_by(done=1).count(),
    ])

    if total_items == 0:
        return 0

    return round((completed_items / total_items) * 100)


@app.route('/')
def index():
    headline = "Completion"

    total_koroks = Koroks.query.count()
    total_armors = Armors.query.count()
    total_shrines = Shrines.query.count()
    total_caves = Caves.query.count()
    total_lightroots = Lightroots.query.count()
    total_chests = Chests.query.count()
    total_compendium = Compendium.query.count()

    armorsper = armor_percent()
    shrinesper = shrines_percent()
    koroksper = korok_percent()
    cavesper = caves_percent()
    lightrootsper = lightroots_percent()
    chestsper = chests_percent()
    compendiumper = compendium_percent()
    overall = overall_percent()
    return render_template('index.html', headline=headline, armorsper=armorsper, total_armors=total_armors,
                           shrinesper=shrinesper,koroksper=koroksper, cavesper=cavesper, 
                           total_caves=total_caves, lightrootsper=lightrootsper, 
                           total_lightroots=total_lightroots, chestsper=chestsper, 
                           total_chests=total_chests, compendiumper=compendiumper, overall=overall)

@app.route('/chest_page')
def chest_page():
    headline = "Chests"
    chests_data = Chests.query.order_by(Chests.chest_location.asc()).all()
    unique_values = Chests.query.with_entities(Chests.chest_region).distinct().order_by(Chests.chest_location.asc()).all()
    unique_regions = [value[0] for value in unique_values]
    # print("Testing")
    # print("Values ->", unique_values)
    # print("Regions ->", unique_regions)
    return render_template('chests.html', chests_data=chests_data, headline=headline, unique_regions=unique_regions)

def chest_def(chest_id):  
    chest = Chests.query.get_or_404(chest_id)
    return render_template('chests.html', chest=chest)

@app.route('/sort_chest_region', methods=('POST',))
def sort_chest_region():
    try:
        chestSort = request.json.get('chest_sort')
        chest = Chests.query.filter(Chests.chest_location == chestSort).order_by(Chests.chest_done.asc()).all()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return render_template('chests.html', chest=chest) 
    
@app.route('/add_chest', methods=('GET', 'POST'))
def add_chest():
    try:
        # Get data from the form
        done = request.json.get('done')
        chest_item = request.json.get('chest_item')
        chest_type = request.json.get('chest_type')
        chest_coord = request.json.get('chest_coord')
        chest_region = request.json.get('chest_region')
        chest_location = request.json.get('chest_location')
        chest_sideq = request.json.get("chest_sideq")

        # Create a new Chests instance
        new_chest = Chests(
            chest_done=done,
            chest_item=chest_item,
            chest_type=chest_type,
            chest_coord=chest_coord,
            chest_region=chest_region,
            chest_location=chest_location,
            chest_sideq=chest_sideq
        )

        # Add the new chest entry to the database
        db.session.add(new_chest)
        db.session.commit()
        
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)
        db.session.rollback()
        return jsonify(success=False, error=str(e), message="An error occurred while processing your request."), 400

def checkArmor(pieceName):
    armor = Armors.query.filter_by(name=pieceName).first()
    if armor:
        print("piece:", pieceName, "\nNAME MATCH")
        armor.done = 1
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error:", e)

def checkFabric(pieceName):
    fabric = Fabrics.query.filter_by(f_name=pieceName).first()
    if fabric:
        print("piece:", pieceName, "\nNAME MATCH")
        fabric.f_done = 1
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error:", e)

@app.route('/update_chest', methods=('POST',))
def update_chest():
    try:
        chestID = request.json.get('chest_id')
        chestDone = request.json.get('chest_done')
        chestItem = request.json.get('chest_item')
        checkArmor(chestItem)
        checkFabric(chestItem)

        chest = Chests.query.get_or_404(chestID)

        chest.chest_id = chestID
        chest.chest_done = chestDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 
    
@app.route('/shrine_page')
def shrine_page():
    headline = "Shrines"
    shrines_data = Shrines.query.options(db.joinedload(Shrines.chests)).all()
    chests_data = ShrinesChests.query.all()
    return render_template('shrines.html', shrines_data=shrines_data,chests_data=chests_data, headline=headline)

def shrine_def(shrine_id):  
    shrine = Shrines.query.get_or_404(shrine_id)
    return render_template('shrines.html', shrine=shrine)

# @app.route('/sort_shrine_region', methods=('POST',))
# def sort_shrine_region():
#     try:
#         shrineSort = request.json.get('shrine_sort')
#         shrine = Shrines.query.filter(Shrines.shrine_location == shrineSort).order_by(Shrines.shrine_done.asc()).all()
#         return jsonify(success=True)
#     except Exception as e:
#         print("Error:", e)  # Add this line for debugging
#         return render_template('shrines.html', shrine=shrine) 

@app.route('/update_shrine', methods=('POST',))
def update_shrine():
    try:
        shrineID = request.json.get('shrine_id')
        shrineDone = request.json.get('shrine_done')

        shrine = Shrines.query.get_or_404(shrineID)

        shrine.id = shrineID
        shrine.done = shrineDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 
    
@app.route('/update_shrine_chest', methods=('POST',))
def update_shrine_chest():
    try:
        shrineID = request.json.get('shrine_id')
        chestID = request.json.get('chest_id')
        chestDone = request.json.get('chest_done')

        shrine = Shrines.query.get_or_404(shrineID)
        chest = ShrinesChests.query.get_or_404(chestID)

        shrine.id = shrineID
        shrine.chest_done = chestDone

        chest.id = chestID
        chest.chest_done = chestDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 

@app.route('/lightroot_page')
def lightroot_page():
    headline = "lightroots"
    lightroots_data = Lightroots.query.all()
    unique_values = Lightroots.query.with_entities(Lightroots.root_region).distinct().order_by(Lightroots.root_region.asc()).all()
    unique_regions = [value[0] for value in unique_values]
    # print("Testing")
    # print("Values ->", unique_values)
    # print("Regions ->", unique_regions)
    return render_template('lightroots.html', lightroots_data=lightroots_data, headline=headline, unique_regions=unique_regions)

@app.route('/update_lightroot', methods=('POST',))
def update_lightroot():
    try:
        root_id = request.json.get('root_id')
        root_done = request.json.get('root_done')

        lightroot = Lightroots.query.get_or_404(root_id)

        lightroot.root_id = root_id
        lightroot.root_done = root_done

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)
        db.session.rollback()
        return jsonify(success=False, error=str(e)), 500

@app.route('/cave_page')
def cave_page():
    headline = "Caves"
    caves_data = Caves.query.order_by(Caves.region.asc()).all()
    #unique_values = Caves.query.with_entities(Caves.cave_region).distinct().order_by(Caves.cave_location.asc()).all()
    #unique_regions = [value[0] for value in unique_values]
    # print("Testing")
    # print("Values ->", unique_values)
    # print("Regions ->", unique_regions)
    return render_template('caves.html', caves_data=caves_data, headline=headline)

def cave_def(cave_id):  
    cave = Caves.query.get_or_404(cave_id)
    return render_template('caves.html', cave=cave)
	
@app.route('/update_cave', methods=('POST',))
def update_cave():
    try:
        caveID = request.json.get('cave_id')
        caveDone = request.json.get('cave_done')

        cave = Caves.query.get_or_404(caveID)

        cave.id = caveID
        cave.done = caveDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 
    
@app.route('/update_cave_bfrog', methods=('POST',))
def update_cave_bfrog():
    try:
        caveID = request.json.get('cave_id')
        caveDone = request.json.get('bfrog_done')

        cave = Caves.query.get_or_404(caveID)

        cave.id = caveID
        cave.bfrog_done = caveDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 

@app.route('/korok_page')
def korok_page():
    headline = "Koroks"
    koroks_data = Koroks.query.all()
    unique_values = Koroks.query.with_entities(Koroks.region).distinct().order_by(Koroks.location.asc()).all()
    unique_regions = [value[0] for value in unique_values]
    print("Testing")
    print("Values ->", unique_values)
    print("Regions ->", unique_regions)
    return render_template('koroks.html', koroks_data=koroks_data, headline=headline,unique_regions=unique_regions)

def korok_def(korok_id):  
    korok = Koroks.query.get_or_404(korok_id)
    return render_template('koroks.html', korok=korok)

@app.route('/sort_korok_region', methods=('POST',))
def sort_korok_region():
    try:
        korokSort = request.json.get('korok_sort')
        korok = Koroks.query.filter(Koroks.location == korokSort).order_by(Koroks.korok_done.asc()).all()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return render_template('koroks.html', korok=korok) 
	
@app.route('/update_korok', methods=('POST',))
def update_korok():
    try:
        korokID = request.json.get('korok_id')
        korokDone = request.json.get('korok_done')

        korok = Koroks.query.get_or_404(korokID)

        korok.korok_id = korokID
        korok.korok_done = korokDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 
    
@app.route('/compendium_page')
def compendium_page():
    headline = "Compendium"
    creatures_data = []
    monsters_data = []
    materials_data = []
    equipment_data = []
    treasure_data = []

    compendium_data = Compendium.query.all()
    for data in compendium_data:
        if data.type == "Creatures":
            creatures_data.append(data)
        elif data.type == "Monsters":
            monsters_data.append(data)
        elif data.type == "Materials":
            materials_data.append(data)
        elif data.type == "Equipment":
            equipment_data.append(data)
        elif data.type == "Treasure":
            treasure_data.append(data)

    #unique_values = Compendium.query.with_entities(Compendium.compendium_region).distinct().order_by(Compendium.compendium_location.asc()).all()
    #unique_regions = [value[0] for value in unique_values]
    # print("Testing")
    # print("Values ->", unique_values)
    # print("Regions ->", unique_regions)
    return render_template('compendium.html', compendium_data=compendium_data,creatures_data=creatures_data,
                           monsters_data=monsters_data, materials_data=materials_data,
                           equipment_data=equipment_data,treasure_data=treasure_data, headline=headline)

def compendium_def(compendium_id):  
    compendium = Compendium.query.get_or_404(compendium_id)
    return render_template('compendium.html', compendium=compendium)
	
@app.route('/update_compendium', methods=('POST',))
def update_compendium():
    try:
        compendiumID = request.json.get('compendium_id')
        compendiumDone = request.json.get('compendium_done')

        compendium = Compendium.query.get_or_404(compendiumID)

        compendium.id = compendiumID
        compendium.done = compendiumDone

        db.session.commit()

        return jsonify(succes=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(succes=False, error=str(e)) 

@app.route('/armors')
def armors():
    armors_data = Armors.query.all()
    armor_sets = Armor_sets.query.all()
    
    all_sets_data = create_armor_sets_dictionary()
    print("All Sets Data ->", all_sets_data)
    
    return render_template('armors.html', armors_data=armors_data, all_sets_data=all_sets_data)

def create_armor_sets_dictionary():
    # Initialize the dictionary to store all sets
    all_sets_dict = {}

    # Query all distinct sets from Armor_sets table
    all_set_names = Armor_sets.query.all()

    # Loop through each set and create a dictionary entry
    for set_name in all_set_names:
        set_name = set_name.sets

        # Query all armor items for the current set from Armors table
        armor_items = Armors.query.filter_by(set=set_name).order_by(Armors.set.asc()).all()
        armor_itemsList = [{'id': armor.id, 'done': armor.done, 'name': armor.name} for armor in Armors.query.filter_by(set=set_name).all()]


        print("Armor_itemsList ->", armor_itemsList)
        print("Armor Items ->", armor_items)

        # Create a dictionary for the current set
        set_dict = {"Set": set_name}

        # Loop through each armor item and add it to the dictionary
        for armor_item in armor_itemsList:
            set_dict["Cap"] = armor_itemsList[0]
            set_dict["Tunic"] = armor_itemsList[1]
            set_dict["Trousers"] = armor_itemsList[2]

        # Add the set dictionary to the overall dictionary
        all_sets_dict[set_name] = set_dict

    return all_sets_dict

def armor(Armors_id):  
    armor = Armors.query.get_or_404(Armors_id)
    return render_template('Armors.html', armor=armor)

def checkChest(pieceName):
    chest = Chests.query.filter_by(chest_item=pieceName).first()
    if chest:
        print("piece:", pieceName, "\nNAME MATCH")
        chest.chest_done = 1
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("Error:", e)

@app.route('/update_armor', methods=('POST',))
def update_armor():
    try:
        armorID = request.json.get('armor_id')
        armorDone = request.json.get('armor_done')
        armorPiece = request.json.get('armor_item')
        checkChest(armorPiece)

        armors = Armors.query.get_or_404(armorID)

        armors.id = armorID
        armors.done = armorDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 
    
@app.route('/well_page')
def well_page():
    headline = "Wells"
    wells_data = Locations.query.filter_by(type="Well").order_by(Locations.region.asc()).all()
    #unique_values = Locations.query.with_entities(Locations.well_region).distinct().order_by(Locations.well_location.asc()).all()
    #unique_regions = [value[0] for value in unique_values]
    # print("Testing")
    # print("Values ->", unique_values)
    # print("Regions ->", unique_regions)
    return render_template('well.html', wells_data=wells_data, headline=headline)

def well_def(well_id):  
    well = Locations.query.get_or_404(well_id)
    return render_template('well.html', well=well)
	
@app.route('/update_well', methods=('POST',))
def update_well():
    try:
        wellID = request.json.get('well_id')
        wellDone = request.json.get('well_done')

        well = Locations.query.get_or_404(wellID)

        well.id = wellID
        well.done = wellDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 
    
@app.route('/sort_well_region', methods=('POST',))
def sort_well_region():
    try:
        wellSort = request.json.get('well_sort')
        well = Locations.query.filter(Locations.location == wellSort).order_by(Locations.well_done.asc()).all()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return render_template('well.html', well=well) 
	
@app.route('/mines_page')
def mines_page():
    headline = "Depths Mines"
    mines_data = Locations.query.filter_by(type="Depths Mine").order_by(Locations.region.asc()).all()
    #unique_values = Locations.query.with_entities(Locations.region).distinct().order_by(Locations.location.asc()).all()
    #unique_regions = [value[0] for value in unique_values]
    # print("Testing")
    # print("Values ->", unique_values)
    # print("Regions ->", unique_regions)
    return render_template('mines.html', mines_data=mines_data, headline=headline)

def mine_def(mine_id):  
    mine = Locations.query.get_or_404(mine_id)
    return render_template('mines.html', mine=mine)
	
@app.route('/update_mine', methods=('POST',))
def update_mine():
    try:
        mineID = request.json.get('mine_id')
        mineDone = request.json.get('mine_done')

        mine = Locations.query.get_or_404(mineID)

        mine.id = mineID
        mine.done = mineDone

        db.session.commit()

        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(success=False, error=str(e)) 

@app.route('/tear_page')
def tear_page():
    headline = "Dragon's Tears"
    tears_data = Dragontears.query.all()
    
    return render_template('dragontears.html', tears_data=tears_data, headline=headline)

def tear_def(tear_id):  
    tear = Dragontears.query.get_or_404(tear_id)
    return render_template('dragontears.html', tear=tear)
	
@app.route('/update_tear', methods=('POST',))
def update_tear():
    try:
        tearID = request.json.get('tear_id')
        tearDone = request.json.get('tear_done')

        tear = Dragontears.query.get_or_404(tearID)

        tear.id = tearID
        tear.done = tearDone

        db.session.commit()

        return jsonify(succes=True)
    except Exception as e:
        print("Error:", e)  # Add this line for debugging
        return jsonify(succes=False, error=str(e)) 

if __name__ == "__main__":
    app.run(debug=True)
