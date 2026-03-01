# Architecture

## Components
- app.py: Streamlit entrypoint and dashboard orchestration
- simulation.py: stochastic simulation engine
- formulas.py: reusable math equations
- optimizer.py: optimal control derivations
- templates/: Jinja layout components

## Data Flow
1. User selects parameters
2. Simulation engine generates paths
3. Optimizer computes controls
4. Dashboard renders charts and tables
