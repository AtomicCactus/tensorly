import tensorly as tl
from tensorly import random
from ..tt_matrix import tt_matrix_to_matrix, tt_matrix_to_tensor, tt_matrix_to_vec

def test_tt_matrix_manipulation():
    """Test for tt_matrix manipulation"""
    shape = (2, 2, 2, 3, 3, 3)
    tt_matrix = random.random_tt_matrix(shape, rank=2, full=False)
    rec = tt_matrix_to_tensor(tt_matrix)
    assert(tl.shape(rec) == shape)

    mat = tt_matrix_to_matrix(tt_matrix)
    assert(tl.shape(mat) == (8, 27))

    vec = tt_matrix_to_vec(tt_matrix)
    assert(tl.shape(vec) == (8*27,))