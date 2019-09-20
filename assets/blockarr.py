# もっといい方法ないかなぁ…

ARR_Z = {
    # 0°
    0: [
        ['Z', 'Z', 'EMP', 'EMP'],
        ['EMP', 'Z', 'Z', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP']
    ],
    # 90°
    1: [
        ['EMP', 'Z', 'EMP', 'EMP'],
        ['Z', 'Z', 'EMP', 'EMP'],
        ['Z', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP']
    ],
    # 180°
    2: [
        ['Z', 'Z', 'EMP', 'EMP'],
        ['EMP', 'Z', 'Z', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['EMP', 'Z', 'EMP', 'EMP'],
        ['Z', 'Z', 'EMP', 'EMP'],
        ['Z', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP']
    ]
}

ARR_T = {
    0: [
        ['T', 'T', 'T', 'EMP'],
        ['EMP', 'T', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 90°
    1: [
        ['EMP', 'T', 'EMP', 'EMP'],
        ['T', 'T', 'EMP', 'EMP'],
        ['EMP', 'T', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 180°
    2: [
        ['EMP', 'T', 'EMP', 'EMP'],
        ['T', 'T', 'T', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['T', 'EMP', 'EMP', 'EMP'],
        ['T', 'T', 'EMP', 'EMP'],
        ['T', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ]
}


ARR_O = {
    0: [
        ['O', 'O', 'EMP', 'EMP'],
        ['O', 'O', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 90°
    1: [
        ['O', 'O', 'EMP', 'EMP'],
        ['O', 'O', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 180°
    2: [
        ['O', 'O', 'EMP', 'EMP'],
        ['O', 'O', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['O', 'O', 'EMP', 'EMP'],
        ['O', 'O', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ]
}

ARR_S = {
    0: [
        ['EMP', 'S', 'S', 'EMP'],
        ['S', 'S', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 90°
    1: [
        ['S', 'EMP', 'EMP', 'EMP'],
        ['S', 'S', 'EMP', 'EMP'],
        ['EMP', 'S', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 180°
    2: [
        ['EMP', 'S', 'S', 'EMP'],
        ['S', 'S', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['S', 'EMP', 'EMP', 'EMP'],
        ['S', 'S', 'EMP', 'EMP'],
        ['EMP', 'S', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ]
}

ARR_L = {
    0: [
        ['L', 'EMP', 'EMP', 'EMP'],
        ['L', 'EMP', 'EMP', 'EMP'],
        ['L', 'L', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 90°
    1: [
        ['L', 'L', 'L', 'EMP'],
        ['L', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 180°
    2: [
        ['L', 'L', 'EMP', 'EMP'],
        ['EMP', 'L', 'EMP', 'EMP'],
        ['EMP', 'L', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['EMP', 'EMP', 'L', 'EMP'],
        ['L', 'L', 'L', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ]
}

ARR_I = {
    0: [
        ['I', 'EMP', 'EMP', 'EMP'],
        ['I', 'EMP', 'EMP', 'EMP'],
        ['I', 'EMP', 'EMP', 'EMP'],
        ['I', 'EMP', 'EMP', 'EMP'],
    ],
    # 90°
    1: [
        ['I', 'I', 'I', 'I'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 180°
    2: [
        ['I', 'EMP', 'EMP', 'EMP'],
        ['I', 'EMP', 'EMP', 'EMP'],
        ['I', 'EMP', 'EMP', 'EMP'],
        ['I', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['I', 'I', 'I', 'I'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ]
}


ARR_J = {
    0: [
        ['EMP', 'J', 'EMP', 'EMP'],
        ['EMP', 'J', 'EMP', 'EMP'],
        ['J', 'J', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 90°
    1: [
        ['J', 'EMP', 'EMP', 'EMP'],
        ['J', 'J', 'J', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 180°
    2: [
        ['J', 'J', 'EMP', 'EMP'],
        ['J', 'EMP', 'EMP', 'EMP'],
        ['J', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ],
    # 270°
    3: [
        ['J', 'J', 'J', 'EMP'],
        ['EMP', 'EMP', 'J', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
        ['EMP', 'EMP', 'EMP', 'EMP'],
    ]
}
