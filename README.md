i declared a bunch of things in the first lines;
then created the character usin x and y dots "torso_top_y = stick_y - 28", "torso_bottom_y = stick_y + 10" and connecting the dots;
made the character move using "if stick_x < target_x:";
made a retangular poster centered on the stickman "poster_x = stick_x - (poster_width / 2)";
with a message inside it using "poster_text = poster_font.render(poster_message, True, (255, 255, 255))poster_text_rect = poster_text.get_rect(center=(int(poster_x + poster_width / 2), int(poster_y + poster_height / 2)));
