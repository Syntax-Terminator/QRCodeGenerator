import qrcode
import os
import pygame
import sys

pygame.init()
pygame.font.init()

width = 800
height = 500

window = pygame.display.set_mode((width, height))
pygame.display.set_caption('QR CODE GENERATOR')

def render_font(x, y, text, size):
	base_font = pygame.font.Font("minecraft like.fon", size)
	render_font = base_font.render(text, True, (255, 255, 255))
	window.blit(render_font, (x, y))

button_rect = pygame.Rect(470 - 180, 140 + 50, 135, 40)
button_color = pygame.Color("Green")
base_font = pygame.font.Font("minecraft like.fon", 24)
button_text = base_font.render("Generate", True, pygame.Color("Black"))
user_input = ""
load_qrcode = False
button_color2 = pygame.Color("Green")
button_text2 = base_font.render("Open in Explorer", True, pygame.Color("Black"))
button_rect2 = pygame.Rect(button_rect.x + button_rect.w + 20, button_rect.y, 230, 40)

input_rect = pygame.Rect(295, 150 - 6, 140, 32)
color = pygame.Color("white")
bruh_color = pygame.Color("lightskyblue")
box_select = False

draw_error_message = False

FPS = 60
clock = pygame.time.Clock()	

def qr_code():
	global final_img
	img = qrcode.make(user_input)
	img.save("Qrcode.png")
	os.system("start Qrcode.png")

def qr_code_generate():

	img = qrcode.make(user_input)
	img.save("Qrcode.png")
	bruh = pygame.image.load("Qrcode.png")
	final_bruh = pygame.transform.scale(bruh, (200, 200))
	window.blit(final_bruh, (290, 250))

while True:

	clock.tick(FPS)

	mouse = pygame.mouse.get_pos()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if box_select:
				if event.key == pygame.K_BACKSPACE:
					user_input = user_input[:-1]
				else:
					user_input += event.unicode

				if event.key == pygame.K_RETURN:
					box_select = False

		if mouse[0] > input_rect.x and mouse[0] < input_rect.x + input_rect.w and mouse[1] > input_rect.y and mouse[1] < input_rect.y + input_rect.h and event.type == pygame.MOUSEBUTTONDOWN:
			box_select = True

		elif event.type == pygame.MOUSEBUTTONDOWN and mouse[0] < input_rect.x or event.type == pygame.MOUSEBUTTONDOWN and mouse[0] > input_rect.x + input_rect.w or event.type == pygame.MOUSEBUTTONDOWN and mouse[1] < input_rect.y or event.type == pygame.MOUSEBUTTONDOWN and mouse[1] > input_rect.y + input_rect.h:
			box_select = False

		if mouse[0] > button_rect.x and mouse[0] < button_rect.x + button_rect.w and mouse[1] > button_rect.y and mouse[1] < button_rect.y + button_rect.h:
			button_color = (0, 0, 255)
			if event.type == pygame.MOUSEBUTTONDOWN and user_input == "":
				font = pygame.font.Font("minecraft like.fon", 24)
				renderfont = font.render("pls enter somehting in order to generate QRCODE", True, pygame.Color("Red"))
				draw_error_message = True

			elif event.type == pygame.MOUSEBUTTONDOWN and user_input != "":
				#qr_code()
				draw_error_message = False
				load_qrcode = True



		elif mouse[0] < button_rect.x or mouse[0] > button_rect.x + button_rect.w or mouse[1] < button_rect.y or mouse[1] > button_rect.y + button_rect.h:
			button_color = pygame.Color("Green")

		if mouse[0] > button_rect2.x and mouse[0] < button_rect2.x + button_rect2.w and mouse[1] > button_rect2.y and mouse[1] < button_rect2.y + button_rect.h:
			button_color2 = pygame.Color("Red")
			if event.type == pygame.MOUSEBUTTONDOWN and user_input == "":
				font = pygame.font.Font("minecraft like.fon", 24)
				renderfont = font.render("pls enter somehting in order to generate QRCODE", True, pygame.Color("Red"))
				draw_error_message = True

			elif event.type == pygame.MOUSEBUTTONDOWN and user_input != "":
				qr_code()

		if mouse[0] < button_rect2.x or mouse[0] > button_rect2.x + button_rect2.w or mouse[1] < button_rect2.y or mouse[1] > button_rect2.y + button_rect.h:
			button_color2 = pygame.Color("Green")

	window.fill((0, 0, 0))

	base_font = pygame.font.Font(None, 24)

	text_surface = base_font.render(user_input, True, (255, 255, 255))

	render_font(width/2-220, height-(height-50), "QR CODE GENERATOR", 46)
	render_font(width/2-250, 150, "Enter Text: ", 24)

	input_rect.w = max(100, text_surface.get_width() + 10)

	pygame.draw.rect(window, color, input_rect, 2)

	pygame.draw.rect(window, button_color, button_rect)

	if box_select:
		pygame.draw.rect(window, (255, 0, 0), input_rect, 2)

	else:
		box_select = False

	window.blit(text_surface, (300, 150))
	window.blit(button_text, (button_rect.x + 5, button_rect.y+ 10))
	if draw_error_message:
		window.blit(renderfont, (150, 250))

	if load_qrcode:
		qr_code_generate()

	pygame.draw.rect(window, button_color2, button_rect2)
	window.blit(button_text2, (button_rect2.x + 5, button_rect2.y + 10))


	#window.blit(final_img, (230, 280))

	pygame.display.update()