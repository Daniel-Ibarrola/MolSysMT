"""
Unit and regression test for the get module of the molsysmt package.
"""

# Import package, test suite, and other packages as needed
import molsysmt as msm
import numpy as np


# Get on molsysmt.MolSys

def test_get_1():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    output = msm.get(molsys, target='atom', indices=[32,33,34], name=True)
    true_output = np.array(['N', 'CA', 'C'], dtype=object)
    assert np.all(output == true_output)

def test_get_2():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    names, group_indices, group_names = msm.get(molsys, target='atom', indices=[32,33,34], name=True, group_index=True, group_name=True)
    true_names = np.array(['N', 'CA', 'C'], dtype=object)
    true_group_indices = np.array([4, 4, 4])
    true_group_names = np.array(['ILE', 'ILE', 'ILE'], dtype=object)
    assert np.all(names == true_names) and np.all(group_indices == true_group_indices) and np.all(group_names == true_group_names)

def test_get_3():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='atom', indices=[32,33,34], n_groups=True)
    true_n_groups = 1
    assert n_groups == true_n_groups

def test_get_4():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    names, atom_indices, atom_names = msm.get(molsys, target='group', indices=[10,11,12],
                                            name=True, atom_index=True, atom_name=True)
    true_names = np.array(['LYS', 'CYS', 'ASN'], dtype=object)
    true_atom_indices = np.array([np.array([77, 78, 79, 80, 81, 82, 83, 84, 85]),
       np.array([86, 87, 88, 89, 90, 91]),
       np.array([92, 93, 94, 95, 96, 97, 98, 99])], dtype=object)
    true_atom_names = np.array([np.array(['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD', 'CE', 'NZ'], dtype=object),
       np.array(['N', 'CA', 'C', 'O', 'CB', 'SG'], dtype=object),
       np.array(['N', 'CA', 'C', 'O', 'CB', 'CG', 'OD1', 'ND2'], dtype=object)],
      dtype=object)

    check_names = np.all(names==true_names)
    check_atom_indices = np.all([np.all(ii==jj) for ii,jj in zip(atom_indices, true_atom_indices)])
    check_atom_names = np.all([np.all(ii==jj) for ii,jj in zip(atom_names, true_atom_names)])

    assert check_names and check_atom_indices and check_atom_names

def test_get_5():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_atoms = msm.get(molsys, target='group', indices=[10,11,12], n_atoms=True)
    assert np.all(n_atoms==np.array([9, 6, 8]))

def test_get_6():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    indices, component_indices = msm.get(molsys, target='group', indices=[550, 551, 552],
                                    index=True, component_index=True)
    true_indices = np.array([550, 551, 552])
    true_component_indices = np.array([55, 56, 57])
    check_indices = np.all(indices==true_indices)
    check_component_indices = np.all(component_indices==true_component_indices)
    assert check_indices and check_component_indices

def test_get_7():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_components = msm.get(molsys, target='group', indices=[550, 551, 552], n_components=True)
    true_n_components = 3
    assert n_components==true_n_components

def test_get_8():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    indices, component_indices = msm.get(molsys, target='component', indices=[55, 56, 57],
                                    index=True, group_index=True)
    true_indices = np.array([55, 56, 57])
    true_component_indices = np.array([[550], [551], [552]], dtype=object)
    check_indices = np.all(true_indices==indices)
    check_component_indices = np.all([np.all(ii==jj) for ii,jj in zip(component_indices, true_component_indices)])
    assert check_indices and check_component_indices

def test_get_9():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='component', indices=[55, 56, 57], n_groups=True)
    assert np.all(n_groups==np.array([1, 1, 1]))

def test_get_10():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_atoms = msm.get(molsys, target='atom', n_atoms=True)
    assert n_atoms==3983

def test_get_11():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_chains = msm.get(molsys, target='atom', n_chains=True)
    assert n_chains==4

