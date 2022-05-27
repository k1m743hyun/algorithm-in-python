if __name__ == '__main__':
    students = []
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        
        students.append([name, score])
    
    students.sort(key=lambda x: (x[1], x[0]))
    for name, score in students:
        if score == list(set(map(lambda x: x[1], students)))[1]:
            print(name)