import pickle

# имя фаила, в который мы сохраним объект
shoplistfile = 'shoplist.data'
# список покупок 
shoplist = ['яблоко', 'манго', 'морковь']

# Запись в фаил
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещаем объект в фаил
f.close()

del shoplist # уничтожаем переменную shoplist

# Считываем из хранилища
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загружаем обект из фаила
print(storedlist)
