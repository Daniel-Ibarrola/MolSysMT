from molsysmt._private_tools.exceptions import *
from molsysmt.forms.common_gets import *
import numpy as np

form_name='mol2'

is_form = {
    'mol2': form_name,
    'MOL2': form_name
    }

info=["",""]
with_topology=True
with_coordinates=True
with_box=False
with_bonds=True
with_parameters=True
with_simulation=False

def to_parmed_Structure(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from parmed import load_file as _parmed_file_loader

    tmp_item = _parmed_file_loader(item)
    tmp_item = tmp_item.to_structure()

    return tmp_item

def to_mdtraj_Trajectory(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from mdtraj import load_mol2 as _mdtraj_load_mol2

    tmp_item = _mdtraj_load_mol2(item)
    del(_mdtraj_load_mol2)

    return tmp_item

def to_mdtraj_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from mdtraj import load_mol2 as _mdtraj_load_mol2

    tmp_item = _mdtraj_load_mol2(item).topology
    del(_mdtraj_load_mol2)

    return tmp_item

def to_openmm_Topology(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from molsysmt.forms.classes.api_mdtraj_Topology import to_openmm_Topology as mdtraj_Topology_to_openmm_Topology

    tmp_item = to_mdtraj_Topology(item, molecular_system, atom_indices=atom_indices, frame_indices=atom_indices)
    tmp_item = mdtraj_Topology_to_openmm_Topology(tmp_item)

    return tmp_item

def to_openmm_Modeller(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from molsysmt.forms.classes.api_mdtraj_Trajectory import to_openmm_Modeller as mdtraj_Trajectory_to_openmm_Modeller

    tmp_item = to_mdtraj_Trajectory(item, atom_indices=atom_indices, frame_indices=atom_indices)
    tmp_item = mdtraj_Trajectory_to_openmm_Modeller(tmp_item)

    return tmp_item

    #from molsysmt.forms.engines.api_parmed import to_modeller as _parmed_to_modeller
    #tmp_form = to_parmed(item)
    #tmp_form = _parmed_to_modeller(tmp_form)
    #del(_parmed_to_modeller)
    #return tmp_form

def to_pdb(item, molecular_system=None, atom_indices='all', frame_indices='all', output_filename=None):

    from parmed import load_file as _parmed_file_loader

    tmp_item = _parmed_file_loader(item)
    tmp_item.save(output_filename)

    return output_filename

def to_nglview_NGLWidget(item, molecular_system=None, atom_indices='all', frame_indices='all'):

    from nglview import show_file as nglview_show_file

    tmp_item = nglview_show_file(item)

    return tmp_item

def extract(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def copy(item):

    raise NotImplementedError

def add(item, from_item, atom_indices='all', frame_indices='all'):

    raise NotImplementedError

def append_frames(item, step=None, time=None, coordinates=None, box=None):

    raise NotImplementedError

###### Get

## atom

def get_atom_id_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_atom_name_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_atom_type_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_group_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_component_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_index_from_atom as _get
    return _get(item, indices=indices)

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_molecule_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_index_from_atom as _get
    return _get(item, indices=indices)

def get_entity_index_from_atom (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_index_from_atom as _get
    return _get(item, indices=indices)

def get_inner_bonded_atoms_from_atom (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_inner_bonds_from_atom (item, indices='all', frame_indices='all'):

    if indices is 'all':
        return get_n_inner_bonds_from_system (item)
    else:
        raise NotImplementedError

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_frame_from_atom(item, indices='all', frame_indices='all'):

    raise NotImplementedError

## group

def get_group_id_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_group_name_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_group_type_from_group(item, indices='all', frame_indices='all'):

    raise NotImplementedError

## component

def get_component_id_from_component (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_id_from_component as get
    return get(item, indices)

def get_component_name_from_component (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_name_from_component as get
    return get(item, indices)

def get_component_type_from_component (item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_component_type_from_component as get
    return get(item, indices)

## molecule

def get_molecule_id_from_molecule (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_id_from_molecule as get
    return get(item, indices)

def get_molecule_name_from_molecule (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_name_from_molecule as get
    return get(item, indices)

def get_molecule_type_from_molecule (item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_molecule_type_from_molecule as get
    return get(item, indices)

## chain

def get_chain_id_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_chain_name_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_chain_type_from_chain (item, indices='all', frame_indices='all'):

    raise NotImplementedError

## entity

def get_entity_id_from_entity (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_id_from_molecule as get
    return get(item, indices)

def get_entity_name_from_entity (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_name_from_molecule as get
    return get(item, indices)

def get_entity_type_from_entity (item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_entity_type_from_molecule as get
    return get(item, indices)

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_groups_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_components_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.elements.component import get_n_components_from_system as get
    return get(item, indices)

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.elements.molecule import get_n_molecules_from_system as get
    return get(item, indices)

def get_n_entities_from_system(item, indices='all', frame_indices='all'):

    from molsysmt.elements.entity import get_n_entities_from_system as get
    return get(item, indices)

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_box_volume_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_time_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_step_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    raise NotImplementedError

## bond

def get_bond_order_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_bond_type_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError

def get_atom_index_from_bond(item, indices='all', frame_indices='all'):

    raise NotImplementedError

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    raise NotImplementedError


