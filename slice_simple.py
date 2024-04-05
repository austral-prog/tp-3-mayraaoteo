def slice_simple():
    txt = "Awesome"
    print(txt.lower()[0: 3])
    print(txt.lower()[2: 5])
    print(txt.lower()[0: 4] + txt.lower()[-3: ])
