import json

from ...rpc.client import Client
from .sport_api import *

"""
" SPORT_PATH_POINT_SIZE
"""
SPORT_PATH_POINT_SIZE = 30


"""
" class PathPoint
"""
class PathPoint:
    def __init__(self, timeFromStart: float, x: float, y: float, yaw: float, vx: float, vy: float, vyaw: float):
        self.timeFromStart = timeFromStart
        self.x = x
        self.y = y
        self.yaw = yaw
        self.vx = vx
        self.vy = vy
        self.vyaw = vyaw


"""
" class SportClient
"""
class SportClient(Client):
    def __init__(self, enableLease: bool = False):
        super().__init__(SPORT_SERVICE_NAME, enableLease)


    def Init(self):
        # set api version
        self._SetApiVerson(SPORT_API_VERSION)

        # regist api
        self._RegistApi(SPORT_API_ID_DAMP, 0)
        self._RegistApi(SPORT_API_ID_BALANCESTAND, 0)
        self._RegistApi(SPORT_API_ID_STOPMOVE, 0)
        self._RegistApi(SPORT_API_ID_STANDUP, 0)
        self._RegistApi(SPORT_API_ID_STANDDOWN, 0)
        self._RegistApi(SPORT_API_ID_RECOVERYSTAND, 0)
        self._RegistApi(SPORT_API_ID_MOVE, 0)
        self._RegistApi(SPORT_API_ID_SWITCHGAIT, 0)
        self._RegistApi(SPORT_API_ID_BODYHEIGHT, 0)
        self._RegistApi(SPORT_API_ID_SPEEDLEVEL, 0)
        self._RegistApi(SPORT_API_ID_TRAJECTORYFOLLOW, 0)
        self._RegistApi(SPORT_API_ID_CONTINUOUSGAIT, 0)
        self._RegistApi(SPORT_API_ID_MOVETOPOS, 0)
        self._RegistApi(SPORT_API_ID_SWITCHMOVEMODE, 0)
        self._RegistApi(SPORT_API_ID_VISIONWALK, 0)
        self._RegistApi(SPORT_API_ID_HANDSTAND, 0)
        self._RegistApi(SPORT_API_ID_AUTORECOVERY_SET, 0)
        self._RegistApi(SPORT_API_ID_FREEWALK, 0)
        self._RegistApi(SPORT_API_ID_CLASSICWALK, 0)
        self._RegistApi(SPORT_API_ID_FASTWALK, 0)
        self._RegistApi(SPORT_API_ID_FREEEULER, 0)


    # 1001
    def Damp(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_DAMP, parameter)
        return code

    # 1002
    def BalanceStand(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_BALANCESTAND, parameter)
        return code

    # 1003
    def StopMove(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_STOPMOVE, parameter)
        return code

    # 1004
    def StandUp(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_STANDUP, parameter)
        return code

    # 1005
    def StandDown(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_STANDDOWN, parameter)
        return code

    # 1006
    def RecoveryStand(self):
        p = {}
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_RECOVERYSTAND, parameter)
        return code

    # 1008
    def Move(self, vx: float, vy: float, vyaw: float):
        p = {}
        p["x"] = vx
        p["y"] = vy
        p["z"] = vyaw
        parameter = json.dumps(p)
        code = self._CallNoReply(SPORT_API_ID_MOVE, parameter)
        return code

    # 1011
    def SwitchGait(self, t: int):
        p = {}
        p["data"] = t
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_SWITCHGAIT, parameter)
        return code

    # 1013
    def BodyHeight(self, height: float):
        p = {}
        p["data"] = height
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_BODYHEIGHT, parameter)
        return code

    # 1015
    def SpeedLevel(self, level: int):
        p = {}
        p["data"] = level
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_SPEEDLEVEL, parameter)
        return code

    # 1018
    def TrajectoryFollow(self, path: list):
        l = len(path)
        if l != SPORT_PATH_POINT_SIZE:
            return SPORT_ERR_CLIENT_POINT_PATH

        path_p = []
        for i in range(l):
            point = path[i]
            p = {}
            p["t_from_start"] = point.timeFromStart
            p["x"] = point.x
            p["y"] = point.y
            p["yaw"] = point.yaw
            p["vx"] = point.vx
            p["vy"] = point.vy
            p["vyaw"] = point.vyaw
            path_p.append(p)

        parameter = json.dumps(path_p)
        code = self._CallNoReply(SPORT_API_ID_TRAJECTORYFOLLOW, parameter)
        return code

    # 1019
    def ContinuousGait(self, flag: int):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_CONTINUOUSGAIT, parameter)
        return code

    # 1036
    def MoveToPos(self, x: float, y: float, yaw: float):
        p = {}
        p["x"] = x
        p["y"] = y
        p["yaw"] = yaw
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_MOVETOPOS, parameter)
        return code
    
    # 1038
    def SwitchMoveMode(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_SWITCHMOVEMODE, parameter)
        return code
    # 1101
    def VisionWalk(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_VISIONWALK, parameter)
        return code
    # 1039
    def HandStand(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_HANDSTAND, parameter)
        return code
    # 1040
    def AutoRecoverySet(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_AUTORECOVERY_SET, parameter)
        return code
    # 1045
    def FreeWalk(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_FREEWALK, parameter)
        return code
    # 1049
    def ClassicWalk(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_CLASSICWALK, parameter)
        return code
    # 1050
    def FastWalk(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_FASTWALK, parameter)
        return code
    # 1051
    def FreeEuler(self, flag: bool):
        p = {}
        p["data"] = flag
        parameter = json.dumps(p)
        code, data = self._Call(SPORT_API_ID_FREEEULER, parameter)
        return code
