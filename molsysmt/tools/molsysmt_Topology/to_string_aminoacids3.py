def to_string_aminoacids3(item, group_indices='all', check=True):

    if check:
        from molsysmt.tools.molsysmt_Topology import is_molsymst_Topology
        from molsysmt._private_tools.exceptions import WrongFormError
        if not is_molsysmt_Topology(item):
            raise WrongFormError('molsysmt.Topology')

    from molsysmt.tools.molsysmt_Topology import get_group_name_from_group

    group_names = get_group_name_from_group(item, indices=group_indices, check=False)
    tmp_item = ''.join([ii.title() for ii in group_names])

    return tmp_item

