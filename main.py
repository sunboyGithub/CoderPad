# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print('hello gitted!')
    num, stack, sign = 0, [], '+'
    s += ' '
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == '(':
            num, skip = self.calculate(s[i+1:])
            i += skip
        elif s[i] in '+-*/)' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop * num)
            else:
                stack.append(int(stack.pop()/num))

            num = 0
            sign = s[i]
        i += 1
    return sum(stack)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
