# Based on https://leetcode.com/problems/prison-cells-after-n-days/


class Solution:
    def prisonAfterNDays(self, cells, N):

        ncells = len(cells)
        state_transitions = dict()  # key: string of one state, value: next state (list of ints)
        state_on_day_x = dict()  # key: index (0-based), value: string of state
        first_day_for_state = dict()  # key: string of state, value: index for first date

        def determine_next_state(current_state):
            new_cells = [0] * ncells
            for j in range(1, ncells - 1):
                new_cells[j] = abs((current_state[j - 1] ^ current_state[j + 1]) - 1)
            return new_cells

        for i in range(N):
            if str(cells) in first_day_for_state:
                base_idx = first_day_for_state[str(cells)]
                cycle_length = i - base_idx
                effective_index = (N-base_idx) % cycle_length + base_idx
                return state_on_day_x[effective_index]
            else:
                state_on_day_x[i] = str(cells)
                first_day_for_state[str(cells)] = i
                state_transitions[str(cells)] = determine_next_state(cells)
                cells = state_transitions[str(cells)]

        return state_transitions[state_on_day_x[N - 1]]


if __name__ == '__main__':
    sol = Solution()
    print(sol.prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], N = 1000000000))
