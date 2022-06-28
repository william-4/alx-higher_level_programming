#!/usr/bin/python3
"""
This module contains a function that multiplies a 2 matrices by using the
module NumPy

"""
import numpy
def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies matrix m_a with matrix m_b
    """
    return numpy.matmul(m_a, m_b)
