'''root of views'''
from sre_parse import State
from flask import jsonify
from api.v1.views import app_views
from models.amenity import Amenity
from models import storage
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


@app_views.route('/status')
def status():
    '''checks status'''
    return jsonify({'status': 'ok'})


@app_views.route('/stats')
def stats():
    '''fetches stats'''
    data= {
        "amenities": storage.all(Amenity), 
        "cities": storage.all(City), 
        "places": storage.all(Place), 
        "reviews": storage.all(Review), 
        "states": storage.all(State), 
        "users": storage.all(User)
    }
    return jsonify(data)
