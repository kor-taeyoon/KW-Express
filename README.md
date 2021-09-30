발표영상 : https://www.youtube.com/watch?v=glNhybFhy6Y

# 물류시스템의 최적화를 위한 도심형 무인 운송 로봇

물류 유통 시스템의 효율을 높이기 위해 아파트 단지 내부에서의 택배 운송을 모두 자동화하는 로봇 및 제어 시스템.

<div align="right">
KW-특송
</div>
<div align="right">
김태윤, 김지원, 이지원, 정세훈(전자통신공학과)
</div>
<div align="right">
지도교수: 채주형&nbsp;&nbsp;&nbsp;&nbsp;산업체: 김성용 (에스오엑스 대표)
</div>
<br>

- - -
## 과제 선정 배경 및 필요성
&nbsp;최근 아파트 단지 내 택배 차량 통행을 막으면서, 운송 업체와 아파트 단지와의 갈등이 심화되고 있다. 입주민의 수요를 충족시키기 위한 운송업체의 정당한 노동을 입주민이 제한한다는 것에 문제가 있다. 이를 해결하기 위해 최근 발전한 무인기 제어 시스템을 활용하여 단지 내의 운송을 담당하는 무인 로봇을 설계, 개발하는 것을 주제로 한다.




<br>

- - - 
## 해결방안 및 과정
&nbsp;운송 업체 기사가 물품을 정문 또는 중앙관제실에 전달하면, 무인 운송 로봇에 물품이 전달되어 로봇이 물품을 각 호로 배송하게 된다. 도착지 까지는 기존에 입력된 환경을 인식하여 다른 차량이나 보행자의 안전을 지키면서 목적지에 도달하도록 한다.




<br>

- - -
## 개념설계 및 상세설계
- 서비스의 형태
	&nbsp;기존의 아파트 동, 호까지 직접 배달하던 운송 기사는 아파트 단지나 학교의 정문, 또는 중앙 관제실 까지만 운송한다. 중앙 관제실의 근무자는 무인 운송 로봇에 도착지에 관련한 정보가 담긴 바코드를 스캔 후 적재하여, 해당 장소를 목적지로 설정시킨다.
	&nbsp;무인 운송 로봇은 다수의 물품을 적재하여 여러 목적지를 순차적으로 순회하며 운송할 수 있도록 한다. 목적지까지는 미리 로봇이 운용될 장소에 관련한 3D 매핑 정보와 실시간 스캐닝 정보를 연동하여 자율 주행이 가능하도록 한다. 또한, 사물인터넷 시스템을 응용하여 엘리베이터 이용이나 출입문 입출입을 모두 가능하도록 유연하게 시스템을 개발하도록 한다.

- 무인 운송 로봇의 주행
	&nbsp;무인 운송 로봇은 설정된 목적지까지 자율주행을 수행한다. 라즈베리파이 등의 초소형 임베디드 보드 보다는 itx PC를 활용한다. 자율주행을 구현함에 있어, 완전히 자유롭게 동작하면서 목적지까지 도달하는 것을 목표로 하기에는 아직 현대 자율주행 기술로는 어렵다. 따라서, 기존에 동 단위로 장소에 대한 이동 경로를 GPS 등으로 구현해 두고, 해당 경로를 최대한 따라가는 형태로 자율주행을 구현할 예정이다.
	&nbsp;그리고 기존 운송 시스템 수준을 달성하기 위하여, BLDC 모터를 적극적으로 활용하여 안전한 범위 안에서 고속으로 구동되도록 한다.




<br>

- - -
## 자체평가 및 최종결론
&nbsp;최근 코로나 19로 인해 운송 시스템의 수요가 폭증하고 있다. 동시에, 비대면 서비스를 선호하여 외부인의 출입을 최대한 막는 경우가 많아지고 있어 문앞 배송 서비스에 관련한 문제가 많은 곳에서 발생하고 있다. 이 서비스를 유지하는데 무인 운송 로봇이 큰 도움이 될 수 있다.
&nbsp;또한, 원칙적으로 외부인의 출입을 금지하는 단지, 학교 안에서의 운송 과정에도 기여하여 기존의 보안, 안전을 위한 원칙을 지키는데에도 해결방안이 될 수 있다.
&nbsp;결론적으로, 운송 기사 1인의 노동 시간에 의존하지 않고 기존의 운송 시스템을 가속할 수 있으며, 이는 관련 인력의 인건비 감소와 물류 유통 관련 기업의 생산성을 증대시킴과 동시에 이용사의 편의 증진에도 큰 기여가 가능하다.




<br>

- - -
## 캡스톤디자인(종합설계)을 앞둔 후배들에게 남기는 말
파이팅 !




<br>

- - -
# 캡스톤 디자인은 ( &nbsp; 재미지 &nbsp; ) 이다.

