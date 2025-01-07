# GBF SPARK CALCULATOR

print('''Welcome to GBF Spark Calculator by Mikey.
This is a simple project made from python.''')

def xtall_counter():
    one_draw = 300
    ten_draw = 3000
    one_spark = 90000
    try:
        player_xtall = int(input("How many xtall you have now?\n"))
        player_10_tix = int(input("How many 10 draw tickets you have now?\n"))
        player_1_tix = int(input("How many 1 draw  tickets you have now?\n"))
        ten_draw_to_xtall = player_10_tix * ten_draw
        one_draw_to_xtall = player_1_tix * one_draw
        total_for_spark = player_xtall + ten_draw_to_xtall + one_draw_to_xtall
        print(total_for_spark)
    except ValueError:
        print("Must be a number!")
        xtall_counter()
    spark = total_for_spark / one_spark
    rolls_counter = total_for_spark / 300
    if total_for_spark >= one_spark:
        print(f"You can do {round(spark)} spark, you have {round(rolls_counter)} draw")
    elif total_for_spark < one_spark:
        print(f"You can't spark, you only have {round(rolls_counter)} draw")
    
        
xtall_counter()
