# Logging
## Strategy
Logging should be woven throughout the application. Log levels supported here are TRACE, DEBUG, INFO, WARNING, ERROR, and CRITICAL.
* **TRACE**:
  * Class instantiations - only done at the most base classes in the model layer to denote the usage of any class
  * Base function invocations - only done on core functions found in the model layer to denote the usage of it
* **DEBUG**:
  * Model class method returns - done in the service layer to highlight the outputs of service class methods
  * Command line tool argument - done in the package script to show which option is being used
* **INFO**:
  * Service class instantiations - highlight key stages in the happy path for a particular option
  * Interface class method returns - to confirm the end of the happy path for a given option
* **WARNING**:
  * Any time there is a "try/except" structure
* **ERROR**:
  * Base functions - capture any unhandled exceptions in the model class
  * Non-trivial service methods - any method in the service layer that does more than just call a base function


## Happy Path Tests
### 0.5.0 - 2022-02-10
Lines of logging (values in brackets include expected output):

| CLI Flag | Control | INFO  | DEBUG   | TRACE         |
|----------|---------|-------|---------|---------------|
| Help     | 8       | 0 (8) | 0 (8)   | 2 (10)        |
| Version  | 1       | 2 (3) | 27 (28) | 11582 (11583) |
| Sun      | 4       | 3 (7) | 29 (33) | 11584 (11588) |
| Alarms   | 4       | 3 (7) | 34 (38) | 11591 (11594) |
| Time     | 3       | 3 (6) | 30 (33) | 11585 (11588) |
