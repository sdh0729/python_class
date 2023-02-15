#문제) Abstact 클래스에서 상속 받은 두 개의 클래스를 구현 하는 프로그램을 작성 한다
from abc import abstractmethod, ABCMeta

class Mobile(metaclass=ABCMeta):
    __mobileName = ''
    __batterSize = 0
    __osType = 0

    @abstractmethod # abstract class
    def operate(self, time):
        pass

    def __init__(self, mobileName, batterySize, osType):
        self.__mobileName = mobileName
        self.__batterySize = batterySize
        self.__osType = osType

    def getMobileName(self):
        return self.__mobileName

    def getBatterySize(self):
        return self.__batterySize

    def getOsType(self):
        return self.__osType

    def setBatterySize(self, batterySize):
        self.__batterySize = batterySize

    def setOsType(self, osType):
        self.__osType = osType
class IChange(metaclass=ABCMeta):

    @abstractmethod # abstract class
    def charge(self, time):
        pass


class Ltab(Mobile, IChange) :

    def __init__(self, mobileName,batterySize,osType):
        Mobile.__init__(self, mobileName, batterySize, osType)

    def operate(self, time):
        usedAmount = time * 10
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) - usedAmount)
        return Mobile.getBatterySize(self)

    def charge(self, time) :
        chargedAmount = time * 10
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) + chargedAmount)
        return Mobile.getBatterySize(self)

class Otab(Mobile, IChange) :
    def __init__(self, mobileName,batterySize,osType):
        Mobile.__init__(self, mobileName, batterySize, osType)

    def operate(self, time):
        usedAmount = time * 12
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) - usedAmount)
        return Mobile.getBatterySize(self)

    def charge(self, time) :
        chargedAmount = time * 8
        Mobile.setBatterySize(self, Mobile.getBatterySize(self) + chargedAmount)
        return Mobile.getBatterySize(self)

if __name__ == '__main__':
    # 각각의 mobile 객체 생성
    lt = Ltab("Ltab", 500, "AP-01")
    ot = Otab("Otab", 1000, "AND-20")
    # 생성된 객체의 정보 출력
    print("Mobile \t Battery \t OS")
    print("----------------------------")
    print(f"{lt.getMobileName()}\t\t{str(lt.getBatterySize())}\t{lt.getOsType()}")
    print(f"{ot.getMobileName()}\t\t{str(ot.getBatterySize())}\t{ot.getOsType()}")
    print("----------------------------")
    print("10분 충전")
    lt.charge(10)
    ot.charge(10)
    print(f"{lt.getMobileName()}\t\t{str(lt.getBatterySize())}\t{lt.getOsType()}")
    print(f"{ot.getMobileName()}\t\t{str(ot.getBatterySize())}\t{ot.getOsType()}")
    print("----------------------------")
    print("5분 사용")
    lt.operate(5)
    ot.operate(5)
    print(f"{lt.getMobileName()}\t\t{str(lt.getBatterySize())}\t{lt.getOsType()}")
    print(f"{ot.getMobileName()}\t\t{str(ot.getBatterySize())}\t{ot.getOsType()}")