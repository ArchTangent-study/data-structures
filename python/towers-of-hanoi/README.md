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

## Big Picture

A breakdown of the major steps in the algorithm (using 5 discs):

```
     SRC          TGT          AUX

     =1=  
    ==2==  
   ===3===  
  ====4====  
 =====5=====  
                               

                               =1=
                              ==2==
                             ===3===
              =====5=====   ====4====   topmost n-1 discs from src to aux, bottom to tgt



     =1=
    ==2==      ====4====
   ===3===    =====5=====               topmost n-1 discs from aux to src, bottom to tgt



                ===3===  
               ====4====       =1=
              =====5=====     ==2==     topmost n-1 discs from src to aux, bottom to tgt


                 ==2==
                ===3===
               ====4====
     =1=      =====5=====               topmost n-1 discs from src to aux, bottom to tgt

                  =1=  
                 ==2==
                ===3===
               ====4====
              =====5=====               topmost n-1 discs from aux to src, bottom to tgt

     SRC          TGT          AUX
```
The order of the discs moved (with 4 discs):
```
      n-1       n
-----------------
121312141213121 5
    1213121     4
      121       3
       1        2
                1
```
## Approaches

### Recursive

Some patterns emerge from the above diagrams:
- There is *symmetry* in the order of discs moved
- The topmost `n-1` disks *alternate* between `src` and `aux` stacks
- For odd numbers of `n`: start by moving topmost disc stack from `src` to `tgt`
- For even numbers of `n`: start by moving topmost disc stack from `aux` to `src`

The symmetric parts indicate that *recursion* would be an ideal strategy, with the *base case* occurring when `n=1`.
