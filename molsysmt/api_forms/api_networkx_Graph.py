from molsysmt._private.exceptions import *

from molsysmt.form.networkx_Graph.is_networkx_Graph import is_networkx_Graph as is_form
from molsysmt.form.networkx_Graph.extract import extract
from molsysmt.form.networkx_Graph.add import add
from molsysmt.form.networkx_Graph.append_structures import append_structures
from molsysmt.form.networkx_Graph.get import *
from molsysmt.form.networkx_Graph.set import *

import numpy as np

form_name='networkx.Graph'
form_type='class'
form_info=["",""]

form_attributes = {

    'atom_index' : True,
    'atom_id' : False,
    'atom_name' : False,
    'atom_type' : False,

    'bond_index' : True,
    'bond_id' : False,
    'bond_name' : False,
    'bond_type' : False,
    'bond_order' : False,
    'bonded_atoms' : True,

    'group_index' : False,
    'group_id' : False,
    'group_name' : False,
    'group_type' : False,

    'component_index' : False,
    'component_id' : False,
    'component_name' : False,
    'component_type' : False,

    'molecule_index' : False,
    'molecule_id' : False,
    'molecule_name' : False,
    'molecule_type' : False,

    'chain_index' : False,
    'chain_id' : False,
    'chain_name' : False,
    'chain_type' : False,

    'entity_index' : False,
    'entity_id' : False,
    'entity_name' : False,
    'entity_type' : False,

    'coordinates' : False,
    'velocities' : False,
    'box' : False,
    'time' : False,
    'step' : False,

    'forcefield' : False,
    'temperature' : False,
    'pressure' : False,
    'integrator' : False,
    'damping' : False,

}

def extract(item, atom_indices='all', structure_indices='all'):

    if (atom_indices is 'all') and (structure_indices is 'all'):
        tmp_item = item.copy()
    else:
        tmp_item = item.subgraph(atom_indices).copy()

    return tmp_item

def merge(item_1, item_2):

    raise NotImplementedError

def add(to_item, item):

    raise NotImplementedError

def append_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

def concatenate_structures(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError()

###### Get

## system


