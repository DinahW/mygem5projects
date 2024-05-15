#include "learning_gem5/part2/photonic_accel_object.hh"
#include "base/event.hh"
#include <iostream>
#include <vector>
#include <cmath>

using namespace gem5;
{
PhotonicAccelObject::PhotonicAccelObject(const PhotonicAccelObjectParams &params) :
    SimObject(params),
    event1([this] { processDacEvent1(); }, name() + ".event1"),
    event2([this] { processDataEvent2(); }, name() + ".event2"),
    event3([this] { processAdcEvent3(); }, name() + ".event3"),
    duration_of_event1(0),
    duration_of_event2(0),
    duration_of_event3(0),

    bandwidth(params.bandwidth),
    delays(params.delays),
    responseTime(params.response_time),
    powerConsumption(params.power_consumption),
    jitter(params.jitter),
    signalLoss(params.signal_loss),
    conversionEfficiency(params.conversion_efficiency),
    bitNumber(params.bit_number),
    carrierFrequency(params.carrier_frequency),
    responsivity(params.responsivity),
    conversionTime(params.conversionTime)
  
}

void PhotonicAccelObject::startup() 
{
    DPRINTF(PhotonicSimObjectFlag, "%s: Hello Worlds! From a SimObject (startup).\n", __func__);

    // Schedule event1 immediately
    schedule(event1, curTick());

    // Schedule event2 after event1
    if (event1.scheduled()) {
        schedule(event2, event1.when() + duration_of_event1);
    } else {
        warn("Event 1 not scheduled yet.");
    }

    // Schedule event3 after event2
    if (event2.scheduled()) {
        schedule(event3, event2.when() + duration_of_event2);
    } else {
        warn("Event 2 not scheduled yet.");
    }
}

void PhotonicAccelObject::processDacEvent1() 
{
    Tick startTime = curTick();

    // Digital-to-Analog Conversion logic
    std::vector<int> digitalData = {0, 1, 2, 3, 4, 5, 6, 7}; // Example digital data
    double voltageRange = 5.0; // Voltage range of the analog signal (e.g., 0 to 5 volts)
    int resolution = 3; // Resolution (number of bits)
    double stepSize = voltageRange / (pow(2, resolution) - 1); // Calculate the step size

    // Perform Digital-to-Analog Conversion
    std::vector<double> analogSignal;
    for (int digitalValue : digitalData) {
        double analogVoltage = digitalValue * stepSize; // Calculate analog voltage
        analogSignal.push_back(analogVoltage);
    }

    // Output the analog signal
    std::cout << "Digital-to-Analog Conversion Result:" << std::endl;
    for (double voltage : analogSignal) {
        std::cout << voltage << " volts" << std::endl;
    }

    Tick endTime = curTick();
    Tick duration = endTime - startTime;
    DPRINTF(AcceleratorObjectFlag, "Event 1 (DigitalToAnalog conversion) took %d cycles to complete.\n", duration);
}

void PhotonicAccelObject::processDataEvent2() 
{
    Tick startTime = curTick();

    // Data Processing logic
    std::cout << "Data Processing Event" << std::endl;
    // Add your data processing logic here

    Tick endTime = curTick();
    Tick duration = endTime - startTime;
    DPRINTF(AcceleratorObjectFlag, "Event 2 (ProcessData) took %d cycles to complete.\n", duration);
}

void PhotonicAccelObject::processAdcEvent3() 
{
    Tick startTime = curTick();

    // Analog-to-Digital Conversion logic
    std::vector<double> analogSignal = {0.0, 1.0, 2.5, 4.0, 5.0}; // Example analog signal (voltage levels)
    double voltageRange = 5.0; // Voltage range of the analog signal (e.g., 0 to 5 volts)
    int numBits = 3; // Number of bits for digital representation
    double stepSize = voltageRange / (pow(2, numBits) - 1); // Calculate the step size

    // Perform Analog-to-Digital Conversion
    std::vector<int> digitalData;
    for (double analogVoltage : analogSignal) {
        int digitalValue = static_cast<int>(analogVoltage / stepSize); // Calculate digital value
        digitalData.push_back(digitalValue);
    }

    // Output the digital data
    std::cout << "Analog-to-Digital Conversion Result:" << std::endl;
    for (int digitalValue : digitalData) {
        std::cout << digitalValue << std::endl;
    }

    Tick endTime = curTick();
    Tick duration = endTime - startTime;
    DPRINTF(AcceleratorObjectFlag, "Event 3 (AnalogToDigital conversion) took %d cycles to complete.\n", duration);
}
