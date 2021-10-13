# class for wait code
import time

from simtypes import SimResponse, smsStatus

class WaitCode:
    def __init__(self, py5sim_class, timeout: int = 90, repeat_time: int = 5):
        # timeout - sec. | max code wait time.
        # repeat_time - sec. | timeout between requests.
        self.STATUS = smsStatus()
        self.api = py5sim_class
        self.timeout = timeout
        self.repeat_time = repeat_time
        
    def wait(self, sms: SimResponse):
        for i in range(self.timeout // self.repeat_time):
            res = self.api.sms.getStatus(id = sms.id)
            if res.status == self.STATUS.OK:
                break
            else:
                print(i, res)
                time.sleep(self.repeat_time)
        return res
            
        