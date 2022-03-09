from molsysmt.tools.string_pdb_id.is_string_pdb_id import is_string_pdb_id
from molsysmt._private_tools.exceptions import WrongFormError, WrongAtomIndicesError, WrongStructureIndicesError
from molsysmt._private_tools.atom_indices import digest_atom_indices, digest_structure_indices

def to_parmed_Structure(item, atom_indices='all', structure_indices='all', check=True):

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

    from molsysmt.tools.string_pdb_id import to_string_pdb_text as string_pdb_id_to_string_pdb_text
    from molsysmt.tools.string_pdb_text import to_parmed_Structure as string_pdb_text_to_parmed_Structure

    tmp_item = string_pdb_id_to_string_pdb_text(item, check=False)
    tmp_item = string_pdb_text_to_parmed_Structure(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices, check=True)

    return tmp_item

