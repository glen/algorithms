# Implementation of Linear Search

[Linear Search Algorithm](#linear-search-algorithm)
 - [Example](#example)

[Installation](#installation)
 - [Pre-requisites](#prerequisites)
 - [Installation Process](#installation-process)
[Running the code](#running-the-code)
[Tests](#tests)

## Linear Search Algorithm

This is an implementation of [Linear Search Algorithm](https://guides.github.com/features/mastering-markdown/). The Algorithm goes like this

1. Start from the leftmost element of arrary[] and one by one compare x with each element of array[]
2. If x matches with an element, return the index.
3. If x doesn’t match with any of elements, return -1 (No).

# Example

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
1. Ensure that you have a ruby version manager present ([*rvm*](https://rvm.io/) or [*rbenv*](https://github.com/rbenv/rbenv)).

# Installation
1. Install ruby.
2. Install bundler through `gem install bundler`
3. Do `bundle install` - which will install all gems and dependencies.

## Running the code
1. Go ahead and just `ruby app.rb 5` in the terminal or use `./bin/run 5`
2. You will get an error complaining of `input.json` not found - but don't worry an `input.json` will be created and put in `config/input.json`.
3. The `config/input.json` has the data that is being used as input for the linear search code. Fill it in with random numbers.
4. Try it again `ruby app.rb 5` ( `./bin/run 5` ).
5. Based on the numbers present in the `input.json` file - you will either get the index of the number if located or `-1`.

# Tests
Run `bundle exec rspec` which will run the rspecs located under `spec` folder and give a coverage report.
