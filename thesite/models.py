from application import db

class Chests(db.Model):
    chest_id = db.Column(db.Integer, primary_key=True)
    chest_done = db.Column(db.Integer, nullable=False)
    chest_item = db.Column(db.String(100), nullable=False)
    chest_type = db.Column(db.Text, nullable=False)
    chest_coord = db.Column(db.Text)
    chest_region = db.Column(db.Text)
    chest_location = db.Column(db.Text)
    chest_sideq = db.Column(db.Text)
    
    def __repr__(self):
        return f'{self.chest_name}'
    
class Lightroots(db.Model):
    root_id = db.Column(db.Integer, primary_key=True)
    root_done = db.Column(db.Integer, nullable=False)
    root_name = db.Column(db.String(100), nullable=False)
    root_coord = db.Column(db.Text)
    root_region = db.Column(db.Text)
    
    def __repr__(self):
        return f'{self.root_name}'
    
class Shrines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text)
    title = db.Column(db.Text)
    location = db.Column(db.Text)
    region = db.Column(db.Text)
    coord = db.Column(db.Text)
    quest = db.Column(db.Text)
    chests = db.relationship('ShrinesChests', backref='shrine', lazy=True)

    def __repr__(self):
        return f'{self.name}'

class ShrinesChests(db.Model):
    chests_id = db.Column(db.Integer, primary_key=True)
    shrine_id = db.Column(db.Integer, db.ForeignKey('shrines.id'), nullable=False)
    name = db.Column(db.Text)
    chest_done = db.Column(db.Integer, nullable=False)
    chest = db.Column(db.Text)
    
    def __repr__(self):
        return f'{self.name}'
    
class Caves(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text)
    location = db.Column(db.Text)
    region = db.Column(db.Text)
    coord = db.Column(db.Text)
    bfrog = db.Column(db.Text)
    bfrog_done = db.Column(db.Integer, nullable=False)
    shrine = db.Column(db.Text)
    def __repr__(self):
        return f'{self.name}'
    
class cave_things(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    items = db.Column(db.String(100), nullable=False)
    chests = db.Column(db.String(100), nullable=False)
    enemies = db.Column(db.Text, nullable=False)    
    
    def __repr__(self):
        return f'{self.name}'
    
class Koroks(db.Model):
    korok_id = db.Column(db.Integer, primary_key=True)
    korok_name = db.Column(db.Text)
    korok_done = db.Column(db.Integer, nullable=False)
    korok_type = db.Column(db.Text)
    startcoord = db.Column(db.Text)
    coord = db.Column(db.Text)
    location = db.Column(db.Text)
    region = db.Column(db.Text)
    tower = db.Column(db.Text)
    def __repr__(self):
        return f'{self.name}'

class Compendium(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Text)
    type = db.Column(db.Text)
    done = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f'{self.name}'
    
class Armors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    set = db.Column(db.String(100), nullable=False)
    chest_id = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f'{self.name}'
    
class Armor_sets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sets = db.Column(db.String(100), nullable=False)
   
    def __repr__(self):
        return f'{self.sets}'

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text)
    region = db.Column(db.Text)
    coord = db.Column(db.Text)
    type = db.Column(db.Text)
    
    def __repr__(self):
        return f'{self.name}'
    
class Fabrics(db.Model):
    f_id = db.Column(db.Integer, primary_key=True)
    f_done = db.Column(db.Integer, nullable=False)
    f_name = db.Column(db.Text)
    f_description = db.Column(db.Text)
    f_type = db.Column(db.Text)
    f_pic = db.Column(db.Text)
    
    def __repr__(self):
        return f'{self.name}'
    
class Dragontears(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text)
    memory = db.Column(db.Text)
    coord = db.Column(db.Text)
    location = db.Column(db.Text)
    tower = db.Column(db.Text)

    def __repr__(self):
        return f'{self.name}'