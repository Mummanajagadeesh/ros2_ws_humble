from setuptools import find_packages, setup

package_name = 'robot_controller'

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
    maintainer='jagadeesh97',
    maintainer_email='jagadeesh97@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node = robot_controller.node0:main",
            "draw_circle = robot_controller.draw_circle:main",
            "pose_subscriber = robot_controller.pose_subscriber:main",
            "turtle_controller = robot_controller.turtle_controller:main",
            "draw_square = robot_controller.draw_square:main"
        ],
    },
)
