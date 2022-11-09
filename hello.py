print("\nWELCOME TO MY TRIVIA GAME\n"
      "Answer 5 questions about me\n"
      "Correct Answer = +100\n"
      "Wrong Answer = -50\n")

score = 0
fav_food = "Pizza"
fav_sport = "Soccer"
fav_color = "Red"
fav_book = "SOAR"
fav_hobby = "Hiking"

ans_food = input("\nWhat is my favorite Food? ")
if ans_food.upper() == fav_food.upper():
    score += 100
    print("Correct Answer\n"
          "Score: ", score)
else:
    score -= 50
    print("Wrong Answer\n"
          "Score: ", score)

ans_sport = input("\nWhat is my favorite Sport? ")
if ans_sport.upper() == fav_sport.upper():
    score += 100
    print("Correct Answer\n"
          "Score: ", score)
else:
    score -= 50
    print("Wrong Answer\n"
          "Score: ", score)

ans_color = input("\nWhat is my favorite Color? ")
if ans_color.upper() == fav_color.upper():
    score += 100
    print("Correct Answer\n"
          "Score: ", score)
else:
    score -= 50
    print("Wrong Answer\n"
          "Score: ", score)

print("\nTotal Score: ", score, "\n"
      "Favorite Food: ", fav_food, "\n"
      "Favorite Sport: ", fav_sport, "\n"
      "Favorite Color: ", fav_color, "\n"
      "Favorite Book: ", fav_book, "\n"
      "Favorite Hobby: ", fav_hobby)
