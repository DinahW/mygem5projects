from m5.params import *
from m5.proxy import *
from m5.SimObject import SimObject

class PhotonicAccelerator(SimObject):
    type = "PhotonicAccelerator"
    cxx_header = "learning_gem5/part2/photonic_accelerator.hh"
    cxx_class = "gem5::PhotonicAccelerator"
    
    photonic_accelerator_side = ResponsePort("Accelerator side port, receives requests")
   
    mem_side = RequestPort("Memory side port, sends requests")

    latency = Param.Int(0, "Time delay between the input of data into the accelerator and the output of the processed data")
    power_consumption = Param.Float(0.0, "The amount of power consumed by the accelerator during operation measured in watts (W) or milliwatts (mW)")
    expected_throughput = Param.Int(200ops, "The rate at which data can be processed by the accelerator measured in operations per second (ops) or floating-point operations per second (FLOPs)")
    
