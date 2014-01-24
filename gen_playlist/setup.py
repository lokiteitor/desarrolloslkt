from distutils.core import setup


setup(
    name='generator playlist'
    , url='http://www.desarrolloslkt.tk'
    , author='David Delgado'
    , author_email='lokiteitor513@gmail.com'
    , version='1.0.0' # remember to change me for new versions!
    , description='simple script que genera listas de reproduccion'
    , long_description=open('README.txt').read()
    , scripts=['playgen.py']
    , license='GPL'

    )