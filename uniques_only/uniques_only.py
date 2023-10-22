from collections.abc import Iterable


def uniques_only(seq: Iterable) -> Iterable:
    to_eval = False
    try:
        result = dict.fromkeys(seq)
    except TypeError:
        to_eval = True
        result = dict.fromkeys([str(x) for x in seq])
    for key in result.keys():
        if to_eval:
            yield eval(key)
        else:
            yield key


if __name__ == "__main__":
    sample = [1, 2, 2, 1, 1, 3, 2, 1]
    sample_res = uniques_only(sample)
    print(f"sample_res: {list(sample_res)}")
    # print(f"sample_res: {next(sample_res)}")
    # print(f"sample_res: {next(sample_res)}")
    # print(f"sample_res: {next(sample_res)}")
    # print(f"sample_res: {next(sample_res)}")
    nums = [1, -3, 2, 3, -1]
    squares = (n**2 for n in nums)
    res_squares = uniques_only(squares)
    print(f"res_squares: {list(res_squares)}")
    list_of_lists = [["a", "b"], ["a", "c"], ["a", "b"]]
    list_of_lists_res = uniques_only(list_of_lists)
    print(f"list_of_lists_res: {list(list_of_lists_res)}")
    # [['a', 'b'], ['a', 'c']]
    nums_iter = iter([1, 2, 3])
    output = uniques_only(nums_iter)
    assert iter(output) == iter(output)
    assert next(output) == 1
    # The below line tests that the incoming generator isn't exhausted.
    # It may look odd to test the nums input, but this is correct
    # because after 1 item has been consumed from the uniques_only
    # iterator, nums should only have 1 item consumed as well
    try:
        assert next(nums_iter) == 2
    except StopIteration:
        print("The incoming nums iterator was fully consumed!")
