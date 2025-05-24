class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        size_to_people = defaultdict(list)
        result = []

        for person, size in enumerate(groupSizes):
            size_to_people[size].append(person)
            # Once a group of the correct size is formed, add it to result
            if len(size_to_people[size]) == size:
                result.append(size_to_people[size])
                size_to_people[size] = []

        return result