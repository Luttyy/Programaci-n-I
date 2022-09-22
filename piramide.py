def Piramide(altura):
    var1=""
    for i in range (altura):
        for j in range(altura+(altura-1)):
            if (j == (altura+(altura-1)-1)/2):
                var1 = var1 + "*"
            else:
                var1 = var1 + " "
        print(var1)
        var=""

Piramide(6)