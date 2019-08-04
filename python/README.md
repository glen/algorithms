# Implementation of Linear Search

[Algorithms](#algorithms)
  - [Linear Search Algorithm](#linear-search-algorithm)
    - [Example](#example)

[Installation](#installation)
 - [Pre-requisites](#prerequisites)
 - [Installation Process](#installation-process)
[Running the code](#running-the-code)
[Tests](#tests)

# Algorithms

## Linear Search Algorithm

This is an implementation of [Linear Search Algorithm](https://guides.github.com/features/mastering-markdown/). The Algorithm goes like this

1. Start from the leftmost element of arrary[] and one by one compare x with each element of array[]
2. If x matches with an element, return the index.
3. If x doesn’t match with any of elements, return -1 (No).

### Example

Element present in  array
```
Input: 	          [4, 6, 2, 5, 3, 7]
Number to Search: 5
Located:          Yes
Iterations:       4
```
Element _not_ present in  array
```
Input: 	          [4, 6, 2, 5, 3, 7]
Number to Search: 11
Located:          No
Iterations:       6
```

## Installation

# Prerequisites
1. Ensure that you have a python version manager present ([*pyenv*](https://github.com/pyenv/pyenv)).

# Installation
1. Install python.
2. Install the required packages in *requirements.txt* through `pip install -r requirements.txt`
3. You all set!

## Configuration
1. Update the data present in the file *input.json*

## Running the code
1. Go ahead and just `python [algorithm] [input]` in the terminal.
For example `python linear_search.py 5`
2. Based on the numbers present in the `input.json` file - you will either get the index of the number if located or `No`.

# Tests
