^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pr2eus_moveit
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.3.10 (2017-03-02)
-------------------

0.3.9 (2017-02-22)
------------------
* Support Kinetic (`#284 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/284>`_ )
  * pr2_controllers_msgs is not released on J/K

* [pr2eus_moveit/collision-object-publisher.l] fix bug in :wipe-all (`#283 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/283>`_ )
  * separate wipe-all and fix bug
  * set new hash-table in :clear-all
* [pr2eus_moveit/robot-moveit.l] support angle-vector-sequence with MoveIt! (`#282 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/282>`_ )
  * support angle-vector-sequence for motion plan
  * remove trajectory-constraints for motion plan
* Contributors: Kei Okada, Shingo Kitagawa

0.3.8 (2017-02-07)
------------------

* robot-moveit.l
  * enable set default planner in moveit-env initialization (`#280 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/280>`_ )
  * [pr2eus_moveit] pass start-offset-time as starttime to :send-trajectory (`#276 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/276>`_)
  * pass start-offset-time to :send-trajectory
  * angle-vector-motion-plan return angle-vector (`#268 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/268>`_)
  * angle-vector-motion-plan accepts angle-vector seq
    modify :angle-vector-motion-plan to accept angle-vector-sequence
    set (butlast avs) as TrajectoryConstraints (`#259 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/259>`_)
  * add :ctype args in angle-vector-motion-plan to set controller-type for :angle-vector-motion-plan(`#261 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/261>`_)
  * total-time is msec ,and orig-total-time is sec, :total-time in :trajectory-fiter is msec (`#257 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/257>`_) FIx bugs in `#252 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/252>`_

* collision-object-publisher.l
  * [pr2eus_moveit/collision-object-publisher] support body class object (`#269 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/269>`_)
  * fix bug in collision-object-publisher :wipe-all (`#267 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/267>`_)
  * remove unused key in collision-object-publisher (`#266 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/266>`_)

* Contributors: Naoya Yamaguchi, Kei Okada, Shingo Kitagawa

0.3.7 (2016-11-08)
------------------
* :trajectory-filter add clear-velocities
* Contributors: Kei Okada

0.3.6 (2016-11-02)
------------------
* Update on robot-modeit.l ( `#252 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/252>`_ )
  * :angle-vector-motion send trajectory for joints not incldued in move-arm
  * :trajectory-filter scale based on original time sequences
  * add feature to filter trajectory using total-time
  * robot-moveit.l (:trajectory-filter) add start-offset-time
  * more message on ros-info
  * cleanup :angle-vector-motion-plan function using orig-total-time variable
* Contributors: Kei Okada

0.3.5 (2016-09-16)
------------------

0.3.4 (2016-06-22)
------------------

0.3.3 (2016-05-28)
------------------
* CMakeLists.txt : forget to install euslisp directory ( `#230 <https://github.com/jsk-ros-pkg/jsk_pr2eus/issues/230>`_ )
* Contributors: Kei Okada

0.3.2 (2016-05-26)
------------------

0.3.1 (2016-05-22)
------------------
* add pr2eus_moveit/README.md
* pr2eus_moveit: add test program
* robot-moveit.l : add info message for mumber of points and duration
* use RRTConnectkConfigDefault as a defualt planner
* robot-moveit.l : fix wrong commit on https://github.com/jsk-ros-pkg/jsk_pr2eus/commit/7d461b7ef199e26f0f9826ed4f1b1fd4cea606fe#commitcomment-17502889
* move pr2eus-moveit -> robot-moveit.l
* pr2eus_moveit: CMakeLists.txt install euslisp/ tutorials/ directory
* pr2eus-moveit.l : fix wrong commit on https://github.com/jsk-ros-pkg/jsk_pr2eus/commit/a55cfb08724ae0034382e2407f60d6830729e04b#commitcomment-17500452
* Contributors: Kei Okada

0.3.0 (2016-03-20)
------------------

0.2.1 (2016-03-04)
------------------

0.2.0 (2015-11-03)
------------------

0.1.11 (2015-06-11)
-------------------

0.1.10 (2015-04-03 18:49)
-------------------------

0.1.9 (2015-04-03 16:52)
------------------------

0.1.8 (2015-02-25)
------------------
* [pr2eus_moveit] package.xml fix version number
* [pr2eus_moveit] Catkinize pr2eus_moveit
* Contributors: Kei Okada, aginika

0.1.7 (2015-02-10)
------------------
* fix typo
* add code for using action-server instead of service
* add check-state-validity service and fix minor bug
* fix bug in collision-object-publisher.l
* change moveit groupname
* add code for using arms
* added eus2scene.l
* add publish-eusscene-marker.l
* add publish-eusscene.l
* Contributors: YoheiKakiuchi, mmurooka, tarukosu

0.1.6 (2014-05-11)
------------------

0.1.5 (2014-05-03)
------------------

0.1.4 (2014-05-02 22:28)
------------------------

0.1.3 (2014-05-02 18:04)
------------------------

0.1.2 (2014-05-01 22:43)
------------------------

0.1.1 (2014-05-01 02:14)
------------------------
* add pr2-tabletop-demo, picking object up on table useing moveit
* comment out debug message
* update pr2eus_moveit for using constraints
* Merge pull request #9 from YoheiKakiuchi/add_use_directly_joint_trajectory
  use joint trajectory mode for moveit
* add clear-world-scene method to pr2eus-moveit
* use joint trajectory mode for moveit
* fix typo :frame_id -> :frame-id
* enable to set object-id with keyword
* update publish-eusobject.l
* add publish-eusobject.l for publishing eus model to moveit environment
* change loading order for pr2eus-moveit
* fix minor bug
* add pr2-moveit.l
* fix typo
* add publish-collision-object
* add make-virtual-joint-constraints
* add :motion-plan-raw method for testing planning
* delete method for attached-object
* add :add-attached-object to collision-object-publisher
* add :query-planner-interface to pr2eus-moveit
* update
* add keyword for adding constraints to motion-plan
* add making constraints functions
* update pr2eus-moveit.l
* add method for robot-interface on pr2eus-moveit
* update pr2eus-moveit
* update pr2eus_moveit tutorials
* add :sync-robot-model method to pr2eus-moveit
* move collision-object-sample.l to tutorials
* add tutorials to pr2eus_moveit
* add :execute-trajectory method to pr2eus-moveit
* update sample for pr2eus_moveit
* add updating faces coords
* add collision-object-sample
* add :relative-pose keyword to collision-object-publisher.l
* fix typo and minor bug
* implement :motion-plan method to pr2eus-moveit.l
* fix typo
* add using torso configuration to pr2eus-moveit.l
* rename pr2eus_moveit.l -> pr2eus-moveit.l
* implement :get-ik-for-pose to moveit-environment
* rename scene-topic -> scene-service
* add pr2eus_moveit.l for using moveit from roseus interface
* add package dependancy to pr2eus_moveit
* move :get-planning-scene method to get-planning-scene function
* add pr2eus_moveit for using moveit components from roseus
* Contributors: Yohei Kakiuchi, YoheiKakiuchi, youhei
