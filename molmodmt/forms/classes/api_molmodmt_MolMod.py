from os.path import basename as _basename
from molmodmt.utils.exceptions import *
from molmodmt import MolMod as _molmodmt_MolMod

form_name=_basename(__file__).split('.')[0].replace('api_','').replace('_','.')

is_form={
    _molmodmt_MolMod : form_name,
    'molmodmt.MolMod': form_name
}


def to_aminoacids3_seq(item, atom_indices='all', frame_indices='all'):

    from .api_mdtraj_Topology import to_aminoacids3_seq as mdtraj_Topology_to_aminoacids3_seq

    tmp_item = to_mdtraj_Topology(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = mdtraj_Topology_to_aminoacids3_seq(tmp_item)
    return tmp_item

def to_aminoacids1_seq(item, atom_indices='all', frame_indices='all'):

    from molmodmt.forms.seqs.api_aminoacids3 import to_aminoacids1_seq as aminoacids3_seq_to_aminoacids1_seq
    tmp_item = to_aminoacids3_seq(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = aminoacids3_seq_to_aminoacids1_seq(tmp_item)
    return tmp_item

def to_biopython_Seq(item, atom_indices='all', frame_indices='all'):

    from molmodmt.forms.seqs.api_aminoacids1 import to_biopython_Seq as aminoacids1_to_biopython_Seq
    tmp_item = to_aminoacids1_seq(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = aminoacids1_to_biopython_Seq(tmp_item)
    return tmp_item

def to_biopython_SeqRecord(item, atom_indices='all', frame_indices='all'):

    from molmodmt.forms.seqs.api_aminoacids1 import to_biopython_SeqRecord as aminoacids1_to_biopython_SeqRecord
    tmp_item = to_aminoacids1_seq(item, atom_indices=atom_indices, frame_indices=frame_indices)
    tmp_item = aminoacids1_to_biopython_SeqRecord(tmp_item)
    return tmp_item

def to_mdtraj_Trajectory(item, atom_indices='all', frame_indices='all'):

    from simtk import unit as _unit
    from mdtraj.core.trajectory import Trajectory as mdtraj_Trajectory

    tmp_item_topology = to_mdtraj_Topology(item, atom_indices=atom_indices)
    tmp_box_lengths = get_box_lengths_from_system(item, frame_indices=frame_indices)
    tmp_box_lengths = tmp_box_lengths.in_units_of(_unit.nanometers)._value
    tmp_box_angles = get_box_angles_from_system(item, frame_indices=frame_indices)
    tmp_box_angles = tmp_box_angles.in_units_of(_unit.degrees)._value
    tmp_coordinates = get_coordinates_from_atom(item, indices=atom_indices, frame_indices=frame_indices)
    tmp_coordinates = tmp_coordinates.in_units_of(_unit.nanometers)._value
    tmp_time = get_coordinates_from_system(item, frame_indices=frame_indices)
    tmp_time = tmp_time.in_units_of(_unit.picoseconds)._value
    tmp_item = mdtraj_Trajectory(tmp_coordinates,tmp_item_topology, tmp_time,
            unitcell_lengths=tmp_box_lengths, unitcell_angles=tmp_box_angles)

    return tmp_item

def to_mdtraj_Topology(item, atom_indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import to_mdtraj_Topology as molmodmt_Topology_to_mdtraj_Topology
    return molmodmt_Topology_to_mdtraj_Topology(item.topology, atom_indices=atom_indices,
                                                frame_indices=frame_indices)

def to_pdb(item, output_file_path=None, atom_indices='all', frame_indices='all'):

    from molmodmt.native.io_molmod import to_pdb as molmodmt_MolMod_to_pdb
    return molmodmt_MolMod_to_pdb(item, output_file_path=output_file_path, selection=atom_indices,
            frame_indices=frame_indices)

def select_with_MDTraj(item, selection=None):
    from molmodmt import select
    return select(item.topology, selection=selection, syntaxis="MDTraj")

def extract_subsystem(item, atom_indices='all', frame_indices='all'):

    if (atom_indices is 'all') and (frame_indices is 'all'):
        return item
    else:
        raise NotImplementedError

def to_nglview(item, atom_indices='all', frame_indices='all'):

    from .api_mdtraj_Trajectory import to_nglview as mdtraj_to_nglview

    tmp_item = to_mdtraj_Trajectory(item, atom_indices=atom_indices, frame_indices=frame_indices)

    return mdtraj_to_nglview(tmp_item)

def duplicate(item):

    return tmp_item.duplicate()

###### Get

## atom

def get_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_element_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_element_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_residue_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_residue_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_residue_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_residue_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_residue_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_residue_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_name_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_chain_name_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_index_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_chain_index_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_chain_id_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_chain_id_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_aminoacids_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_aminoacids_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_nucleotides_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_nucleotides_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_waters_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_waters_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_ions_from_atom (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_ions_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_coordinates_from_atom(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Trajectory import get_coordinates_from_atom as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_bonded_atoms_from_atom(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_bonded_atoms_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    tmp_indices = [trajectory_indices[ii] for ii in indices]
    bonded_atoms_topology = _get(item.topology, indices=tmp_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    bonded_atoms = {}
    for ii_topology, ii_bonded_topology in bonded_atoms_topology.items():
        bonded_atoms[traduction[ii_topology]]=[traduction[jj] for jj in ii_bonded_topology]

    return bonded_atoms

def get_molecules_from_atom(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_molecules_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    tmp_indices = [trajectory_indices[ii] for ii in indices]
    molecules_topology = _get(item.topology, indices=tmp_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    molecules = []
    for tmp_molecule in molecules_topology:
        molecules.append([traduction[ii] for ii in tmp_molecule])

    return molecules

def get_molecule_type_from_atom(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_molecule_type_from_atom as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

## residue

## chain

## system

def get_n_atoms_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Trajectory import get_n_atoms_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_n_residues_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_residues_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_chains_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_chains_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_aminoacids_from_system (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_aminoacids_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_nucleotides_from_system (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_nucleotides_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_waters_from_system (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_waters_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_ions_from_system (item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_ions_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_n_molecules_from_system(item, indices='all', frame_indices='all'):

    return len(get_molecules_from_system(item, indices=indices))

def get_n_frames_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Trajectory import get_n_frames_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_n_bonds_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_n_bonds_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)


def get_masses_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_masses_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_bonded_atoms_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_bonded_atoms_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    bonded_atoms_topology = _get(item.topology, indices=trajectory_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    bonded_atoms = {}
    for ii_topology, ii_bonded_topology in bonded_atoms_topology.items():
        bonded_atoms[traduction[ii_topology]]=[traduction[jj] for jj in ii_bonded_topology]

    return bonded_atoms

def get_bonds_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_bonds_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_graph_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_graph_from_system as _get
    return _get(item.topology, indices=indices, frame_indices=frame_indices)

def get_molecules_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Topology import get_molecules_from_atom as _get
    trajectory_indices = item.trajectory.file.atom_indices
    molecules_topology = _get(item.topology, indices=trajectory_indices, frame_indices=frame_indices)
    traduction = { trajectory_indices[ii] : ii for ii in range(len(trajectory_indices)) }
    molecules = []
    for tmp_molecule in molecules_topology:
        molecules.append([traduction[ii] for ii in tmp_molecule])

    return molecules

def get_coordinates_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Trajectory import get_coordinates_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Trajectory import get_box_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_time_from_system(item, indices='all', frame_indices='all'):

    from .api_molmodmt_Trajectory import get_time_from_system as _get
    return _get(item.trajectory, indices=indices, frame_indices=frame_indices)

def get_box_shape_from_system(item, indices='all', frame_indices='all'):

    return item.trajectory.box_shape

def get_box_lengths_from_system(item, indices='all', frame_indices='all'):

    tmp_box_lengths = item.trajectory.get_box_lengths()
    tmp_box_lengths = tmp_box_lengths[frame_indices,:]
    return tmp_box_lengths

def get_box_angles_from_system(item, indices='all', frame_indices='all'):

    tmp_box_angles = item.trajectory.get_box_angles()
    tmp_box_angles = tmp_box_angles[frame_indices,:]
    return tmp_box_angles

def get_form_from_system(item, indices='all', frame_indices='all'):

    from molmodmt import get_form
    return get_form(item)

###### Set

def set_box_to_system(item, indices='all', frame_indices='all', value=None):

    item.trajectory.box = value
    pass

def set_coordinates_to_system(item, indices='all', frame_indices='all', value=None):

    item.trajectory.coordinates = value
    pass

