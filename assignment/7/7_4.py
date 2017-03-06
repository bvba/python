from Fan import Fan
# Fan 파일에서 Fan 클래스 import

fan1 = Fan(Fan.FAST, 10, "yellow", True)    # fan1 객체 생성
fan2 = Fan(Fan.MEDIUM, 5, "blue", False)    # fan2 객체 생성

fan1.print()    
fan2.print()    # fan1, fan2 객체의 필드 값 출력
