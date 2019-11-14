from os.path import basename as _basename
from pandas import DataFrame

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    'pandas.DataFrame' : form_name,
    DataFrame : form_name
}

def extract_subsystem(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def duplicate(item):

    raise NotImplementedError

###### Get

## atom


## system

def get_form_from_system(item, indices='all', frame_indices='all'):

    return form_name

