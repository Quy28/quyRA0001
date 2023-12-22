import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("UEH Student")

# Load file hình nền 
background = pygame.image.load('background_image.png')
background = pygame.transform.scale(background, (800, 600))

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font chữ
font = pygame.font.Font(None, 36)
# Hàm hiển thị thông báo luật chơi
def show_rules_screen():
    rules = True
    while rules:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Nhấn SPACE để bắt đầu chơi
                    rules = False

        screen.fill((255, 255, 255))  # Màn hình trắng

        # Hiển thị luật chơi
        intro_font = pygame.font.Font(None, 36)
        intro_text = intro_font.render("RULE:", True, (0, 0, 0))
        screen.blit(intro_text, (50, 50))

        rules_text = [
            "1. Collect good qualities to score points.",
            "2. Move the mouse cursor to collect qualities.",
            "3. Time for each play is 30 seconds.",
            "4. Try to score the highest score!",
            "Press SPACE to start."
        ]
        for i, text in enumerate(rules_text):
            rule = intro_font.render(text, True, (0, 0, 0))
            screen.blit(rule, (50, 100 + i * 40))

        pygame.display.update()

# Điểm số ban đầu và biến đếm
score = 0

# Hình ảnh các phẩm chất của sinh viên tốt
volunteer_img = pygame.image.load('volunteer.png')
good_healthy_img = pygame.image.load('good_healthy.png')
communication_skills_img = pygame.image.load('communication_skills.png')
study_skills_img = pygame.image.load('study_skills.png')

# Hình ảnh các phẩm chất đã resize
volunteer = pygame.transform.scale(volunteer_img, (50, 50))
good_healthy = pygame.transform.scale(good_healthy_img, (50, 50))
communication_skills = pygame.transform.scale(communication_skills_img, (50, 50))
study_skills = pygame.transform.scale(study_skills_img, (50, 50))

# Tốc độ rơi của các tiêu chí
fall_speed = 1

# Tọa độ ban đầu của các tiêu chí
volunteer_x, volunteer_y = random.randint(50, 750), -50
good_healthy_x, good_healthy_y = random.randint(50, 750), -50
communication_skills_x, communication_skills_y = random.randint(50, 750), -50
study_skills_x, study_skills_y = random.randint(50, 750), -50

# Hình ảnh con trỏ chuột
cursor_image = pygame.image.load('custom_cursor.png')
pygame.mouse.set_visible(False)  # Ẩn con trỏ chuột mặc định

# Thời gian chơi
game_time = 30  # 30 giây 
start_time = pygame.time.get_ticks() // 1000  # Thời gian bắt đầu tính từ khi khởi động

# Hàm vẽ các tiêu chí, phẩm chất
def draw_qualities():
    screen.blit(volunteer, (volunteer_x, volunteer_y))
    screen.blit(good_healthy, (good_healthy_x, good_healthy_y))
    screen.blit(communication_skills, (communication_skills_x, communication_skills_y))
    screen.blit(study_skills, (study_skills_x, study_skills_y))

# Hàm xử lý va chạm và điểm số
def collision_check():
    global score, volunteer_y, good_healthy_y, communication_skills_y, study_skills_y
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if volunteer_x < mouse_x < volunteer_x + 50 and volunteer_y < mouse_y < volunteer_y + 50:
        volunteer_y = -50
        score += 5
    if good_healthy_x < mouse_x < good_healthy_x + 50 and good_healthy_y < mouse_y < good_healthy_y + 50:
        good_healthy_y = -50
        score += 5
    if communication_skills_x < mouse_x < communication_skills_x + 50 and communication_skills_y < mouse_y < communication_skills_y + 50:
        communication_skills_y = -50
        score += 5
    if study_skills_x < mouse_x < study_skills_x + 50 and study_skills_y < mouse_y < study_skills_y + 50:
        study_skills_y = -50
        score += 5
# Hàm hiển thị điểm số và kết quả
def show_score_result():
    text = font.render(f"SCORE: {score}", True, BLACK)
    screen.blit(text, (10, 10))

    result = ""
    if score >= 90:
        result = "EXCELLENT"
    elif 80 <= score <= 89:
        result = "VERY GOOD"
    elif 70 <= score <= 79:
        result = "GOOD"
    elif 60 <= score <= 69:
        result = "PASS"
    else:
        result = "NOT PASS"

    result_text = font.render(f"RESULT: {result}", True, BLACK)
    screen.blit(result_text, (10, 50))
# Hiển thị thời gian còn lại lên màn hình
    current_time = pygame.time.get_ticks() // 1000
    time_left = game_time - (current_time - start_time)
    time_text = font.render(f"time left: {time_left} s", True, BLACK)
    screen.blit(time_text, (600, 10))
# Hàm hiển thị điểm số và kết quả cuối cùng
def display_final_score(score):
    screen.fill((255, 255, 255))  # Xóa màn hình
    final_result_text = font.render(f"final score: {score}", True, (0, 0, 0))
    screen.blit(final_result_text, (200, 200))
    final_result = ""
    if score >= 90:
        final_result = "EXCELLENT"
    elif 80 <= score < 90:
        final_result = "VERYGOOD"
    elif 70 <= score < 80:
        final_result = "GOOD"
    elif 60 <= score < 70:
        final_result = "PASS"
    else:
        final_result = "NOT PASS"
    final_result_text = font.render(f"final result: {final_result}", True, (0, 0, 0))
    screen.blit(final_result_text, (200, 250))
    pygame.display.update()
    pygame.time.wait(5000)  # Chờ 5 giây trước khi thoát
    
# Vòng lặp chính
running = True
clock = pygame.time.Clock()
show_rules_screen()  # Hiển thị luật chơi trước khi bắt đầu
while running:
    screen.blit(background, (0, 0))  # Vẽ hình nền
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
    current_time = pygame.time.get_ticks() // 1000
    time_left = game_time - (current_time - start_time)
    if time_left <= 0:
        running = False
    # Rơi phẩm chất
    volunteer_y += fall_speed
    good_healthy_y += fall_speed
    communication_skills_y += fall_speed
    study_skills_y += fall_speed

    # Kiểm tra va chạm và cập nhật điểm số
    collision_check()

    # Vẽ phẩm chất
    draw_qualities()

    # Hiển thị điểm số và kết quả
    show_score_result()

    # Thay đổi hình ảnh con trỏ chuột
    mouse_pos = pygame.mouse.get_pos()
    screen.blit(cursor_image, mouse_pos)

    pygame.display.update()
    clock.tick(60)
# Khi kết thúc thời gian, hiển thị điểm số cuối cùng và xếp loại
display_final_score(score)
pygame.quit()