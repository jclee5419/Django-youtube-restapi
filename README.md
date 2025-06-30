# Django-youtube-restapi

## Docker  
Docker는 애플리케이션의 실행에 필요한 환경을 하나의 이미지로 모아두고, 그 이미지를 사용하여 다양한 환경에서 애플리케이션 실행 환경을 구축 및 운용하기 위한 오픈소스 플랫폼.
도커는 일반적으로 도커 엔진(Docker Engine) 혹은 도커에 관련된 모든 프로젝트를 말합니다.
--------
## Docker의 구성요소  
### Docker daemon (dockerd) : 도커 엔진
Docker API에 따라 이미지, 컨테이너, 네트워크 등의 도커 오브젝트들을 관리한다. 다른 daemon과 통신할 수도 있다.

### Client
도커 사용자들이 도커를 사용하는 방법이다. 사용자가 입력한 명령어를 도커 엔진에 전달하고, 수행하게 된다.

### Docker Host
도커가 띄워져있는 서버이다. 컨테이너와 이미지를 관리한다.

### Docker registry
외부 이미지 저장소이다. docker pull 명령어를 통해 필요한 이미지를 가져올 수 있고, 가져온 이미지를 docker run하면 컨테이너가 된다. docker push 를 통해 이미지를 푸시할 수 있다.

### Docker Image
먼저, 도커 이미지는 Docker File을 사용하여 docker build 명령어를 실행하면 만들어진다. 그 후에 해당 이미지와 Docker run 명령어를 통해 Docker Container가 만들어진다.

도커 이미지는 컨테이너를 생성하고 실행할 때 읽기 전용으로 사용되며, 여러 계층으로 binary 파일로 존재한다.

[저장소 이름]/[이미지 이름]:[태그]

저장소 이름 : 이미지의 저장소. 명시되어 있지 않은 이미지는 도커 허브의 공식 이미지라는 뜻이다.  
이미지 이름 : 이미지의 역할. 필수로 설정해야 한다. (ex. ubuntu -> 우분투 컨테이너를 생성하기 위한 이미지라는 뜻)  
태그 : 이미지의 버전. 생략하면 latest로 인식한다.  

### Docker Container
이미지의 실행 가능한 인스턴스이다. Docker API 또는 CLI를 사용해서 컨테이너를 생성/시작/중지/이동/삭제를 한다. 컨테이너를 네트워크나 스토리지를 연결하거나 새로운 이미지를 만들 수도 있다.

컨테이너는 이미지에 의해 정의되며, 다른 컨테이너 및 호스트 시스템과 격리된 시스템 자원 및 네트워크를 사용할 수 있다. 따라서 특정 컨테이너에서 수정사항이 생겨도 다른 컨테이너와 호스트는 변경 사항이 없다.

컨테이너는 이미지를 읽기 전용으로 사용하되, 이미지에서 변경된 사항만 컨테이너 계층에 저장하기 때문에 컨테이너에서 무엇을 해도 이미지는 영향을 받지 않는다.


# CI/CD
CI/CD는 Continuous Integration(지속적 통합)과 Continuous Deployment(지속적 배포)를 뜻한다.  

이 개념은 개발자가 더 효율적으로 코드를 작성하고, 빠르고 안정적으로 사용자에게 소프트웨어를 제공하는 것을 목표로 한다.  

한마디로 CI/CD는 테스트(Test), 통합(Merge), 배포(Deploy)의 과정을 자동화하는 걸 의미한다.  

 
서비스를 운영하다보면 새로운 기능을 추가하는 일이 많아진다.  

새로운 기능에 대한 코드를 작성한 뒤에 Commit을 하고, 브랜치에 Merge를 하고 배포를 한다.  

배포를 할 때 직접 컴퓨터 서버(ex. AWS EC2)에 접속해서 새로운 코드를 다운받아 실행시켜주어야 한다.   

이 과정을 코드의 수정이 일어날 때마다 반복하기란 너무 귀찮은 일이다. 그래서 이런 반복적인 과정을 자동화시키기 위해 CI/CD를 도입한다.  

 
CI(Continuous Integration)  

코드를 올리면 자동으로 빌드하고, 테스트해서 문제가 있는지 바로 확인해주는 단계  
 

CD(Continuous Deployment)  

테스트 통과하면 운영 서버까지 완전 자동 배포  
 

GitHub Actions는 자동화된 워크플로우를 지원하는 도구로, 저장소의 빌드, 테스트, 배포 등의 작업을 자동화할 수 있다.  

CI/CD 과정은 일반적으로 다음과 같은 과정으로 일어난다.  

https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdna%2F7JrXc%2FbtsOpFfe520%2FAAAAAAAAAAAAAAAAAAAAAKSU9q_1QmyxHEca2VPQzqpYZE6ssggSn97iMU8vvpOK%2Fimg.png%3Fcredential%3DyqXZFxpELC7KVnFOS48ylbz2pIh7yKj8%26expires%3D1751295599%26allow_ip%3D%26allow_referer%3D%26signature%3D8e15u4HlJ9BfEWZTza7jT4QFpjI%253D

