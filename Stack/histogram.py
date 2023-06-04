def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    i = 0

    while i < len(heights):
        if not stack or heights[i] >= heights[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            area = (heights[top] * ((i - stack[-1] - 1) if stack else i))
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        area = (heights[top] * ((i - stack[-1] - 1) if stack else i))
        max_area = max(max_area, area)

    return max_area
