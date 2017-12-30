from Bodypart import Bodypart
from anytree import Node, RenderTree


class Body:
    def __init__(self):
        self.bodyparts = None
        self.initializeBody()
        self.alive = True

    def initializeBody(self):
        head = Bodypart(None, "Ett", None, "huvud", True)

        leftEye = Bodypart(head, "Ett", "vänster", "öga")
        rightEye = Bodypart(head, "Ett", "höger", "öga")

        nose = Bodypart(head, "En", None, "näsa")

        mouth = Bodypart(head, "En", None, "mun")
        tongue = Bodypart(mouth, "En", None, "tunga")

        leftEar = Bodypart(head, "Ett", "vänster", "öra")
        leaftEarlobe = Bodypart(leftEar, "En", "vänster", "örsnibb")

        rightEar = Bodypart(head, "Ett", "höger", "öra")
        rightEarlobe = Bodypart(rightEar, "En", "höger", "örsnibb")

        neck = Bodypart(head, "En", None, "nacke", True)
        chest = Bodypart(neck, "Ett", None, "bröst", True)

        leftShoulder = Bodypart(chest, "En", "vänster", "axel")
        leftUpperArm = Bodypart(leftShoulder, "En", "vänster", "överarm")
        leftElbow = Bodypart(leftUpperArm, "En", "vänster", "armbåge")
        leftLowerArm = Bodypart(leftElbow, "En", "vänster", "underarm")
        leftWrist = Bodypart(leftLowerArm, "En", "vänster", "handled")
        leftPalm = Bodypart(leftWrist, "En", "vänster", "handflata")
        leftThumb = Bodypart(leftPalm, "En", "vänster", "tumme")
        leftIndex = Bodypart(leftPalm, "Ett", "vänster", "pekfinger")
        leftMiddle = Bodypart(leftPalm, "Ett", "vänster", "långfinger")
        leftRing = Bodypart(leftPalm, "Ett", "vänster", "ringfinger")
        leftLittle = Bodypart(leftPalm, "Ett", "vänster", "lillfinger")

        rightShoulder = Bodypart(chest, "En", "höger", "axel")
        rightUpperArm = Bodypart(rightShoulder, "En", "höger", "överarm")
        rightElbow = Bodypart(rightUpperArm, "En", "höger", "armbåge")
        rightLowerArm = Bodypart(rightElbow, "En", "höger", "underarm")
        rightWrist = Bodypart(rightLowerArm, "En", "höger", "handled")
        rightPalm = Bodypart(rightWrist, "En", "höger", "handflata")
        rightThumb = Bodypart(rightPalm, "En", "höger", "tumme")
        rightIndex = Bodypart(rightPalm, "Ett", "höger", "pekfinger")
        rightMiddle = Bodypart(rightPalm, "Ett", "höger", "långfinger")
        rightRing = Bodypart(rightPalm, "Ett", "höger", "ringfinger")
        rightLittle = Bodypart(rightPalm, "Ett", "höger", "lillfinger")

       	belly = Bodypart(chest, "En", None, "mage", True)
        navel = Bodypart(belly, "En", None, "navel")

        back = Bodypart(belly, "En", None, "rygg", True)
        ass = Bodypart(back, "En", None, "röv")

        hips = Bodypart(belly, "En", None, "höft")
        groin = Bodypart(hips, "Ett", None, "skrev")

        leftThigh = Bodypart(hips, "Ett", "vänster", "lår")
        leftKnee = Bodypart(leftThigh, "Ett", "vänster", "knä")
        leftLowerLeg = Bodypart(leftKnee, "Ett", "vänster", "smalben")
        leftAnkle = Bodypart(leftLowerLeg, "En", "vänster", "vrist")
        leftFoot = Bodypart(leftAnkle, "En", "vänster", "fot")
        leftBigtoe = Bodypart(leftFoot, "En", "vänster", "stortå")
        leftIndextoe = Bodypart(leftFoot, "En", "vänster", "pektå")
        leftMiddletoe = Bodypart(leftFoot, "En", "vänster", "långtå")
        leftRingtoe = Bodypart(leftFoot, "En", "vänster", "ringtå")
        leftLittletoe = Bodypart(leftFoot, "En", "vänster", "lilltå")

        rightThigh = Bodypart(hips, "Ett", "höger", "lår")
        rightKnee = Bodypart(rightThigh, "Ett", "höger", "knä")
        rightLowerLeg = Bodypart(rightKnee, "Ett", "höger", "smalben")
        rightAnkle = Bodypart(rightLowerLeg, "En", "höger", "vrist")
        rightFoot = Bodypart(rightAnkle, "En", "höger", "fot")
        rightBigtoe = Bodypart(rightFoot, "En", "höger", "stortå")
        rightIndextoe = Bodypart(rightFoot, "En", "höger", "pektå")
        rightMiddletoe = Bodypart(rightFoot, "En", "höger", "långtå")
        rightRingtoe = Bodypart(rightFoot, "En", "höger", "ringtå")
        rightLittletoe = Bodypart(rightFoot, "En", "höger", "lilltå")

        self.bodyparts = head