class TimeMap:

    def __init__(self):
        self.my_map= dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.my_map:
            self.my_map[key][timestamp]=value
        else:
            self.my_map[key]={timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        res= ""
        if key in self.my_map:
            timestamps = list(self.my_map[key].keys())
            l,r= 0 , len(timestamps)-1
            while l<=r:
                m = (l+r)//2
                if timestamps[m]>timestamp:
                    r=m-1
                else:
                    res=self.my_map[key][timestamps[m]]
                    l=m+1
        return res 
