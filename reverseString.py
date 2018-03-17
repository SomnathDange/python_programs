def reverse(name):
    if len(name) == 0:
        return name
    else:
        return reverse(name[1:]) + name[0] 
print reverse("school")
