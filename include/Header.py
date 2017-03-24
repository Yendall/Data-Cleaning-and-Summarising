
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