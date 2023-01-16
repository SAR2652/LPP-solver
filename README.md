# LPP-solver
A simple implementation of an LPP solver that minimizes the target function for the given variables and constraints.

## Files and their description

1. ```solution.py``` contains the code for the generalized implementation of an LPP solver for **minimization** problem using the *highs* method. The *simplex* method is generally used to find the solution for an LPP. However, the *highs* method has been used instead of the simplex method because it is faster and more efficient. It has been implemented using the ```linprog``` function within the ```optimize``` submodule of the ```scipy``` library for scientific computing in Python.  

2. ```sample.csv``` contains the example with the values described in CLRS Chapter 29 under the subsection **"A Political Problem"**.
**Note** that this format must be strictly followed for any input file.

3. ```solution.sh``` contains the command to execute the script ```solution.py``` on the given ```sample.csv```. 

4. ```environment.yml``` and ```requirements.txt``` files contain the list of libraries required to execute the code in *anaconda* and *pip* based environments respectively.

## Environment Setup
To load the environment in *anaconda* simply open a terminal and type the following command:
```
conda env create -f environment.yml
```
To install libraries using *pip*, type the following command in a terminal:
```
pip install -r requirements.txt
``` 
## Execution
To execute the code type the following command in a terminal:
```
python solution.py sample.csv
```
OR
```
./solution.sh
```
**Note:** The ```--verbose``` argument can be used to get more details about the processing of input data and intermediate calculations.
