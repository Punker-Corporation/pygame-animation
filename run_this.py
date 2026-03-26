import subprocess
import sys

try:
    import pygame
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame


pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Dont be sad.py")
clock = pygame.time.Clock()

running = True
start_screen = True

stick_x = -40
stick_y = 180
target_x = 180
arm_offset = 0
arm_direction = 1
wave_start_time = None
wave_duration = 1150
final_arm_offset = 5
pause_after_wave_start = None
pause_after_wave_duration = 1000
search_start_time = None
search_duration = 1500
pause_before_poster_start = None
pause_before_poster_duration = 1000
poster_visible = False
poster_display_start = None
poster_message_duration = 3000
dance_frame_duration = 220

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            start_screen = False

    screen.fill((0, 0, 0))

    if start_screen:
        font = pygame.font.Font(None, 36)
        text = font.render("Press Enter!", True, (255, 255, 255))
        screen.blit(text, (120, 125))
    else:
        torso_x = stick_x
        torso_top_y = stick_y - 28
        torso_bottom_y = stick_y + 10
        head_x = stick_x
        head_y = stick_y - 40
        left_arm_end = (stick_x - 15, stick_y)
        right_arm_end = (stick_x + 18, stick_y - 17 - arm_offset)
        left_elbow = None
        right_elbow = None
        left_leg_end = (stick_x - 12, stick_y + 30)
        right_leg_end = (stick_x + 12, stick_y + 30)

        poster_width = 300
        poster_height = 40
        poster_end_x = stick_x - 150
        poster_end_y = stick_y - 95
        poster_messages = ["Hello Lavi!", "how you doing?", "hope you're doing well.", "since you were sad yesterday", "i wanted to cheer you up!", "so i made this for you...", "i hope it works!", "whenever you feel sad", "just remember:", "there is people", "that started coding...", "because you encourage,", "and help us!", "me...", "raposo...", "and everyone else who you encourage!", "(not to mention punker corps...)", "I don't know you very well...", "but I already consider you a friend.", "You must be tired...", "maybe discouraged...", "or going through a personal problem...", "but know that:", "if it weren't for you...", "i wouldn't be here.", "i wouldn't have started coding...", "or making a silly animation like this (haha)", "And I know others think the same.", "So on behalf of all of us...", "thank you very much, Lavi!", "If you want to talk about your problems...", "or just want to chat...", "i'm here for you!", "and so are everyone else!", "we all care about you!", "and we want to see you happy!", "if this wasn't enough to cheer you up...", "then take a look at those moves!!"]
        dance_mode = False

        if stick_x < target_x:
            stick_x += 2
        else:
            if wave_start_time is None:
                wave_start_time = pygame.time.get_ticks()

            elapsed = pygame.time.get_ticks() - wave_start_time

            if elapsed < wave_duration:
                arm_offset += arm_direction * 2
                if arm_offset > 5 or arm_offset < -5:
                    arm_direction *= -1
            else:
                arm_offset = final_arm_offset
                now = pygame.time.get_ticks()

                if pause_after_wave_start is None:
                    pause_after_wave_start = now
                elif now - pause_after_wave_start < pause_after_wave_duration:
                    pass
                else:
                    if search_start_time is None:
                        search_start_time = now

                    search_elapsed = now - search_start_time

                    if search_elapsed < search_duration:
                        pose = (search_elapsed // 250) % 2

                        if pose == 0:
                            torso_x = stick_x - 6
                            head_x = torso_x - 4
                            left_elbow = (torso_x - 18, stick_y - 8)
                            left_arm_end = (torso_x - 1, stick_y - 4)
                            right_elbow = (torso_x + 15, stick_y - 6)
                            right_arm_end = (torso_x + 1, stick_y - 6)
                        else:
                            torso_x = stick_x + 6
                            head_x = torso_x + 4
                            left_elbow = (torso_x - 15, stick_y - 6)
                            left_arm_end = (torso_x - 1, stick_y - 6)
                            right_elbow = (torso_x + 18, stick_y - 8)
                            right_arm_end = (torso_x + 1, stick_y - 4)

                        left_leg_end = (torso_x - 10, stick_y + 30)
                        right_leg_end = (torso_x + 8, stick_y + 28)
                    else:
                        if pause_before_poster_start is None:
                            pause_before_poster_start = now
                        elif now - pause_before_poster_start >= pause_before_poster_duration:
                            poster_visible = True
                            if poster_display_start is None:
                                poster_display_start = now
                            left_arm_end = (stick_x - 45, stick_y - 45)
                            right_arm_end = (stick_x + 45, stick_y - 45)

        poster_x = stick_x - (poster_width / 2)
        poster_y = stick_y - 95

        if poster_visible and poster_display_start is not None:
            poster_elapsed = pygame.time.get_ticks() - poster_display_start
            if poster_elapsed >= len(poster_messages) * poster_message_duration:
                dance_mode = True

        if dance_mode:
            dance_frame = (pygame.time.get_ticks() // dance_frame_duration) % 4
            dance_drop = 10 if dance_frame in (1, 3) else 0
            face_right = dance_frame in (0, 1)
            dance_arm_start_y = stick_y - 8 + dance_drop

            torso_x = stick_x
            torso_top_y = stick_y - 28 + dance_drop
            torso_bottom_y = stick_y + 10 + dance_drop
            head_x = stick_x
            head_y = stick_y - 40 + dance_drop

            if face_right:
                left_arm_end = (stick_x + 28, stick_y - 8 + dance_drop)
                right_arm_end = (stick_x + 28, stick_y + 10 + dance_drop)
            else:
                left_arm_end = (stick_x - 28, stick_y - 8 + dance_drop)
                right_arm_end = (stick_x - 28, stick_y + 10 + dance_drop)

            left_elbow = None
            right_elbow = None
            left_leg_end = (stick_x - 18, stick_y + 34 + dance_drop)
            right_leg_end = (stick_x + 18, stick_y + 34 + dance_drop)

        pygame.draw.circle(screen, (255, 255, 255), (int(head_x), int(head_y)), 12, 2)
        pygame.draw.line(screen, (255, 255, 255), (int(torso_x), int(torso_top_y)), (int(torso_x), int(torso_bottom_y)), 2)

        if poster_visible and not dance_mode:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (int(torso_x), stick_y - 15),
                left_arm_end,
                2,
            )
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (int(torso_x), stick_y - 15),
                right_arm_end,
                2,
            )
        else:
            if left_elbow is not None and right_elbow is not None:
                pygame.draw.line(screen, (255, 255, 255), (int(torso_x), stick_y - 15), left_elbow, 2)
                pygame.draw.line(screen, (255, 255, 255), left_elbow, left_arm_end, 2)
                pygame.draw.line(screen, (255, 255, 255), (int(torso_x), stick_y - 15), right_elbow, 2)
                pygame.draw.line(screen, (255, 255, 255), right_elbow, right_arm_end, 2)
            else:
                arm_start_y = dance_arm_start_y if dance_mode else stick_y - 15
                pygame.draw.line(screen, (255, 255, 255), (int(torso_x), int(arm_start_y)), left_arm_end, 2)
                pygame.draw.line(screen, (255, 255, 255), (int(torso_x), int(arm_start_y)), right_arm_end, 2)

        pygame.draw.line(screen, (255, 255, 255), (int(torso_x), int(torso_bottom_y)), left_leg_end, 2)
        pygame.draw.line(screen, (255, 255, 255), (int(torso_x), int(torso_bottom_y)), right_leg_end, 2)

        if poster_visible and not dance_mode:
            poster_elapsed = pygame.time.get_ticks() - poster_display_start
            poster_index = min(poster_elapsed // poster_message_duration, len(poster_messages) - 1)
            poster_message = poster_messages[int(poster_index)]
            pygame.draw.rect(
                screen,
                (255, 255, 255),
                (int(poster_x), int(poster_y), poster_width, poster_height),
                3,
            )
            poster_font = pygame.font.Font(None, 20)
            poster_text = poster_font.render(poster_message, True, (255, 255, 255))
            poster_text_rect = poster_text.get_rect(center=(int(poster_x + poster_width / 2), int(poster_y + poster_height / 2)))
            screen.blit(poster_text, poster_text_rect)

    pygame.display.flip()
    clock.tick(24)

pygame.quit()
