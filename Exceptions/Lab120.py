# Exception
# abnormal event during the execution program

print("Insert the card")


try:
    a = 10/0
except Exception as e:
    print("Error", e)

print("Take the card")
