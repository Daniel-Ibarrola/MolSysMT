from molsysmt._private_tools.box import digest_box_angles, digest_box_lengths
from molsysmt.lib import box as libbox
import numpy as np
from molsysmt import puw

def box_vectors_from_box_lengths_and_angles(lengths, angles):

    lengths=digest_box_lengths(lengths)
    angles=digest_box_angles(angles)

    units = puw.get_unit(lengths)
    lengths_value = puw.get_value(lengths)
    angles_value = puw.get_value(angles, to_unit='degrees')
    lengths_value =  np.asfortranarray(lengths_value, dtype='float64')
    angles_value =  np.asfortranarray(angles_value, dtype='float64')
    n_frames = lengths.shape[0]

    box = libbox.lengths_and_angles_to_box(lengths_value, angles_value, n_frames)
    box = np.ascontiguousarray(box, dtype='float64').round(6)*units

    del(lengths_value, angles_value)

    return box
