# Towers of Hanoi

My solutions to the `Towers of Hanoi` puzzle, including visualization (via console) and testing (via `pytest`).

## About

A logic/math puzzle which requires the transfer of discs from one rod to another, following a specific set of rules:

- There are three rods: source (`src`), target (`tgt`), and auxiliary (`aux`)
- All discs start on the `src` rod, ordered from smallest to largest (top to bottom)
- Only one disc can be moved at a time
- Discs are moved by pulling the topmost disc from a rod, and placing it through the top of another rod
- A disc can only be moved onto either (1) an empty rod or (2) a larger disc

## Approaches

### Recursive

The cleanest approach I've found so far - recursion seems to be very well suited for this task.  It took some struggling through the *Data Structures & Algorithms Made Easy* explanation to get a good grasp on this method; an iterative approach makes more sense to me, but is *much* less elegant.
