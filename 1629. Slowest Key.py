class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        slowKey=keysPressed[0]
        relTime=releaseTimes[0]
        keys='abcdefghijklmnopqrstuvwxyz'
        for i in range(1,len(keysPressed)):
            if(releaseTimes[i]-releaseTimes[i-1]>relTime):
                slowKey=keysPressed[i]
                relTime=releaseTimes[i]-releaseTimes[i-1]
            
            elif (releaseTimes[i]-releaseTimes[i-1]==relTime and keys.index(keysPressed[i])>keys.index(slowKey)):
                slowKey=keysPressed[i]
        
        return slowKey