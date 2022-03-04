from molsysmt._private_tools.exceptions import *
from molsysmt._private_tools.digestion import *

def get_center_of_mass(molecular_system, selection='all', groups_of_atoms=None, structure_indices='all', syntaxis='MolSysMT', engine='MolSysMT', parallel=False):

    from molsysmt.structure.get_center import get_center

    return get_center(molecular_system, selection=selection, groups_of_atoms=groups_of_atoms, weights='masses', structure_indices=structure_indices, syntaxis=syntaxis,
                      engine=engine, parallel=parallel)
