import pygame
import sys
import os


# To do: organize button code into functions so code is more compact
# User: Joyce Hu

# working directory variable
workingdir = os.getcwd()

# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()


# Create a Pygame window
screen = pygame.display.set_mode((1240,930))
pygame.display.set_caption('TCHS Interactive Map')


# Load map
map = pygame.image.load('graphics/map_copy.png')


# Load images of school
rm_601_image = pygame.image.load(workingdir +'/graphics/601.png')
staff_lounge_image = pygame.image.load(workingdir + '/graphics/staff_lounge.png')
rm_216_image = pygame.image.load(workingdir + '/graphics/214.png')
rm_215_image = pygame.image.load(workingdir + '/graphics/214.png')
rm_214_image = pygame.image.load(working + '/graphics/214.png')
RR_1_image = pygame.image.load(workingdir + '/graphics/214.png')
rm_116_image = pygame.image.load(workingdir + '/graphics/116.png')
rm_115_image = pygame.image.load(workingdir + '/graphics/115.png')
rm_114_image = pygame.image.load(workingdir + '/graphics/114.png')
RR_2_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_213_image = pygame.image.load(workingdir + '/graphics/213.png')
rm_113_image = pygame.image.load(workingdir + '/graphics/113.png')
rm_108_image = pygame.image.load(workingdir + '/graphics/108.png')
rm_208_image = pygame.image.load(workingdir + '/graphics/208.png')
rm_212_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_211_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_210_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_209_image = pygame.image.load(workingdir + '/graphics/601.png')
RR_3_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_112_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_111_image = pygame.image.load(workingdir + '/graphics/601.png')
rm_110_image = pygame.image.load(workingdir + '/graphics/110.png')
rm_109_image = pygame.image.load(workingdir + '/graphics/601.png')
RR_4_image = pygame.image.load(workingdir + '/graphics/601.png')


# Create current screen variable
current_screen = map
# Create a font object
font = pygame.font.Font(None, 33)
font1 = pygame.font.Font(None, 25)


# Create a surface for the button
rm_601_button_surface = pygame.Surface((50, 25))
staff_lounge_button_surface = pygame.Surface((115, 51))
rm_216_button_surface = pygame.Surface((50, 25))
rm_215_button_surface = pygame.Surface((50, 25))
rm_214_button_surface = pygame.Surface((50, 25))
RR_1_button_surface = pygame.Surface((50, 25))
rm_116_button_surface = pygame.Surface((50, 25))
rm_115_button_surface = pygame.Surface((50, 25))
rm_114_button_surface = pygame.Surface((50, 25))
RR_2_button_surface = pygame.Surface((50, 25))
rm_213_button_surface = pygame.Surface((50, 25))
rm_113_button_surface = pygame.Surface((50, 25))
rm_108_button_surface = pygame.Surface((50, 25))
rm_208_button_surface = pygame.Surface((50, 25))
rm_212_button_surface = pygame.Surface((50, 25))
rm_211_button_surface = pygame.Surface((50, 25))
rm_210_button_surface = pygame.Surface((50, 25))
rm_209_button_surface = pygame.Surface((50, 25))
RR_3_button_surface = pygame.Surface((50, 25))
rm_112_button_surface = pygame.Surface((50, 25))
rm_111_button_surface = pygame.Surface((50, 25))
rm_110_button_surface = pygame.Surface((50, 25))
rm_109_button_surface = pygame.Surface((50, 25))
RR_4_button_surface = pygame.Surface((50, 25))


# Render text on the button
rm_601_text = font.render("601", True, (0, 0, 0))
rm_601_text_rect = rm_601_text.get_rect(center=(rm_601_button_surface.get_width()/2, rm_601_button_surface.get_height()/2))


staff_lounge_text = font1.render("Staff Lounge", True, (0, 0, 0))
staff_lounge_text_rect = staff_lounge_text.get_rect(center=(staff_lounge_button_surface.get_width()/2, staff_lounge_button_surface.get_height()/2))


rm_216_text = font.render("216", True, (0, 0, 0))
rm_216_text_rect = rm_216_text.get_rect(center=(rm_216_button_surface.get_width()/2, rm_216_button_surface.get_height()/2))


