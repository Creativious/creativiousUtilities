box1 = ((100,100), (200,200))
box2 = ((400,400), (500,500))

box1Dict = {
    "top_left": box1[0],
    "top_right": (box1[1][0],box1[0][1]),
    "bottom_right": box1[1],
    "bottom_left": (box1[0][0], box1[1][1])
}

box2Dict = {
    "top_right": box2[0],
    "top_left": (box2[1][0],box2[0][1]),
    "bottom_right": box2[1],
    "bottom_left": (box2[0][0], box2[1][1])
}

