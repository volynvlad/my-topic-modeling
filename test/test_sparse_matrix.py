import pytest

from my_topic_modeling.sparse_matrix import SparseMatrix, multiply_sp_matrix

import numpy as np


def test_sparse_matrix_eq():
    matrix = np.array(
        [[0, 1, 0],
        [1, 0, 0],
        [1, 0, 0]]
    )

    assert SparseMatrix(matrix) == SparseMatrix(matrix)


def test_sparse_matrix_not_eq():
    matrix1 = np.array(
        [[0, 1, 0],
        [1, 0, 0],
        [1, 0, 0]]
    )
    matrix2 = np.array(
        [[0, 1, 0],
        [1, 0, 0],
        [2, 0, 0]]
    )
    matrix3 = np.array(
        [[0, 1, 0],
        [1, 0, 0],
        [1, 0, 1]]
    )

    assert SparseMatrix(matrix1) != SparseMatrix(matrix2)
    assert SparseMatrix(matrix1) != SparseMatrix(matrix3)

def test_sparse_square_matrix_multiply():
    matrix1 = SparseMatrix(
        np.array(
            [[0, 1, 0],
            [1, 0, 0],
            [1, 0, 0]]
        )
    )
    matrix2 = SparseMatrix(
        np.array(
            [[1, 0, 0],
            [1, 0, 1],
            [0, 1, 1]]
        )
    )
    result_matrix = SparseMatrix(
        np.array(
            [[1, 0, 1],
             [1, 0, 0],
             [1, 0, 0]]
        )
    )

    result_mult_matrix = multiply_sp_matrix(matrix1, matrix2)

    assert result_mult_matrix == result_matrix


def test_sparse_rect_matrix_multiply():
    matrix1 = SparseMatrix(
        np.array(
            [[2, 0, 1],
            [0, -3, 0]]
        )
    )
    matrix2 = SparseMatrix(
        np.array(
            [[0, 3, 0, -1],
            [3, 0, 0, 1],
            [0, 0, 1, 1]]
        )
    )
    result_matrix = SparseMatrix(
        np.array(
            [[0, 6, 1, -1],
             [-9, 0, 0, -3]]
        )
    )

    result_mult_matrix = multiply_sp_matrix(matrix1, matrix2)

    assert result_mult_matrix == result_matrix

