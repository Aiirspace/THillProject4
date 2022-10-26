import arcade
#Travis Hill
my_file = open("nationsPop.txt", "r")
all_lines = my_file.readlines()
for line in all_lines:
    print(line)
words = line.split(" ")


my_window = arcade.open_window(1920,1000,"My Drawing")
my_text = arcade.Text("100M", 50,100, arcade.color.DEEP_SPACE_SPARKLE)
my_text2 = arcade.Text("200M", 50,200, arcade.color.DEEP_SPACE_SPARKLE)
my_text3 = arcade.Text("300M", 50,300, arcade.color.DEEP_SPACE_SPARKLE)
my_text4 = arcade.Text("400M", 50,400, arcade.color.DEEP_SPACE_SPARKLE)
my_text5 = arcade.Text("500M", 50,500, arcade.color.DEEP_SPACE_SPARKLE)
my_text6 = arcade.Text("600M", 50,600, arcade.color.DEEP_SPACE_SPARKLE)
my_text7 = arcade.Text("700M", 50,700, arcade.color.DEEP_SPACE_SPARKLE)
my_text8 = arcade.Text("800M", 50,800, arcade.color.DEEP_SPACE_SPARKLE)
my_text9 = arcade.Text("900M+", 50,900, arcade.color.DEEP_SPACE_SPARKLE)
my_text10 = arcade.Text("China", 100,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text11 = arcade.Text("India", 200,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text12 = arcade.Text("USA", 300,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text13 = arcade.Text("Indonesia", 400,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text14 = arcade.Text("Pakistan", 500,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text15 = arcade.Text("Nigeria", 600,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text16 = arcade.Text("Brazil", 700,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text17 = arcade.Text("Bangladesh", 800,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text18 = arcade.Text("Russia", 900,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text19 = arcade.Text("Mexico", 1000,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text20 = arcade.Text("Japan", 1100,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text21 = arcade.Text("Ethiopia", 1200,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text22 = arcade.Text("Philippines", 1300,50, arcade.color.DEEP_SPACE_SPARKLE)
my_text23 = arcade.Text("Egypt", 1400,50, arcade.color.DEEP_SPACE_SPARKLE)








arcade.set_background_color(arcade.color.DIAMOND)
arcade.start_render()
arcade.draw_line(100,100,1900,100,arcade.color.BABY_POWDER, 5)
arcade.draw_line(100,100,100,1000,arcade.color.BABY_POWDER,5)
arcade.draw_xywh_rectangle_filled(110,100, 50, 900, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(210,100, 50, 850, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(310,100, 50, 250, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(410,100, 50, 150, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(510,100, 50, 100, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(610,100, 50, 75, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(710,100, 50, 50, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(810,100, 50, 40, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(910,100, 50, 30, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(1010,100, 50, 25, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(1110,100, 50, 20, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(1210,100, 50, 15, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(1310,100, 50, 10, arcade.color.BOSTON_UNIVERSITY_RED)
arcade.draw_xywh_rectangle_filled(1410,100, 50, 5, arcade.color.BOSTON_UNIVERSITY_RED)




my_text.draw()
my_text2.draw()
my_text3.draw()
my_text4.draw()
my_text5.draw()
my_text6.draw()
my_text7.draw()
my_text8.draw()
my_text9.draw()
my_text10.draw()
my_text11.draw()
my_text12.draw()
my_text13.draw()
my_text14.draw()
my_text15.draw()
my_text16.draw()
my_text17.draw()
my_text18.draw()
my_text19.draw()
my_text20.draw()
my_text21.draw()
my_text22.draw()
my_text23.draw()
arcade.finish_render()
arcade.run()







