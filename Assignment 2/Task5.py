def smallest_average(person1:dict, person2: dict, person3: dict) -> dict:
    person1_average = (calculate_average(get_scores(person1)), person1)
    person2_average = (calculate_average(get_scores(person2)), person2)
    person3_average = (calculate_average(get_scores(person3)), person3)

    sorted_averages = sorted([person1_average, person2_average, person3_average])
    smallest = sorted_averages[0]
    return smallest[1]

def calculate_average(score_list:list) -> float:
    result = 0
    for score in score_list:
        result += score
    return result/len(score_list)

def get_scores(person:dict) -> list:
    return [person["result1"], person["result2"], person["result3"]]

def main() -> None:
    person1 = {
        "name": "John",
        "result1": 9,
        "result2": 6,
        "result3": 3
    }
    person2 = {
        "name": "Mike",
        "result1": 4,
        "result2": 0,
        "result3": 7
    }
    person3 = {
        "name": "Peter",
        "result1": 9,
        "result2": 0,
        "result3": 5
    }
    print(smallest_average(person2, person1, person3))

if __name__ == '__main__':
    main()