# Towers of Hanoi

My solutions to the [Towers of Hanoi]([https://en.wikipedia.org/wiki/Tower_of_Hanoi) puzzle, including step-by-step visualization (via CLI) and testing (via *pytest*).

## Usage / Testing

Due to the usage of [structural pattern matching](https://peps.python.org/pep-0636/), Python 3.10 is required.

`python towers_recursive.py <#discs>` displays solution for specified number of discs.

`pytest python towers_recursive.py` performs testing for the implementation.

## About

A logic/math puzzle which requires the transfer of discs from one rod to another, following a specific set of rules:

- There are three rods: source (`src`), target (`tgt`), and auxiliary (`aux`)
- All discs start on the `src` rod, ordered from smallest to largest (top to bottom)
- Only one disc can be moved at a time
- Discs are moved by pulling the topmost disc from a rod, and placing it through the top of another rod
- A disc can only be moved onto either (1) an empty rod or (2) a larger disc

## Approaches

### Recursive

The cleanest approach I've found so far - recursion seems to be very well suited for this task.  It took some struggling to get a good grasp on this method, the book *Data Structures & Algorithms Made Easy* helped me out.
