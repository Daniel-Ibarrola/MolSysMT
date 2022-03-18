from .is_string_pdb_id import is_string_pdb_id
from molsysmt._private_tools.exceptions import WrongFormError, WrongAtomIndicesError, WrongStructureIndicesError
from molsysmt._private_tools.atom_indices import digest_atom_indices
from molsysmt._private_tools.structure_indices import digest_structure_indices

def to_file_msmpk(item, atom_indices='all', structure_indices='all', output_filename=None, check=True):

    if check:

        try:
            is_string_pdb_id(item)
        except:
            raise WrongFormError('string:pdb_id')

        try:
            atom_indices = digest_atom_indices(atom_indices)
        except:
            raise WrongAtomIndicesError()

        try:
            structure_indices = digest_structure_indices(structure_indices)
        except:
            raise WrongStructureIndicesError()

    from molsysmt.tools.string_pdb_id import to_molsysmt_MolSys as string_pdb_id_to_molsysmt_MolSys
    from molsysmt.tools.molsysmt_MolSys import to_file_msmpk as molsysmt_MolSys_to_file_msmpk

    tmp_item = string_pdb_id_to_molsysmt_MolSys(item, atom_indices=atom_indices, structure_indices=structure_indices, check=False)
    tmp_item = molsysmt_MolSys_to_file_msmpk(tmp_item, output_filename=output_filename, check=False)

    return tmp_item

