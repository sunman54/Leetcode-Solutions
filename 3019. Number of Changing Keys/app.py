class Solution:
    def countKeyChanges(self, s: str) -> int:

        changes = -1

        f = ['*']

        for i in s:
            i = i.lower()

            if i != f[-1]:
                changes += 1

            f.append(i)

        
        return changes