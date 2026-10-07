[баламут.py](https://github.com/user-attachments/files/33149346/default.py)
import random
print("========================================")
print("       ЛЕГЕНДА О БЕДНОМ СТУДЕНТЕ")
print("========================================")
print("Баламут — обычный бедный студент.")
print("Сегодня он проспал и опаздывает в колледж.")
print("Если он не придёт, его ждёт отчисление!")
print()
print("Будильник звонит. Баламут должен решить, что делать.")
print()
print("1 - Встать и пойти в колледж")
print("2 - Выключить будильник и поспать")
vubor = input("Твой выбор: ")
if vubor == "1":
    print()
    print("Баламут вскочил с кровати и побежал в колледж!")
    print("Но впереди его ждут опасные приключения...")
elif vubor == "2":
    print()
    print("Баламут выключил будильник и лёг спать.")
    print("Прошло три часа...")
    print("Поздравляем! Баламут отчислен!")
    print("game over")
else:
    print()
    print("Баламут не понял, что происходит, и снова лёг спать.")
    print("game over")
class personazh:
    def __init__ (self, imya, zdorovie, sila):
        self.imya = imya
        self.zdorovie = zdorovie
        self.sila = sila
    def obychnaya_ataka(self, vrag):
        uron = random. randit(5, self.sila)
        vrag.zdorovie -= uron
        print(self.imya, "нанес", uron, "урона")
    def zhiv(self):
        return self.zdorovie > 0
class balamut(personazh):
    def __init__(self):
        super().__init__("баламут", 100, 15)
        self.superudary = 4
    def super_ataka(self, vrag):
        if self.superudar > 0:
            uron = random.rendit(25, 40)
            vrag.zdorovie -= uron
            self.superudary -= 1
            print("баламут использовал СУПЕРУДАР")
            print("нанесено урона:", uron)
            print("осталось суперударов:", self.superudary)
        else:
            print("у баламута закончились суперудары")
            
    
