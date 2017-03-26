#!/usr/bin/env python
"""

Header.py : Header Class File for storing look-up tables

"""
__author__ = "Max Yendall - s3436993"
__version__ = "1.0"


class Header:
    def __init__(self):
        pass

    header = \
        {
            'minority': 'object',
            'age': 'int64',
            'gender': 'object',
            'credits': 'object',
            'beauty': 'float64',
            'eval': 'float64',
            'division': 'object',
            'native': 'object',
            'tenure': 'object',
            'students': 'int64',
            'allstudents': 'int64',
            'prof': 'object'

        }
    type_conversions = \
        {
            'object': 'string',
            'int64': 'numeric_int',
            'float64': 'numeric_float',
            'boolean': 'boolean'
        }

    range_lookup = \
        {
            'age': {'lower': 0, 'upper': 100, 'round': 0},
            'eval': {'lower': 1, 'upper': 5, 'round': 1}
        }

    typo_lookup = \
        {
            'credits': ['more', 'single'],
            'division': ['upper', 'lower'],
            'native': ['yes', 'no'],
            'tenure': ['yes', 'no'],
            'gender': ['male', 'female'],
            'minority': ['yes', 'no'],
        }