def test_get_12():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    atom_names, atom_indices = msm.get(molsys, target='atom', selection='group_index==20', name=True, index=True)
    true_atom_names = np.array(['N', 'CA', 'C', 'O', 'CB', 'CG', 'CD'], dtype=object)
    true_atom_indices = np.array([148, 149, 150, 151, 152, 153, 154])
    check_atom_names = np.all(atom_names==true_atom_names)
    check_atom_indices = np.all(atom_indices==true_atom_indices)
    assert check_atom_names and check_atom_indices

def test_get_13():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_atoms = msm.get(molsys, target='atom', selection='molecule_type=="protein"', n_atoms=True)
    assert n_atoms==3818

def test_get_14():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_molecules = msm.get(molsys, target='atom', selection='molecule_type=="water"', n_molecules=True)
    assert n_molecules==165

def test_get_15():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    atom_names = msm.get(molsys, target='atom', indices=[0,1,2], name=True)
    true_atom_names = np.array(['N', 'CA', 'C'], dtype=object)
    assert np.all(atom_names==true_atom_names)

def test_get_16():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    atom_names = msm.get(molsys, target='atom', selection='atom_index in [0,1,2]', name=True)
    true_atom_names = np.array(['N', 'CA', 'C'], dtype=object)
    assert np.all(atom_names==true_atom_names)

def test_get_17():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    group_ids = msm.get(molsys, target='atom', selection='atom_index in [0,1,2]', group_id=True)
    true_group_ids = np.array([4, 4, 4])
    assert np.all(group_ids==true_group_ids)

def test_get_18():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='atom', selection='atom_index in [0,1,2]', n_groups=True)
    assert n_groups==1

def test_get_19():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    ids = msm.get(molsys, target='group', indices=[0,1,2], id=True)
    true_ids = np.array([4, 5, 6])
    assert np.all(ids==true_ids)

def test_get_20():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    ids = msm.get(molsys, target='group', selection='group_index in [0,1,2]', id=True)
    true_ids = np.array([4, 5, 6])
    assert np.all(ids==true_ids)

def test_get_21():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    atom_indices = msm.get(molsys, target='group', indices=[0,1], atom_index=True)
    true_atom_indices = np.array([np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]),
       np.array([ 9, 10, 11, 12, 13, 14, 15])], dtype=object)
    check_atom_indices = np.all([np.all(ii==jj) for ii,jj in zip(atom_indices, true_atom_indices)])
    assert check_atom_indices

def test_get_22():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    group_indices = msm.get(molsys, target='atom', indices=range(5,10), group_index=True)
    true_group_indices = np.array([0, 0, 0, 0, 1])
    assert np.all(group_indices==true_group_indices)

def test_get_23():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='atom', indices=range(5,10), n_groups=True)
    assert n_groups==2

def test_get_24():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    group_indices = msm.get(molsys, target='molecule', indices=[0,1], group_index=True)
    true_group_indices = np.array([np.array(range(497)), np.array([497])], dtype=object)
    check_group_indices = np.all([np.all(ii==jj) for ii,jj in zip(group_indices, true_group_indices)])
    assert check_group_indices

def test_get_25():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    group_names = msm.get(molsys, target='molecule', indices=[1,2], group_name=True)
    true_group_names = np.array([['HOH'], ['HOH']], dtype=object)
    check_group_names = np.all([np.all(ii==jj) for ii,jj in zip(group_names, true_group_names)])
    assert check_group_names

def test_get_26():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_molecules = msm.get(molsys, target='molecule', selection='molecule_type=="protein"', n_molecules=True)
    assert n_molecules==1

def test_get_27():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='molecule', selection='molecule_type=="protein"', n_groups=True)
    true_n_groups = [497]
    assert np.all(n_groups==true_n_groups)

def test_get_28():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='group', selection='molecule_type=="water"', n_groups=True)
    assert n_groups==165

