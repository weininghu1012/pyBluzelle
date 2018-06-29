import pyBluzelle

try:
    from setuptools import setup
    from setuptools.command.install import install
except ImportError:
    from distutils.core import setup


setup(name='pyBluzelle',
      version=pyBluzelle.get_version(),
      description='Python implementation for bluzelle APIs',
      url='http://github.com/bluzelle/pybluzelle',
      author='krxsky, liangjiaxing, weininghu1012, exeex, amastracci',
      author_email='devops@bluzelle.com',
      license='Apache2.0',
      packages=['pyBluzelle', 'pyBluzelle.test', 'pyBluzelle.proto'],
      install_requires=['websocket-client>=0.47.0',
                        'protobuf>=3.6.0',
                        'mockito',
                        'pytest'],
      scripts=['scripts/crud'],
      zip_safe=False)
