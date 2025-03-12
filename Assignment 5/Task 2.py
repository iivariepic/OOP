class ListHelper:
    @staticmethod
    def greatest_frequency(my_list: list):
        return max(my_list, key=my_list.count)

    @staticmethod
    def doubles(my_list: list):
        single_items:list = []
        doubled_items:list = []

        for item in my_list:
            if item not in single_items and item not in doubled_items:
                single_items.append(item)
            elif item in doubled_items:
                continue
            else:
                doubled_items.append(item)

        return len(doubled_items)

def main():
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))

if __name__ == '__main__':
    main()