def reverse(variable):
    res=''
    for i in range(len(variable)-1,-1,-1):
        res+=variable[i]
    return res

print(reverse("привет как дела")) #алед как тевирп
