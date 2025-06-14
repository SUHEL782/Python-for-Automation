#  devops = ['jenkins', 'docker', 'kubernetes']
#  print(devops[0])
#  print(devops[-1])

#  itemquantity = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#  Newitemquantity = [itemquantity[i] for i in range(len(itemquantity)) if itemquantity[i] > 50]
#  print(Newitemquantity)

#  a = [1, 2, 3, 4, 5]
#  b = [item for item in a if item > 2]
#  print(b)

# using slice 
#a = [1, 2, 3, 4, 5]
#  b = a[0:2]
#  print(b)
# cpuuses = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# highload = [cpuuses[i] for i in range(len(cpuuses)) if cpuuses[i] >70]
# print(highload)

# buildstatus = ['success', 'failed', 'success', 'failed', 'success']
# failed_builds = [buildstatus[i] for i in range(len(buildstatus)) if buildstatus[i] == 'failed']
# print(failed_builds)

# # Using list comprehension to filter items
# logs = ['start', 'running', 'error', 'retry', 'success']

# print(logs[-2])  # Accessing the last item

# job_result = ['passed', 'failed', 'passed', 'failed', 'passed']
# recent_jobs = job_result[-3:]  # Slicing the last three items
# print(recent_jobs)
containers = ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7']
middle = containers[2:5]
print(middle)