from sunau import AUDIO_FILE_ENCODING_LINEAR_16, AUDIO_FILE_ENCODING_LINEAR_24


class Triangle:
    numberOfSides = 3

    def __init__(self, a1, a2, a3):
        self.angle1 = a1
        self.angle2 = a2
        self.angle3 = a3

    def __str__():
        print()

    def setAngle1(self, n):
        self.angle1 = n

    def setAngle2(self, n):
        self.angle2 = n

    def setAngle3(self, n):
        self.angle3 = n

    def getAngle1(self):
        return self.angle1

    def getAngle2(self):
        return self.angle2

    def getAngle3(self):
        return self.angle3

    def checkAngles(self, angle1, angle2, angle3):
        if 180 == (angle1+angle2+angle3):
            return True
        else:
            return False


c = Triangle(45, 45, 90)
print(c.checkAngles(c.getAngle1(), c.getAngle2(), c.getAngle3()))
