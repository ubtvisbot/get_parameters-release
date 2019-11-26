%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/melodic/.*$
%global __requires_exclude_from ^/opt/ros/melodic/.*$

Name:           ros-melodic-get-parameters
Version:        0.0.3
Release:        1%{?dist}
Summary:        ROS get_parameters package

License:        TODO
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-std-msgs
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-std-msgs

%description
The get_parameters package

%prep
%autosetup

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_LIBDIR="lib" \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/melodic

%changelog
* Tue Nov 26 2019 qlf <qlf246801@126.com> - 0.0.3-1
- Autogenerated by Bloom

