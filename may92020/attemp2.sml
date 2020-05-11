(* This problem was asked by Uber.

   Given an array of integers, return a new array such that each element at index i
   of the new array is the product of all the numbers in the original array except 
   the one at i.
   For example, if our input was [1, 2, 3, 4, 5], the expected output would be     
   [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
   [2, 3, 6].

   Follow-up: what if you can't use division?

   alg laws: [cons x xs] == [x1 * x2 * ... * xn, x1 * x3 * ... * xn, ... , x1 * x2 * ... * xn-1]
             [x, y ,z]   == [y*z, x*z, x*y]
             [x, y]      == [y, x]
             [x]         == [x]
             []          == []

   example inputs ==> [3, 2, 1] == [2, 3, 6]*)
(*datatype Node = *)


fun multiplyExceptI (x::y::ys) = 
  | multiplyExceptI (x)