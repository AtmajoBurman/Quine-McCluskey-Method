def compare(str1, str2, N):
    new_str = str1[:]
    count = 0
    for i in range(N):
        if (str1[i] == '_' and str2[i] != '_') or (str1[i] != '_' and str2[i] == '_'):
            return ""
        elif abs(ord(str1[i]) - ord(str2[i])) == 1:
            count += 1
            new_str = new_str[:i] + '_' + new_str[i+1:]
    if count == 1:
        return new_str
    else:
        return ""

def d2b(n):
    one = 0
    if n == 0:
        return "0", one
    binary = ""
    while n > 0:
        if n % 2 == 0:
            binary = "0" + binary
        else:
            binary = "1" + binary
            one += 1
        n //= 2
    return binary, one

def build_prime_implicant_chart(PI, imp, arr1):
    # Header row with all the integers
    print("\nPrime Implicant Chart:")
    header = ["PI"] + [f"[{num}]" for num in arr1]
    print("\t".join(header))
    # Marking the chart
    for pi in PI:
        row = [pi]
        for num in arr1:
            if f"[{num}]" in imp[pi]:
                row.append("X")
            else:
                row.append(" ")
        print("\t".join(row))

def minimize_prime_implicant_chart(PI, imp, arr1):
    def get_essential_prime_implicants(chart, rows, cols):
        essential_prime_implicants = set()
        for col in cols:
            marked_rows = [row for row in rows if chart[row][col] == 'X']
            if len(marked_rows) == 1:
                essential_prime_implicants.add(marked_rows[0])
        return essential_prime_implicants

    def remove_covered_columns(chart, rows, cols, essential_prime_implicants):
        remaining_cols = set(cols)
        for epi in essential_prime_implicants:
            for col in cols:
                if chart[epi][col] == 'X' and sum(chart[row][col] == 'X' for row in rows) > 1:
                    remaining_cols.discard(col)
        return remaining_cols

    def remove_dominating_columns(chart, rows, remaining_cols):
        cols_to_remove = set()
        cols_list = list(remaining_cols)
        for i in range(len(cols_list)):
            for j in range(i + 1, len(cols_list)):
                col1 = cols_list[i]
                col2 = cols_list[j]
                col1_marks = [row for row in rows if chart[row][col1] == 'X']
                col2_marks = [row for row in rows if chart[row][col2] == 'X']
                if set(col1_marks).issubset(set(col2_marks)):
                    cols_to_remove.add(col2)
                elif set(col2_marks).issubset(set(col1_marks)):
                    cols_to_remove.add(col1)
        remaining_cols = set(remaining_cols)  # Convert to set to perform subtraction
        remaining_cols -= cols_to_remove
        return list(remaining_cols)  # Convert back to list if necessary

    def print_minimized_chart(chart, PI, arr1, remaining_cols):
        header = ["PI"] + [f"[{arr1[col]}]" for col in remaining_cols]
        print("\t".join(header))
        for pi in chart:
            row = [pi] + ["X" if chart[pi][col] == 'X' else " " for col in remaining_cols]
            print("\t".join(row))

    # Create the initial chart as a dictionary of dictionaries
    chart = {pi: {i: ' ' for i in range(len(arr1))} for pi in PI}
    for pi in PI:
        for num in arr1:
            if f"[{num}]" in imp[pi]:
                chart[pi][arr1.index(num)] = 'X'
    rows = list(PI)
    cols = list(range(len(arr1)))

    # Apply Rule 1: Essential Prime Implicants
    while True:
        essential_prime_implicants = get_essential_prime_implicants(chart, rows, cols)
        remaining_cols = remove_covered_columns(chart, rows, cols, essential_prime_implicants)
        if len(remaining_cols) == len(cols):  # No changes made, break loop
            break
        cols = list(remaining_cols)

    # Apply Rule 2: Remove Dominating Columns
    while True:
        previous_cols = set(cols)
        cols = list(remove_dominating_columns(chart, rows, cols))
        if previous_cols == set(cols):  # No changes made, break loop
            break

    print("\nMinimized Prime Implicant Chart:")
    print_minimized_chart(chart, PI, arr1, cols)

def main():
    N = int(input())
    arr = []
    for i in range(N):
        ch = input(f"variable {i+1}: ")
        arr.append(ch)
    arr1 = []
    y = 1
    while y:
        nums = int(input())
        arr1.append(nums)
        y = int(input("more ?"))

    group = [set() for _ in range(N+1)]
    imp = {}
    for nums in arr1:
        one = 0
        st, one = d2b(nums)
        st = st.zfill(N)  # Left pad the binary string with '0's to make it of length N
        imp[st] = f"[{nums}]"
        group[one].add(st)

    level = [group]
    mp = {}
    index = 0
    i = N
    while i >= 1:
        Group = [set() for _ in range(i)]
        for j in range(i):
            for str1 in level[index][j]:
                for str2 in level[index][j+1]:
                    x = compare(str1, str2, N)
                    if x != "":
                        Group[j].add(x)
                        mp[str1] = mp.get(str1, 0) + 1
                        mp[str2] = mp.get(str2, 0) + 1
                        imp[x] = imp[str1] + imp[str2]
        if any(Group):
            level.append(Group)
            i -= 1
            index += 1
        else:
            break

    z = 1
    PI = []
    for grp in level:
        print(f"\nLEVEL {z}")
        for st in grp:
            for str1 in st:
                print(str1, end='')
                if str1 not in mp:
                    print("(PI)\t" + imp[str1])
                    PI.append(str1)
                else:
                    print()
        print(".................")
        z += 1

    print("Prime Implicants:")
    for str1 in PI:
        s = ""
        for i in range(len(str1)):
            if str1[i] == '0':
                s += arr[i] + "'"
            elif str1[i] == '1':
                s += arr[i]
        print(s)

    # Build and display the prime implicant chart
    build_prime_implicant_chart(PI, imp, arr1)

    # Minimize the prime implicant chart
    minimize_prime_implicant_chart(PI, imp, arr1)

if __name__ == "__main__":
    main()