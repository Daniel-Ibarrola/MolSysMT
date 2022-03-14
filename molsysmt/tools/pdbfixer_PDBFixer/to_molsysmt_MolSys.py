from molsysmt.tools.pdbfixer_PDBFixer.is_pdbfixer_PDBFixer import is_pdbfixer_PDBFixer
from molsysmt._private_tools.exceptions import WrongFormError, WrongAtomIndicesError
from molsysmt._private_tools.atom_indices import digest_atom_indices

def to_molsysmt_MolSys(item, atom_indices='all', check=True):

    if check:

        try:
            is_pdbfixer_PDBFixer(item)
        except:
            raise WrongFormError('pdbfixer.PDBFixer')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

    from molsysmt.native.molsys import MolSys
    from molsysmt.tools.pdbfixer_PDBFixer import to_molsysmt_Topology as pdbfixer_PDBFixer_to_molsysmt_Topology
    from molsysmt.tools.pdbfixer_PDBFixer import to_molsysmt_Structures as pdbfixer_PDBFixer_to_molsysmt_Structures

    tmp_item = MolSys()

    tmp_item.topology = pdbfixer_PDBFixer_to_molsysmt_Topology(item, atom_indices=atom_indices, check=False)
    tmp_item.structures = pdbfixer_PDBFixer_to_molsysmt_Structures(item, atom_indices=atom_indices, check=False)

    return tmp_item

