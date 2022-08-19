# import json

# result=[]
# stack_data = ['Java', 'MySQL', 'Spring Boot', 'AWS', 'REST API', 'Node.js', 'MariaDB', 'Redis', 'Docker', 'Spring Framework', 'TypeScript', 'Linux', 'Spring', 'Python', 'ExpressJS', 'Kubernetes', 'React', 'JavaScript', 'Vue.js', 'HTML5', 'CSS 3', 'Git', 'Redux', 'React Native', 'Next.js', 'SQL', 'jQuery', 'Oracle', 'Kotlin', 'Android OS', 'Swift', 'Unity', 'C#', 'C++', 'Unreal Engine', 'WebGL', 'iOS', 'AR', 'MSSQL', 'C', 'NoSql', 'MongoDB', 'Network', 'PyTorch', 'MachineLearning', 'AI/인공지능', 'TensorFlow', 'DeepLearning', 'OpenCV', 'K8S', 'Terraform', 'Windows', 'AZURE', 'GCP', 'Ansible', 'Ubuntu', 'AWS Shell', 'ISMS', 'CISA', 'CISSP', 'CPPG', 'AWS WAF', 'QA', 'Jira', 'SW', 'Confluence', 'Redmine', 'PHP', 'HW', 'Embedded', 'Orcad', 'MCU', 'Pads', 'FW', 'PCB', 'FPGA', 'RF', 'ROS', 'Mfc', 'Objective-C', 'SwiftUI', 'Xcode', 'Rxswift', 'Zeplin', 'Figma', 'JSP', 'Flutter', 'Android Studio', 'BigData', 'Hadoop', 'R', 'Spark', 'Kafka', '3D Rendering', 'OpenGL', 'VR', 'three.js']
# for value in stack_data:
#     if value not in result:
#         result.append(value)

# M = dict(zip(range(1, len(result) + 1), result))
# json.dumps(M)
# print(M)

import json
#-*-coding:utf-8 -*-

description_data={
    'Java': '그 자체로 플랫폼으로 사용할 수 있는 다중 플랫폼, 객체 지향 및 네트워크 중심 언어입니다. 모바일 앱 및 엔터프라이즈 소프트웨어에서 빅 데이터 애플리케이션 및 서버 측 기술에 이르기까지 모든 것을 코딩하기 위한 빠르고 안전하며 안정적인 프로그래밍 언어','MySQL': '오픈소스의 관계형 데이터베이스 서비스','Spring Boot' : 'spring 개발을 좀 더 쉽게 만들어주는 도구이며 spring은 java를 기반으로 웹 어플리케이션 서비스를 만들 수 있는 프레임워크이다.','AWS':'아마존의 자회사로 같은 이름의 퍼블릭 클라우드 컴퓨팅 서비스를 제공한다. 클라우드 컴퓨팅은 직접 서버 장비를 구매하거나 임대 계약을 하지 않고도, 요청하는 즉시 컴퓨팅 자원을 제공해주는 서비스이다.','REST API' : '요청된 정보를 검색하는 데 관련된 서버의 각 유형을 클라이언트가 볼 수 없는 계층 구조로 체계화하는 계층화된 시스템이다','Node.js' : '확장성 있는 네트워크 애플리케이션 개발에 사용되는 소프트웨어 플랫폼이다.',
    'Maria DB' : '오픈 소스의 관계형 데이터베이스 관리 시스템이다. MySQL과 동일한 소스 코드를 기반으로 하며, GPL v2 라이선스를 따른다.',
    'Redis' : ' 오픈소스 NoSql로서 key-value 타입의 저장소로 주요 특징은 다음과 같습니다. 영속성을 지원하는 인메모리 데이터 저장소이다.',
    'Docker' : '컨테이너를 위한 운영 체제(또는 런타임)입니다. 컨테이너를 실행하려는 각 서버에 Docker Engine이 설치되어 컨테이너를 구축, 시작 또는 중단하는 데 사용할 수 있는 간단한 명령 세트를 제공한다.',
    'Spring Framework' : '자바 플랫폼을 위한 오픈 소스 애플리케이션 프레임워크로서 간단히 스프링(Spring)이라고도 한다. 동적인 웹 사이트를 개발하기 위한 여러 가지 서비스를 제공하고 있다.',
    'TypeScript': 'Microsoft에서 개발한 프로그래밍 언어이다. Javascript의 superset, 즉 확대집합 이라고 한다.',
    'Linux' : '리눅스는 윈도우나 MacOS 같은 컴퓨터의 운영체제이며, OS의 한 종류이다.',
    'Spring' : '자바 플랫폼을 위한 오픈 소스 애플리케이션 프레임워크로서 springframework라고도 한다. 동적인 웹 사이트를 개발하기 위한 여러 가지 서비스를 제공하고 있다.',
    'Python' : '고급 프로그래밍 언어로, 플랫폼에 독립적이며 인터프리터식, 객체지향적, 동적 타이핑 등의 특성을 가지는 대화형 언어이다.',
    'ExpressJS' : '웹 및 모바일 애플리케이션을 위한 일련의 강력한 기능을 제공하는 간결하고 유연한 Node.js 웹 애플리케이션 프레임워크이다.',
    'Kubernetes' : ' 컨테이너화된 워크로드와 서비스를 관리하기 위한 이식과 확장이 가능한 오픈소스 플랫폼으로, 선언적 구성과 자동화를 모두 지원한다.',
    'React' : '컴포넌트 기반 라이브러리 이며, 컴포넌트 기반은 기존의 웹 페이지를 작성할 때 처럼 하나의 HTML 코드를 집어넣고 하는 것이 아닌, 여러 부분을 분할 해서 코드의 재사용성과 유지보수성을 증가시켜 준다는 특성이 있다.',
    'JavaScript' : '개발자가 브라우저 게임을 만드는 데 사용할 수 있는 편리한 프로그래밍 언어이다.',
    'Vue.js' : '사용자 인터페이스를 만들기 위한 프로그레시브 프레임워크이다.',
    'HTML' : '웹 페이지와 그 내용을 구조화하기 위해 사용하는 코드이며, 여러 개의 문단, 글 머리 목록이 구조화된 것이거나 사진이나 데이터 테이블 등을 구조화할 수 있다. ',
    'CSS' : '문서의 콘텐츠와 레이아웃, 글꼴 및 시각적 요소들로 표현되는 문서의 외관, 즉 디자인을 분리하기 위한 목적으로 만들어졌다.',
    'Git' : '컴퓨터 파일의 변경사항을 추적하고 여러 명의 사용자들 간에 해당 파일들의 작업을 조율하기 위한 분산 버전 관리 시스템이다. ',
    'Redux' : '모든 컴포넌트들이 state 를 쉽게 공유할 수 있게 해주는 방식이다. React 내부에 있는 기술이 아니며 순수 HTML, JAVASCRIPT 내에서도 사용이 가능하다.',
    'React Native' : ' iOS와 안드로이드에서 동작하는 네이티브 모바일 앱을 만드는 자바스크립트 프레임워크이다. ',
    'Next.js' : 'React로 만드는 서버사이드 렌더링 프레인 워크이다. 사용자가 소요해야하는 대기 시간이 긴 클라이언트 렌더링을 사용하지 않아, 시간을 단축할 수 있는 장점이 있다.',
    'SQL' : ' 관계형 데이터베이스 관리 시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.'
}

# f= open('C:\Users\User\Desktop\likelion coding\switch json','w',encoding='cp949')
# json.dump(description_data,f)

with open('./data.json', 'w', encoding="UTF-8") as f:
    json_string = json.dump(description_data, f, ensure_ascii=False,indent=4)