Source: @(Package)
Section: misc
Priority: extra
Maintainer: @(Maintainer)
Build-Depends: debhelper (>= 7.0.50~), @(', '.join(BuildDepends)), ros-groovy-pr2-controllers, ros-groovy-pr2-common, ros-groovy-navigation, ros-groovy-audio-common
Homepage: @(Homepage)
Standards-Version: 3.9.2

Package: @(Package)
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, @(', '.join(Depends)), ros-groovy-pr2-controllers, ros-groovy-pr2-common, ros-groovy-navigation, ros-groovy-audio-common
Description: @(Description)
