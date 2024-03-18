from m5.params import *
from m5.proxy import *
from MemObject import MemObject
from Prefetcher import BasePrefetcher
from Tags import *

class BaseCache(MemObject):
    type = 'BaseCache'
    cxx_header = "mem/cache/base.hh"
    assoc = Param.Int("associativity")
    hit_latency = Param.Cycles("The hit latency for this cache")
    response_latency = Param.Cycles(
            "Additional cache latency for the return path to core on a miss");
    access_latency = Param.Cycles("Time it takes for the CPU to access the cache/Memory")
    max_miss_count = Param.Counter(0,
        "number of misses to handle before calling exit")
    mshrs = Param.Int("number of MSHRs (max outstanding requests)")
    demand_mshr_reserve = Param.Int(1, "mshrs to reserve for demand access")
    size = Param.MemorySize("capacity in bytes")
    forward_snoops = Param.Bool(True,
        "forward snoops from mem side to cpu side")
    is_top_level = Param.Bool(False, "Is this cache at the top level (e.g. L1)")
    tgts_per_mshr = Param.Int("max number of accesses per MSHR")
    two_queue = Param.Bool(False,
        "whether the lifo should have two queue replacement")
    write_buffers = Param.Int(8, "number of write buffers")
    prefetch_on_access = Param.Bool(False,
        "notify the hardware prefetcher on every access (not just misses)")
    prefetcher = Param.BasePrefetcher(NULL,"Prefetcher attached to cache")
    cpu_side = SlavePort("Port on side closer to CPU")
    mem_side = MasterPort("Port on side closer to MEM")
    addr_ranges = VectorParam.AddrRange([AllMemory], "The address range for the CPU-side port")
    system = Param.System(Parent.any, "System we belong to")
    sequential_access = Param.Bool(False,
        "Whether to access tags and data sequentially")
    tags = Param.BaseTags(LRU(), "Tag Store for LRU caches")
