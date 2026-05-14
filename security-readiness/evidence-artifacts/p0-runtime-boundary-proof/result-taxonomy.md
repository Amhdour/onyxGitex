# P0 Result Taxonomy

## Status values
- **PASSED**: command executed, assertions reached, expected behavior observed.
- **FAILED_ASSERTION**: command executed, assertions reached, security assertion failed.
- **FAILED_TEST_RUNTIME**: command executed and collected, failed due to runtime exception after collection.
- **BLOCKED_IMPORT_DEPENDENCY**: blocked by missing Python dependency.
- **BLOCKED_TEST_COLLECTION**: pytest collection blocked by conftest/import/discovery/config/syntax issue.
- **BLOCKED_ENVIRONMENT**: missing required environment/service/dependency runtime.
- **BLOCKED_COMMAND_MISSING**: no executable command exists.
- **NOT_EXECUTED**: control was not attempted.

## Evidence levels
LOCAL_HARNESS, LOCAL_RUNTIME, CI_RUNTIME, STAGING_RUNTIME, PRODUCTION_RUNTIME, BLOCKED_NO_RUNTIME, BLOCKED_IMPORT_DEPENDENCY, BLOCKED_TEST_COLLECTION.

## Rules
Import/collection/dependency blockers are not security-control failures.
A failed assertion is only valid if assertions were reached.
Local harness/runtime evidence is not staging/production evidence.
