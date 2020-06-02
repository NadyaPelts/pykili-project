import os
import colorama
from colorama import Fore, Back, Style
colorama.init()

while True:
 finish="0"
 cofe="0"
 ###ДЕНЬ ПЕРВЫЙ###
 while True:
  print("Привет! Добро пожаловать в Надин и Лизин текстовый квест. Ты просыпаешься")
  print("в универе, снова и снова. Дни слишком похожи на друг друга. Только ты замечаешь это,")
  print("а все остальные ведут себя как обычно. Что же случилось? Кто в этом виноват?")
  print("")
  print("Нажимайте Enter для продолжения")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Утро. Ты просыпаешься. Всё тело странно ломит, как будто ты очень долго сидела в неудобной позе.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Стоп, почему я в библиотеке?\nПолучается я заснула в универе?")
  print("Вот это я даю, конечно. Интересно, почему меня не выгнали… Басмач не Покра все-таки…")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Ты выходишь из библиотеки и оглядываешься вокруг. И как ты могла уснуть в библиотеке? смотришь на часы и…")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Сколько времени???? 10:25?? Да у меня же пара через 5 минут на 8 этаже в Б корпусе.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("*после пары*")
  print("Ого, я даже что-то поняла по этой новой теме, после такого-то сна….")
  print("*урчит живот*")
  print("Надо заглянуть в столовую, а то с таким утром даже позавтракать не удалось.")
  print("*в столовой*")
  print("Ты только перешагиваешь порог в столовую как вдруг…")
  print("О, чёрт, прости, пожалуйста, не заметил тебя!")
  print("Какой-то парень врезался в тебя и вылил почти весь стакан кофе на твои штаны.")
  print("Что сделаешь?")
  print("1. Разозлиться и наорать.")
  print("2. Да ладно, сейчас все стрессуют, он случайно, с кем не бывает.")
  answer = input()
  os.system("cls")
  if answer=="1":
   cofe="1"   
   while True:
    print("Эй! Ты вообще видишь, куда прешь?! Куда мне теперь с таким пятнищем на штанах?")
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ################## 
   break
  if answer=="2":
   while True:
    print("Блин, чувак, не переживай, все нормально, я тебя понимаю, тоже сил уже не осталось…")
 
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ##################
   break
  if answer!="1" or answer!="2":
   os.system("cls")
  else:
   os.system("cls")
   break
    
   #print("Введите 1 или 2")
  # os.system("cls")
   #continue


 while True:
  print("Хоть и с пятном на штанах, но покушать надо. Пришло время выбирать. В комплексе сегодня сердечки.")
  print("Что будешь брать?")
  print("1.Комплекс")
  print("2.Не комплекс")
  answer=input()
  os.system("cls")
  if answer=="1":
   while True:
    print("Фух, хорошо, что хоть обед за 110 рублей не подводит, сегодня довольно вкусно.")
    
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ##################
   break
  if answer=="2":
   while True:
    print("Что будешь брать?")
    print("1. Котлетка с макарошками и щавелевый кисель")
    print("2. Нет с пюрешкой и щавелевый кисель ")
    print("3. Овощное рагу с картошкой с картошкой (виган опшен) и щавелевый кисель.")
    eat=input()
    if eat=="1":
     os.system("cls")
     print("Так, поесть поели (какие же вкусные были котлетки с макарошками), теперь надо бы до следующей пары дойти.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    if eat=="2":
     os.system("cls")
     print("Так, поесть поели (какие же вкусные были котлетки с пюрешкой), теперь надо бы до следующей пары дойти.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    if eat=="3":
     os.system("cls")
     print("Так, поесть поели (какое же вкусное было овощное рагу с картошкой), теперь надо бы до следующей пары дойти.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    
    if eat!="1" or eat!="2" or eat!="3":
     os.system("cls")
    else:
     os.system("cls")
     break  
   break         
  if answer!="1" or answer!="2":
   os.system("cls")
  else:
   os.system("cls")
   break
    
 while True:
  print("Стоп")
  print("Я почему в библиотеке-то осталась, надо было к тесту по проге подготовиться.")
  print("С этой последней темой вообще не разобралась...")
  print("И естественно уснула в библиотеке, супер.")
  print("Что же теперь делать?")
  print("1. Пойти, попытать удачу, но скорее всего все равно завалить")
  print("2. Просто не пойти. Что уж там. Все равно 0 будет, зачем париться?")
  answer=input()
  os.system("cls")
  if answer=="1":
   while True:  
    print("*после пары*")
    print("Эх, ещё один ноль..:C")
    print("В любом случае там три худших теста не учитываются, я ничего не теряю.")
    
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ##################
   break
  if answer=="2":
   while True:  
    print("Ты не пошла на пару, но подружка, которая пошла,")
    print("рассказала, что там было (всё было плохо)")
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ##################

   break
  if answer!="1" or answer!="2":
    os.system("cls")
  else:
   os.system("cls")
   break
 while True:
  print("Дохожу до метро, на автомате достаю социалку из кармана и пытаюсь пробить. С первого раза не получается.")
  print("Со второго не получается.")
  print("Супер, давайте еще так сегодняшний день украсим, да.")
  print("Третья попытка.")
  print("Фух, пробилась.")
  print("Уставшая я доезжаю до дома на автопилоте и очухиваюсь уже в собственном лифте.")
  print("")
  print("*дома*")
  print("Ну и денёк конечно…. А завтра у меня что? Чёрт, надо написать эссе по английскому и не забыть пройти СОП.")
  print("Чем бы таким перекусить….")
  
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
  ##################

 while True:
  print("ДЕНЬ ВТОРОЙ")
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
  ##################
   
  ###------------------------------------------------------------------------------------------------------------------ ДЕНЬ ВТОРОЙ  ###
 while True:
  print("Почему снова всё так болит? Я что, опять уснула за столом? ")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Ты открываешь глаза и...")
  print("Стоп, это что, снова библиотека?? Как это вообще возможно, я же заснула дома вчера...")
  print("Мне что, всё это приснилось?")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Ты выходишь из библиотеки и оглядываешься вокруг.")
  print("Почему всё выглядит так же, как в моём сне?")
  print("Так значит... если всё это мне приснилось... Я что, снова опаздываю на пару???")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("*после пары*")
  print("Всё ещё не могу поверить, что на паре было всё то же самое, что мне приснилось...")
  print("Неужели это был вещий сон? Да ну, бред какой")
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
  ##################
 while True:
  print("*урчит живот*")
  print("О, а поесть-то я и правда забыла. Опять. Опять?")
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
  ##################  
 while True:
  print("*в столовой*")
  print("Ты переступаешь порог столовой и вдруг вспоминаешь, что в твоём сне именно на этом моменте тебя облили кофе.")
  print("Опасливо оглядываешься по сторонам и замечаешь парня из своего сна.")
  print("Он сидит за столиком и, кажется, доедает свой обед.")
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
  ##################
 while True:
  print("Ого, ну хоть эта часть сна не сбылась. Можно спокойно поесть. Может и меню не такое, как мне приснилось? А, нет...")
  print("Что будешь брать?")
  print("1.Комплекс.")
  print("2.Не комплекс.")
  answer=input()
  os.system("cls")
  if answer=="1":
   while True:
    print("Комплекс никогда не подводит.")
    
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ##################
   break
  if answer=="2":
   while True:
    print("Что будешь брать?")
    print("1. Котлетка с макарошками и щавелевый кисель.")
    print("2. Нет с пюрешкой и щавелевый кисель.")
    print("3. Овощное рагу с картошкой с картошкой (виган опшен) и щавелевый кисель.")
    eat=input()
    if eat=="1":
     os.system("cls")
     print("Так, поесть поели (какие же вкусные были котлетки с макарошками), теперь надо бы до следующей пары дойти.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    if eat=="2":
     os.system("cls")
     print("Так, поесть поели (какие же вкусные были котлетки с пюрешкой), теперь надо бы до следующей пары дойти.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    if eat=="3":
     os.system("cls")
     print("Так, поесть поели (какое же вкусное было овощное рагу с картошкой), теперь надо бы до следующей пары дойти.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    
    if eat!="1" or eat!="2" or eat!="3":
     os.system("cls")
    else:
     os.system("cls")
     break   
   break         
  if answer!="1" or answer!="2":
   os.system("cls")
  else:
   os.system("cls")
   break
    
 while True:
  print("Стоп")
  print("Это что, и тест по проге снова надо писать? А я всё ещё ничего не знаю.")
  print("Хотя, я же знаю, что будет в тесте...")
  print("Что если и это повторится?")
  print("1. Пойти, написать тест.")
  print("2. Не пойти. Быть не может, что мне приснился именно тот тест, который дадут сегодня на занятии.")
  answer=input()
  os.system("cls")
  if answer=="1":
   while True:  
    print("*после пары*")
    print("Поверить не могу, что это правда сработало, это просто безумие. ")
    print("Может, во мне проснулся талант предсказательницы будущего?")
    
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
    ##################
   break
  if answer=="2":
   break
  if answer!="1" or answer!="2":
    os.system("cls")
  else:
   os.system("cls")
   break
 while True:
  print("Дохожу до метро, на автомате достаю социалку из кармана и пытаюсь пробить. С первого раза не получается.")
  print("Со второго не получается.")
  print("Супер, опять, все повторяется даже в мелочах.")
  print("Третья попытка.")
  print("Фух, пробилась.")
  print("Еле еле доезжаю до дома.")
  print("")
  print("*дома*")
  print("Опять же надо пройти СОП (ведь если я его и прошла то только во сне...) и сделать домаху.")
  print("Лечь бы спать уже поскорее...")
  
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
  ##################
   
  ###------------------------------------------------------------------------------------------------------------------ ДЕНЬ ТРЕТИЙ  ###

 while True:
  print("ДЕНЬ ТРЕТИЙ")
  ###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
    ################## 
 
 
 while True:
  print("Утро. Ты просыпаешься и тело снова неприятно ломит. Да что же это… Я что, снова в библиотеке???")
  print("Что будешь делать?")
  print("1. Конечно запаникую, как так может быть???")
  print("2. Попытаться снова уснуть")
  answer = input()
  os.system("cls")
  if answer=="1":
   while True:
    while True:
     print("Ты вскакиваешь и оглядываешься по сторонам. Да, всё выглядит точно так же как вчера, и как позавчера…")
    ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
    ##################
    while True:  
     print("Или это был сон? Опять?")
    ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
    ##################
    while True:
     print("Нет, не может быть, что это снова сон.")
    ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
    ##################
    while True:
     print("Или ты сходишь с ума, или…")
    ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
    ##################
    while True:  
     print("Надо разобраться")
    ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
    ################## 
    break 
   break
  if answer=="2":
   while True:
    while True:
     print("Вдруг это всё ещё один бесконечный рекурсивный сон…")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    while True:
     print("Может, если снова заснуть, то получится проснуться по-настоящему?")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    while True:
     print("Ты пытаешься уснуть, но беспокойные мысли не дают этого сделать.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    while True:
     print("Нужно пойти и разобраться, что же происходит на самом деле.")
     ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
     ##################
    break
   break
  if answer!="1" or answer!="2":
   os.system("cls")
  else:
   os.system("cls")
   break


 while True:
  print("Так что же происходит?")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Я продолжаю просыпаться в библиотеке, хотя засыпаю совершенно точно дома. И дни выглядят абсолютно одинаково. Это что, временная петля?")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Хотя…. ")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Этот парень в столовой…")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
##################
 while True:
  print("Он единственный вчера повёл себя не так, как позавчера, и, учитывая ситуацию, это странно.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
 while True:
  print("Возможно, он тоже попал в эту временную петлю? Нужно найти его и всё выяснить.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls") 
 while True:
  print("Ты отправляешься в столовую.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
 while True:
  print("Заходишь в столовую, но парня нигде не видно.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
 while True:
  print("Точно, обычно же я приходила в столовую позже, после пары... Не пойду же я на эту пару третий раз, лучше подожду здесь.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")  
 while True:
  print("Ты садишься за столик и самые долгие полтора часа в твоей жизни начинаются...")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")
 while True:
  print("В этот раз от нервов есть не хотелось. Хотелось поскорее все выяснить, тревожные мысли переполняли голову.")
###Кнопка далее###
  skip=input()
  if skip=="":
   os.system("cls")
   break
  else:
   os.system("cls")


 while True:
  print("О, вот же он! Нужно действовать!")
  print("1. Подойти и прямо спросить, что происходит")
  print("2. Понаблюдать за парнем и посмотреть, что он будет делать")
  print("3. Подойти и просто заговорить")
  answer=input()
  os.system("cls")
  if answer!="1" or answer!="2":
   os.system("cls")
  else:
   os.system("cls")
   break

  if answer=="1":
      
   while True:   
    print(Style.BRIGHT + Fore.GREEN + "- Хей! Слушай, подожди минуту, можно тебя спросить?")
    print(Style.RESET_ALL + "*парень испуганно оглянулся*")
    print(Style.BRIGHT + Fore.CYAN + "- Да, что такое?")     
    print(Style.BRIGHT + Fore.GREEN + "- Изо дня в день я продолжаю просыпаться в библиотеке, все вокруг повторяется, ты единственный, чьи действия каждый день разнятся. Ты точно должен что-то знать, что происходит???")
    print(Style.BRIGHT + Fore.CYAN + "Черт... Ты…. Ты не должна была узнать…  Подожди, я не понимаю… Ты что была в библиотеке в ночь со вторника на среду?")
    print(Style.BRIGHT + Fore.GREEN + "- Я готовилась к чему-то там и уснула прямо в библиотеке, да…")
    print(Style.BRIGHT + Fore.CYAN + "- О нет. Кажется мне нужно тебе кое-что рассказать…  Пошли куда-нибудь подальше")
    print(Style.RESET_ALL)
    ###Кнопка далее###
    skip=input()
    if skip=="":
     os.system("cls")
     break
    else:
     os.system("cls")
     ##################
   break
  if answer=="2":
   while True:
    print("Парень подходит к кассе, оплачивает свой кофе и какую-то булку и стремительно направляется к выходу.")
    print("1. Cразу пойти за ним, иногда смотря в свой телефон и делая вид, что ничего не происходит ")
    print("2. Дать ему отойти на небольшое расстояние и следить издалека")     
    answer=input()
    os.system("cls")
    if answer!="1" or answer!="2":
     os.system("cls")
    if answer=="1":    
     while True:
      print("Так, он идет к лестнице. Блин, наверное, слишком странно, что я иду за ним уже 4 этажа. Надеюсь, не заметит…")
      print("Ты отвлекаешься на телефон и тут…")
      print("БУМ")
      print("Ты врезаешься в него на повороте…")
      print(Style.BRIGHT + Fore.GREEN + "- Ой, прости, я не хотела…")     
      print(Style.BRIGHT + Fore.CYAN + "- Ничего. Подожди, ты так долго идешь за мной, что ты хочешь?! ")
      print(Style.BRIGHT + Fore.GREEN + "- Просто… Просто я заметила, что ты единственный, чьи действия не повторяются изо дня в день. ты должен что-то знать.")
      print(Style.BRIGHT + Fore.CYAN + "- Cтоп, ты что была в библиотеке в ночь со вторника на среду??? Черт, этого не должно было случиться… нам нужно поговорить где-нибудь, где не так много людей…")
      print(Style.RESET_ALL)
      ###Кнопка далее###
      skip=input()
      if skip=="":
       os.system("cls")
       break
      else:
       os.system("cls")
     ##################      
     break
    if answer=="2":
     while True:   
      while True:   
       print("Кажется он повернул к лестницам. Так, пошел наверх. На третьем этаже не свернул. Значит идет выше…")
       print("О, на четвертом пошел направо! Наверное, он сядет у автоматов.")
       print("Да, видимо я не одна люблю это место. Он сел за те столы. И что теперь делать?")
       print("Я же не могу пойти сесть напротив.. Сяду в коридоре. Да. Оттуда мне будет его видно.")
       ###Кнопка далее###
       skip=input()
       if skip=="":
        os.system("cls")
        break
       else:
        os.system("cls")
      ##################      
      while True:
       print("*прошел час*")
       ###Кнопка далее###
       skip=input()
       if skip=="":
        os.system("cls")
        break
       else:
        os.system("cls")
      ##################
      while True:    
       print("Надо все-таки к нему подойти. Я же не могу так сидеть вечно.")     
       print("Судя по всему, он просто сидит и пишет, иногда выходя за едой.")
       print("*ты решаешься и подходишь*")
       print(Style.BRIGHT + Fore.GREEN + "- Хей! Можно к тебе подсесть?")
       print(Style.BRIGHT + Fore.CYAN + "- Да, конечно")
       print(Style.RESET_ALL + "*Долгие пять секунд молчания и ты замечаешь ужас осознания в глазах парня*")
       print(Style.BRIGHT + Fore.GREEN + "- Я хотела у тебя кое-что спросить")
       print(Style.BRIGHT + Fore.CYAN + "- Эммм, да?")
       print(Style.BRIGHT + Fore.GREEN + "- Уже три дня я просыпаюсь в библиотеке, все вокруг повторяется, ты единственный, чьи действия каждый день разнятся.")
       print(Style.BRIGHT + Fore.GREEN + "Ты точно должен что-то знать, что происходит???")
       print(Style.BRIGHT + Fore.CYAN + "- Чёрт... Ты…. Ты не должна была узнать… Подожди, я не понимаю…")
       print(Style.BRIGHT + Fore.CYAN + "Ты что была в библиотеке в ночь со вторника на среду?")
       print(Style.BRIGHT + Fore.GREEN + "- Я готовилась к чему-то там и уснула прямо в библиотеке, да…")
       print(Style.BRIGHT + Fore.CYAN + "- О нет. Кажется мне нужно тебе кое-что рассказать… / Пошли куда-нибудь подальше")
       print(Style.RESET_ALL)
       ###Кнопка далее###
       skip=input()
       if skip=="":
        os.system("cls")
        break
       else:
        os.system("cls")
      ##################


      break 
     break
    
   break     
  if answer=="3":
   while True:
       print(Style.BRIGHT + Fore.GREEN + "- Привет, можно здесь сесть?")
       print(Style.RESET_ALL + "*Долгие пять секунд молчания и ты замечаешь ужас осознания в глазах парня*")
       print("1. Заговорить о погоде")     
       print("2. Заговорить об учёбе.")
       print("3. Заговорить о том, что в комплексе снова сердечки")
       answer=input()
       os.system("cls")
       if answer!="1" or answer!="2" or answer!="3":
        os.system("cls")       
       if answer=="1":
        while True:
         print(Style.BRIGHT + Fore.GREEN + "- Хорошая сегодня погода, да?")
         print(Style.BRIGHT + Fore.CYAN + "- Эмм, да, наверное")
         print(Style.BRIGHT + Fore.GREEN + "- Давно в Москве не было такого чистого голубого неба")
         print(Style.BRIGHT + Fore.CYAN + "- Кхм да, извини, мне пора")
         print(Style.RESET_ALL)
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break
         else:
          os.system("cls")  
        break
       if answer=="2":
        while True:
         print(Style.BRIGHT + Fore.GREEN + "- Блин, сессия уже близко, надо бы начать готовиться")
         print(Style.BRIGHT + Fore.CYAN + "- Эмм, да, наверное")
         print(Style.BRIGHT + Fore.GREEN + "- Не переживаешь из-за экзаменов?")
         print(Style.BRIGHT + Fore.CYAN + "- Да.. нет.. кхм.. извини, мне пора")
         print(Style.RESET_ALL)
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break
         else:
          os.system("cls")  
        break       
       if answer=="3":
        while True:
         print(Style.BRIGHT + Fore.GREEN + "- В комплексе сегодня опять сердечки, сколько можно!")
         print(Style.BRIGHT + Fore.CYAN + "- Ты даже представить не мож… кхм.. да, снова сердечки. извини, мне пора")
         print(Style.BRIGHT + Fore.GREEN + "- Не переживаешь из-за экзаменов?")
         print(Style.BRIGHT + Fore.CYAN + "- Да.. нет.. кхм.. извини, мне пора")
         print(Style.RESET_ALL)
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break
         else:
          os.system("cls")
        break          
       if answer!="1" or answer!="2" or answer!="3":
        os.system("cls")
   while True:

         print("Парень быстро собрался и быстрым шагом направился к выходу из столовой.")
         print("Ничего ценного узнать не вышло… Нужно догнать его и прямо обо всём спросить.")
         print("Или лучше ещё проследить и убедиться что он точно что-то знает?")
         print("1. Догнать и спросить")
         print("2. Проследить и убедиться")
         answer=input()
         os.system("cls")
         if answer=="1":
          while True:
           print(Style.BRIGHT + Fore.GREEN + "- Стой, подожди! - парень оглядывается на тебя, как и большинство людей в столовой.")
           print(Style.BRIGHT + Fore.GREEN + "- Изо дня в день я продолжаю просыпаться в библиотеке, все вокруг повторяется, ты единственный, чьи действия каждый день разнятся. Ты точно должен что-то знать, что происходит???")
           print(Style.BRIGHT + Fore.CYAN + "- Черт... Ты….  Ты не должна была узнать…  Подожди, я не понимаю… Ты что была в библиотеке в ночь со вторника на среду?")
           print(Style.BRIGHT + Fore.GREEN + "- Я готовилась к чему-то там и уснула прямо в библиотеке, да…")
           print(Style.BRIGHT + Fore.CYAN + "- О нет. Кажется мне нужно тебе кое-что рассказать… Пошли куда-нибудь подальше")
           print(Style.RESET_ALL)             
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break
           else:
            os.system("cls")      
          break        
         if answer=="2":
          while True:

              while True:
                print("Кажется он повернул к лестницам. Так, пошел наверх. На третьем этаже не свернул. Значит идет выше…")
                print("О, на четвертом пошел направо! Наверное, он сядет у автоматов.")
                print("Да, видимо я не одна люблю это место. Он сел за те столы. И что теперь делать?")
                print("Я же не могу пойти сесть напротив.. Сяду в коридоре. Да. Оттуда мне будет его видно.")
                ###Кнопка далее###
                skip=input()
                if skip=="":
                 os.system("cls")
                 break
                else:
                 os.system("cls")
                ##################      
              while True:
               print("*прошел час*")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break
               else:
                os.system("cls")
               ##################
              while True:    
               print("Надо все-таки к нему подойти. Я же не могу так сидеть вечно.")     
               print("Судя по всему, он просто сидит и пишет, иногда выходя за едой.")
               print("*Ты решаешься и подходишь*")
               print(Style.BRIGHT + Fore.GREEN + "- Хей! Можно к тебе подсесть?")
               print(Style.BRIGHT + Fore.CYAN + "- Да, конечно")
               print(Style.RESET_ALL + "*Долгие пять секунд молчания и ты замечаешь ужас осознания в глазах парня*")
               print(Style.BRIGHT + Fore.GREEN + "- Я хотела у тебя кое-что спросить")
               print(Style.BRIGHT + Fore.CYAN + "- Эммм, да?")
               print(Style.BRIGHT + Fore.GREEN + "- Уже три дня я просыпаюсь в библиотеке, все вокруг повторяется, ты единственный, чьи действия каждый день разнятся.")
               print(Style.BRIGHT + Fore.GREEN + "Ты точно должен что-то знать, что происходит???")
               print(Style.BRIGHT + Fore.CYAN + "- Чёрт... Ты…. Ты не должна была узнать… Подожди, я не понимаю…")
               print(Style.BRIGHT + Fore.CYAN + "Ты что была в библиотеке в ночь со вторника на среду?")
               print(Style.BRIGHT + Fore.GREEN + "- Я готовилась к чему-то там и уснула прямо в библиотеке, да…")
               print(Style.BRIGHT + Fore.CYAN + "- О нет. Кажется мне нужно тебе кое-что рассказать… / Пошли куда-нибудь подальше")
               print(Style.RESET_ALL)
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break
               else:
                os.system("cls")
               ##################
              break

         if answer!="1" or answer!="2":
          os.system("cls")
         if answer=="1" or answer=="2":
          os.system("cls")
          break      
   break

 while True:
  while True:
   print(Style.BRIGHT + Fore.CYAN + "В общем, глупая история на самом деле. Я до последнего тянул с написанием курсовой и дотянул до того, что через 3 дня сдача, а у меня ещё ничего не написано.")
   print(Style.BRIGHT + Fore.CYAN + "И я вспомнил, как дедушка в детстве рассказывал мне про колдовство и часто читал из одной книги.")
   print(Style.BRIGHT + Fore.CYAN + "Я тогда думал, что это всё сказки, но оказалось, что в книге описана настоящая магия.")
   print(Style.BRIGHT + Fore.CYAN + "Я долго думал, стоит ли оно того, ведь дедушка говорил, что пользоваться этим лучше только в самых крайних случаях.")
   print(Style.BRIGHT + Fore.CYAN + "И я решился. Временную петлю, как видишь, получилось наколдовать вполне успешно.")
   print(Style.BRIGHT + Fore.CYAN + "Прости, я не хотел, чтобы так вышло, я не думал, что хоть кто-то был тогда в библиотеке кроме меня, в петлю никто не должен был попасть никто, кроме меня.")
   print(Style.RESET_ALL)
   ###Кнопка далее###
   skip=input()
   if skip=="":
    os.system("cls")
    break;
   else:
    os.system("cls")


  while True:
   print(Style.BRIGHT + Fore.GREEN + "- Что….. Это не может быть правдой…. Это всё один большой страшный сон. Но как же… Но что же теперь делать? Я не хочу проживать этот день снова и снова.")
   print(Style.RESET_ALL)
   ###Кнопка далее###
   skip=input()
   if skip=="":
    os.system("cls")
    break;
   else:
    os.system("cls")
    
  while True:
   if cofe=="1":
    print(Style.BRIGHT + Fore.CYAN + "- Извини конечно, но я не собираюсь отменять петлю только ради тебя. Тебе придётся подождать, пока я закончу курсовую.")
    print(Style.RESET_ALL)
   if cofe=="0":
    print(Style.BRIGHT + Fore.CYAN + "- Блин, мне очень жаль, но я не могу отменить всё сейчас… Я всё ещё не дописал курсовую, и это правда очень важно!")
    print(Style.RESET_ALL)  
   ###Кнопка далее###
   skip=input()
   if skip=="":
    os.system("cls")
    break;
   else:
    os.system("cls")    
   #################
  while True:
   print(Style.BRIGHT + Fore.GREEN + "- Ну и что же мне теперь делать?")
   print(Style.RESET_ALL)
   ###Кнопка далее###
   skip=input()
   if skip=="":
    os.system("cls")
    break;
   else:
    os.system("cls")
  while True:
   print("1. Разобраться во всем самой")
   print("2. Помочь парню написать курсовую чтобы все быстрее закончилось")
   print("3. Я же тоже могу воспользоваться этим бесконечным днем....")
   otv=input()

   os.system("cls")
   if otv!="1" or otv!="2" or otv!="3":
      os.system("cls")
   if otv=="1":
       finish="1"
       while True:
           print(Style.BRIGHT + Fore.GREEN + "- А что если ты будешь писать свою курсовую ещё месяц? Я не собираюсь торчать здесь всё это время!")
           print(Style.BRIGHT + Fore.CYAN + "- И что же ты собираешься делать?")
           print(Style.BRIGHT + Fore.GREEN + "- Я… Я….. не знаю, что-нибудь придумаю")
           print(Style.RESET_ALL)
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################       
       while True:
           print("*Ты бродишь по корпусу и ноги доводят до библиотеки. Нужно присесть.*")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("В библиотеке довольно пусто, ты садишься на диванчик и начинаешь думать.Что же делать?")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("Получается, что единственный выбор, который у меня есть, это попытаться самой отменить петлю. Но вот как?")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("Вдруг ты заметила, как что-то блеснуло из-под подушки на соседнем диване. Что это такое?")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("Ты подходишь, поднимаешь подушку и видишь довольно потрепанную книгу. Ты открываешь её и видишь непонятные надписи, размытые картинки.")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("Это же… книга, о которой говорил этот странный парень. Неужели он оставил её лежать здесь просто так? Как глупо… Но это тебе на руку! Ты же могу сама попытаться отменить петлю!!!")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("Только, вот бы разобраться, что здесь написано… Выглядит знакомо, кажется, это на латыни. Можно попробовать перевести со словарём, кажется, в библиотеке был…")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print("Спустя долгие часы перевода ты находишь нужный раздел: “Mutato tempus”. Отлично, осталось только разобраться в том, что же нужно сделать. Кажется вот оно, нужное место:")
           ###Кнопка далее###
           skip=input()
           if skip=="":
            os.system("cls")
            break;
           else:
            os.system("cls")    
           ##################
       while True:
           print(Style.BRIGHT + Fore.MAGENTA + "------------------------------------------------------------------")
           print(Style.BRIGHT + Fore.MAGENTA + "Vos postulo ut reperio in desertum locum, ubi utique non est.")
           print(Style.BRIGHT + Fore.MAGENTA + "Ut illuc perveniant ad exacte XI horam in vespere. Praeparet omnia materiae:")
           print(Style.BRIGHT + Fore.MAGENTA + "hoc libro, vetus vigilia, et nihil aliud.")
           print(Style.BRIGHT + Fore.MAGENTA + "11:30 Et, vos postulo ut satus per manum vertit ad XII horologium prohibere non, ut prorsus in")
           print(Style.BRIGHT + Fore.MAGENTA + "media nocte in tempore horologium ostendit XII.")
           print(Style.BRIGHT + Fore.MAGENTA + "------------------------------------------------------------------")
           print(Style.RESET_ALL)
           print("Так, ага, взять книгу... часы… поворачивать стрелку, чтобы в полночь она оказалась на 12...Так, ну, допустим. Только вот…. в какую сторону крутить стрелки?")
           print("1. Против часовой ")
           print("2. По часовой")
           answer=input()
           os.system("cls")
           if answer=="1":
            while True:             
               print("Ты выполнила ритуал, поворачивая стрелку часов в обратном направлении.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print("Тааааак, ощущение, что ничего не произошло. И телефон как назло не включается. Нужно выйти из библиотеки и посмотреть, что там во внешнем мире.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Ты проходишь по корпусу и понимаешь, что все вокруг выглядит как-то странно. Почему стены другого цвета? Где все постеры?")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Ты доходишь до выхода и понимаешь, что раздевалка выглядит совсем по-другому… Все вокруг выглядит по-другому!")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Ты выходишь из здания и замечаешь, что и на улице всё совсем иначе, нет табличек у входа, нет парковки для велосипедов. Да что же это…")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Выбегаешь на улицу и видишь, что нет ни кофейни через дорогу, ни пиццерии, ни магазина вдалеке. И вообще всё выглядит… странно.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Ты замечаешь газетный киоск, подходишь и видишь что-то совсем странное…")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Календарь за 1993 год. Возможно, они просто зачем-то вывесили старый календарь и.. ")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Нет. На всех журналах и газетах стоит дата. 1993.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Ты возвращаешься к зданию корпуса, садишься на ступеньки. ")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Это не может быть правдой. Наверное, ты окончательно сошла с ума.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Это всё просто плод воображения твоего уставшего разума.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ################## 
            while True:
               print("Но что если… ")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################     

           if answer=="2":
            while True:
               print("Ты выполнила ритуал, поворачивая стрелку по обычному ходу часов. Но как понять, наступил ли новый день?")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################

            while True:
               print("Ты смотришь на экран телефона и…. ДАА!!! На календаре сменилась дата. ЭТО ПРАВДА СРАБОТАЛО!!!!")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print("Теперь надо как-то незаметно выйти из здания и добраться до дома. Ты почти доходишь до главного выхода, как вдруг тебя резко хватают за руку.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print(Style.BRIGHT + Fore.GREEN +"- Ай, что за..")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print(Style.BRIGHT + Fore.CYAN + "- Что ты наделала??!! Зачем ты расколдовала петлю? И главное как?")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print(Style.BRIGHT + Fore.GREEN +"- Я сказала тебе, что не собираюсь проживать этот день снова и снова.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print(Style.BRIGHT + Fore.GREEN +"Я не виновата в том, что у тебя проблемы с распределением времени, нужно было раньше начинать писать свою работу.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print(Style.RESET_ALL)
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print("Ты вырываешь свою руку из его и выбегаешь на улицу. Так, нужно быстро думать.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print("Сейчас только начало первого, метро ещё работает, отлично.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            while True:
               print("Ты бежишь к метро, только на середине дороги оборачиваешься и видишь, что он не бежал за тобой.")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
                
            while True:
               print("Ты добираешься до дома в целости и безопасности, с надеждой на то, что не будешь слишком часто натыкаться на этого странного парня в универе. ")
               print("")
               print("")
               ###Кнопка далее###
               skip=input()
               if skip=="":
                os.system("cls")
                break;
               else:
                os.system("cls")    
              ##################
            
           if answer!="1" or answer!="2":
            os.system("cls")
           if answer=="1" or answer=="2":
            os.system("cls")
            break
   if otv=="2":
      while True: 
       print(Style.BRIGHT + Fore.GREEN +"- Может быть я смогу как-то тебе помочь? Вдвоём мы закончим быстрее и быстрее выберемся из этой ситуации")
       print(Style.BRIGHT + Fore.CYAN + "- О, хорошая идея..")
       print(Style.BRIGHT + Fore.GREEN +"- А какая у тебя тема?")
       print(Style.BRIGHT + Fore.CYAN +"- Исследование влияния светового давления на движение астероида в проблеме астероидной опасности")
       print(Style.RESET_ALL)
       print("1. О, я тоже увлекаюсь астрономией ")
       print("2. Что, физика???!! ")    
       answer=input()
       os.system("cls")
       if answer=="1":
        while True:
         print(Style.BRIGHT + Fore.GREEN +"- Какая классная тема! Я тоже увлекаюсь астрономией, хотя учусь на лингвистике")   
         print(Style.BRIGHT + Fore.CYAN + "- Правда? это круто!")
         print(Style.BRIGHT + Fore.GREEN +"- Может быть я смогу помочь тебе с выбором литературы? я довольно много читала об этом.")
         print(Style.BRIGHT + Fore.CYAN + "- Ой, было бы классно. но кажется, мы до сих пор не представились? Я Саша")
         print(Style.BRIGHT + Fore.GREEN +"- Ой, и правда. очень приятно, я Аня!")
         print(Style.RESET_ALL)
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
         ##################
        while True:
             print("Вдвоём вам довольно быстро удалось закончить всю работу, поэтому уже через три дня Саша расколдовал петлю.")
             ###Кнопка далее###
             skip=input()
             if skip=="":
              os.system("cls")
              break;
             else:
              os.system("cls")    
            ##################
        while True:
             print("За это короткое время вы сблизились и даже стали друзьями. ")
             ###Кнопка далее###
             skip=input()
             if skip=="":
              os.system("cls")
              break;
             else:
              os.system("cls")    
            ##################
        while True:
             print("Эта история стала вашим секретом (потому что всё равно никто бы в неё не поверил).")
             ###Кнопка далее###
             skip=input()
             if skip=="":
              os.system("cls")
              break;
             else:
              os.system("cls")    
            ##################
       if answer=="2":
        while True:
         print(Style.BRIGHT + Fore.GREEN +"- Ой, ты что…. на физике")   
         print(Style.BRIGHT + Fore.CYAN + "- Эм, ну да")
         print(Style.BRIGHT + Fore.GREEN +"- Ну ладно, я тоже люблю звезды… может чем-нибудь и помогу. тебя хоть как звать-то?")
         print(Style.BRIGHT + Fore.CYAN + "- Ой, мы же и правда не познакомились даже.. я Саша")
         print(Style.BRIGHT + Fore.GREEN +"- Очень приятно, а я Аня")
         print(Style.BRIGHT + Fore.GREEN +"- Супер, тогда давай подумаем, чем ты можешь мне помочь. как у тебя с физикой?")   
         print(Style.BRIGHT + Fore.CYAN + "- Ну как тебе сказать….. плохо…")
         print(Style.BRIGHT + Fore.GREEN +"- Так, ладно. может, ты сможешь оформить список литературы и всё такое? это довольно простая работа, но занимает кучу времени.")
         print(Style.BRIGHT + Fore.CYAN + "- О, это я могу!")
         print(Style.RESET_ALL)
        ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ##################
        while True:
         print("Твоя вклад очень помог, работа пошла намного быстрее.")
        ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ##################
        while True:
         print("Уже через три дня вы внесли последние правки, и Саша расколдовал петлю. ")
        ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ##################
        while True:
         print("За это короткое время вы успели немного познакомиться, а эта история стала вашим общим секретом, что сблизило вас ещё больше. ")
        ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ##################
          
       if answer!="1" or answer!="2":
        os.system("cls")
       if answer=="1" or answer=="2":
        os.system("cls")
        break
   if otv=="3":
      while True: 
       print("1. Ходить на один и тот же концерт стаса михайлова целую неделю")
       print("2. Каждый день ходить в кино")
       print("3. Прочитать кучу полезных книжек по учёбе, доделать все долги")
       print("4. Каждый день рассказывать эту историю людям но они всё будут забывать")
       print("5. Отоспаться за всю жизнь пока есть время")
       answer=input()
       os.system("cls")
       if answer=="1":
        while True:
         print("Оказалось, что именно в этот день проходил концерт стаса михайлова, на который у тебя совершенно случайно был билет.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ##################
         
        while True:
         print("Целую неделю ты просыпалась в универе и проверяла, как идут дела у того парня с курсовой,")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("а после ходила на этот концерт снова и снова, пока однажды Саша")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("(ты увидела его имя на брелке на рюкзаке и долго подкалывала его по этому поводу) не сказал тебе, что дописал курсовую и сегодня отменит петлю.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ##################        
       if answer=="2":
        while True:
         print("Целую неделю ты просыпалась в библиотеке.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ################## 
        while True:
         print("За это время ты успела посмотреть всё, что шло в кино, а на некоторые фильмы даже сходила два раза.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("И вот наконец-то Саша (ты увидела его имя на брелке на рюкзаке и долго подкалывала его по этому поводу) сказал тебе, что дописал курсовую и сегодня отменит петлю.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ##################               
       if answer=="3":
        while True:
         print("Ты решила провести время с пользой и тоже заняться учёбой.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("Каждый день ты просыпалась в библиотеке, шла перекусить в столовую, а потом возвращалась обратно.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("Оказалось, целая свободная неделя была очень кстати: ты смогла доделать все долги и подготовиться к грядущим экзаменам.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("Спустя семь одинаковых дней Саша (вы познакомились за порцией гречки, когда однажды одновременно пришли в столовую) нашёл тебя и сказал, что закончил свою работу и теперь можно расколдовать петлю. ")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ##################             
       if answer=="4":
        while True:
         print("Каждый день ты ходила гулять с друзьями и каждый день рассказывала всю эту странную историю.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("некоторые удивлялись, некоторые смеялись и не верили, некоторые просто странно смотрели, но все они забывали об этом как только наступал новый (тот же самый) день.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("И вот спустя эту странную, но весёлую неделю Саша (вы познакомились за порцией гречки, когда однажды одновременно пришли в столовую) нашёл тебя и сказал, что закончил свою работу и теперь можно расколдовать петлю. ")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ##################                
       if answer=="5":
        while True:
         print("Ты решила провести это время с пользой и отоспаться за все бессонные ночи.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ################## 
        while True:
         print("Целыми днями ты только спала на диванчике в библиотеке и иногда ходила в столовую перекусить.")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
       ################## 
        while True:
         print("Целыми днями ты только спала на диванчике в библиотеке, ходила в столовую, читала в свое удовольствие и просто наслаждалась этим маленьким отпуском. ")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ################## 
        while True:
         print("Спустя семь одинаковых дней Саша (вы познакомились за порцией гречки, когда однажды одновременно пришли в столовую) нашёл тебя и сказал, что закончил свою работу и теперь можно расколдовать петлю. ")
         ###Кнопка далее###
         skip=input()
         if skip=="":
          os.system("cls")
          break;
         else:
          os.system("cls")    
        ##################   
       if answer!="1" or answer!="2" or answer!="3" or answer!="4" or answer!="5":
        os.system("cls")
       if answer=="1" or answer=="2" or answer=="3" or answer=="4" or answer=="5":
        os.system("cls")
        break
   if otv=="1" or otv=="2" or otv=="3":
      break        
  break
 if finish=="0":
  while True:
     print("Это было… приключение. Вряд ли ты сможешь рассказать об этом хоть кому-то и не поймать на себе взволнованный взгляд в ответ. ")
     print("Возможно когда-нибудь ты напишешь об этом книгу.")
     print("Или сделаешь игру…")
    ###Кнопка далее###
     skip=input()
     if skip=="":
      os.system("cls")
      break
     else:
      os.system("cls")
   ##################
  while True:
     print("Cпасибо за игру хотите началать сначала?")
     print("1. Да")
     print("2. Нет")
     answer=input()
     if answer=="1":
         os.system("cls")
         break        
     if answer=="2":
         exit()
     if answer!=1 or answer!=2:
         os.system("cls")
     else:
         break
 if finish=="1":
  while True:
     print("Cпасибо за игру хотите началать сначала?")
     print("1. Да")
     print("2. Нет")
     answer=input()
     if answer=="1":
         os.system("cls")
         break        
     if answer=="2":
         exit()
     if answer!=1 or answer!=2:
         os.system("cls")
     else:
         break













      
