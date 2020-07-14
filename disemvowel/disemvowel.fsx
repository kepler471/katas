let isVowel ch = Set.contains ch (set "aeiouAEIOU")
let disemvowel s =
  s
  |> Seq.filter (not << isVowel)
  |> Seq.map string
  |> String.concat ""