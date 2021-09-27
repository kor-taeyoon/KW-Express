RCMS 프로토콜 정리






필요한 파일

- rosmater, ydlidar Rviz 한번에 실행하는 스크립트 파일
- FoxtrotGPS 한번에 실행하는 스크립트 파일
- OpenCR에 키보드 이벤트 보내고, 바코드 리더기로부터 신호 받는 프로그램


<br>
<br>

4 Grid

|  |  |
| --- | --- |
| roscore | foxtrotgps | 
|roslaunch ydlidar lidar_view.launch |   python3 RCMS.py