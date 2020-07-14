def likes(names):
    dic = {
        0: lambda x: "no one likes this",
        1: lambda x: f"{x[0]} likes this",
        2: lambda x: f"{x[0]} and {x[1]} like this",
        3: lambda x: f"{x[0]}, {x[1]} and {x[2]} like this",
        4: lambda x: f"{x[0]}, {x[1]} and {str(len(x) - 2)} others like this",
    }
    return dic[len(names) if len(names) < 4 else 4](names)
