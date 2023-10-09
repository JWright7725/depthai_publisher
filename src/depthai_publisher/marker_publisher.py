#!/usr/bin/env python3

import rospy
from visualization_msgs.msg import Marker

if __name__ == "__main__":
	rospy.init_node('node_name')
	pub = rospy.Publisher("tile_marker", Marker, queue_size=10, latch=True)

	# Set up the message header
	msg_out = Marker()
	msg_out.header.frame_id = "map"
	msg_out.header.stamp = rospy.Time.now()

	# Namespace allows you to manage
	# adding and modifying multiple markers
	msg_out.ns = "my_marker"
	# ID is the ID of this specific marker
	msg_out.id = 0
	# Type can be most primitive shapes
	# and some custom ones (see rviz guide
	# for more information)
	msg_out.type = Marker.CUBE
	# Action is to add / create a new marker
	msg_out.action = Marker.ADD
	# Lifetime set to Time(0) will make it
	# last forever
	msg_out.lifetime = rospy.Time(0)
	# Frame Locked will ensure our marker
	# moves around relative to the frame_id
	# if this is applicable
	msg_out.frame_locked = True

	# Place the marker at [1.0,1.0,0.0]
	# with no rotation
	msg_out.pose.position.x = 1.0
	msg_out.pose.position.y = 1.0
	msg_out.pose.position.z = 0.0
	msg_out.pose.orientation.w = 1.0
	msg_out.pose.orientation.x = 0.0
	msg_out.pose.orientation.y = 0.0
	msg_out.pose.orientation.z = 0.0

	# Make a square tile marker with
	# size 0.1x0.1m square and 0.02m high
	msg_out.scale.x = 0.1
	msg_out.scale.y = 0.1
	msg_out.scale.z = 0.02

	# Make the tile a nice opaque blue
	msg_out.color.r = 0.0
	msg_out.color.g = 0.2
	msg_out.color.b = 0.8
	msg_out.color.a = 1.0

	# Publish the marker
	pub.publish(msg_out)

	try:
		rospy.spin()
	except rospy.ROSInterrupyException:
		pass