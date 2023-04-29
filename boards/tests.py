from django.test import TestCase,Client
from django.urls import reverse
from .models import Board

c=Client()
class BoardTest(TestCase):
    
    TITLE1 = "파이썬에 대해 알아보기"
    CONTENT1 ="파이썬은 초보자부터 전문가까지 사용자층을 보유하고 있다.동적 타이핑(dynamic typing) 범용 프로그래밍 언어로,펄 및 루비와 자주 비교된다.다양한 플랫폼에서 쓸 수 있고, 라이브러리(모듈)가 풍부하여, 대학을 비롯한 여러 교육 기관, 연구 기관 및 산업계에서 이용이 증가하고 있다.또 파이썬은 순수한 프로그램 언어로서의 기능 외에도 다른 언어로 쓰인 모듈들을 연결하는 접착제 언어로써 자주 이용된다.실제 파이썬은 많은 상용 응용 프로그램에서 스크립트 언어로 채용되고 있다. 도움말 문서도 정리가 잘 되어 있으며, 유니코드 문자열을 지원해서 다양한 언어의 문자 처리에도 능하다.구문이 강조된 파이썬 코드 예제파이썬은 기본적으로 해석기(인터프리터) 위에서 실행될 것을 염두에 두고 설계되었다."


    TITLE2 = "자바에 대해 알아보기"
    CONTENT2 = "va의 가장 큰 특징은 플랫폼에 독립적인 언어라는 점이다. 소스 코드를 기계어로 직접 컴파일하여 링크하는 C/C++의 컴파일러와 달리 자바 컴파일러는 바이트코드인 클래스 파일(.class)을 생성하고, 이 파일의 바이트코드를 읽은 뒤 기계어로 바꾸어 실행하는 것은 자바 가상 머신이다.예를 들어 플랫폼에 종속된 경우 윈도우에서 빌드한 프로그램을 그대로 리눅스나 macOS에서 실행하려 하면 일반적으로 오류가 나지만 Java로 작성 된 프로그램은 플랫폼에 맞는 Java Runtime Environment만 설치되어 있다면 문제 없이 동작한다. 이는 Java 코드 자체가 플랫폼이 아닌 가상머신에 종속적이라는 점, 그리고 프로그램 실행의 주체가 운영 체제가 아닌 Java Runtime Environment이라는 점 때문이며 이러한 점을 통틀어 Java는 플랫폼 종속성이 낮은 언어라고 표현한다."

    TITLE3 = "자바스크립트에 대해 알아보기"
    CONTENT3 = "JavaScript는 멀티-패러다임 언어로 명령형, 함수형, 객체 지향형 언어다. 기본적으로는 함수가 일급 시민으로 취급되는 언어로써 함수형 프로그래밍 패러다임을 따른다. 자연스럽게 이는 클로저로 시작해 끝을 보는 것이 가능하다.[19] 멀티 패러다임 언어인만큼 원한다면 명령형 프로그래밍(imperative programming)으로 코드를 쓸 수도 있지만 보통은 함수형/선언형 프로그래밍으로 작성해야 JavaScript가 제공하는 장점을 백분 활용하는 것이 가능하다. 객체 지향으로 코드를 작성하는 것도 가능하고 심지어 class도 ECMAScript 6이후로 제공하지만, JavaScript에서의 class는 그냥 function을 class형식으로 쓸 수 있게 제공하는 syntatic sugar에 지나지 않으므로 타 객체 지향 프로그래밍 언어처럼 사용하다가는 장벽에 부딪히기 쉽다. 즉 JavaScript에서 class는 존재하지만 C++의 class와는 완전히 다른 개념이며, JavaScript의 객체 지향 프로그래밍은 함수 프로토타입에 기반한 객체 지향 프로그래밍이다. # 결국 근본적으로 JavaScript는 함수와 함수형 프로그래밍을 제대로 이해하지 않으면 제대로 다룰 수 없는 언어인 셈이다. 좋게 얘기하자면 확장성이 무한한 것이고, 나쁘게 말하자면 일관성이 바닥이다." 

    TITLE4 = "Django에 대해 알아보기"
    CONTENT4 = "장고는 파이썬으로 코딩한 모델을 관계형 데이터베이스로 구축해주는 모델(Model), HTTP 요청을 처리하는 웹 템플릿 시스템인 뷰(View), URL의 라우팅을 처리하는 URL 컨트롤러 (Controller) 로 구성된 MVC 디자인 패턴을 따른다.하지만 전통적인 MVC 디자인 패턴에서 이야기하는 컨트롤러의 기능을 프레임워크를 자체에서 하기 때문에 모델(Model), 템플릿(Template), 뷰(View)로 분류해 MTV 프레임워크라고 보기도 한다"
    
    def setUp(self) -> None:
        
        self.board1 = Board.objects.create(title=self.TITLE1,content=self.CONTENT1)
        self.board2 =Board.objects.create(title=self.TITLE2,content=self.CONTENT2)
        self.board3 = Board.objects.create(title=self.TITLE3,content=self.CONTENT3)
    
    # 게시물 리스트에 3개 있는지 확인
    def test_list_get_board(self): 
        response = c.get(reverse("board:board_list"))
        self.assertQuerysetEqual(response.context['boards'],Board.objects.all())
        self.assertEqual(len(response.context['boards']),3)
    
    # 게시물 하나 만들고(TITLE4) 확인
    def test_post_board(self):
        response = c.post(reverse("board:board_create"),data={"title":self.TITLE4,"content":self.CONTENT4})
        self.assertEqual(response.status_code,302) 
        self.assertEqual(len(Board.objects.all()),4)
        self.assertEqual(Board.objects.filter(pk=4).first().title,self.TITLE4)
    
    def test_related_board(self):
        response = c.get("/board/1/")
        board_word = Board.objects.filter(pk=1).first().candidate_realted_word()
        
    
    
        
