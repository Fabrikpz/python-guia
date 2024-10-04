import py5

arr = [45, 50, 21, 234, 4, 60, 30, 820, 10]
n = len(arr)
i = 0
j = 0
sorting = False

def setup():
    py5.size(400, 400)
    py5.background(255)

def draw():
    global i, j, sorting
    
    py5.background(255)
    draw_array(arr)

    if sorting:
        if j < n - i - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
            j += 1
        else:
            i += 1
            j = 0
            if i >= n - 1:
                sorting = False

def draw_array(arr):
    bar_width = py5.width / len(arr)
    for index, value in enumerate(arr):
        py5.fill(150, 0, 150)
        py5.rect(index * bar_width, py5.height - value * 3, bar_width - 2, value * 3)

def mouse_pressed():
    global sorting, i, j
    sorting = True
    i = 0
    j = 0

py5.run_sketch()
