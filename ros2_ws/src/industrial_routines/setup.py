from setuptools import find_packages, setup

package_name = 'industrial_routines'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='alejandra',
    maintainer_email='alejandra.lea.2023@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
     'console_scripts': [
         'programa1 = industrial_routines.programa1_iniciales:main',
         'programa2 = industrial_routines.programa2_control_externo:main',
         'programa3 = industrial_routines.programa3_pick_and_place:main',
     ],
 },
)
