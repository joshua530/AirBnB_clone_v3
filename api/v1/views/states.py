#!/usr/bin/python3
'''contains state routes'''
from flask import jsonify, abort
from models.state import State
from api.v1.views import app_views
from models import storage


@app_views.route('/states', methods=['GET'])
def states():
    '''retrieves all state objects'''
    states = storage.all(State)
    data = [state.to_dict() for state in states.values()]
    return jsonify(data)


@app_views.route('/states/<state_id>', methods=['GET'])
def state_from_id(state_id):
    '''retrieves state using id'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())

@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''deletes a state'''
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({}), 200
