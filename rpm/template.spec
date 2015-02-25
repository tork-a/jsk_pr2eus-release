Name:           ros-hydro-pr2eus
Version:        0.1.8
Release:        0%{?dist}
Summary:        ROS pr2eus package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2eus
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-control-msgs
Requires:       ros-hydro-dynamic-reconfigure
Requires:       ros-hydro-euscollada
Requires:       ros-hydro-move-base-msgs
Requires:       ros-hydro-nav-msgs
Requires:       ros-hydro-pr2-controllers-msgs
Requires:       ros-hydro-pr2-description
Requires:       ros-hydro-pr2-msgs
Requires:       ros-hydro-roseus
Requires:       ros-hydro-rostest
Requires:       ros-hydro-sound-play
BuildRequires:  ros-hydro-catkin
BuildRequires:  ros-hydro-control-msgs
BuildRequires:  ros-hydro-dynamic-reconfigure
BuildRequires:  ros-hydro-euscollada
BuildRequires:  ros-hydro-move-base-msgs
BuildRequires:  ros-hydro-nav-msgs
BuildRequires:  ros-hydro-pr2-controllers-msgs
BuildRequires:  ros-hydro-pr2-description
BuildRequires:  ros-hydro-pr2-msgs
BuildRequires:  ros-hydro-roseus
BuildRequires:  ros-hydro-rosgraph-msgs
BuildRequires:  ros-hydro-rostest
BuildRequires:  ros-hydro-sound-play

%description
pr2eus

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Wed Feb 25 2015 Kei Okada <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.8-0
- Autogenerated by Bloom

* Wed Feb 11 2015 furuta <k-okada@jsk.t.u-tokyo.ac.jp> - 0.1.7-0
- Autogenerated by Bloom

