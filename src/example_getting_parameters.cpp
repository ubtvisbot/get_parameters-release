#include "ros/ros.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "getParameters");
    ros::NodeHandle n;

    std::string publisher_data_type;
    if (n.getParam("/node_2_pub_string/publisher_data_type", publisher_data_type))
    {
        ROS_INFO("Got param publisher_data_type: %s", publisher_data_type.c_str());
    }
    else
    {
        ROS_INFO("there is no param publisher_data_type");
    }


    std::string wait_duration;
    if (n.getParam("/node_2_pub_string/wait_duration", wait_duration))
    {
        ROS_INFO("Got param wait_duration: %s", wait_duration.c_str());
    }
    else
    {
        ROS_ERROR("Failed to get param 'wait_duration'");
    }

    int i;
    n.param("my_num", i, 42);

    std::string s1;
    n.param<std::string>("my_param1", s1, "default_value");
    ROS_INFO("my_param is %s", s1.c_str());

    n.setParam("my_param", "hello there 1");
    n.getParam("my_param", s1);
    ROS_INFO("my_param is %s", s1.c_str());

//    n.deleteParam("my_param");

    if (!n.hasParam("my_param"))
    {
        ROS_INFO("No param named 'my_param'");
    }
    else
    {
        ROS_INFO("ther is param named 'my_param'");
    }

    std::string param_name;
    if (n.searchParam("/node_2_pub_string/param_name_b", param_name))
    {
        // Found parameter, can now query it using param_name
        ROS_INFO("Found parameter %s", param_name.c_str());
        int i = 0;
        n.getParam(param_name, i);
        ROS_INFO("param_name_b is %d", i);
    }
    else
    {
        ROS_INFO("No param 'param_name_b' found in an upward search");
    }

    return 0;
}
