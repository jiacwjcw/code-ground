class Solution:
    def __init__(self) -> None:
        self.tree_count = 0
        self.flower_count = 0

    def __plant_tree(self, flowerbed, index=0):
        if index >= len(flowerbed):
            return

        if flowerbed[index] == 1:
            return self.__plant_tree(flowerbed, index + 2)

        if flowerbed[index] == 2:
            return self.__plant_tree(flowerbed, index + 1)

        if (index + 1 < len(flowerbed)) and flowerbed[index + 1] == 1:
            return self.__plant_tree(flowerbed, index + 3)

        if flowerbed[index] == 0:
            flowerbed[index] = 1
            self.tree_count += 1
            return self.__plant_tree(flowerbed, index + 2)

    def __plant_flower(self, flowerbed, index=0):
        if index >= len(flowerbed):
            return

        if flowerbed[index] == 1 or flowerbed[index] == 2:
            return self.__plant_flower(flowerbed, index + 1)

        # 0220X
        if ((index + 2 < len(flowerbed)) and flowerbed[index + 2] == 2) and (
            (index + 1 < len(flowerbed)) and flowerbed[index + 1] == 2
        ):
            return self.__plant_flower(flowerbed, index + 4)
        # 220X
        if ((index - 2 >= 0) and flowerbed[index - 2] == 2) and (
            (index - 1 >= 0) and flowerbed[index - 1] == 2
        ):
            return self.__plant_flower(flowerbed, index + 1)
        # 202X
        if ((index + 1 < len(flowerbed)) and flowerbed[index + 1] == 2) and (
            (index - 1 >= 0) and flowerbed[index - 1] == 2
        ):
            return self.__plant_flower(flowerbed, index + 2)

        if flowerbed[index] == 0:
            flowerbed[index] = 2
            self.flower_count += 1
            return self.__plant_flower(flowerbed, index + 1)

    def can_place(self, flowerbeds: list[int]):
        results = []
        for flowerbed in flowerbeds:
            self.tree_count = 0
            self.flower_count = 0
            self.__plant_flower(flowerbed)
            self.__plant_tree(flowerbed)
            results.append([self.tree_count, self.flower_count])
        return results


def test():
    assert Solution().can_place([[0, 1, 0, 0, 0]]) == [[1, 3]]
    assert Solution().can_place([[0, 0, 0, 0, 0]]) == [[1, 4]]
    assert Solution().can_place([[2, 2, 0, 2, 0]]) == [[1, 1]]
    assert Solution().can_place([[2, 2, 0, 1, 2, 2, 1]]) == [[0, 0]]
    assert Solution().can_place([[0]]) == [[0, 1]]
    assert Solution().can_place([[0, 2, 2, 1, 0, 0, 1, 0, 0, 2, 2]]) == [[2, 3]]
    assert Solution().can_place([[1, 0, 0, 1, 0]]) == [[0, 3]]

    assert Solution().can_place(
        [[0, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 2, 2, 1, 0, 0, 1, 0, 0, 2, 2]]
    ) == [[1, 3], [1, 4], [2, 3]]
