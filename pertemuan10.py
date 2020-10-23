#dictionary

phone = {
    "Jhon" : 89121311,
    "Jack" : 98328482,
    "Doe" : 8283752,
}
phone['mylist'] = [1, 2, 3]
print(phone)


phone = [
    {
        "name" : "Luke Skywalker",
        "role" : "Jedi",
        "email" : "luke@gmail.com",
    },
    {   "name" : "Padme Amidala",
        "role" : "Princesses",
        "email" : "padme@gmail.com",
    },
    {   "name" : "Han Solo",
        "role" : "Solo",
        "email" : "solo@gmail.com",
    },
]

phone = { "Jhon Doe" : 20393413, "Max Speed": 94875373822 }

del phone['Jhon Doe'] #hapus dict 
print(phone)


phone = [
    {
        "name" : "Luke Skywalker",
        "role" : "Jedi",
        "email" : "luke@gmail.com",
    },
    {   "name" : "Padme Amidala",
        "role" : "Princesses",
        "email" : "padme@gmail.com",
    },
    {   "name" : "Han Solo",
        "role" : "Solo",
        "email" : "solo@gmail.com",
    },
]

phone = { "Jhon Doe" : 20393413, "Max Speed": 94875373822 }
dict1 = phone.pop("Jhon Doe")
print(dict1)

phone = [
    {
        "name" : "Luke Skywalker",
        "role" : "Jedi",
        "email" : "luke@gmail.com",
    },
    {   "name" : "Padme Amidala",
        "role" : "Princesses",
        "email" : "padme@gmail.com",
    },
    {   "name" : "Han Solo",
        "role" : "Solo",
        "email" : "solo@gmail.com",
    },
]

phone = { "Jhon Doe" : 20393413, "Max Speed": 94875373822 }

for i, v in phone.items():
   print(f"Name: {i}, phone: {v}")


#belajar tuple 

tp = ("Kambing", "Kucing", "Sapi")  #untuk data yang sudah pasti, data yg bakal di ganti-ganti
print(tp)

#kecuali bisa di ganti dengan konversi ke list
ls = list(tp)
print(ls)

