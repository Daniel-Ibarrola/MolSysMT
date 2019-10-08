from os.path import basename as _basename
from simtk.unit.quantity import Quantity

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    'xyz' : form_name,
    'XYZ' : form_name,
    Quantity : form_name
}



def get_coordinates_from_atom(item, indices=None, frame_indices=None):

    tmp_coordinates=None

    if len(item.shape)==3:
        tmp_coordinates = item[:,indices,:]
    elif len(item.shape)==2:
        from numpy import zeros
        n_frames=1
        n_atoms=item.shape[0]
        tmp_coordinates = zeros([n_frames, n_atoms, 3])*item.unit
        tmp_coordinates[0,:,:] = item[:,:]
        tmp_coordinates = tmp_coordinates[:,indices,:]

    return tmp_coordinates

def get_coordinates_from_system(item, indices=None, frame_indices=None):

    tmp_coordinates=None

    if len(item.shape)==3:
        tmp_coordinates = item
    elif len(item.shape)==2:
        from numpy import zeros
        n_frames=1
        n_atoms=item.shape[0]
        tmp_coordinates = zeros([n_frames, n_atoms, 3])*item.unit
        tmp_coordinates[0,:,:] = item[:,:]

    return tmp_coordinates

def get_n_frames_from_system(item, indices=None, frame_indices=None):

    n_frames=0
    if len(item.shape)==3:
        n_frames = item.shape[0]
    elif len(item.shape)==2:
        n_frames = 1

    return n_frames

def get_n_atoms_from_system(item, indices=None, frame_indices=None):

    n_atoms=0
    if len(item.shape)==3:
        n_atoms = item.shape[1]
    elif len(item.shape)==2:
        n_atoms = item.shape[0]

    return n_atoms

def get_box_from_system(item, indices=None, frame_indices=None):

    return None

def get_box_shape_from_system(item, indices=None, frame_indices=None):

    return None

