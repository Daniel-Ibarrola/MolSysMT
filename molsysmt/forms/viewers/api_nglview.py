from os.path import basename as _basename
from nglview import widget as _nglview_widget

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form = {
    'nglview': form_name,
    _nglview_widget.NGLWidget: form_name
    }

info=["",""]

with_topology=True
with_trajectory=True

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

###### Get

## system

def get_form_from_system(item, indices='all', frame_indices='all'):

    from molsysmt import get_form
    return get_form(item)

