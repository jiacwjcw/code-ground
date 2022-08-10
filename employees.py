# [[1,8,[2,3]],[2,-6,[4]],[3,-1,[]],[4,-1,[]]], id = 1, 10
# index=0, 編號
# index=1, 重要度
# index=2, 下屬成員


def get_min_employees(employees: list):
    employees_dict = d = dict()

    for employee in employees:
        employees_dict[employee[0]] = employee

    for id in employees_dict.keys():
        stack = list()
        total_importance = 0

        stack.append(employees_dict[id])

        while stack:
            employee = stack.pop()
            total_importance += employee[1]

            for i in employee[2]:
                stack.append(employees_dict[i])

        d[id] = total_importance

    return [k for k, v in d.items() if v == min(d.values())]


def test():
    assert (
        get_min_employees(
            [
                [1, -10, [2, 3, 4, 5, 6, 7, 8, 9, 10]],
                [2, 0, []],
                [3, 0, []],
                [4, 0, []],
                [5, 0, []],
                [6, 0, []],
                [7, 0, []],
                [8, 0, []],
                [9, 0, []],
                [10, -12, []],
            ]
        )
        == [1]
    )

    assert get_min_employees(
        [[1, 8, [2, 3]], [2, -6, [4]], [3, -1, []], [4, 9, []]]
    ) == [3]
