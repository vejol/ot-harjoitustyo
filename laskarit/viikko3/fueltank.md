```mermaid
sequenceDiagram
actor user
user->>+machine: Machine()
machine->>tank: FuelTank()
machine->>tank: fill(40)
machine->>engine: Engine(tank)
machine-->>-user: 

user->>+machine: drive()
machine->>+engine: start()
engine->>-tank: consume(5)
machine->>+engine: is_running()
engine-->>-machine: True
machine->>+engine: use_energy()
engine->>-tank: consume(10)
machine-->>-user: 
```