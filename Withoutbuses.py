import m5
from m5.objects import *

# Instantiate system
system = System()

# Define clock and voltage domains
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz'
system.clk_domain.voltage_domain = VoltageDomain()

# CPU configuration
system.cpu = TimingSimpleCPU()

# L1 cache configuration
system.cpu.icache = L1Cache()
system.cpu.dcache = L1Cache()

# Setting data access latency for L1 cache
system.cpu.icache.response_latency = 2
system.cpu.dcache.response_latency = 2

# Connect L1 caches directly to L2 cache
system.cpu.icache.connectMemSide(system.l2_cache)
system.cpu.dcache.connectMemSide(system.l2_cache)

# L2 cache configuration
system.l2_cache = L2Cache()

# Setting data access latency for L2 cache
system.cpu.L2cache.response_latency = 8

# Main memory configuration
system.mem_ranges = [AddrRange('512MB')]
system_mem_ctrl_response_latency= 16

# Connect L2 cache directly to main memory
system.l2_cache.connectMemSide(system.mem_ctrl)

# Create process
process = Process()

# Assign the process to the CPU
system.cpu.workload = process
system.cpu.createThreads()

# Set up the simulation
root = Root(full_system=False, system=system)

# Instantiate and run the simulation
m5.instantiate()
exit_event = m5.simulate(1000)
m5.stats.dump()
