(*
Backwards Read Primes are primes that when read backwards in
base 10 (from right to left) are a different prime. (This rules
out primes which are palindromes.)

Examples:
13 17 31 37 71 73 are Backwards Read Primes

13 is such because it's prime and read from right to left writes
31 which is prime too. Same for the others.
Task

Find all Backwards Read Primes between two positive given numbers
(both inclusive), the second one always being greater than or equal
to the first one. The resulting array or the resulting string will
be ordered following the natural order of the prime numbers.
Example

backwardsPrime(2, 100) => [13, 17, 31, 37, 71, 73, 79, 97]
backwardsPrime(9900, 10000) => [9923, 9931, 9941, 9967]
backwardsPrime(501, 599) => []
*)
open System

let isPrimeRec n =
    let rec check i =
        i > n/2 || (n % i <> 0 && check (i + 1))
    check 2

let aSequence primeAlgo n =
    seq {
        for i in [1..n] do
            if primeAlgo i then
                i
    }

// Improve with sqrt limit on search
let isprime n =
  let sqrtlim x = x |> float |> sqrt |> ceil |> int
  let rec check i =
    // printfn "%d" i
    float i > sqrt(float n)  || (n % i <> 0 && check (i + 1))
  check 2


// let rec isPrimeMy n =
//   let root n = 
//     n |> float |> sqrt |> int
//   let tests n = 
//     seq { 3 .. 2 .. root n + 1 }
//     |> Seq.map ( fun x -> n % x <> 0 && isPrimeMy x )
//   tests n


for x in aSequence isprime do
    printfn "%d" x