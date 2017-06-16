"""
Author: Leo Vidarte <http://nerdlabs.com.ar>

This is free software,
you can redistribute it and/or modify it
under the terms of the GPL version 3
as published by the Free Software Foundation.

"""

import flask_shelve as shelve
from flask import request


def get(path, db):
    if path:
        keys = _get_keys(path)
        return _get(db, *keys)
    else:
        return dict(db), None

def post(path, db, value):
    keys = _get_keys(path)
    return _post(db, value, *keys)

def delete(path, db):
    keys = _get_keys(path)
    return _delete(db, *keys)


# Private

def _get_keys(path):
    if path.endswith('/'):
        path = path[:-1]
    return path.split('/')

def _get(db, key, *keys, path=''):
    if not _is_dict(db):
        return None, "{} not a dict".format(path)
    if key not in db.keys():
        return None, "{} not in {}".format(key, path)
    if keys:
        path = _get_path(path, key)
        return _get(db[key], *keys, path=path)
    else:
        return db[key], None

def _post(db, value, key, *keys, path=''):
    if not _is_dict(db):
        return None, "not a dict"
    if key not in db.keys():
        db[key] = {}
    if keys:
        path = _get_path(path, key)
        return _post(db[key], value, *keys, path=path)
    else:
        if _is_dict(value) and _is_dict(db[key]):
            _id = _get_next_id(db[key])
            value['_id'] = _id
            db[key][_id] = value
        else:
            db[key] = value
        return value, None

def _delete(db, key, *keys, path=''):
    if not _is_dict(db):
        return None, "{} not a dict".format(path)
    if key not in db.keys():
        return None, "{} not in {}".format(key, path)
    if keys:
        path = _get_path(path, key)
        return _delete(db[key], *keys, path=path)
    else:
        value = db[key]
        del db[key]
        return value, None

def _get_path(path, key):
    return key if path == '' else path + '/' + key

def _is_dict(db):
    return type(db) in (dict, shelve.shelve.DbfilenameShelf)

def _get_next_id(db):
    keys = sorted([int(k) for k in db.keys()])
    return str(keys[-1] + 1) if keys else '1'

