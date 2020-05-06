from os.path import basename as _basename

form_name=_basename(__file__).split('.')[0].split('_')[-1]

is_form = {
    'dcd': form_name,
    'DCD': form_name
    }

info=["",""]
with_topology=False
with_trajectory=True

def to_mdtraj_Trajectory(item, topology=None, atom_indices='all', frame_indices='all'):

    if not topology:
        raise ValueError('"topology" argument is required to convert a dcd file to mdtraj_Trajectory')

    raise NotImplementedError

def to_mdanalysis_Universe(item, topology=None, atom_indices='all', frame_indices='all'):

    if not topology:
        raise ValueError('"topology" argument is required for dcd.to_mdtraj')

    raise NotImplementedError

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

    return form_name

