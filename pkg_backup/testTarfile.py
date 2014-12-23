#!/usr/bin/env python2.7

import tarfile
import os


candidate = os.environ['HOME'] + '/Documentos/test.tar.gz'


if tarfile.is_tarfile(candidate):

    with tarfile.open(candidate,) as tar:

        tar.list()

        tar.extractall()