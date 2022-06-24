from molsysmt._private.digestion import digest_item, digest_atom_indices, digest_structure_indices

def to_molsysmt_Structures(item, atom_indices='all', structure_indices='all', check=True):

    if check:

        digest_item(item, 'file:xtc')
        atom_indices = digest_atom_indices(atom_indices)
        structure_indices = digest_structure_indices(structure_indices)

    from . import to_mdtraj_XTCTrajectoryFile
    from ..mdtraj_XTCTrajectoryFile import to_molsysmt_Structures as mdtraj_XTCTrajectoryFile_to_molsysmt_Structures

    tmp_item = to_mdtraj_XTCTrajectoryFile(item, check=False)
    tmp_item = mdtraj_XTCTrajectoryFile_to_molsysmt_Structures(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices, check=False)

    return tmp_item
