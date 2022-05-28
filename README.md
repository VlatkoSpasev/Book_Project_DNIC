BookProject

Ова претставува едноставен Django проект за приказ и чување на информации за книги, која се изработува во рамки на аудиториските вежби по предметот Дизајн на интеракцијата човек-компјутер во летен семестар 2021/2022 година.

Во рамки на проектот има една апликација Books. Моделите во апликацијата се организирани на следниот начин:
  - Една книга е опишана со isbn број, наслов, кратка содржина, корисник кој ја креирал, автор и издавачка куќа
  - Авторот е опишан преку неговото име и презиме, година на раѓање, земја на потекло и кратка биографија
  - Издавачката куќа е опишана преку нејзиното име и адреса (улица и број, град, држава)
Дополнително, издавачките куќи имаат автори со кои соработуваат, па во таа насока креиран е моделот PublicationAuthor кој ја моделира оваа релација.

Во сите модели се регистрирани во рамки на администраторскиот панел. Измени во однос на нормалното однесување се наравени на моделот за автор, каде додавање на нов автор е дозволено само доколку корисникот кој се обидува да го додаде авторот е superuser. Дополнително, за овој модел не се дозволува промена или бришење на зачуваните објекти. 

Моделот PublicationAuthor е поставен како Inline модел во рамки на моделот Publication, што овозможува лесно и брзо додавање на објектите од овој модел.