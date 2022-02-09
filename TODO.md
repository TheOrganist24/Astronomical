# Actions for Astronomical
## For 1.0.0
- [x] Build CLI with calls to desired functionality (0.1.0)
- [x] Build desired functionality (0.2.0)
  - [x] Sun position and horizon times (0.1.0)
  - [x] Annually cycling alarms (0.1.0)
  - [x] NAC time calculator (0.2.0)
- [x] Create own model to manage functionality (0.1.0)
  - [x] Build basic Physics (0.1.0)
- [x] Refactor to follow Hexagonal Architecture (0.3.0)
  - [x] Sketch out architecture design (0.3.0)
  - [X] Build "Real World Calculators" module (0.3.0)
    - [x] Build Alarms class (0.3.0)
    - [X] Build Time class (0.3.0)
  - [x] Modify "Service/Requirements" module to provide Abstract Base Classes (0.3.0)
  - [x] Modify cli interface to instantiate "Service/Requirements" (0.3.0)
- [x] Sort out Defaults (0.4.0)
  - [x] (Re-)configure Default config imports (0.4.0)
  - [x] Sort out sensible class defaults (0.4.0)
  - [X] Add Requirements to defaults (0.4.0)
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
  - [ ] Remove `earth` and `sun` from Solar System module
  - [ ] Ensure diagram is logically laid out

### Pre-Release Tasks
- [ ] Is code coverage about 95%?
- [ ] Is logging complete?
- [ ] Are all versions correctly set to 1.0.0?
- [ ] Are Docstrings complete?
- [ ] Are the README documentation and diagrams up-to-date and representative?
- [ ] Is there an up-to-date changelog?


## For 2.0.0
- [ ] Create calendar items
- [ ] Improve own model to manage functionality
  - [ ] Investigate possible causes of loss of accuracy

### Pre-Release Tasks
- [ ] Is code coverage about 95%?
- [ ] Is logging complete?
- [ ] Are all versions correctly set to 2.0.0?
- [ ] Are Docstrings complete?
- [ ] Are the README documentation and diagrams up-to-date and representative?
- [ ] Is there an up-to-date changelog?
