# Timmy & Sarah creen que estan enamorados, la forma de comprobarlo estan
# cogiendo flores, si uno coge una flor con pétalos impares y el otro con
# pétalos pares significan que están enamorados, sino no.

def lovefunc(flower1, flower2):
    while flower1 % 2 != flower2 % 2:
        print("They are in love")
        break
    else:
        print("They aren't")

lovefunc(313, 214)