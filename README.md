# Project Testing Suite

This repository contains test scripts used for both regression and performance testing of the website [SauceDemo](https://www.saucedemo.com/).

## Files
- **end.py**: The code used for regression testing.
- **p.py**: The code used for performance testing.

## Overview

### Regression Testing (`end.py`)
The `end.py` script performs automated regression tests to ensure that recent changes or updates have not adversely affected existing functionalities.

### Performance Testing (`p.py`)
The `p.py` script conducts performance testing to measure the responsiveness, stability, and scalability of the website under varying load conditions.

## How to Run

1. **Setup Environment:**
   - Install necessary dependencies
     
2. **Running Regression Tests:**
   - Execute the regression tests using:
     ```bash
     python end.py
     ```

3. **Running Performance Tests:**
   - Start the performance tests with:
     ```bash
     locust -f p.py --host https://www.saucedemo.com
     ```

## Notes
- Ensure your environment is properly configured with all necessary dependencies and drivers.
- Review the logs and results after running the tests to identify any issues or areas for improvement.


