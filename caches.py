from m5.objects import BaseCache

class L1Cache(BaseCache):
        assoc = 2
        hit_latency = 2
        access_latency = 1
        response_latency = 2
        mshrs = 4
      
       

        def connectCPU(self, cpu):
            # need to define this in a base class!
            raise NotImplementedError

        def connectBus(self, bus):
            self.mem_side = bus.slave

class L1ICache(L1Cache):
        size = '16kB'
        def connectCPU(self,cpu):
            self.cpu_side = cpu.icache_port

class L1DCache(L1Cache):
        size = '64kB'
        def connectCPU(self,cpu):
            self.cpu_side = cpu.dcache_port

class L2Cache(BaseCache):
        size = '256kB'
        assoc = 8
        hit_latency = 20
        access_latency = 4
        response_latency = 20
     

        def connectCPUSideBus(self,bus):
            self.cpu_side = bus.master

        def connectMemSideBus(self,bus):
            self.mem_side = bus.slave
