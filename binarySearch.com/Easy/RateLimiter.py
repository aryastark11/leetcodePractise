class RateLimiter:
    def __init__(self, expire):
        self.rateExpireInterval = expire
        self.uidMap = {}
        return None

    def limit(self, uid, timestamp):
        # first time limit is invoked for userId
        # if expire = 0
        if not self.rateExpireInterval:
            return False

        if uid not in list(self.uidMap.keys()):
            # Add the last expire time to the dict as value
            self.uidMap.update({
                uid: timestamp})
            return False
        else:
            #expire=5, last request 15, now it is 16.
            # 16-5 = 11 , last =15 --> should fail --> return True
            if self.uidMap[uid] > timestamp-self.rateExpireInterval:
                return True
            else:
                self.uidMap.update(
                    {uid: timestamp})
                return False

## optimised solution
class RateLimiter:
    def __init__(self, expire):
        self.expire = expire
        self.lastCall = defaultdict(lambda: -1)

    def limit(self, uid, timestamp):
        last = self.lastCall[uid]
        # if new timestamp coming in is greater than LastOne + expire interval --> return False
        if last == -1 or last + self.expire <= timestamp:
            self.lastCall[uid] = timestamp
            return False
        return True         
