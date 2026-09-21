class Solution:
    def punishmentNumber(self, n: int) -> int:
        def compute_partition_sums(num_string):
            l = len(num_string)
            result = set()
            result.add(int(num_string))
            if l>1:
                for split_before in range(1,l):
                    left = compute_partition_sums(num_string[:split_before])
                    right = compute_partition_sums(num_string[split_before:])
                    for lt in left:
                        for rt in right:
                            result.add(int(lt+rt))
            print(f'returning {result=}')
            return result

        print(compute_partition_sums(str(45353)))

        result = 0
#        for i in range(1,n+1):
#            squared = i**2
#            if i in compute_partition_sums(str(squared)):
#                result += squared
        return result

if __name__ == '__main__':
    sol = Solution()
    sol.punishmentNumber(10)