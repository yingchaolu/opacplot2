#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import os.path

import nose
from numpy.testing import assert_allclose
import numpy as np

import opacplot2 as opp
from opacplot2.opg_multi import OpgMulti



BASE_DIR = os.path.join(os.path.dirname(__file__), 'data')
reference_name =  'He_snp'
tmp_name =  'He_snp_tmp'


def test_multi_read():
    He = OpgMulti.open_file(BASE_DIR, reference_name )


def test_multi_read_write():
    He = OpgMulti.open_file(BASE_DIR, reference_name )
    tmp_file =  os.path.join(BASE_DIR, 'tmp_name')

    try:
        He.write(tmp_file)

        # Open generated file to check there are no errors.
        He_new = OpgMulti.open_file(BASE_DIR,  'tmp_name' )

        for key in He:
            yield assert_allclose, He[key] , He_new[key]

    except:
        raise
    finally:
        for ext in ['opp', 'opr', 'opz', 'eps']:
            real_file = "{prefix}.{ext}.gz".format(prefix=tmp_file, ext=ext)
            if os.path.exists(real_file):
                #os.remove(real_file) 
                pass
