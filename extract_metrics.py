import m5
from m5.objects import *

def extract_metrics(stats_file):
    # Load statistics from the stats file
    stats = m5.stats.Stats.parse(stats_file)
    
    # Extract  metrics
    sim_seconds = stats.system.simSeconds.value
    sim_ticks = stats.system.simTicks.value
    final_tick = stats.system.finalTick.value
    sim_freq = stats.system.simFreq.value
    host_seconds = stats.system.hostSeconds.value
    host_tick_rate = stats.system.hostTickRate.value
    host_memory = stats.system.hostMemory.value
    sim_insts = stats.system.simInsts.value
    sim_ops = stats.system.simOps.value
    host_inst_rate = stats.system.hostInstRate.value
    host_op_rate = stats.system.hostOpRate.value
    clk_domain_clock = stats.system.clk_domain.clock.value
    voltage_domain_voltage = stats.system.clk_domain.voltage_domain.voltage.value
    
    # Print the extracted metrics
    print("simSeconds: ", sim_seconds)
    print("simTicks: ", sim_ticks)
    print("finalTick: ", final_tick)
    print("simFreq: ", sim_freq)
    print("hostSeconds: ", host_seconds)
    print("HostTickRate: ", host_tick_rate)
    print("hostMemory: ", host_memory)
    print("simInsts: ", sim_insts)
    print("simOps: ", sim_ops)
    print("hostInstRate: ", host_inst_rate)
    print("hostOpRate: ", host_op_rate)
    print("system.clk_domain.clock: ", clk_domain_clock)
    print("system.clk_domain.voltage_domain.voltage: ", voltage_domain_voltage)

if __name__ == "__main__":
 
    stats_file = "m5out/stats.txt"  

    extract_metrics(stats_file)