rm_215_text = font.render("215", True, (0, 0, 0))
rm_215_text_rect = rm_215_text.get_rect(center=(rm_215_button_surface.get_width()/2, rm_215_button_surface.get_height()/2))


rm_214_text = font.render("214", True, (0, 0, 0))
rm_214_text_rect = rm_214_text.get_rect(center=(rm_214_button_surface.get_width()/2, rm_214_button_surface.get_height()/2))


RR_1_text = font.render("RR", True, (0, 0, 0))
RR_1_text_rect = RR_1_text.get_rect(center=(RR_1_button_surface.get_width()/2, RR_1_button_surface.get_height()/2))


rm_116_text = font.render("116", True, (0, 0, 0))
rm_116_text_rect = rm_116_text.get_rect(center=(rm_116_button_surface.get_width()/2, rm_116_button_surface.get_height()/2))


rm_115_text = font.render("115", True, (0, 0, 0))
rm_115_text_rect = rm_115_text.get_rect(center=(rm_115_button_surface.get_width()/2, rm_115_button_surface.get_height()/2))


rm_114_text = font.render("114", True, (0, 0, 0))
rm_114_text_rect = rm_114_text.get_rect(center=(rm_114_button_surface.get_width()/2, rm_114_button_surface.get_height()/2))


RR_2_text = font.render("RR", True, (0, 0, 0))
RR_2_text_rect = RR_2_text.get_rect(center=(RR_2_button_surface.get_width()/2, RR_2_button_surface.get_height()/2))


rm_213_text = font.render("213", True, (0, 0, 0))
rm_213_text_rect = rm_213_text.get_rect(center=(rm_213_button_surface.get_width()/2, rm_213_button_surface.get_height()/2))


rm_113_text = font.render("113", True, (0, 0, 0))
rm_113_text_rect = rm_113_text.get_rect(center=(rm_113_button_surface.get_width()/2, rm_113_button_surface.get_height()/2))


rm_108_text = font.render("108", True, (0, 0, 0))
rm_108_text_rect = rm_108_text.get_rect(center=(rm_108_button_surface.get_width()/2, rm_108_button_surface.get_height()/2))


rm_208_text = font.render("208", True, (0, 0, 0))
rm_208_text_rect = rm_208_text.get_rect(center=(rm_208_button_surface.get_width()/2, rm_208_button_surface.get_height()/2))


rm_212_text = font.render("212", True, (0, 0, 0))
rm_212_text_rect = rm_212_text.get_rect(center=(rm_212_button_surface.get_width()/2, rm_212_button_surface.get_height()/2))


rm_211_text = font.render("211", True, (0, 0, 0))
rm_211_text_rect = rm_211_text.get_rect(center=(rm_211_button_surface.get_width()/2, rm_211_button_surface.get_height()/2))


rm_210_text = font.render("210", True, (0, 0, 0))
rm_210_text_rect = rm_210_text.get_rect(center=(rm_210_button_surface.get_width()/2, rm_210_button_surface.get_height()/2))


rm_209_text = font.render("209", True, (0, 0, 0))
rm_209_text_rect = rm_209_text.get_rect(center=(rm_209_button_surface.get_width()/2, rm_209_button_surface.get_height()/2))


RR_3_text = font.render("RR", True, (0, 0, 0))
RR_3_text_rect = RR_3_text.get_rect(center=(RR_3_button_surface.get_width()/2, RR_3_button_surface.get_height()/2))


rm_112_text = font.render("112", True, (0, 0, 0))
rm_112_text_rect = rm_112_text.get_rect(center=(rm_112_button_surface.get_width()/2, rm_112_button_surface.get_height()/2))


rm_111_text = font.render("111", True, (0, 0, 0))
rm_111_text_rect = rm_111_text.get_rect(center=(rm_111_button_surface.get_width()/2, rm_111_button_surface.get_height()/2))


rm_110_text = font.render("110", True, (0, 0, 0))
rm_110_text_rect = rm_110_text.get_rect(center=(rm_110_button_surface.get_width()/2, rm_110_button_surface.get_height()/2))


