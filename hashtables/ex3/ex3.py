def intersection(arrays):
    count = {}

    # nested loop to access inner arrays
    for array in arrays:
        for num in array:
            # if it's there already increment
            if num in count:
                count[num] += 1
            # if not there, add it
            else:
                count[num] = 1

    # check each item's value. If it has a value equal to how many arrays there were, add it
    result = [item[0] for item in count.items() if item[1] == len(arrays)]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
