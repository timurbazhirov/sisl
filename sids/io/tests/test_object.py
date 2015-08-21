from __future__ import print_function, division

from nose.tools import *

from sids.io import *


class TestObject(object):
    # Base test class for MaskedArrays.

    def test_cube(self):
        for obj in [BaseSile,Sile,CUBESile]:
            assert_true( isinstance(get_sile('test.cube'),obj) )
            assert_true( isinstance(get_sile('test.CUBE'),obj) )

    def test_fdf(self):
        for obj in [BaseSile,Sile,FDFSile]:
            assert_true( isinstance(get_sile('test.fdf'),obj) )
            assert_true( isinstance(get_sile('test.FDF'),obj) )

    def test_fdf_gz(self):
        for obj in [BaseSile,Sile,FDFSile]:
            assert_true( isinstance(get_sile('test.fdf.gz'),obj) )
            assert_true( isinstance(get_sile('test.FDF.gz'),obj) )

    def test_gout(self):
        for obj in [BaseSile,Sile,GULPSile]:
            assert_true( isinstance(get_sile('test.gout'),obj) )

    def test_gout_gz(self):
        for obj in [BaseSile,Sile,GULPSile]:
            assert_true( isinstance(get_sile('test.gout.gz'),obj) )

    def test_nc(self):
        for obj in [BaseSile,NCSile,SIESTASile]:
            assert_true( isinstance(get_sile('test.nc'),obj) )

    def test_tb(self):
        for obj in [BaseSile,Sile,TBSile]:
            assert_true( isinstance(get_sile('test.tb'),obj) )
            assert_true( isinstance(get_sile('test.TB'),obj) )

    def test_tb_gz(self):
        for obj in [BaseSile,Sile,TBSile]:
            assert_true( isinstance(get_sile('test.tb.gz'),obj) )
            assert_true( isinstance(get_sile('test.TB.gz'),obj) )

    def test_tbtrans(self):
        for obj in [BaseSile,NCSile,TBtransSile]:
            assert_true( isinstance(get_sile('test.TBT.nc'),obj) )

    def test_vasp(self):
        for obj in [BaseSile,Sile,POSCARSile]:
            assert_true( isinstance(get_sile('CONTCAR'),obj) )
            assert_true( isinstance(get_sile('POSCAR'),obj) )

    def test_vasp_gz(self):
        for obj in [BaseSile,Sile,POSCARSile]:
            assert_true( isinstance(get_sile('CONTCAR.gz'),obj) )
            assert_true( isinstance(get_sile('POSCAR.gz'),obj) )


    def test_xyz(self):
        for obj in [BaseSile,Sile,XYZSile]:
            assert_true( isinstance(get_sile('test.xyz'),obj) )
            assert_true( isinstance(get_sile('test.XYZ'),obj) )

    def test_xyz_gz(self):
        for obj in [BaseSile,Sile,XYZSile]:
            assert_true( isinstance(get_sile('test.xyz.gz'),obj) )
            assert_true( isinstance(get_sile('test.XYZ.gz'),obj) )

    def test_xv(self):
        for obj in [BaseSile,Sile,XVSile]:
            assert_true( isinstance(get_sile('test.XV'),obj) )

    def test_xv_gz(self):
        for obj in [BaseSile,Sile,XVSile]:
            assert_true( isinstance(get_sile('test.XV.gz'),obj) )

