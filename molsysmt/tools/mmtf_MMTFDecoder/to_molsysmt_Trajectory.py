def to_molsysmt_Trajectory(item, atom_indices='all', frame_indices='all', check_form=True):

    if check_form:
        from molsysmt.tools.mmtf_MMTFDecoder.is_mmtf_MMTFDecoder import _checking_form
        _checking_form(item, check_form=check_form)

    from molsysmt.native.trajectory import Trajectory
    from molsysmt.tools.api_mmtf_MMTFDecoder.get import get_frame_from_atom

    tmp_item = Trajectory()
    step, time, coordinates, box = get_frame_from_atom(item, indices=atom_indices, frame_indices=frame_indices, check_form=False)
    tmp_item.append_frames(step=step, time=time, coordinates=coordinates, box=box)

    return tmp_item

