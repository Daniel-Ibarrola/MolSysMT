from .trajectory import Trajectory as _Trajectory
import numpy as _np

def from_mdtraj_Trajectory(item=None):

    tmp_coordinates = _np.asfortranarray(item.xyz) # the same array and same units
    tmp_box = _np.asfortranarray(item.unitcell_vectors)
    tmp_time = _np.asfortranarray(item.time)
    try:
        tmp_timestep = _np.asfortranarray(item.timestep)
    except:
        tmp_timestep = None

    return _Trajectory(coordinates=tmp_coordinates, box=tmp_box, time=tmp_time,
                      timestep=tmp_timestep)

def to_mdtraj_Trajectory(item=None):
    from mdtraj import Trajectory as _mdtraj_Trajectory
    tmp_mdtraj_trajectory_item = _mdtraj_Trajectory(item.trajectory.coordinates,item.topology)
    tmp_mdtraj_trajectory_item.unitcell_vectors = _np.ascontiguousarray(item.trajectory.box)
    tmp_mdtraj_trajectory_item.time = _np.ascontiguousarray(item.trajectory.time)
    #try:
    #    tmp_mdtraj_trajectory_item.timestep = _np.ascontiguousarray(item.trajectory.timestep)
    #except:
    #    tmp_mdtraj_trajectory_item.timestep = None
    del(_mdtraj_Trajectory)
    return tmp_mdtraj_trajectory_item

def from_xtc(item=None):

    tmp_molmod_trajectory = _Trajectory(filename=item)
    return tmp_molmod_trajectory