Name:           ros-indigo-pr2eus-moveit
Version:        0.3.9
Release:        0%{?dist}
Summary:        ROS pr2eus_moveit package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2eus_moveit
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-pr2eus
Requires:       ros-indigo-roseus
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-moveit-planners-ompl
BuildRequires:  ros-indigo-pr2-gazebo
BuildRequires:  ros-indigo-pr2-moveit-config
BuildRequires:  ros-indigo-pr2-moveit-plugins
BuildRequires:  ros-indigo-pr2eus
BuildRequires:  ros-indigo-roseus
BuildRequires:  ros-indigo-rostest

%description
pr2eus_moveit

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Feb 22 2017 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.9-0
- Autogenerated by Bloom

* Fri Sep 16 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.5-0
- Autogenerated by Bloom

* Wed Jun 22 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.4-0
- Autogenerated by Bloom

* Sat May 28 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.3-0
- Autogenerated by Bloom

* Thu May 26 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.2-0
- Autogenerated by Bloom

* Sun May 22 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.1-0
- Autogenerated by Bloom

* Mon Mar 21 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.3.0-0
- Autogenerated by Bloom

* Fri Mar 04 2016 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Tue Nov 03 2015 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.0-0
- Autogenerated by Bloom

* Fri Jun 19 2015 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.11-0
- Autogenerated by Bloom

* Fri Apr 03 2015 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.10-0
- Autogenerated by Bloom

* Fri Apr 03 2015 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.9-0
- Autogenerated by Bloom

* Wed Feb 25 2015 YoheiKakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.8-0
- Autogenerated by Bloom

