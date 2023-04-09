## Genetic Experiments
Objective is to find the solution to the NP-hard Travelling Salesperson Problem as close to the actual solution as possible.

Employed Genetic Algorithm to breed generations of individuals and following the "survival of the fittest" policy to arrive at a very good approximate answer to the original problem.

### How to run?
**requirements.txt** => contains the necessary python libraries to run the project
**main.py** => main file with the evolution loop and plots
**env.py** => to generate city map and evolve generations
**person.py** => individual class with cross-breeding functionality
**constants.py** => contains run parameters which can be tinkered with

```
$> pip install -r requirements.txt
```
This will install the necessary python libraries to run the project

```
$> python main.py
```
This will run the project. First it will generate a city map using **env.py** and find the shortest path through every city by cross-breeding generations of populations. The visualization is handled by the **main.py** file.

