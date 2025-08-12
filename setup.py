from setuptools import setup

package_name = 'stonefish_resources'

setup(
    name=package_name,
    version='0.0.0',
    packages=[],
    py_modules=["stonefish_resources.logitechF310teleop","stonefish_resources.bluerov2_logitechF310teleop.py"],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/bluerov2_heavy_simulation.launch.py', 'launch/bluerov_fls_simulation.launch.py','launch/blueboat_launch.py','launch/falcon_launch.py', 'launch/bluerov2_laser_simulation.launch.py', 'launch/bluerov2_alpha.py', 'launch/console_test.py', 'launch/asv_auv_sim.py', 'turtlebot_switfpro_kobuki.launch.py', ]),
        ('lib/' + package_name, [
            'scripts/logitechF310teleop.py',
            'scripts/magpy_subsea_cable.py',
            'scripts,bluerov2_logitechF310teleop.py',
            'scripts/odom2tf.py',
            'scripts/openmeteo.py'
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Michele Grimaldi',
    maintainer_email='michelegrmld@egmail.com',
    description='Description of your package',
    license='License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stonefish_resources_node = stonefish_resources.stonefish_resources_node:main',
            'logitechF310teleop = stonefish_resources.logitechF310teleop:main',
            'bluerov2_logitechF310teleop = stonefish_resources.bluerov2_logitechF310teleop:main',
            'magpy_subsea_cable = stonefish_resources.magpy_subsea_cable:main',
            'odom2tf = stonefish_resources.odom2tf:main',
            'openmeteo = stonefish_resources.openmeteo:main',
        ],
    },
)

