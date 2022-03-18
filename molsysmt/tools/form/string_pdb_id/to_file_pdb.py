from .is_string_pdb_id import is_string_pdb_id
from molsysmt._private_tools.exceptions import WrongFormError, WrongAtomIndicesError, WrongStructureIndicesError
from molsysmt._private_tools.atom_indices import digest_atom_indices
from molsysmt._private_tools.structure_indices import digest_structure_indices

def to_file_pdb(item, atom_indices='all', structure_indices='all', output_filename=None, check=True):

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

    from molsysmt.tools.file_pdb import download, extract

    download_pdb(item, output_filename, check=False)
    tmp_item = extract(tmp_item, atom_indices=atom_indices, structure_indices=structure_indices,
            output_filename=output_filename, copy_if_all=False, check=False)

    return tmp_item

