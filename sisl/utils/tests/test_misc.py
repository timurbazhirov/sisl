from __future__ import print_function, division

import pytest

from sisl.utils.misc import *

import math as m


class TestMisc(object):

    def test_direction_int(self):
        assert direction(0) == 0
        assert direction(1) == 1
        assert direction(2) == 2
        assert direction(2) != 1

    def test_direction_str(self):
        assert direction('A') == 0
        assert direction('B') == 1
        assert direction('C') == 2
        assert direction('a') == 0
        assert direction('b') == 1
        assert direction('c') == 2
        assert direction('X') == 0
        assert direction('Y') == 1
        assert direction('Z') == 2
        assert direction('x') == 0
        assert direction('y') == 1
        assert direction('z') == 2

    def test_angle_r2r(self):
        assert pytest.approx(angle('2pi')) == 2*m.pi
        assert pytest.approx(angle('2pi/2')) == m.pi
        assert pytest.approx(angle('3pi/4')) == 3*m.pi/4

        assert pytest.approx(angle('a2*180')) == 2*m.pi
        assert pytest.approx(angle('2*180', in_radians=False)) == 2*m.pi

    def test_angle_a2a(self):
        assert pytest.approx(angle('a2pia')) == 360
        assert pytest.approx(angle('a2pi/2a')) == 180
        assert pytest.approx(angle('a3pi/4a')) == 3*180./4

        assert pytest.approx(angle('a2pia', True, True)) == 360
        assert pytest.approx(angle('a2pi/2a', True, False)) == 180
        assert pytest.approx(angle('a2pi/2a', False, True)) == 180
        assert pytest.approx(angle('a2pi/2a', False, False)) == 180

    def test_iter1(self):
        for i, slc in enumerate(iter_shape([2, 1, 3])):
            if i == 0:
                assert slc == [0, 0, 0]
            elif i == 1:
                assert slc == [0, 0, 1]
            elif i == 2:
                assert slc == [0, 0, 2]
            elif i == 3:
                assert slc == [1, 0, 0]
            elif i == 4:
                assert slc == [1, 0, 1]
            elif i == 5:
                assert slc == [1, 0, 2]
            else:
                # if this is reached, something is wrong
                assert False
