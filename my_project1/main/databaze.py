from pymongo import MongoClient

cluster = MongoClient('mongodb+srv://sdovi:820722zz@cluster0.wan4jgq.mongodb.net/?retryWrites=true&w=majority')
db = cluster['information']
collection = db['info']
collection.insert_one({
    '_id': 2,
    'photo': 'main/img/watch/2.png',
    'text1': 'Apple Watch Series 8',
    'text2': 'Gold Stainless Steel Case/Gold Stainless Steell Milanese Loop/45mm',
    'text3': 'Размер',
    'text4': '49ММ',
    'text5': 'Цвета',
    'text6': 'Черный',
    'text8': 'Желтый',
    'text9': 'Зеленый',
    'text10': 'Белый',
    'text11': 'Серый',
    'text12': 'Оранжевый',
    'text13': 'Кремовый',
    'text14': 'Темно серый',
    'text15': 'Сияющая звезда',

})