def test_get_28():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    names = msm.get(molsys, target='entity', indices=0, name=True)
    true_names = np.array(['TRIOSEPHOSPHATE ISOMERASE'], dtype=object)
    assert np.all(names==true_names)

def test_get_29():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    types = msm.get(molsys, target='entity', indices=1, type=True)
    true_types = np.array(['water'], dtype=object)
    assert np.all(types==true_types)

def test_get_30():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_molecules = msm.get(molsys, target='entity', indices=1, n_molecules=True)
    true_n_molecules = [165]
    assert np.all(n_molecules==true_n_molecules)

def test_get_31():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    molecule_index = msm.get(molsys, target='entity', indices=1, molecule_index=True)
    true_molecule_index = np.array([list(range(1,166))], dtype=object)
    check_molecule_index = np.all([np.all(ii==jj) for ii,jj in zip(molecule_index, true_molecule_index)])
    assert check_molecule_index

def test_get_31():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    molecule_types = msm.get(molsys, target='group', indices=[10,11,12], molecule_type=True)
    true_molecule_types = np.array(['protein', 'protein', 'protein'], dtype=object)
    check_molecule_types = np.all(molecule_types==true_molecule_types)
    assert check_molecule_types

def test_get_32():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    molecule_types = msm.get(molsys, target='molecule', indices=range(1,10), molecule_type=True)
    true_molecule_types = np.array(['water', 'water', 'water', 'water', 'water', 'water', 'water',
       'water', 'water'], dtype=object)
    check_molecule_types = np.all(molecule_types==true_molecule_types)
    assert check_molecule_types

def test_get_33():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='group', selection='group_type=="aminoacid"', n_groups=True)
    assert n_groups==497

def test_get_34():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='component', indices=[0,1], n_groups=True)
    true_n_groups = [248, 249]
    assert np.all(n_groups==true_n_groups)

def test_get_35():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_groups = msm.get(molsys, target='atom', selection='component_index==[0,1]', n_groups=True)
    assert n_groups==497

def test_get_36():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_aminoacids = msm.get(molsys, target='system', n_aminoacids=True)
    assert n_aminoacids==497

def test_get_37():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_waters = msm.get(molsys, target='system', n_waters=True)
    assert n_waters==165

def test_get_38():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_ions = msm.get(molsys, target='system', n_ions=True)
    assert n_ions==0

def test_get_39():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_proteins = msm.get(molsys, target='system', n_proteins=True)
    assert n_proteins==1

def test_get_40():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_rnas = msm.get(molsys, target='system', n_rnas=True)
    assert n_rnas==0

def test_get_41():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_atoms = msm.get(molsys, target='system', n_atoms=True)
    assert n_atoms==3983

def test_get_42():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_entities = msm.get(molsys, target='system', n_entities=True)
    assert n_entities==2

def test_get_43():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    bonded_atoms = msm.get(molsys, target='atom', indices=[0,1,2,3,4,5], bonded_atoms=True)
    true_bonded_atoms = np.array([np.array([1]), np.array([0, 2, 4]), np.array([1, 3, 9]), np.array([2]),
       np.array([1, 5]), np.array([4, 6])], dtype=object)
    check_bonded_atoms = np.all([np.all(ii==jj) for ii,jj in zip(bonded_atoms, true_bonded_atoms)])
    assert check_bonded_atoms

def test_get_44():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    bond_index = msm.get(molsys, target='atom', indices=[0,1,2,3,4,5], bond_index=True)
    true_bond_index = np.array([np.array([0]), np.array([0, 1, 3]), np.array([   1,    2, 3395]),
       np.array([2]), np.array([3, 4]), np.array([4, 5])], dtype=object)
    check_bond_index = np.all([np.all(ii==jj) for ii,jj in zip(bond_index, true_bond_index)])
    assert check_bond_index

def test_get_45():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_bonds = msm.get(molsys, target='atom', indices=[0,1,2,3,4,5], n_bonds=True)
    true_n_bonds = np.array([1, 3, 3, 1, 2, 2])
    assert np.all(n_bonds==true_n_bonds)

