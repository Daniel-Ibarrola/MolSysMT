def to_mdanalysis_Universe(item, atom_indices='all', model_indices='all', check_form=True):

    if check_form:
        from molsysmt.tools.string_pdb_id.is_string_pdb_id import _checking_form
        _checking_form(item, check_form=check_form)

    from molsysmt.tools.string_pdb_id import to_molsysmt_MolSys as string_pdb_id_to_molsysmt_MolSys
    from molsysmt.tools.molsysmt_MolSys import to_mdanalysis_Universe as molsysmt_MolSys_to_mdanalysis_Universe

    tmp_item = string_pdb_id_to_molsysmt_MolSys(item, atom_indices=atom_indices, model_indices=frame_indices, check_form=False)
    tmp_item = molsysmt_MolSys_to_mdanalysis_Universe(tmp_item, check_form=False)

    return tmp_item