즉, GitHub Actions는 CI/CD 과정에서 빌드, 테스트, 배포에 대한 로직을 실행시키는 서버(컴퓨터)의 역할을 한다.  

https://blog.kakaocdn.net/dna/mD9VZ/btsJuFSvmwX/AAAAAAAAAAAAAAAAAAAAAKW1XNwYZh57lqqcP-9ikw2YKaZYs2qbZhMv7hncmxFL/img.png?credential=yqXZFxpELC7KVnFOS48ylbz2pIh7yKj8&expires=1751295599&allow_ip=&allow_referer=&signature=KLYhnb1%2FmepukeFKJxxIooWw%2BUg%3D

1. 코드 작성 후 Github에 Commit & Push  
2.Push를 감지해서 Github Actions에 작성한 로직이 실행  
빌드(Build) -> 테스트(Test)-> 서버로 배포(Deploy)  
3. 서버에서 배포된 최신 코드로 서버를 재실행  
 

# PostgreSQL
개발자가 코드를 작성 후 커밋 & 푸시를 하는 순간 GitHub Actions는 빌드 및 테스트를 하고 EC2에 배포까지 자동화 할 수 있다.  
물론 테스트 코드에서 오류가 난다면 배포가 중단된다.(서비스가 중단되는 것은 아니다.)  

PostgreSQL(또는 Postgres)은 사용자 정의 객체와 테이블 접근 방식을 결합하여 보다 복잡한 데이터 구조를 구축하는 엔터프라이즈급 오픈소스 객체 관계형(object-relational) 데이터베이스 관리 시스템(DBMS)입니다. 확장성과 SQL 규정 준수를 위해 관계형 및 비관계형 쿼리를 위한 SQL과 JSON을 모두 지원합니다. PostgreSQL은 고급 데이터 유형과 성능 최적화 기능을 지원하며, 이는 보통 Oracle 및 SQL Server와 같은 고가의 상용 데이터베이스에서만 사용할 수 있는 기능입니다.

PostgreSQL 글로벌 개발 그룹(Global Development Group)이 소유하고 개발해 왔으며, 완전한 오픈소스로 남아 있습니다. 이 DBMS는 Microsoft, iOS, Android 등의 플랫폼에서 사용이 가능합니다.


# PostgreSQL의 장점  

1) 뛰어난 확장성 
수직적 확장성은 PostgreSQL의 특징입니다. 거의 모든 맞춤형 소프트웨어 솔루션이 성장하여 데이터베이스를 확장하는 경향이 있다는 점을 고려할 때, 이 특정 옵션은 확실한 비즈니스 성장과 개발을 지원합니다.


2) 사용자 정의 데이터 유형 지원
PostgreSQL은 기본적으로 JSON, XML, H-Store 등 다양한 데이터 유형을 지원합니다. PostgreSQL은 NoSQL 기능을 강력하게 지원하는 몇 안 되는 관계형 데이터베이스 중 하나이기 때문에 그 많은 데이터 유형을 지원하는 것입니다. 또한 사용자가 직접 데이터 유형을 정의할 수 있습니다. 소프트웨어 비즈니스 모델에 따라 더 나은 성능이나 애플리케이션의 포괄성을 위해 다양한 유형의 데이터베이스가 필요할 수 있으므로, 이 옵션을 사용하면 유연성이 향상되는 것을 확인할 수 있습니다.


3) 쉽게 통합 가능한 서드파티 도구 

PostgreSQL DBMS는 무료 및 상용 도구에 강력한 추가 지원을 제공합니다. 여기에는 Postgres의 여러 측면을 개선하기 위한 확장 기능(extension)들이 포함됩니다. 예를 들어, ClusterControl은 SQL 및 NoSQL 오픈소스 데이터베이스를 관리하고 모니터링 및 확장에 대한 지원을 합니다. 데이터 비교 및 동기화를 보다 효과적으로 수행하려면 DB Data Directive를 사용하는 것을 권장합니다. 워크로드가 많은 데이터로 확장하려는 경우, pgBackRest 백업 및 복원 시스템이 좋은 옵션이 될 것입니다.


4) 오픈소스 및 커뮤니티 중심 지원

PostgreSQL은 완전한 오픈소스이며 다양한 커뮤니티의 지원을 받아 완전한 에코시스템으로 자리를 잡았습니다. 소스코드가 오픈소스 라이선스를 따르기 때문에 비즈니스 요구에 따라 자유롭게 사용, 수정, 구현할 수 있습니다.

이 외에 PostgreSQL의 주목할 만한 장점을 소개합니다.

LAMP 스택 옵션으로 웹사이트와 웹 애플리케이션을 실행
WAL(미리 쓰기 로그)로 데이터베이스의 내결함성 향상
지리적 개체를 지원하므로 위치 기반 서비스 및 지리 정보 시스템을 위한 지리 공간 데이터 저장소로 사용 가능
사용하기 쉽기 때문에 많은 교육이 필요하지 않음
임베디드 및 엔터프라이즈에서 PostgreSQL을 사용할 때 간편한 유지 및 관리
