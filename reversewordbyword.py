def reverse(name):
    words=name.split()
    reverse_words=words[-1::-1]
    reverse_string=" ".join(reverse_words)
    print reverse_string

reverse("I live in pune")
