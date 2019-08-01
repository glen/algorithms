# Implementation of Binary Search

[Binary Search Algorithm](#linear-search-algorithm)
 - [Example](#example)

[Installation](#installation)
 - [Pre-requisites](#prerequisites)
 - [Installation Process](#installation-process)
[Running the code](#running-the-code)
[Tests](#tests)

## Binary Search Algorithm

This is an implementation of [Binary Search Algorithm](https://en.wikipedia.org/wiki/Binary_search_algorithm). The Algorithm goes like this

1. Sort the array
2. Compare the target value to the middle element of the array.
3. If not equal, the half in which the target cannot lie is eliminated.
4. Repeat Steps 2 and 3 until the target value is found or the array is empty.

# Example

Element present in  array
```
Input: 	          [1, 2, 3, 4, 5, 6, 7, 8, 9]
Number to Search: 3
Located:          Yes
Iterations:       2
```
Element _not_ present in  array
```
Input: 	          [1, 2, 3, 4, 5, 6, 7, 8, 9]
Number to Search: 11
Located:          No
Iterations:       4
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
