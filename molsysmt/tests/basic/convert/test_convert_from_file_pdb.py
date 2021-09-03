"""
Unit and regression test for the convert module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
import numpy as np
import os

# Whole systems (selection='all' and frame_indices='all')

def test_file_pdb_to_mdtraj_Trajectory():
    molsys = msm.demo.files['1tcd.pdb']
    molsys = msm.convert(molsys, to_form='mdtraj.Trajectory')
    form = msm.get_form(molsys)
    assert 'mdtraj.Trajectory'==form

def test_file_pdb_to_openmm_Topology():
    molsys = msm.demo.files['1tcd.pdb']
    molsys = msm.convert(molsys, to_form='openmm.Topology')
    form = msm.get_form(molsys)
    assert 'openmm.Topology'==form

def test_file_pdb_to_string_pdb():
    molsys = msm.demo.files['1tcd.pdb']
    molsys = msm.convert(molsys, to_form='string:pdb')
    form = msm.get_form(molsys)
    assert 'string:pdb'==form

def test_file_pdb_to_pdbfixer_PDBFixer():
    molsys = msm.demo.files['1tcd.pdb']
    molsys = msm.convert(molsys, to_form='pdbfixer.PDBFixer')
    form = msm.get_form(molsys)
    assert 'pdbfixer.PDBFixer'==form

def test_file_pdb_to_parmed_Structure():
    molsys = msm.demo.files['1tcd.pdb']
    molsys = msm.convert(molsys, to_form='parmed.Structure')
    form = msm.get_form(molsys)
    assert 'parmed.Structure'==form

# Selection

## Multiple outputs


