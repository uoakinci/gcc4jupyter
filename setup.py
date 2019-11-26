from distutils.core import setup

setup(
    name='GCCPlugin',
    version='0.0.1',
    author='Uğur Özgü Akıncı',
    author_email='uoakinci@gmail.com',
    py_modules=['gcc_plugin', 'v2.v2', 'common.helper'],
    url='htpps://github.com/uoakinci/gcc4jupyter',
    license='LICENSE',
    description='Jupyter notebook plugin to run GCC C/C++ code. Forked from Andrei Nechaev\'s nvcc4jupyter @ https://github.com/andreinechaev/nvcc4jupyter',
    # long_description=open('README.md').read(),
)