rm_109_text = font.render("109", True, (0, 0, 0))
rm_109_text_rect = rm_109_text.get_rect(center=(rm_109_button_surface.get_width()/2, rm_109_button_surface.get_height()/2))


RR_4_text = font.render("RR", True, (0, 0, 0))
RR_4_text_rect = RR_4_text.get_rect(center=(RR_4_button_surface.get_width()/2, RR_4_button_surface.get_height()/2))


# Create a pygame.Rect object that represents the button's boundaries
rm_601_button_rect = pygame.Rect(775, 400, 50, 25)  # Adjust the position as needed
staff_lounge_button_rect = pygame.Rect(743, 268, 115, 51)
rm_216_button_rect = pygame.Rect(847, 655, 50, 25)
rm_215_button_rect = pygame.Rect(904, 655, 50, 25)
rm_214_button_rect = pygame.Rect(960, 655, 50, 25)
RR_1_button_rect = pygame.Rect(1016, 655, 50, 25)
rm_116_button_rect = pygame.Rect(847, 690, 50, 25)
rm_115_button_rect = pygame.Rect(904, 690, 50, 25)
rm_114_button_rect = pygame.Rect(960, 690, 50, 25)
RR_2_button_rect = pygame.Rect(1015, 690, 50, 25)
rm_213_button_rect = pygame.Rect(1133, 655, 50, 25)
rm_113_button_rect = pygame.Rect(1133, 692, 50, 25)
rm_108_button_rect = pygame.Rect(1133, 773, 50, 25)
rm_208_button_rect = pygame.Rect(1133, 738, 50, 25)
rm_212_button_rect = pygame.Rect(795, 738, 50, 25)
rm_211_button_rect = pygame.Rect(852, 738, 50, 25)
rm_210_button_rect = pygame.Rect(908, 738, 50, 25)
rm_209_button_rect = pygame.Rect(963, 738, 50, 25)
RR_3_button_rect = pygame.Rect(1020, 738, 50, 25)
rm_112_button_rect = pygame.Rect(795, 773, 50, 25)
rm_111_button_rect = pygame.Rect(852, 773, 50, 25)
rm_110_button_rect = pygame.Rect(908, 773, 50, 25)
rm_109_button_rect = pygame.Rect(963, 773, 50, 25)
RR_4_button_rect = pygame.Rect(1020, 773, 50, 25)


# Create button hover effect function (to be called for each button)
def button_hover_effect(rect1, surface):
   if rect1.collidepoint(pygame.mouse.get_pos()):
       pygame.draw.rect(surface, (127, 255, 212), (1, 1, 148, 48))
   else:
       pygame.draw.rect(surface, (255, 255, 255), (0, 0, 150, 50))
       pygame.draw.rect(surface, (255, 255, 255), (1, 1, 148, 48))
       pygame.draw.rect(surface, (255, 255, 255), (1, 1, 148, 1), 2)
       pygame.draw.rect(surface, (255, 255, 255), (1, 48, 148, 10), 2)


