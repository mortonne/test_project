import setuptools
import glob

scripts = glob.glob('bin/hello*')
setuptools.setup(scripts=scripts)
