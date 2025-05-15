seconds = int(input("Введіть кількість секунд: "))

days = seconds // (24 * 60 * 60)
remainder = seconds % (24 * 60 * 60)

hours = remainder // 3600
remainder %= 3600

minutes = remainder // 60
secs = remainder % 60

if days % 10 == 1 and days != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"

time_str = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(secs).zfill(2)}"

print(f"{days} {day_word}, {time_str}")