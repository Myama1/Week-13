#ifndef SYSTEM_H
#define SYSTEM_H

#include <vector> //to use standard C++ vectors
// #include "box.h" //yet to be created!
// #include "particle.h" //yet to be created!

class System {

  public:
    System();
    int particleNumber;
    double noiseStrength;
    // Box simulationBox;
    // std::vector<Particle> particles;

    void updateRule();
};

#endif