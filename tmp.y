def smartAssigning(names, statuses, projects, tasks):
    id = 0
    for i in range(len(names)):
        if statuses[i] == False :
            id = i
            break
            
    for i in range(len(names)):
        if statuses[i] == False :
            if tasks[i] < tasks[id]:
                id = i
            elif (tasks[i] == tasks[id]):
                if projects[i] < projects[id] :
                    id = i
    return names[id]
    
    
    
    For names = ["John", "Martin"], statuses = [false, false],
projects = [2, 1] and tasks = [16, 5],
the output should be
smartAssigning(names, statuses, projects, tasks) = "Martin".

The arguments represent information about two team members:

"John", with status = false, projects = 2 and tasks = 16;
"Martin", with status = false, projects = 1 and tasks = 5.
Here John and Martin's vacation indicators are both true, so both of them are open to new assignments. Martin is only assigned 5 tasks while John is assigned 6, so Martin has the highest availability.

For names = ["John", "Martin"], statuses = [false, true],
projects = [2, 1] and tasks = [6, 5],
the output should be
smartAssigning(names, statuses, projects, tasks) = "John".

The arguments stand for the following team members:

"John", with status = false, projects = 2 and tasks = 1;
"Martin", with status = true, projects = 1 and tasks = 5.
In this example Martin cannot be assigned any new tasks because his vacation indicator is true. Therefore, "John" has the highest availability.

For names = ["John", "Martin"], statuses = [false, false],
projects = [1, 2] and tasks = [6, 6],
the output should be
smartAssigning(names, statuses, projects, tasks) = "John".

For the following information is given:

"John", with status = false, projects = 1 and tasks = 6;
"Martin", with status = false, projects = 2 and tasks = 6.
Both John and Martin's vacation indicators are false, and the number of tasks each of them is assigned is 6. However, John is involved in just 1 project, while Martin is involved in 2, so John has the highest availability.
