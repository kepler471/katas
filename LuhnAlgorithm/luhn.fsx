let validate (str: string) =
    let transform x = if 2 * x > 9 then (2*x) - 9 else 2*x

    let rec everyOther items =
        match items with
        | a :: b :: c -> a :: transform b :: everyOther c
        | [ z ] -> [ z ]
        | [] -> []

    [for i in str.Replace(" ", "") -> i |> string |> int]
    |> List.rev
    |> everyOther
    |> List.sum
    |> fun sum -> sum % 10 = 0

let validate2 (str: string) =
    let rec everyOther transform items =
        match items with
        | a :: b :: c -> a :: transform b :: everyOther transform c
        | [ z ] -> [ z ]
        | [] -> []

    [for i in str.Replace(" ", "") -> i |> string |> int]
    |> List.rev
    |> everyOther (function x when 2 * x > 9 -> 2 * x - 9 | x -> 2 * x)
    |> List.sum
    |> fun sum -> sum % 10 = 0

    //|> everyOther (fun x -> if 2 * x > 9 then (2 * x) - 9 else 2 * x)

let validate3 (str: string) =
    let rec everyOther  items =
        match items with
        | a::b::c -> a :: (function 9 -> 9 | y -> 2 * y % 9) b :: everyOther  c
        | _ -> items

    [for i in str.Replace(" ", "") -> i |> string |> int]
    |> List.rev |> everyOther |> List.sum |> fun sum -> sum % 10 = 0

let python (str: string) =

    // This version returns only the required elements
    let rec everyOther items =
        match items with
        | _ :: b :: c -> b :: everyOther c
        | _ -> []

    [for i in str.Replace(" ", "") -> i |> string |> int]
    |> List.rev
    // Have separate lists: ( a, b )
    |> fun d -> everyOther d, d.Head :: everyOther d.Tail
    |> fun x -> snd x @ (List.map (function 9 -> 9 | y -> 2 * y % 9) (fst x))
    |> List.sum |> fun sum -> sum % 10 = 0


let valTest (str:string) =
    //let transform x = if 2 * x > 9 then (2*x) - 9 else 2*x
    let transform x =
        //match x with
        | 2 * x > 9 -> 2 * x - 9
        | 2*x

    let rec everyOther list =
        match list with
        | a::b::c -> a :: transform b :: everyOther c
        | [last] -> [last]
        //| a::b::[] -> a :: [b]
        //| _::e::[] ->  everyOther [e]
        | [] -> []

    let ans =
        [for i in str.Replace(" ", "") -> i |> string |> int]
        |> everyOther
    ans, [for i in str.Replace(" ", "")->i|>string|>int]
valTest "6466 2631 57527"
valTest "6466 2631 5752"
valTest "6466 2"
valTest "7737  6212  43880"



let validate2 (str:string) =
    let rec valRevAcc xs acc =
        match xs with
        | [] -> acc
        | h::t -> valRevAcc t (h::acc)

    let valRev xs =
        match xs with
        | [] -> xs
        | [_] -> xs
        | h1::h2::t -> valRevAcc t [h2;h1]

    let transform (x: int) = if 2 * x > 9 then x - 9 else x

    let rec everyOther list =
        match list with
        | a::b::c -> a ::  transform b :: everyOther c
        | _ -> []


    //str |> Seq.toList |> List.map string |> List.map int |> List.sum = 10
    [for i in str -> i |> string |> int]
    |> List.rev |> everyOther |> List.sum |> fun sum -> sum % 10 = 0


let rec revAcc xs acc =
   match xs with
   | [] -> acc
   | h::t -> revAcc t (h::acc)

let rev xs =
   match xs with
   | [] -> xs
   | [_] -> xs
   | h1::h2::t -> revAcc t [h2;h1]

let rec everyOtherButLast list =
    match list with
    | a::b::[] -> a :: [b]
    | a::b::c -> a :: 2*b :: everyOtherButLast c
    | _ -> []
