#from data_gen import gen
import time

def input(filename):
  with open(filename) as f:
    [N, M] = [int(x) for x in f.readline().split()]
    info_classes = [[int(x) for x in f.readline().split()] + [i] for i in range(N)] # [number of lessons, teacher assigned, number of students, class]
    rooms = [int(x) for x in f.readline().split()]
  return info_classes, rooms

def greedy(filename):
  info_classes, rooms = input(filename)
  info_classes_sorted = sorted(info_classes, key=lambda x: -x[2]) # sort classes by its number of students (decreasing)
  rooms_sort = sorted([(rooms[i], i) for i in range(len(rooms))], key = lambda x : x[0]) # sort rooms by its capacity (increasing)
  teacher = [g for t, g, s, _ in info_classes]

  state_room = [[True for _ in range(len(rooms))] for __ in range(60)] # state_room[i][j] = True if room i is available in period j (0-59)
  state_teacher = [[True for _ in range(len(set(teacher)) + 1)] for __ in range(60)] # state_teacher[i][j] = True if teacher i is available in period j (0-59)

  timetable = {}
  for info_class in info_classes_sorted:
    timetable[info_class[-1]] = [] # timetable of class each class 
    for _ in range(info_class[0]): # If we loop this way, we will sure that each class has enough shift.
      x = select(info_class, state_room, state_teacher, rooms_sort)
      if x == None:
        continue
      timetable[info_class[-1]].append(x)
  return timetable

def select(info_class, state_room, state_teacher, rooms):
  for p in range(60):
    for capacity, room_index in rooms:
      if feasible(info_class, state_room, state_teacher, capacity, p, room_index):
        state_room[p][room_index] = False
        state_teacher[p][info_class[1]] = False
        return p, room_index

def feasible(info_class, state_room, state_teacher, capacity, p, index_room): # check if a partial solution is feasible
  # At a moment, a teacher teaches at most one class
  if not state_teacher[p][info_class[1]]:
    return False
  # At a moment, a room is used by at most one class
  if not state_room[p][index_room]:
    return False
  # The room's capacity is bigger than the number of student in class
  if info_class[2] > capacity:
    return False
  return True

def class_less(index):
  filename = 'data.txt'
  info_classes, rooms = input(filename)
  res = dict()
  for number_lessons, teacher, number_stud, class_index in info_classes:
    res[class_index] = number_lessons
  return res[index]

def print_timetable(timetable):
  #print(timetable)
  sorted_timetable_keys = sorted(timetable.keys())
  num_class = 0
  for i in sorted_timetable_keys:
    if len(timetable[i]) == class_less(i):
      num_class += 1
  print(num_class)
  for i in sorted_timetable_keys:
    if len(timetable[i]) == class_less(i):
      print(f"{i+1} {timetable[i][0][0]+1} {timetable[i][0][1]+1}")
      

def total_less(filename):
    total = 0
    with open(filename) as f:
      [N, M] = [int(x) for x in f.readline().split()]
      for _ in range(N):
        total += int(f.readline().split()[0])
    print(total)


filename = 'data.txt'
info_classes, rooms = input(filename)
solution = greedy(filename)
print_timetable(solution)

  
  
