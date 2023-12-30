import numpy as np


class SparseMatrix:
    def __init__(self, matrix: np.ndarray | None = None) -> None:
        self.values = {}
        self.columns = set() 
        self.rows = set()
        if matrix is not None:
            n_columns, n_rows = matrix.shape
            for col in range(n_columns):
                for row in range(n_rows):
                    self.add_element(col, row, matrix[col, row])

    def __str__(self) -> str:
        result = ""
        for key in self.values:
            result += f"{key}: {self.values[key]}\n"
        return result

    def __setitem__(self, index, value):
        self.add_element(index[0], index[1], value)

    def __getitem__(self, index):
        return self.values[index]

    def __eq__(self, compare_matrix) -> bool:
        if not isinstance(compare_matrix, SparseMatrix):
            return False
        if not (self.columns == compare_matrix.columns and self.rows == compare_matrix.rows):
            return False
        if set(self.values.keys()) != set(compare_matrix.values.keys()):
            return False
        for key in self.values:
            if self.values[key] != compare_matrix.values[key]:
                return False
        return True

    def add_element(self, col: int, row: int, value: float):
        if value:
            self.columns.add(col)
            self.rows.add(row)
            if (col, row) in self.values:
                self.values[(col, row)] += value
            else:
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
    result_matrix = SparseMatrix()
    for lm in left_matrix.values:
        for rm in right_matrix.values:
            if lm[1] == rm[0]:
                result_matrix[(lm[0], rm[1])] = left_matrix[lm] * right_matrix[rm]

    return result_matrix

