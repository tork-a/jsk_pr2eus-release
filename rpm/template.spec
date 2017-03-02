Name:           ros-jade-pr2eus
Version:        0.3.10
Release:        0%{?dist}
Summary:        ROS pr2eus package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2eus
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-control-msgs
Requires:       ros-jade-dynamic-reconfigure
Requires:       ros-jade-euscollada
Requires:       ros-jade-move-base-msgs
Requires:       ros-jade-nav-msgs
Requires:       ros-jade-pr2-controllers-msgs
Requires:       ros-jade-pr2-description
Requires:       ros-jade-pr2-msgs
Requires:       ros-jade-roseus
Requires:       ros-jade-rostest
Requires:       ros-jade-sound-play
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-control-msgs
BuildRequires:  ros-jade-dynamic-reconfigure
BuildRequires:  ros-jade-euscollada
BuildRequires:  ros-jade-move-base-msgs
BuildRequires:  ros-jade-nav-msgs
BuildRequires:  ros-jade-pr2-controllers-msgs
BuildRequires:  ros-jade-pr2-description
BuildRequires:  ros-jade-pr2-msgs
BuildRequires:  ros-jade-roseus
BuildRequires:  ros-jade-rosgraph-msgs
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-sound-play

%description
pr2eus

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Thu Mar 02 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.10-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.9-0
- Autogenerated by Bloom

* Fri Sep 16 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.5-0
- Autogenerated by Bloom

* Wed Jun 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.4-0
- Autogenerated by Bloom

* Sat May 28 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.3-0
- Autogenerated by Bloom

* Thu May 26 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.2-0
- Autogenerated by Bloom

* Sun May 22 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.1-1
- Autogenerated by Bloom

* Mon Mar 21 2016 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.3.0-0
- Autogenerated by Bloom

