# Changelog

All notable changes to this project are documented in this file.


## Version 0.0.1 — November 20, 2025
### Added
- Selected project topic: **Budget Tracker**
- Defined target users (students, dormers, and scholars)
- Identified the problem of managing allowance and expenses
- Created initial proposal draft and discussed planned features


## Version 0.1.0 — December 4, 2025
### Added
- Created GitHub repository
- Uploaded starter project files
- Implemented initial version of `budget_tracker.py`
- Added expense input and category system
- Implemented basic input validation for blank inputs and negative values
- Created initial README documentation

### Changed
- Improved code readability and added comments


## Version 1.0.0 — December 5, 2025
### Added
- Monthly budget tracking
- Remaining budget calculation
- Daily, weekly, and monthly expense summaries
- Improved error handling for invalid numeric inputs
- Organized repository structure

### Fixed
- Program crash when non-numeric values were entered
- Incorrect budget calculations caused by negative inputs

### Documentation
- Completed README file
- Added project documentation
- Added project journal entries
- Prepared project files for submission


## Version 1.1.0 — March 2026
### Added
- **Savings Tracker feature**
- Ability to set a savings goal
- Savings progress monitoring
- Menu-based navigation system
- Improved console UI with headers and organized output

### Improved
- Clearer prompts and user guidance
- More structured summaries for better readability
- Better error handling and input validation

### Fixed
- Navigation issues when selecting program options
- Incorrect calculations when savings and expenses were both updated

### Documentation
- Updated README and documentation files
- Added user guide and methodology section
- Updated project structure in GitHub repository

  ## Version 1.2.0 — March 21, 2026 (Major Feature Update)

### Added
- On-the-spot calculation feature (e.g., users can input "1400*4")
- Budget top-up feature (add additional allowance)
- Editable savings goal
- Exit option within each feature ("exit" command)
- Strict text-only validation for expense categories

### Improved
- Menu-based navigation with feature-level control
- Loop-based input validation (prevents returning to menu immediately)
- User experience improved through retry prompts
- Cleaner and more structured summary display

### Fixed
- Negative values being accepted in expenses and savings
- Program returning to menu immediately after invalid input
- Incorrect handling when budget is depleted

### Notes
- Program now prevents adding expenses or savings when budget is fully used
- System behaves more like an interactive application rather than a linear program
