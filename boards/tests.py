from django.test import TestCase,Client
from django.urls import reverse
from .models import Board

c=Client()
class BoardTest(TestCase):
    
    TITLE1 = "파이썬에 대해 알아보기"
    CONTENT1 ="파이썬은 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 파이썬 초보자부터 전문가까지 사용자층을 보유하고 있다.동적 타이핑(dynamic typing) 범용 프로그래밍 언어로,펄 및 루비와 자주 비교된다.다양한 플랫폼에서 쓸 수 있고, 라이브러리(모듈)가 풍부하여, 대학을 비롯한 여러 교육 기관, 연구 기관 및 산업계에서 이용이 증가하고 있다.또 파이썬은 순수한 프로그램 언어로서의 기능 외에도 다른 언어로 쓰인 모듈들을 연결하는 접착제 언어로써 자주 이용된다."

    TITLE2 = "자바에 대해 알아보기"
    CONTENT2 = "va의 가장 큰 특징은 플랫폼에 독립적인 언어라는 점이다. 소스 코드를 기계어로 직접 컴파일하여 링크하는 C/C++의 컴파일러와 달리 자바 컴파일러는 바이트코드인 클래스 파일(.class)을 생성하고, 이 파일의 바이트코드를 읽은 뒤 기계어로 바꾸어 실행하는 것은 자바 가상 머신이다.예를 들어 플랫폼에 종속된 경우 윈도우에서 빌드한 프로그램을 그대로 리눅스나 macOS에서 실행하려 하면 일반적으로 오류가 나지만 Java로 작성 된 프로그램은 플랫폼에 맞는 Java Runtime Environment만 설치되어 있다면 문제 없이 동작한다. 이는 Java 코드 자체가 플랫폼이 아닌 가상머신에 종속적이라는 점, 그리고 프로그램 실행의 주체가 운영 체제가 아닌 Java Runtime Environment이라는 점 때문이며 이러한 점을 통틀어 Java는 플랫폼 종속성이 낮은 언어라고 표현한다."

    TITLE3 = "Django에 대해 알아보기"
    CONTENT3 = "장고는 파이썬으로 코딩한 모델을 관계형 데이터베이스로 구축해주는 모델(Model), HTTP 요청을 처리하는 웹 템플릿 시스템인 뷰(View), URL의 라우팅을 처리하는 URL 컨트롤러 (Controller) 로 구성된 MVC 디자인 패턴을 따른다.하지만 전통적인 MVC 디자인 패턴에서 이야기하는 컨트롤러의 기능을 프레임워크를 자체에서 하기 때문에 모델(Model), 템플릿(Template), 뷰(View)로 분류해 MTV 프레임워크라고 보기도 한다"
    
    TITLE4 = "자바스크립트에 대해 알아보기"
    CONTENT4 = "JavaScript는 멀티-패러다임 언어로 명령형, 함수형, 객체 지향형 언어다. 기본적으로는 함수가 일급 시민으로 취급되는 언어로써 함수형 프로그래밍 패러다임을 따른다. 자연스럽게 이는 클로저로 시작해 끝을 보는 것이 가능하다.[19] 멀티 패러다임 언어인만큼 원한다면 명령형 프로그래밍(imperative programming)으로 코드를 쓸 수도 있지만 보통은 함수형/선언형 프로그래밍으로 작성해야 JavaScript가 제공하는 장점을 백분 활용하는 것이 가능하다. 객체 지향으로 코드를 작성하는 것도 가능하고 심지어 class도 ECMAScript 6이후로 제공하지만, JavaScript에서의 class는 그냥 function을 class형식으로 쓸 수 있게 제공하는 syntatic sugar에 지나지 않으므로 타 객체 지향 프로그래밍 언어처럼 사용하다가는 장벽에 부딪히기 쉽다. 즉 JavaScript에서 class는 존재하지만 C++의 class와는 완전히 다른 개념이며, JavaScript의 객체 지향 프로그래밍은 함수 프로토타입에 기반한 객체 지향 프로그래밍이다. # 결국 근본적으로 JavaScript는 함수와 함수형 프로그래밍을 제대로 이해하지 않으면 제대로 다룰 수 없는 언어인 셈이다. 좋게 얘기하자면 확장성이 무한한 것이고, 나쁘게 말하자면 일관성이 바닥이다." 

    TITLE5 = "파이썬이란?"
    CONTENT5 = "파이썬은 1990년 암스테르담의 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어이다. 귀도는 파이썬이라는 이름을 자신이 좋아하는 코미디 쇼인 몬티 파이썬의 날아다니는 서커스(Monty Python’s Flying Circus)에서 따왔다고 한다.인터프리터 언어란 한 줄씩 소스 코드를 해석해서 그때그때 실행해 결과를 바로 확인할 수 있는 언어이다.파이썬의 사전적 의미는 고대 신화에 나오는 파르나소스 산의 동굴에 살던 큰 뱀을 뜻하며, 아폴로 신이 델파이에서 파이썬을 퇴치했다는 이야기가 전해지고 있다. 대부분의 파이썬 책 표지와 아이콘이 뱀 모양으로 그려져 있는 이유가 여기에 있다.파이썬은 컴퓨터 프로그래밍 교육을 위해 많이 사용하지만, 기업의 실무를 위해서도 많이 사용하는 언어이다. 그 대표적인 예가 바로 구글이다. 필자는 구글에서 만든 소프트웨어의 50%이상이 파이썬으로 작성되었다는 이야기를 들었다. 이외에도 많이 알려진 예를 몇 가지 들자면 온라인 사진 공유 서비스 인스타그램(Instagram), 파일 동기화 서비스 드롭박스(Dropbox)등이 있다.또한 파이썬 프로그램은 공동 작업과 유지 보수가 매우 쉽고 편하다. 그 때문에 이미 다른 언어로 작성된 많은 프로그램과 모듈이 파이썬으로 재구성되고 있다. 국내에서도 그 가치를 인정받아 사용자 층이 더욱 넓어지고 있고, 파이썬을 사용해 프로그램을 개발하는 업체들 또한 늘어 가고 있는 추세이다."
    
    TITLE6 = "백엔드란?"
    CONTENT6 = "백엔드 개발자는 기존 개발자라 불리는 스펙과 방식이 약간 다르다. 프로그래밍, 데이터베이스, 웹 서버, 네트워크, 인프라 등에 대한 기술이 필요하다.백엔드 개발은 API 개발이 주가 된다. 프론트에서 요구하는 데이터의 포맷이나 데이터베이스 입출력 및 다양한 비즈니스 프로세스를 코드로 구현하고 이를 위한 DB를 설계하고 백엔드 프레임워크를 이용하여 앱을 구현하는 것이 주요 업무다. 여기에 백엔드 프레임워크와 프론트엔드 서버를 이어주는 서블릿, WSGI 등의 미들웨어 기술도 필요하다. API 명세를 설계하고 실제 배포 단계에서 최대한 문제가 발생하지 않도록 체계적으로 구성하는 능력도 필요하다.핵심은 DB에 담겨진 정보를 프론트엔드에서 활용할 수 있도록 여러 API들을 개발하는 것이 핵심이라고 볼 수 있다. 백엔드와 프론트엔드를 모두 다룰 줄 아는 개발자를 일컬어 풀 스택 개발자라고 한다.위 서술은 웹개발 위주로만 설명되어 있지만 시스템 프로그래밍에서도 크게 다르지는 않다. 결국 '인터페이스'라는 것은 서로 다른 애플리케이션을 이어주는 가교 역할을 하는 것이므로 본질적으론 동일하다. 차이가 있다면 웹 개발에서는 최종적으로 구현된 API들을 Vue.js나 React 같은 프론트엔드 프레임워크가 사용하는 것이고 시스템 프로그래밍에서는 다른 프로그램이 사용할 뿐이다. 백엔드는 거기에 필요한 데이터를 DB에서 꺼내고 JSON 또는 XML 형태의 표준 데이터 포맷으로 잘 보내주기만 하면 된다."
    
    TITLE7 = "파이썬ㅇㅇ"
    CONTENT7 = "파이썬 초보자부터 전문가까지 사용자층을 보유하고 있다.동적 타이핑(dynamic typing) 범용 프로그래밍 언어로,펄 및 루비와 자주 비교된다.다양한 플랫폼에서 쓸 수 있고, 라이브러리(모듈)가 풍부하여, 대학을 비롯한 여러 교육 기관, 연구 기관 및 산업계에서 이용이 증가하고 있다.또 파이썬은 순수한 프로그램 언어로서의 기능 외에도 다른 언어로 쓰인 모듈들을 연결하는 접착제 언어로써 자주 이용된다.파이썬은 1990년 암스테르담의 귀도 반 로섬(Guido Van Rossum)이 개발한 인터프리터 언어이다. 귀도는 파이썬이라는 이름을 자신이 좋아하는 코미디 쇼인 몬티 파이썬의 날아다니는 서커스(Monty Python’s Flying Circus)에서 따왔다고 한다.인터프리터 언어란 한 줄씩 소스 코드를 해석해서 그때그때 실행해 결과를 바로 확인할 수 있는 언어이다.파이썬의 사전적 의미는 고대 신화에 나오는 파르나소스 산의 동굴에 살던 큰 뱀을 뜻하며, 아폴로 신이 델파이에서 파이썬을 퇴치했다는 이야기가 전해지고 있다. 대부분의 파이썬 책 표지와 아이콘이 뱀 모양으로 그려져 있는 이유가 여기에 있다.파이썬은 컴퓨터 프로그래밍 교육을 위해 많이 사용하지만, 기업의 실무를 위해서도 많이 사용하는 언어이다. 그 대표적인 예가 바로 구글이다. 필자는 구글에서 만든 소프트웨어의 50%이상이 파이썬으로 작성되었다는 이야기를 들었다. 이외에도 많이 알려진 예를 몇 가지 들자면 온라인 사진 공유 서비스 인스타그램(Instagram), 파일 동기화 서비스 드롭박스(Dropbox)등이 있다.또한 파이썬 프로그램은 공동 작업과 유지 보수가 매우 쉽고 편하다. 그 때문에 이미 다른 언어로 작성된 많은 프로그램과 모듈이 파이썬으로 재구성되고 있다. 국내에서도 그 가치를 인정받아 사용자 층이 더욱 넓어지고 있고, 파이썬을 사용해 프로그램을 개발하는 업체들 또한 늘어 가고 있는 추세이다."
    def setUp(self) -> None:

        self.board2 =Board.objects.create(title=self.TITLE2,content=self.CONTENT2)
        self.board3 = Board.objects.create(title=self.TITLE3,content=self.CONTENT3)
        self.board4 = Board.objects.create(title=self.TITLE4,content=self.CONTENT4)
        self.board5 = Board.objects.create(title=self.TITLE5,content=self.CONTENT5)
        self.board6 = Board.objects.create(title=self.TITLE7,content = self.CONTENT7)
        self.board1 = Board.objects.create(title=self.TITLE1,content=self.CONTENT1)

    
    # 게시물 리스트에 3개 있는지 확인
    def test_list_get_board(self): 
        response = c.get(reverse("board:board_list"))
        self.assertQuerysetEqual(response.context['boards'],Board.objects.all())
        self.assertEqual(len(response.context['boards']),6)
    
    # 게시물 하나 만들고(TITLE4) 확인
    def test_post_board(self):
        response = c.post(reverse("board:board_create"),data={"title":self.TITLE6,"content":self.CONTENT6})
        self.assertEqual(response.status_code,302) 
        self.assertEqual(len(Board.objects.all()),7)
        self.assertEqual(Board.objects.filter(pk=7).first().title,self.TITLE6)
    
    # 60퍼 이상의 단어는 연관게시물에 찾는데 관여 하면 안됨
    def test_60_over_related_word(self): 
        board_word = self.board1.candidate_realted_word()
        result = False
        if "파이썬" in board_word:
            result = True
        self.assertEqual(result,False)
    
    def test_Related_Board(self):
        response = c.get(reverse("board:board_detail",kwargs={"board_id":1}))
        print(response.context["related_boards"])
        
    
    
        
