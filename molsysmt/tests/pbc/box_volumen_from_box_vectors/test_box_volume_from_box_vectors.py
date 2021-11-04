"""
Unit and regression test for the box_volume_from_box_vectors module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
import numpy as np

# Distance between atoms in space and time

def test_box_volume_from_box_vectors_1():
    molsys = msm.convert(msm.demo['Met-enkephalin']['vacuum.msmpk'], to_form='molsysmt.MolSys')
    molsys = msm.build.solvate(molsys, box_geometry='cubic', clearance='14.0 angstroms', engine='PDBFixer')
    box = msm.get(molsys, target='system', box=True)
    volume = msm.pbc.box_volume_from_box_vectors(box)
    check = np.allclose(msm.puw.get_value(volume, to_unit='nm**3'), [30.4765808])
    assert check

def test_box_volume_from_box_vectors_2():
    molsys = msm.convert(msm.demo['Met-enkephalin']['vacuum.msmpk'], to_form='molsysmt.MolSys')
    molsys = msm.build.solvate(molsys, box_geometry='truncated octahedral', clearance='14.0 angstroms', engine='PDBFixer')
    box = msm.get(molsys, target='system', box=True)
    volume = msm.pbc.box_volume_from_box_vectors(box)
    check = np.allclose(msm.puw.get_value(volume, to_unit='nm**3'), [23.4608828])
    assert check

def test_box_volume_from_box_vectors_3():
    molsys = msm.convert(msm.demo['Met-enkephalin']['vacuum.msmpk'], to_form='molsysmt.MolSys')
    molsys = msm.build.solvate(molsys, box_geometry='rhombic dodecahedral', clearance='14.0 angstroms', engine='PDBFixer')
    box = msm.get(molsys, target='system', box=True)
    volume = msm.pbc.box_volume_from_box_vectors(box)
    check = np.allclose(msm.puw.get_value(volume, to_unit='nm**3'), [21.5501970])
    assert check

