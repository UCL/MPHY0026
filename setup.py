# coding=utf-8
"""
Setup for MPHY0026
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='MPHY0026',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='MPHY0026: Computer Assisted Surgery and Therapy course',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/UCL/MPHY0026',
    author='Matt Clarkson',
    author_email='m.clarkson@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'six>=1.10',
        'numpy>=1.11',
        'scipy',
        'ipykernel',
        'jupyter',
        'nbsphinx',
        'matplotlib',
        'opencv-contrib-python',
        'scikit-surgerycore',
        'scikit-surgeryvtk',
        'scikit-surgerynditracker',
        'scikit-surgeryarucotracker',
        'scikit-surgerypclcpp',
        'scikit-surgeryopencvcpp',
        'scikit-surgeryfred',
        'scikit-surgerybard',
        'scikit-surgerycalibration'
    ],

    entry_points={
        'console_scripts': [
            'mphy0026_manual_registration=mphy0026.ui.mphy0026_manual_registration_command_line:main',
            'mphy0026_registration=mphy0026.ui.mphy0026_register_command_line:main',
            'mphy0026_quadview=mphy0026.ui.mphy0026_quadview_command_line:main',
            'mphy0026_grab_pointer=mphy0026.ui.mphy0026_grab_pointer_command_line:main',
            'mphy0026_template_calibration=mphy0026.ui.mphy0026_template_calibration_command_line:main',
            'mphy0026_pivot_calib=mphy0026.ui.mphy0026_pivot_calib_command_line:main'
        ],
    },
)
