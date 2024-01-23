from polyomino import FixedPolyomino


def get_fixed_polyominoes(n: int):
    if n == 0:
        raise Exception("n value should be bigger than zero!")
    if n == 1:
        return {FixedPolyomino(squares=((0, 0),))}

    combinations = set()
    for polyomino in get_fixed_polyominoes(n - 1):
        for new_polyomino in polyomino.increase_order():
            if new_polyomino.length == n:
                combinations.add(new_polyomino)
    return combinations


if __name__ == '__main__':
    pols = get_fixed_polyominoes(n=4)
    print(len(pols))
    for pol in pols:
        print(pol)
