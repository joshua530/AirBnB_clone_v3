#!/usr/bin/python3
'''contains amenity routes'''
from flask import jsonify, abort, request
from models.city import City
from models.state import State
from models.amenity import Amenity
from api.v1.views import app_views
from models import storage


@app_views.route('/amenities', methods=['GET'])
def all_amenities():
    '''retrieves all amenities'''
    amenities = [a.to_dict() for a in storage.all(Amenity).values()]
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    '''retrieves amenity using id'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    '''deletes amenity'''
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'])
def create_amenity():
    '''creates new amenity'''
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    elif 'name' not in request.get_json():
        return jsonify({'error': 'Missing name'}), 400
    else:
        data = request.get_json()
        obj = Amenity(**data)
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    '''updates amenity'''
    if not request.get_json():
        return jsonify({'error': 'Not a JSON'}), 400
    obj = storage.get('Amenity', amenity_id)
    if obj is None:
        abort(404)
    data = request.get_json()
    obj.name = data['name']
    obj.save()
    return jsonify(obj.to_dict()), 200
