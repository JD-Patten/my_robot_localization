import launch
from launch_ros.actions import Node
def generate_launch_description():
	return launch.LaunchDescription([
		Node(
			package='robot_localization',
			executable='ekf_node',
			name='efk_filter_node',
			parameters=[{'use_sim_time': False}],
			arguments=['--ros-args', '--params-file', 'my_robot_localization.yaml'],
		)
	])
