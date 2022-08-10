"""
第一段輸入正整數N, 後面給輸入N行 數組(包含兩個ID, 表示他們為夫妻),
3
11111 22222
33333 44444
55555 66666
第二段輸入正整數M, 後面輸入M 個ID
7
55555 44444 10000 88888 22222 11111 23333
結果：
印出參與party的ID, 有哪些不是夫妻同時參與
5
10000 23333 44444 55555 88888
"""


class Solution:
    def __init__(self) -> None:
        self.couples = dict()
        self.participants = set()

    def __is_duplicate(self, couple: list) -> bool:
        return len(set(couple)) <= 1

    def __is_invalid_id(self, id: str) -> bool:
        return id in self.couples.keys() or id in self.couples.values()

    def set_couples(self, couple_count: int) -> None:
        for _ in range(couple_count):
            couple = input("請輸入夫妻 / 伴侶編號: ").split(" ")

            # input verification
            if self.__is_duplicate(couple):
                exit("duplicate id")
            elif len(couple) != 2:
                exit(f"it's not couple, len should be 2: {len(couple)}")
            for id in couple:
                if self.__is_invalid_id(id):
                    exit("duplicate id in another couple")

            self.couples[couple[0]] = couple[1]

    def set_participants(self, participant_count: int) -> None:
        for p in input(f"請輸入所有與會者編號: ").split(" "):
            self.participants.add(p)

        # input verification
        if len(self.participants) != participant_count:
            exit(
                f"input count: {len(self.participants)} != participant_count: {participant_count}"
            )

    def find_single(self) -> None:
        mate = ""
        single_list = list()

        for participant in self.participants.copy():
            if participant in self.couples.keys():
                mate = self.couples[participant]
            elif participant in self.couples.values():
                mate = list(self.couples.keys())[
                    list(self.couples.values()).index(participant)
                ]
            else:
                single_list.append(participant)
                continue

            if mate:
                if mate not in self.participants:
                    single_list.append(participant)

        print(f"{len(single_list)}")
        print(", ".join(single_list))


def main():
    solution = Solution()
    solution.set_couples(int(input("請輸入夫妻 / 伴侶數量: ")))
    solution.set_participants(int(input("請輸入參與人數: ")))
    solution.find_single()


if __name__ == "__main__":
    main()
