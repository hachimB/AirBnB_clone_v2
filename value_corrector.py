#!/usr/bin/python3
"""Module documentation"""


def value_corrector(value):
    """value_corrector documentation"""
    if value.startswith('"') and value.endswith('"'):
        value = value[1:-1].replace('\\"', '"').replace('"', r'\"')
        return value
    elif '.' in value:
        return float(value)
    elif value.isdigit():
        return int(value)
    else:
        return None
