# Actions for Astronomical
## For 1.0.0
- [x] Build CLI with calls to desired functionality (0.1.0)
- [x] Build desired functionality (0.2.0)
  - [x] Sun position and horizon times (0.1.0)
  - [x] Annually cycling alarms (0.1.0)
  - [x] NAC time calculator (0.2.0)
- [ ] Create own model to manage functionality
  - [x] Build basic Physics (0.1.0)
  - [ ] Improve accuracy of model
    - [ ] Investigate possible causes of loss of accuracy
- [ ] Refactor to follow Hexagonal Architecture
  - [x] Sketch out architecture design (0.3.0)
  - [ ] Build "Real World Calculators" module
    - [x] Build Alarms class (0.3.0)
    - [ ] Build Time class
  - [ ] Modify "Service/Requirements" module to provide Abstract Base Classes
  - [ ] Modify cli interface to instantiate "Service/Requirements"
- [ ] Sort out Defaults
  - [ ] (Re-)configure Default config imports
  - [ ] Sort out sensible class defaults
- [ ] Ensure full test coverage
  - [ ] Write Model tests
    - [ ] Custom Types
    - [ ] Physics
    - [x] Celestials (0.1.0)
    - [ ] Location
    - [x] Mechanics (0.1.0)
    - [ ] Real World Calculations
  - [ ] Write Service tests
    - [ ] Configuration
    - [ ] Logging
    - [ ] Requirements
  - [ ] Write Interface tests
    - [ ] CLI
- [ ] Ensure logging coverage
- [ ] Tidy up tasks
  - [ ] Break out `_calculate_latest_vernal_equinox` method from "Real World Calculations module (`Alarms` class)
  - [ ] Break out `_calculate_annual_progress` method from "Real World Calculations module (`Alarms` class)



