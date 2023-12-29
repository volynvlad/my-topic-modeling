import numpy as np

from logger import logger


class SparseMatrix:
    def __init__(self, matrix: np.ndarray | None = None) -> None:
        self.values = {}
        self.columns = set() 
        self.rows = set()
        if matrix:
            n_columns, n_rows = matrix.shape
            self.columns = set(range(n_columns))
            self.rows = set(range(n_rows))
            for col in range(n_columns):
                for row in range(n_rows):
                    self.add_element(col, row, matrix[col, row])

    def add_element(self, col: int, row: int, value: float):
        if value:
            self.columns.add(col)
            self.rows.add(row)
            self.values[(col, row)] = value

    def remove_element(self, col: int, row: int):
        if col in self.columns and row in self.rows:
            self.columns.remove(col)
            self.rows.remove(row)
            self.values.pop((col, row))
        else:
            raise IndexError(f"there is no value in ({col}, {row}) element")


def multiply_sp_matrix(
    left_matrix: SparseMatrix,
    right_matrix: SparseMatrix,
    ):
    return SparseMatrix()
