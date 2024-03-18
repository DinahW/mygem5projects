# Import necessary values
import m5
from m5.objects import *
from caches import *

# Create the system
system = System()

# Setup the clock and voltage domains
system.clk_domain = SrcClockDomain()
system.clk_domain.clock = '1GHz' 
system.clk_domain.voltage_domain = VoltageDomain()

# Set up the CPU
system.cpu = X86TimingSimpleCPU() 

# Setup the caches

# L1 caches
system.cpu.icache = L1ICache() 
system.cpu.dcache = L1DCache() 

system.cpu.icache_port = system.cpu.icache.cpu_side
system.cpu.dcache_port = system.cpu.dcache.cpu_side

# L2 cache
system.l2bus = L2XBar()
system.cpu.icache.mem_side = system.l2bus.slave
system.cpu.dcache.mem_side = system.l2bus.slave

# Connect L2 cache to CPU
system.l2cache = L2Cache()
system.l2cache.connectCPUSideBus(system.l2bus) 

# Connect main memory (off-chip RAM)
system.membus = SystemXBar()
system.l2cache.connectMemSideBus(system.membus) 

system.mem_mode = 'timing'
system.mem_ranges = [AddrRange('512MB')] 
system.mem_port = system.membus.master 

# Set up the system
system.cpu.createInterruptController()
system.system_port = system.membus.slave

# Create process
process = Process()

# Assign the process to the CPU
system.cpu.workload = process
system.cpu.createThreads()

# Run the simulation
root = Root(full_system=False, system=system)
m5.instantiate()

# Simulate for a specific number of ticks, for example, 1000
exit_event = m5.simulate(1000) 

# Exit the simulation
m5.stats.dump()
