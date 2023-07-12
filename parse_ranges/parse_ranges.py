import re
from collections import namedtuple
from collections.abc import Generator


def parse_ranges(data: str) -> Generator:
    if not isinstance(data, str):
        raise TypeError

    StartStop = namedtuple("StartStop", ["start", "stop"], defaults=[-1])
    # up to Bonus 2
    # ranges = [
    # StartStop(*[int(x) for x in r.split("-")])
    # for d in data.split(",")
    # for r in d.split()
    # ]

    # Bonus 3
    ranges = []
    for d in data.split(","):
        for r in d.split():
            # spot '->'
            if re.search(r"(->)\w+", r):
                number = re.match(r"(\d+)", r).group()
                ranges.append(StartStop(int(number)))
            else:
                ranges.append(StartStop(*[int(x) for x in r.split("-")]))

    for out_range in sorted(ranges, key=lambda x: x.start):
        if out_range.stop < 0:
            yield out_range.start
            continue

        if out_range.start > out_range.stop:
            raise ValueError
        out = out_range.start
        while out <= out_range.stop:
            yield out
            out += 1


print(list(parse_ranges("1-2,4-4,8-13")))
print(list(parse_ranges("0-0, 4-8, 20-20, 43-45")))

numbers = parse_ranges("100-10000")
print(next(numbers))
print(next(numbers))

print(list(parse_ranges("0,4-8,20,43-45")))
print(list(parse_ranges("0, 4-8, 20->exit, 43-45")))
