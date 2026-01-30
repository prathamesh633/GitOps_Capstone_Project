# Capstone Project
 
## Project Purpose
This project demonstrates Git-based configuration management and CI validation
using GitHub Actions to prevent invalid YAML configurations from reaching main
with proper branching stratergies.
 
## Repository Structure
- app/        : Python source code
- config/     : YAML configuration files
- .github/    : CI workflows
 
## Branching Strategy
- No direct commits to main
- All changes via feature branches
- Pull requests required
- CI must pass before merge
 
## CI Workflow
- Runs on push and pull request
- Validates YAML syntax using yamllint
- Acts as a quality gate for main branch
 
## Failure and Recovery
- Introduced invalid YAML to demonstrate CI failure
- Fixed configuration in a separate commit
- Verified successful CI after fix
 