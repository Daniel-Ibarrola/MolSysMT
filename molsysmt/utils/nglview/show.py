# This should go in 

from .adaptor import MolSysMTTrajectory
from nglview.widget import NGLWidget

def show_molsysmt(molsys, atom_indices='all', frame_indices='all', **kwargs):
    '''Show NGL widget with molsysmt.MolSys object.

    Visit [MolSysmt documentation webpage](xxx) for further info.

    Examples
    --------
    >>> import nglview as nv # doctest: +SKIP
    ... import molsysmt as msm
    ... t = msm.convert([nv.datafiles.GRO, nv.datafiles.XTC])
    ... w = nv.show_mdanalysis(t)
    ... w
    '''
    structure_trajectory = MolSysMTTrajectory(molsys, atom_indices=atom_indices,
                                              frame_indices=frame_indices)
    return NGLWidget(structure_trajectory, **kwargs)