def test_get_46():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    inner_bonded_atoms = msm.get(molsys, target='atom', indices=[0,1,2,3,4,5], inner_bonded_atoms=True)
    true_inner_bonded_atoms = np.array([[1, 0], [2, 1], [3, 2], [4, 1], [5, 4]])
    check_bonded_index = np.all([np.all(ii==jj) for ii,jj in zip(inner_bonded_atoms, true_inner_bonded_atoms)])
    assert check_bonded_index

def test_get_47():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    inner_bond_index = msm.get(molsys, target='atom', indices=[0,1,2,3,4,5], inner_bond_index=True)
    true_inner_bond_index = np.array([0, 1, 2, 3, 4])
    assert np.all(inner_bond_index==true_inner_bond_index)

def test_get_48():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_inner_bonds = msm.get(molsys, target='atom', indices=[0,1,2,3,4,5], n_inner_bonds=True)
    assert n_inner_bonds==5

def test_get_49():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    indices = msm.get(molsys, target='bond', selection='group_index==3', index=True)
    true_indices = np.array([23, 24, 25, 26, 27, 28, 29])
    assert np.all(indices==true_indices)

def test_get_50():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    atom_indices = msm.get(molsys, target='bond', indices=[0,1,2,3,4], atom_index=True)
    true_atom_indices = np.array([[1, 0], [2, 1], [3, 2], [4, 1], [5, 4]])
    assert np.all(atom_indices==true_atom_indices)

def test_get_51():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    order = msm.get(molsys, target='bond', indices=[0,1,2,3], order=True)
    true_order = np.array([1, 1, 2, 1])
    assert np.all(order==true_order)

def test_get_52():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_bonds = msm.get(molsys, target='bond', selection='group_index==3', n_bonds=True)
    assert n_bonds==7

def test_get_53():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_bonds = msm.get(molsys, target='system', n_bonds=True)
    assert n_bonds==3890

def test_get_54():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    n_frames = msm.get(molsys, target='system', n_frames=True)
    assert n_frames==1

def test_get_55():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    coordinates = msm.get(molsys, target='atom', indices=100, frame_indices=0, coordinates=True)
    value = msm.puw.get_value(coordinates)
    unit = msm.puw.get_unit(coordinates)
    assert (unit==msm.puw.unit('nanometers')) and (np.allclose(value, np.array([[[1.8835, 3.8271, 5.0365]]])))

def test_get_56():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    time = msm.get(molsys, target='system', time=True)
    assert (time is None)

def test_get_57():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    box = msm.get(molsys, target='system', frame_indices=0, box=True)
    value = msm.puw.get_value(box)
    unit = msm.puw.get_unit(box)
    true_value = np.array([[[4.37099990e+00, 0.00000000e+00, 0.00000000e+00],
        [1.00000000e-07, 7.76500020e+00, 0.00000000e+00],
        [2.00000000e-07, 2.00000000e-07, 1.49539993e+01]]])
    assert (unit==msm.puw.unit('nanometers')) and (np.allclose(value, true_value))

def test_get_58():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    box_lengths =msm.get(molsys, target='system', frame_indices=0, box_lengths=True)
    value = msm.puw.get_value(box_lengths)
    unit = msm.puw.get_unit(box_lengths)
    assert (unit==msm.puw.unit('nanometers')) and (np.allclose(value, np.array([[ 4.371   ,  7.765   , 14.953999]])))

def test_get_59():
    molsys = msm.convert(msm.demo['TcTIM']['1tcd.msmpk'], to_form='molsysmt.MolSys')
    box_angles =msm.get(molsys, target='system', frame_indices=0, box_angles=True)
    value = msm.puw.get_value(box_angles)
    unit = msm.puw.get_unit(box_angles)
    assert (unit==msm.puw.unit('degree')) and (np.allclose(value, np.array([[ 90., 90., 90.]])))
