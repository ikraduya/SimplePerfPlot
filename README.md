# SimplePerfPlot (spp)

## What problem to solve?
- Problem of manually / semi-manually record performance of parallel algorithm, store to tabular file, and display it

## Usage?
- Used by self to time and plot parallel algorithm running on HPC server

## Functionalities
- MVP
    - Read output from file
    - Fill tabular file with matching pattern using regex (one regex per column)
    - Visualize line graph (x=cores/tasks, y=time)
    - Use config file for tabular setting (research for the best config file, possibly json)
	
## Form
- ~~Shell script?~~
    - \+ highly portable, might also be ported to windows (won't likely)
    - \= HPC didn't need portability (but maybe portability across HPC facility)
    - \-  Quite hard to make & debug (need to learn more about unix cmd tools)
    - \- Visualization still need another tools
- **_Python script_**
    - \? What python? 2 or 3? Might be 3
    - \+ Visualization is easy (just use a popular & easy to use library)
    - \- Python and library dependency (eased by using python pip)
    - \- Need to learn how to create python library and post to pypip
    - \+ Possibility for better functionality improvement is easier(e.g., GUI, regex matcher viz.)
- ~~Binary?~~
    - \- Hardly portable
    - \+ Visualization is possible
    - \+ The most performing option
    - \- Might be hard to make and improve

## Development Phases
- MVP
    - Time a basic MPI program with varying cores
    - Time a basic OpenMP program with varying tasks
    - Time a basic MPI + OpenMP program with varying cores and tasks
- Zero version
    - This is where major functions, refactoring, and rewriting happens as needed by me
- Major update
    - This is after the project is stable (without many major changes needed to happen)