# Start the main loop
while True:
   # Set the frame rate
   clock.tick(60)


   # Fill the display with color
   screen.fill((155, 255, 155))


   # Get events from the event queue
   for event in pygame.event.get():
       # Check for the quit event
       if event.type == pygame.QUIT:
           # Quit the game
           pygame.quit()
           sys.exit()


       # Check for the mouse button down event
       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_601_button_rect.collidepoint(event.pos):
               current_screen = rm_601_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if staff_lounge_button_rect.collidepoint(event.pos):
               current_screen = staff_lounge_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_216_button_rect.collidepoint(event.pos):
               current_screen = rm_216_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_215_button_rect.collidepoint(event.pos):
               current_screen = rm_215_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_214_button_rect.collidepoint(event.pos):
               current_screen = rm_214_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if RR_1_button_rect.collidepoint(event.pos):
               current_screen = RR_1_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_116_button_rect.collidepoint(event.pos):
               current_screen = rm_116_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_115_button_rect.collidepoint(event.pos):
               current_screen = rm_115_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_114_button_rect.collidepoint(event.pos):
               current_screen = rm_114_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if RR_2_button_rect.collidepoint(event.pos):
               current_screen = RR_2_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_213_button_rect.collidepoint(event.pos):
               current_screen = rm_213_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_113_button_rect.collidepoint(event.pos):
               current_screen = rm_113_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_108_button_rect.collidepoint(event.pos):
               current_screen = rm_108_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_208_button_rect.collidepoint(event.pos):
               current_screen = rm_208_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_212_button_rect.collidepoint(event.pos):
               current_screen = rm_212_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_211_button_rect.collidepoint(event.pos):
               current_screen = rm_211_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_210_button_rect.collidepoint(event.pos):
               current_screen = rm_210_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_209_button_rect.collidepoint(event.pos):
               current_screen = rm_209_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if RR_3_button_rect.collidepoint(event.pos):
               current_screen = RR_3_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_112_button_rect.collidepoint(event.pos):
               current_screen = rm_112_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_111_button_rect.collidepoint(event.pos):
               current_screen = rm_111_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_110_button_rect.collidepoint(event.pos):
               current_screen = rm_110_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if rm_109_button_rect.collidepoint(event.pos):
               current_screen = rm_109_image


       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           # Call the on_mouse_button_down() function
           if RR_4_button_rect.collidepoint(event.pos):
               current_screen = RR_4_image


   # Check if the mouse is over the button. This will create the button hover effect
   button_hover_effect(rm_601_button_rect, rm_601_button_surface)
   button_hover_effect(staff_lounge_button_rect, staff_lounge_button_surface)
   button_hover_effect(rm_216_button_rect, rm_216_button_surface)
   button_hover_effect(rm_215_button_rect, rm_215_button_surface)
   button_hover_effect(rm_214_button_rect, rm_214_button_surface)
   button_hover_effect(RR_1_button_rect, RR_1_button_surface)
   button_hover_effect(rm_116_button_rect, rm_116_button_surface)
   button_hover_effect(rm_115_button_rect, rm_115_button_surface)
   button_hover_effect(rm_114_button_rect, rm_114_button_surface)
   button_hover_effect(RR_2_button_rect, RR_2_button_surface)
   button_hover_effect(rm_213_button_rect, rm_213_button_surface)
   button_hover_effect(rm_113_button_rect, rm_113_button_surface)
   button_hover_effect(rm_108_button_rect, rm_108_button_surface)
   button_hover_effect(rm_208_button_rect, rm_208_button_surface)
   button_hover_effect(rm_212_button_rect, rm_212_button_surface)
   button_hover_effect(rm_211_button_rect, rm_211_button_surface)
   button_hover_effect(rm_210_button_rect, rm_210_button_surface)
   button_hover_effect(rm_209_button_rect, rm_209_button_surface)
   button_hover_effect(RR_3_button_rect, RR_3_button_surface)
   button_hover_effect(rm_112_button_rect, rm_112_button_surface)
   button_hover_effect(rm_111_button_rect, rm_111_button_surface)
   button_hover_effect(rm_110_button_rect, rm_110_button_surface)
   button_hover_effect(rm_109_button_rect, rm_109_button_surface)
   button_hover_effect(RR_4_button_rect, RR_4_button_surface)


   # Show the button text
   rm_601_button_surface.blit(rm_601_text, rm_601_text_rect)
   staff_lounge_button_surface.blit(staff_lounge_text, staff_lounge_text_rect)
   rm_216_button_surface.blit(rm_216_text, rm_216_text_rect)
   rm_215_button_surface.blit(rm_215_text, rm_215_text_rect)
   rm_214_button_surface.blit(rm_214_text, rm_214_text_rect)
   RR_1_button_surface.blit(RR_1_text, RR_1_text_rect)
   rm_116_button_surface.blit(rm_116_text, rm_116_text_rect)
   rm_115_button_surface.blit(rm_115_text, rm_115_text_rect)
   rm_114_button_surface.blit(rm_114_text, rm_114_text_rect)
   RR_2_button_surface.blit(RR_2_text, RR_2_text_rect)
   rm_213_button_surface.blit(rm_213_text, rm_213_text_rect)
   rm_113_button_surface.blit(rm_113_text, rm_113_text_rect)
   rm_108_button_surface.blit(rm_108_text, rm_108_text_rect)
   rm_208_button_surface.blit(rm_208_text, rm_208_text_rect)
   rm_212_button_surface.blit(rm_212_text, rm_212_text_rect)
   rm_211_button_surface.blit(rm_211_text, rm_211_text_rect)
   rm_210_button_surface.blit(rm_210_text, rm_210_text_rect)
   rm_209_button_surface.blit(rm_209_text, rm_209_text_rect)
   RR_3_button_surface.blit(RR_3_text, RR_3_text_rect)
   rm_112_button_surface.blit(rm_112_text, rm_112_text_rect)
   rm_111_button_surface.blit(rm_111_text, rm_111_text_rect)
   rm_110_button_surface.blit(rm_110_text, rm_110_text_rect)
   rm_109_button_surface.blit(rm_109_text, rm_109_text_rect)
   RR_4_button_surface.blit(RR_4_text, RR_4_text_rect)


   # Draw the map and button on the screen
   if current_screen == map:
       screen.blit(current_screen,(0,0)) # controls test_surface location
       screen.blit(rm_601_button_surface, (rm_601_button_rect.x, rm_601_button_rect.y))
       screen.blit(staff_lounge_button_surface, (staff_lounge_button_rect.x, staff_lounge_button_rect.y))
       screen.blit(rm_216_button_surface, (rm_216_button_rect.x, rm_216_button_rect.y))
       screen.blit(rm_215_button_surface, (rm_215_button_rect.x, rm_215_button_rect.y))
       screen.blit(rm_214_button_surface, (rm_214_button_rect.x, rm_214_button_rect.y))
       screen.blit(RR_1_button_surface, (RR_1_button_rect.x, RR_1_button_rect.y))
       screen.blit(rm_116_button_surface, (rm_116_button_rect.x, rm_116_button_rect.y))
       screen.blit(rm_115_button_surface, (rm_115_button_rect.x, rm_115_button_rect.y))
       screen.blit(rm_114_button_surface, (rm_114_button_rect.x, rm_114_button_rect.y))
       screen.blit(RR_2_button_surface, (RR_2_button_rect.x, RR_2_button_rect.y))
       screen.blit(rm_213_button_surface, (rm_213_button_rect.x, rm_213_button_rect.y))
       screen.blit(rm_113_button_surface, (rm_113_button_rect.x, rm_113_button_rect.y))
       screen.blit(rm_108_button_surface, (rm_108_button_rect.x, rm_108_button_rect.y))
       screen.blit(rm_208_button_surface, (rm_208_button_rect.x, rm_208_button_rect.y))
       screen.blit(rm_212_button_surface, (rm_212_button_rect.x, rm_212_button_rect.y))
       screen.blit(rm_211_button_surface, (rm_211_button_rect.x, rm_211_button_rect.y))
       screen.blit(rm_210_button_surface, (rm_210_button_rect.x, rm_210_button_rect.y))
       screen.blit(rm_209_button_surface, (rm_209_button_rect.x, rm_209_button_rect.y))
       screen.blit(RR_3_button_surface, (RR_3_button_rect.x, RR_3_button_rect.y))
       screen.blit(rm_112_button_surface, (rm_112_button_rect.x, rm_112_button_rect.y))
       screen.blit(rm_111_button_surface, (rm_111_button_rect.x, rm_111_button_rect.y))
       screen.blit(rm_110_button_surface, (rm_110_button_rect.x, rm_110_button_rect.y))
       screen.blit(rm_109_button_surface, (rm_109_button_rect.x, rm_109_button_rect.y))
       screen.blit(RR_4_button_surface, (RR_4_button_rect.x, RR_4_button_rect.y))
   elif current_screen == rm_601_image:
       screen.blit(current_screen,(0,0))
   elif current_screen == staff_lounge_image:
       screen.blit(current_screen,(0,0))
   elif current_screen == rm_216_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_215_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_214_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_116_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_213_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_115_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_114_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_113_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_108_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_208_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_212_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_211_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_210_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_209_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == RR_3_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_112_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_111_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_110_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == rm_109_image:
       screen.blit(current_screen, (0, 0))
   elif current_screen == RR_4_image:
       screen.blit(current_screen, (0, 0))


   # Update the game state
   pygame.display.update()
