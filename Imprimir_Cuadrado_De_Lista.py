def sqrt_list(list_1):
    return [n ** 2 for n in list_1]

def main():
    list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = sqrt_list(list_1)
    print(result)

if __name__ == "__main__":
    main()