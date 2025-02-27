import pygame
import sys


# User: Joyce Hu


# Initialize Pygame
pygame.init()


clock = pygame.time.Clock()


# Create a Pygame window
screen = pygame.display.set_mode((1240, 930))
pygame.display.set_caption('TCHS Interactive Map')

# Load map
map = pygame.image.load('graphics/map_copy.png')


# Load images of school
# Red
rm_601_image = pygame.image.load('graphics/601.png')
staff_lounge_image = pygame.image.load('graphics/staff_lounge.png')
rm_216_image = pygame.image.load('graphics/214.png')
rm_215_image = pygame.image.load('graphics/214.png')
rm_214_image = pygame.image.load('graphics/214.png')
RR_1_image = pygame.image.load('graphics/214.png')
rm_116_image = pygame.image.load('graphics/116.png')
rm_115_image = pygame.image.load('graphics/115.png')
rm_114_image = pygame.image.load('graphics/114.png')
RR_2_image = pygame.image.load('graphics/601.png')
rm_213_image = pygame.image.load('graphics/213.png')
rm_113_image = pygame.image.load('graphics/113.png')
rm_108_image = pygame.image.load('graphics/108.png')
rm_208_image = pygame.image.load('graphics/208.png')
rm_212_image = pygame.image.load('graphics/601.png')
rm_211_image = pygame.image.load('graphics/601.png')
rm_210_image = pygame.image.load('graphics/601.png')
rm_209_image = pygame.image.load('graphics/601.png')
RR_3_image = pygame.image.load('graphics/601.png')
rm_112_image = pygame.image.load('graphics/601.png')
rm_111_image = pygame.image.load('graphics/601.png')
rm_110_image = pygame.image.load('graphics/110.png')
rm_109_image = pygame.image.load('graphics/601.png')
RR_4_image = pygame.image.load('graphics/601.png')
# Red
# Purple
RR_400_image = pygame.image.load('graphics/boys_ bathroom_200s.png')
rm_401_image = pygame.image.load('graphics/ROOM 401-1.PNG')
rm_402_image = pygame.image.load('graphics/ROOM 402-2.PNG')
rm_403_image = pygame.image.load('graphics/ROOM 403-1.PNG')
rm_404_image = pygame.image.load('graphics/ROOM 404-1.PNG')
rm_405_image = pygame.image.load('graphics/ROOM 405-1.PNG')
rm_406_image = pygame.image.load('graphics/ROOM 406-1.PNG')
rm_407_image = pygame.image.load('graphics/ROOM 407-1.PNG')
rm_408_image = pygame.image.load('graphics/ROOM 408-1.PNG')
rm_409_image = pygame.image.load('graphics/ROOM 409-1.PNG')
rm_410_image = pygame.image.load('graphics/ROOM 410-1.PNG')
# Purple
# Green
gym_image = pygame.image.load('graphics/Front Entrance to Gym.png')
gym_image = pygame.transform.scale(gym_image, (1240, 930))
tennis_image = pygame.image.load('graphics/Tennis Courts.png')
tennis_image = pygame.transform.scale(tennis_image, (1240, 930))
rm_702_image = pygame.image.load('graphics/Room 702 and Tennis Court Entrance.png')
rm_702_image = pygame.transform.scale(rm_702_image, (1240, 930))
circle_image = pygame.image.load('graphics/Senior Circle_1.png')
circle_image = pygame.transform.scale(circle_image, (1240, 930))
rm_703_image = pygame.image.load('graphics/601.png')
rm_703_image = pygame.transform.scale(rm_703_image, (1240, 930))
rm_704_image = pygame.image.load('graphics/700s side and gym stairs.png')
rm_704_image = pygame.transform.scale(rm_704_image, (1240, 930))
rm_705_image = pygame.image.load('graphics/room 705 (edt) and 704.png')
rm_705_image = pygame.transform.scale(rm_705_image, (1240, 930))
rm_706_image = pygame.image.load('graphics/room 706 and 707.png')
rm_706_image = pygame.transform.scale(rm_706_image, (1240, 930))
rm_707_image = pygame.image.load('graphics/room 707.png')
rm_707_image = pygame.transform.scale(rm_707_image, (1240, 930))
rm_708_image = pygame.image.load('graphics/601.png')
rm_708_image = pygame.transform.scale(rm_708_image, (1240, 930))
rm_709_image = pygame.image.load('graphics/Boys restroom and art room.png')
rm_709_image = pygame.transform.scale(rm_709_image, (1240, 930))
rm_801_image = pygame.image.load('graphics/601.png')
rm_801_image = pygame.transform.scale(rm_801_image, (1240, 930))
rm_802_image = pygame.image.load('graphics/601.png')
rm_802_image = pygame.transform.scale(rm_802_image, (1240, 930))
rr_1_image = pygame.image.load('graphics/room 707 windows and girls restroom.png')
rr_1_image = pygame.transform.scale(rr_1_image, (1240, 930))
weight_image = pygame.image.load('graphics/Weight Room.png')
weight_image = pygame.transform.scale(weight_image, (1240, 930))
# Green
# Yellow
rm_501_image = pygame.image.load('graphics/rm_501.png')
rm_501_image = pygame.transform.scale(rm_501_image, (1240, 930))
rm_502_image = pygame.image.load('graphics/rm_502.png')
rm_502_image = pygame.transform.scale(rm_502_image, (1240, 930))
rm_503_image = pygame.image.load('graphics/rm_503.png')
rm_503_image = pygame.transform.scale(rm_503_image, (1240, 930))
rm_504_image = pygame.image.load('graphics/rm_504.png')
rm_504_image = pygame.transform.scale(rm_504_image, (1240, 930))
rm_505_image = pygame.image.load('graphics/rm_505.png')
rm_505_image = pygame.transform.scale(rm_505_image, (1240, 930))
rm_506_image = pygame.image.load('graphics/rm_506.png')
rm_506_image = pygame.transform.scale(rm_506_image, (1240, 930))
rm_507_image = pygame.image.load('graphics/rm_507.png')
rm_507_image = pygame.transform.scale(rm_507_image, (1240, 930))
rm_508_image = pygame.image.load('graphics/rm_508.png')
rm_508_image = pygame.transform.scale(rm_508_image, (1240, 930))
rm_509_image = pygame.image.load('graphics/rm_509.png')
rm_509_image = pygame.transform.scale(rm_509_image, (1240, 930))
rm_510_image = pygame.image.load('graphics/rm_510.png')
rm_510_image = pygame.transform.scale(rm_510_image, (1240, 930))
rm_511_image = pygame.image.load('graphics/rm_511.png')
rm_511_image = pygame.transform.scale(rm_511_image, (1240, 930))
rm_512_image = pygame.image.load('graphics/rm_512.png')
rm_512_image = pygame.transform.scale(rm_512_image, (1240, 930))
rm_514_image = pygame.image.load('graphics/rm_514.png')
rm_514_image = pygame.transform.scale(rm_514_image, (1240, 930))
rm_515_image = pygame.image.load('graphics/rm_515.png')
rm_515_image = pygame.transform.scale(rm_515_image, (1240, 930))
rm_516_image = pygame.image.load('graphics/rm_516.png')
rm_516_image = pygame.transform.scale(rm_516_image, (1240, 930))
rm_517_image = pygame.image.load('graphics/rm_517.png')
rm_517_image = pygame.transform.scale(rm_517_image, (1240, 930))
RR_yellow_image = pygame.image.load('graphics/601.png')
RR_yellow_image = pygame.transform.scale(RR_yellow_image, (1240, 930))
# Yellow
# Blue
rm_905_image = pygame.image.load('graphics/601 Entrance.PNG')
rm_905_image = pygame.transform.scale(rm_905_image, (1240, 930))
rm_904_image = pygame.image.load('graphics/601 Entrance.PNG')
rm_904_image = pygame.transform.scale(rm_904_image, (1240, 930))
tennis_courts_image = pygame.image.load('graphics/601 Entrance.PNG')
tennis_courts_image = pygame.transform.scale(tennis_courts_image, (1240, 930))
lemon_parking_lot_image = pygame.image.load('graphics/601 Entrance.PNG')
lemon_parking_lot_image = pygame.transform.scale(lemon_parking_lot_image, (1240, 930))
lawn_image = pygame.image.load('graphics/601 Entrance.PNG')
lawn_image = pygame.transform.scale(lawn_image, (1240, 930))
media_center_image = pygame.image.load('graphics/601 Entrance.PNG')
media_center_image = pygame.transform.scale(media_center_image, (1240, 930))
senate_room_image = pygame.image.load('graphics/601 Entrance.PNG')
senate_room_image = pygame.transform.scale(senate_room_image, (1240, 930))
mc4_image = pygame.image.load('graphics/601 Entrance.PNG')
mc4_image = pygame.transform.scale(mc4_image, (1240, 930))
mc3_image = pygame.image.load('graphics/601 Entrance.PNG')
mc3_image = pygame.transform.scale(mc3_image, (1240, 930))
mc2_image = pygame.image.load('graphics/601 Entrance.PNG')
mc2_image = pygame.transform.scale(mc2_image, (1240, 930))
mc1_image = pygame.image.load('graphics/601 Entrance.PNG')
mc1_image = pygame.transform.scale(mc1_image, (1240, 930))
# Blue
# Orange
principal_office = pygame.image.load('graphics/principal_s_office.png')
principal_office = pygame.transform.scale(principal_office, (1240, 930))
nurse = pygame.image.load('graphics/nurse_s_office.png')
nurse = pygame.transform.scale(nurse, (1240, 930))
registrar = pygame.image.load('graphics/601.png')
registrar = pygame.transform.scale(registrar, (1240, 930))
conference_room = pygame.image.load('graphics/conference_room.png')
conference_room = pygame.transform.scale(conference_room, (1240, 930))
rm_311 = pygame.image.load('graphics/311_staff_entrance.png')
rm_311 = pygame.transform.scale(rm_311, (1240, 930))
attendance_office = pygame.image.load('graphics/attendance_office_inner_entrance.png')
attendance_office = pygame.transform.scale(attendance_office, (1240, 930))
rm_310 = pygame.image.load('graphics/rm_310.png')
rm_310 = pygame.transform.scale(rm_310, (1240, 930))
ccc = pygame.image.load('graphics/counseling_office.png')
ccc = pygame.transform.scale(ccc, (1240, 930))
rm_304 = pygame.image.load('graphics/rm_304.png')
rm_304 = pygame.transform.scale(rm_304, (1240, 930))
rr_orange = pygame.image.load('graphics/601.png')
rr_orange = pygame.transform.scale(rr_orange, (1240, 930))
rm_309 = pygame.image.load('graphics/601.png')
rm_309 = pygame.transform.scale(rm_309, (1240, 930))
rm_308 = pygame.image.load('graphics/601.png')
rm_308 = pygame.transform.scale(rm_308, (1240, 930))
rm_305 = pygame.image.load('graphics/rm_305.png')
rm_305 = pygame.transform.scale(rm_305, (1240, 930))
rm_306 = pygame.image.load('graphics/rm_306.png')
rm_306 = pygame.transform.scale(rm_306, (1240, 930))
rm_307 = pygame.image.load('graphics/rm_307.png')
rm_307 = pygame.transform.scale(rm_307, (1240, 930))
lunch = pygame.image.load('graphics/601.png')
lunch = pygame.transform.scale(lunch, (1240, 930))
# Orange
# Brown
rm_101_image = pygame.image.load('graphics/rm_101.png')
rm_101_image = pygame.transform.scale(rm_101_image, (1240, 930))
rm_102_image = pygame.image.load('graphics/rm_102.png')
rm_102_image = pygame.transform.scale(rm_102_image , (1240, 930))
rm_103_image = pygame.image.load('graphics/rm_103.png')
rm_103_image = pygame.transform.scale(rm_103_image, (1240, 930))
rm_104_image = pygame.image.load('graphics/rm_104.png')
rm_104_image = pygame.transform.scale(rm_104_image, (1240, 930))
rm_105_image = pygame.image.load('graphics/rm_105.png')
rm_105_image = pygame.transform.scale(rm_105_image, (1240, 930))
rm_106_image = pygame.image.load('graphics/rm_106.png')
rm_106_image = pygame.transform.scale(rm_106_image, (1240, 930))
rm_107_image = pygame.image.load('graphics/rm_107.png')
rm_107_image = pygame.transform.scale(rm_107_image, (1240, 930))
rm_201_image = pygame.image.load('graphics/rm_201.png')
rm_201_image = pygame.transform.scale(rm_201_image, (1240, 930))
rm_202_image = pygame.image.load('graphics/rm_202.png')
rm_202_image = pygame.transform.scale(rm_202_image, (1240, 930))
rm_203_image = pygame.image.load('graphics/rm_203.png')
rm_203_image = pygame.transform.scale(rm_203_image, (1240, 930))
rm_204_image = pygame.image.load('graphics/rm_204.png')
rm_204_image = pygame.transform.scale(rm_204_image, (1240, 930))
rm_205_image = pygame.image.load('graphics/rm_205.png')
rm_205_image = pygame.transform.scale(rm_205_image, (1240, 930))
rm_206_image = pygame.image.load('graphics/rm_206.png')
rm_206_image = pygame.transform.scale(rm_206_image, (1240, 930))
rm_207_image = pygame.image.load('graphics/rm_207.png')
rm_207_image = pygame.transform.scale(rm_207_image, (1240, 930))
rm_804_image = pygame.image.load('graphics/rm_804.png')
rm_804_image = pygame.transform.scale(rm_804_image, (1240, 930))
rm_805_image = pygame.image.load('graphics/601.png')
rm_805_image = pygame.transform.scale(rm_805_image, (1240, 930))
locker_image = pygame.image.load('graphics/locker.png')
locker_image = pygame.transform.scale(locker_image, (1240, 930))
pool_image = pygame.image.load('graphics/pool.png')
pool_image = pygame.transform.scale(pool_image, (1240, 930))
# Brown


# Create current screen variable
current_screen = map


# Create a font object
# Red
font = pygame.font.Font(None, 33)
font1 = pygame.font.Font(None, 25)
# Red
# Purple
font_400s = pygame.font.Font(None, 30)
font_400RR = pygame.font.Font(None, 20)
# Purple
# Green
midfont = pygame.font.Font(None, 20)
smallfont = pygame.font.Font(None, 15)
# Green
# Yellow
yfont = pygame.font.Font(None, 30)
yRRfont = pygame.font.Font(None, 20)
# Yellow
# Blue
mc_font = pygame.font.Font(None, 25)
senate_room_font = pygame.font.Font(None, 16)
# Blue
# Orange
PO_font = pygame.font.Font(None, 13)
font2 = pygame.font.Font(None, 30)
font3 = pygame.font.Font(None, 20)
font4 = pygame.font.Font(None, 18)
font5 = pygame.font.Font(None, 27)
nurse_font = pygame.font.Font(None, 28)  # ToBeUpdated by Orange - 'size' as applicable
rgr_font = pygame.font.Font(None, 28)  # ToBeUpdated by Orange - 'size' as applicable
# Orange


# Create a surface for the button
# Red
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
# Red
# Purple
RR_400_button_surface = pygame.Surface((36, 10))
rm_401_button_surface = pygame.Surface((36, 44))
rm_402_button_surface = pygame.Surface((36, 44))
rm_403_button_surface = pygame.Surface((36, 44))
rm_404_button_surface = pygame.Surface((36, 44))
rm_405_button_surface = pygame.Surface((36, 44))
rm_406_button_surface = pygame.Surface((36, 44))
rm_407_button_surface = pygame.Surface((36, 44))
rm_408_button_surface = pygame.Surface((36, 44))
rm_409_button_surface = pygame.Surface((36, 44))
rm_410_button_surface = pygame.Surface((36, 44))
# Purple
# Green
gym_button_surface = pygame.Surface((70, 50))
tennis_button_surface = pygame.Surface((39, 50))
circle_button_surface = pygame.Surface((49, 33))
rm_702_button_surface = pygame.Surface((50, 25))
rm_703_button_surface = pygame.Surface((48, 25))
rm_705_button_surface = pygame.Surface((23, 25))
rm_704_button_surface = pygame.Surface((23, 25))
rm_706_button_surface = pygame.Surface((21, 25))
rm_707_button_surface = pygame.Surface((21, 25))
rm_708_button_surface = pygame.Surface((21, 25))
rm_709_button_surface = pygame.Surface((25, 22))
rm_801_button_surface = pygame.Surface((22, 25))
rm_802_button_surface = pygame.Surface((22, 25))
rr_1_button_surface = pygame.Surface((21, 25))
weight_button_surface = pygame.Surface((30, 20))
# Green
# Yellow
rm_501_button_surface = pygame.Surface((35, 25))
rm_502_button_surface = pygame.Surface((37, 25))
rm_503_button_surface = pygame.Surface((37, 25))
rm_504_button_surface = pygame.Surface((37, 25))
rm_505_button_surface = pygame.Surface((36, 25))
rm_506_button_surface = pygame.Surface((35, 25))
rm_507_button_surface = pygame.Surface((35, 25))
rm_508_button_surface = pygame.Surface((38, 25))
rm_509_button_surface = pygame.Surface((38.5, 25))
rm_510_button_surface = pygame.Surface((35, 25))
rm_511_button_surface = pygame.Surface((35, 25))
rm_512_button_surface = pygame.Surface((35, 25))
rm_514_button_surface = pygame.Surface((35, 25))
rm_515_button_surface = pygame.Surface((35, 25))
rm_516_button_surface = pygame.Surface((35, 25))
rm_517_button_surface = pygame.Surface((35, 25))
RR_yellow_button_surface = pygame.Surface((35, 10.5))
# Yellow
# Blue
rm_905_button_surface = pygame.Surface((50, 25))
rm_904_button_surface = pygame.Surface((50, 25))
tennis_courts_button_surface = pygame.Surface((120, 25))
lemon_parking_lot_button_surface = pygame.Surface((124, 50))
lawn_button_surface = pygame.Surface((70, 35))
media_center_button_surface = pygame.Surface((120, 25))
senate_room_button_surface = pygame.Surface((80, 25))
mc1_button_surface = pygame.Surface((40, 25))
mc2_button_surface = pygame.Surface((40, 25))
mc3_button_surface = pygame.Surface((40, 25))
mc4_button_surface = pygame.Surface((40, 25))
# Blue
# Orange
PO_button_surface = pygame.Surface((43, 35))
nurse_button_surface = pygame.Surface((36, 24))
rgr_button_surface = pygame.Surface((38, 24))
conf_button_surface = pygame.Surface((43, 35))
rm_311_button_surface = pygame.Surface((40, 35))
attendance_button_surface = pygame.Surface((40, 35))
rm_310_button_surface = pygame.Surface((60, 35))
ccc_button_surface = pygame.Surface((100, 35))
rm_304_button_surface = pygame.Surface((27, 25))
rr_orange_button_surface = pygame.Surface((16, 40))
rm_309_button_surface = pygame.Surface((30, 25))
rm_308_button_surface = pygame.Surface((30, 25))
rm_305_button_surface = pygame.Surface((30, 25))
rm_306_button_surface = pygame.Surface((25, 25))
rm_307_button_surface = pygame.Surface((25, 25))
lunch_button_surface = pygame.Surface((65, 30))
# Orange
# Brown
pool_button_surface = pygame.Surface((50, 25))
rm_804_button_surface = pygame.Surface((50, 25))
rm_805_button_surface = pygame.Surface((50, 25))
locker_rooms_button_surface = pygame.Surface((50, 25))
rm_207_button_surface = pygame.Surface((50, 25))
rm_206_button_surface = pygame.Surface((50, 25))
rm_205_button_surface = pygame.Surface((50, 25))
rm_204_button_surface = pygame.Surface((50, 25))
rm_203_button_surface = pygame.Surface((50, 25))
rm_202_button_surface = pygame.Surface((50, 25))
rm_201_button_surface = pygame.Surface((50, 25))
rm_107_button_surface = pygame.Surface((50, 25))
rm_106_button_surface = pygame.Surface((50, 25))
rm_105_button_surface = pygame.Surface((50, 25))
rm_104_button_surface = pygame.Surface((50, 25))
rm_103_button_surface = pygame.Surface((50, 25))
rm_102_button_surface = pygame.Surface((50, 25))
rm_101_button_surface = pygame.Surface((50, 25))
# Brown
# Back
back_button_surface = pygame.Surface((100, 50))
# Back

# Render text on the button

# Red
rm_601_text = font.render("601", True, (0, 0, 0))
rm_601_text_rect = rm_601_text.get_rect(
 center=(rm_601_button_surface.get_width() / 2, rm_601_button_surface.get_height() / 2))

staff_lounge_text = font1.render("Staff Lounge", True, (0, 0, 0))
staff_lounge_text_rect = staff_lounge_text.get_rect(
 center=(staff_lounge_button_surface.get_width() / 2, staff_lounge_button_surface.get_height() / 2))

rm_216_text = font.render("216", True, (0, 0, 0))
rm_216_text_rect = rm_216_text.get_rect(
 center=(rm_216_button_surface.get_width() / 2, rm_216_button_surface.get_height() / 2))

rm_215_text = font.render("215", True, (0, 0, 0))
rm_215_text_rect = rm_215_text.get_rect(
 center=(rm_215_button_surface.get_width() / 2, rm_215_button_surface.get_height() / 2))

rm_214_text = font.render("214", True, (0, 0, 0))
rm_214_text_rect = rm_214_text.get_rect(
 center=(rm_214_button_surface.get_width() / 2, rm_214_button_surface.get_height() / 2))

RR_1_text = font.render("RR", True, (0, 0, 0))
RR_1_text_rect = RR_1_text.get_rect(center=(RR_1_button_surface.get_width() / 2, RR_1_button_surface.get_height() / 2))

rm_116_text = font.render("116", True, (0, 0, 0))
rm_116_text_rect = rm_116_text.get_rect(
 center=(rm_116_button_surface.get_width() / 2, rm_116_button_surface.get_height() / 2))

rm_115_text = font.render("115", True, (0, 0, 0))
rm_115_text_rect = rm_115_text.get_rect(
 center=(rm_115_button_surface.get_width() / 2, rm_115_button_surface.get_height() / 2))

rm_114_text = font.render("114", True, (0, 0, 0))
rm_114_text_rect = rm_114_text.get_rect(
 center=(rm_114_button_surface.get_width() / 2, rm_114_button_surface.get_height() / 2))

RR_2_text = font.render("RR", True, (0, 0, 0))
RR_2_text_rect = RR_2_text.get_rect(center=(RR_2_button_surface.get_width() / 2, RR_2_button_surface.get_height() / 2))

rm_213_text = font.render("213", True, (0, 0, 0))
rm_213_text_rect = rm_213_text.get_rect(
 center=(rm_213_button_surface.get_width() / 2, rm_213_button_surface.get_height() / 2))

rm_113_text = font.render("113", True, (0, 0, 0))
rm_113_text_rect = rm_113_text.get_rect(
 center=(rm_113_button_surface.get_width() / 2, rm_113_button_surface.get_height() / 2))

rm_108_text = font.render("108", True, (0, 0, 0))
rm_108_text_rect = rm_108_text.get_rect(
 center=(rm_108_button_surface.get_width() / 2, rm_108_button_surface.get_height() / 2))

rm_208_text = font.render("208", True, (0, 0, 0))
rm_208_text_rect = rm_208_text.get_rect(
 center=(rm_208_button_surface.get_width() / 2, rm_208_button_surface.get_height() / 2))

rm_212_text = font.render("212", True, (0, 0, 0))
rm_212_text_rect = rm_212_text.get_rect(
 center=(rm_212_button_surface.get_width() / 2, rm_212_button_surface.get_height() / 2))

rm_211_text = font.render("211", True, (0, 0, 0))
rm_211_text_rect = rm_211_text.get_rect(
 center=(rm_211_button_surface.get_width() / 2, rm_211_button_surface.get_height() / 2))

rm_210_text = font.render("210", True, (0, 0, 0))
rm_210_text_rect = rm_210_text.get_rect(
 center=(rm_210_button_surface.get_width() / 2, rm_210_button_surface.get_height() / 2))

rm_209_text = font.render("209", True, (0, 0, 0))
rm_209_text_rect = rm_209_text.get_rect(
 center=(rm_209_button_surface.get_width() / 2, rm_209_button_surface.get_height() / 2))

RR_3_text = font.render("RR", True, (0, 0, 0))
RR_3_text_rect = RR_3_text.get_rect(center=(RR_3_button_surface.get_width() / 2, RR_3_button_surface.get_height() / 2))

rm_112_text = font.render("112", True, (0, 0, 0))
rm_112_text_rect = rm_112_text.get_rect(
 center=(rm_112_button_surface.get_width() / 2, rm_112_button_surface.get_height() / 2))

rm_111_text = font.render("111", True, (0, 0, 0))
rm_111_text_rect = rm_111_text.get_rect(
 center=(rm_111_button_surface.get_width() / 2, rm_111_button_surface.get_height() / 2))

rm_110_text = font.render("110", True, (0, 0, 0))
rm_110_text_rect = rm_110_text.get_rect(
 center=(rm_110_button_surface.get_width() / 2, rm_110_button_surface.get_height() / 2))

rm_109_text = font.render("109", True, (0, 0, 0))
rm_109_text_rect = rm_109_text.get_rect(
 center=(rm_109_button_surface.get_width() / 2, rm_109_button_surface.get_height() / 2))

RR_4_text = font.render("RR", True, (0, 0, 0))
RR_4_text_rect = RR_4_text.get_rect(center=(RR_4_button_surface.get_width() / 2, RR_4_button_surface.get_height() / 2))
# Red

# Purple
RR_400_text = font_400RR.render("RR", True, (0, 0, 0))
RR_400_text_rect = RR_400_text.get_rect(
 center=(RR_400_button_surface.get_width() / 2, RR_400_button_surface.get_height() / 2))

rm_401_text = font_400s.render("401", True, (0, 0, 0))
rm_401_text_rect = rm_401_text.get_rect(
 center=(rm_401_button_surface.get_width() / 2, rm_401_button_surface.get_height() / 2))

rm_402_text = font_400s.render("402", True, (0, 0, 0))
rm_402_text_rect = rm_402_text.get_rect(
 center=(rm_402_button_surface.get_width() / 2, rm_402_button_surface.get_height() / 2))

rm_403_text = font_400s.render("403", True, (0, 0, 0))
rm_403_text_rect = rm_403_text.get_rect(
 center=(rm_403_button_surface.get_width() / 2, rm_403_button_surface.get_height() / 2))

rm_404_text = font_400s.render("404", True, (0, 0, 0))
rm_404_text_rect = rm_404_text.get_rect(
 center=(rm_404_button_surface.get_width() / 2, rm_404_button_surface.get_height() / 2))

rm_405_text = font_400s.render("405", True, (0, 0, 0))
rm_405_text_rect = rm_405_text.get_rect(
 center=(rm_405_button_surface.get_width() / 2, rm_405_button_surface.get_height() / 2))

rm_406_text = font_400s.render("406", True, (0, 0, 0))
rm_406_text_rect = rm_406_text.get_rect(
 center=(rm_406_button_surface.get_width() / 2, rm_406_button_surface.get_height() / 2))

rm_407_text = font_400s.render("407", True, (0, 0, 0))
rm_407_text_rect = rm_407_text.get_rect(
 center=(rm_407_button_surface.get_width() / 2, rm_407_button_surface.get_height() / 2))

rm_408_text = font_400s.render("408", True, (0, 0, 0))
rm_408_text_rect = rm_408_text.get_rect(
 center=(rm_408_button_surface.get_width() / 2, rm_408_button_surface.get_height() / 2))

rm_409_text = font_400s.render("409", True, (0, 0, 0))
rm_409_text_rect = rm_409_text.get_rect(
 center=(rm_409_button_surface.get_width() / 2, rm_409_button_surface.get_height() / 2))

rm_410_text = font_400s.render("410", True, (0, 0, 0))
rm_410_text_rect = rm_410_text.get_rect(
 center=(rm_410_button_surface.get_width() / 2, rm_410_button_surface.get_height() / 2))
# Purple

# Green
gym_text = font.render("Gym", True, (0, 0, 0))
gym_text_rect = gym_text.get_rect(center=(gym_button_surface.get_width() / 2, gym_button_surface.get_height() / 2))

tennis_text = smallfont.render("Tennis", True, (0, 0, 0))
tennis_text_rect = tennis_text.get_rect(
 center=(tennis_button_surface.get_width() / 2, tennis_button_surface.get_height() / 2))

rm_702_text = font.render("702", True, (0, 0, 0))
rm_702_text_rect = rm_702_text.get_rect(
 center=(rm_702_button_surface.get_width() / 2, rm_702_button_surface.get_height() / 2))

circle_text = smallfont.render("Sr. Circle", True, (0, 0, 0))
circle_text_rect = circle_text.get_rect(
 center=(circle_button_surface.get_width() / 2, circle_button_surface.get_height() / 2))

rm_703_text = font.render("703", True, (0, 0, 0))
rm_703_text_rect = rm_703_text.get_rect(
 center=(rm_703_button_surface.get_width() / 2, rm_703_button_surface.get_height() / 2))

rm_705_text = midfont.render("705", True, (0, 0, 0))
rm_705_text_rect = rm_705_text.get_rect(
 center=(rm_705_button_surface.get_width() / 2, rm_705_button_surface.get_height() / 2))

rm_704_text = midfont.render("704", True, (0, 0, 0))
rm_704_text_rect = rm_704_text.get_rect(
 center=(rm_704_button_surface.get_width() / 2, rm_704_button_surface.get_height() / 2))

rm_706_text = midfont.render("706", True, (0, 0, 0))
rm_706_text_rect = rm_706_text.get_rect(
 center=(rm_706_button_surface.get_width() / 2, rm_706_button_surface.get_height() / 2))

rm_707_text = midfont.render("707", True, (0, 0, 0))
rm_707_text_rect = rm_707_text.get_rect(
 center=(rm_707_button_surface.get_width() / 2, rm_707_button_surface.get_height() / 2))

rm_708_text = midfont.render("708", True, (0, 0, 0))
rm_708_text_rect = rm_708_text.get_rect(
 center=(rm_708_button_surface.get_width() / 2, rm_708_button_surface.get_height() / 2))

rm_709_text = midfont.render("709", True, (0, 0, 0))
rm_709_text_rect = rm_708_text.get_rect(
 center=(rm_709_button_surface.get_width() / 2, rm_709_button_surface.get_height() / 2))

rm_801_text = midfont.render("801", True, (0, 0, 0))
rm_801_text_rect = rm_801_text.get_rect(
 center=(rm_801_button_surface.get_width() / 2, rm_801_button_surface.get_height() / 2))

rm_802_text = midfont.render("802", True, (0, 0, 0))
rm_802_text_rect = rm_802_text.get_rect(
 center=(rm_802_button_surface.get_width() / 2, rm_802_button_surface.get_height() / 2))

rr_1_text = midfont.render("RR", True, (0, 0, 0))
rr_1_text_rect = rr_1_text.get_rect(center=(rr_1_button_surface.get_width() / 2, rr_1_button_surface.get_height() / 2))

weight_text = smallfont.render("Image", True, (0, 0, 0))
weight_text_rect = weight_text.get_rect(
 center=(weight_button_surface.get_width() / 2, weight_button_surface.get_height() / 2))
# Green

# Yellow
rm_501_text = yfont.render("501", True, (0, 0, 0))
rm_501_text_rect = rm_501_text.get_rect(
 center=(rm_501_button_surface.get_width() / 2, rm_501_button_surface.get_height() / 2))

rm_502_text = yfont.render("502", True, (0, 0, 0))
rm_502_text_rect = rm_502_text.get_rect(
 center=(rm_502_button_surface.get_width() / 2, rm_502_button_surface.get_height() / 2))

rm_503_text = yfont.render("503", True, (0, 0, 0))
rm_503_text_rect = rm_501_text.get_rect(
 center=(rm_503_button_surface.get_width() / 2, rm_503_button_surface.get_height() / 2))

rm_504_text = yfont.render("504", True, (0, 0, 0))
rm_504_text_rect = rm_504_text.get_rect(
 center=(rm_504_button_surface.get_width() / 2, rm_504_button_surface.get_height() / 2))

rm_505_text = yfont.render("505", True, (0, 0, 0))
rm_505_text_rect = rm_505_text.get_rect(
 center=(rm_505_button_surface.get_width() / 2, rm_505_button_surface.get_height() / 2))

rm_506_text = yfont.render("506", True, (0, 0, 0))
rm_506_text_rect = rm_506_text.get_rect(
 center=(rm_506_button_surface.get_width() / 2, rm_506_button_surface.get_height() / 2))

rm_507_text = yfont.render("507", True, (0, 0, 0))
rm_507_text_rect = rm_507_text.get_rect(
 center=(rm_507_button_surface.get_width() / 2, rm_507_button_surface.get_height() / 2))

rm_508_text = yfont.render("508", True, (0, 0, 0))
rm_508_text_rect = rm_508_text.get_rect(
 center=(rm_508_button_surface.get_width() / 2, rm_508_button_surface.get_height() / 2))

rm_509_text = yfont.render("509", True, (0, 0, 0))
rm_509_text_rect = rm_509_text.get_rect(
 center=(rm_509_button_surface.get_width() / 2, rm_509_button_surface.get_height() / 2))

rm_510_text = yfont.render("510", True, (0, 0, 0))
rm_510_text_rect = rm_510_text.get_rect(
 center=(rm_510_button_surface.get_width() / 2, rm_510_button_surface.get_height() / 2))

rm_511_text = yfont.render("511", True, (0, 0, 0))
rm_511_text_rect = rm_511_text.get_rect(
 center=(rm_511_button_surface.get_width() / 2, rm_511_button_surface.get_height() / 2))

rm_512_text = yfont.render("512", True, (0, 0, 0))
rm_512_text_rect = rm_512_text.get_rect(
 center=(rm_512_button_surface.get_width() / 2, rm_512_button_surface.get_height() / 2))

rm_514_text = yfont.render("514", True, (0, 0, 0))
rm_514_text_rect = rm_504_text.get_rect(
 center=(rm_514_button_surface.get_width() / 2, rm_514_button_surface.get_height() / 2))

rm_515_text = yfont.render("515", True, (0, 0, 0))
rm_515_text_rect = rm_515_text.get_rect(
 center=(rm_515_button_surface.get_width() / 2, rm_515_button_surface.get_height() / 2))

rm_516_text = yfont.render("516", True, (0, 0, 0))
rm_516_text_rect = rm_516_text.get_rect(
 center=(rm_516_button_surface.get_width() / 2, rm_516_button_surface.get_height() / 2))

rm_517_text = yfont.render("517", True, (0, 0, 0))
rm_517_text_rect = rm_517_text.get_rect(
 center=(rm_517_button_surface.get_width() / 2, rm_517_button_surface.get_height() / 2))

RR_yellow_text = yRRfont.render("RR", True, (0, 0, 0))
RR_yellow_text_rect = RR_yellow_text.get_rect(
 center=(RR_yellow_button_surface.get_width() / 2, RR_yellow_button_surface.get_height() / 2))
# Yellow

# Blue
rm_905_text = font.render("905", True, (0, 0, 0))
rm_905_text_rect = rm_905_text.get_rect(
 center=(rm_905_button_surface.get_width() / 2, rm_905_button_surface.get_height() / 2))

rm_904_text = font.render("904", True, (0, 0, 0))
rm_904_text_rect = rm_904_text.get_rect(
 center=(rm_904_button_surface.get_width() / 2, rm_904_button_surface.get_height() / 2))

tennis_courts_text = mc_font.render("Tennis Courts", True, (0, 0, 0))
tennis_courts_text_rect = tennis_courts_text.get_rect(
 center=(tennis_courts_button_surface.get_width() / 2, tennis_courts_button_surface.get_height() / 2))

lemon_parking_lot_text = senate_room_font.render("Lemon Parking Lot", True, (0, 0, 0))
lemon_parking_lot_text_rect = lemon_parking_lot_text.get_rect(
 center=(lemon_parking_lot_button_surface.get_width() / 2, lemon_parking_lot_button_surface.get_height() / 2))

lawn_text = font.render("Lawn", True, (0, 0, 0))
lawn_text_rect = lawn_text.get_rect(center=(lawn_button_surface.get_width() / 2, lawn_button_surface.get_height() / 2))

media_center_text = mc_font.render("Media Center", True, (0, 0, 0))
media_center_text_rect = media_center_text.get_rect(
 center=(media_center_button_surface.get_width() / 2, media_center_button_surface.get_height() / 2))

senate_room_text = senate_room_font.render("Senate Room", True, (0, 0, 0))
senate_room_text_rect = senate_room_text.get_rect(
 center=(senate_room_button_surface.get_width() / 2, senate_room_button_surface.get_height() / 2))

mc1_text = mc_font.render("MC1", True, (0, 0, 0))
mc1_text_rect = mc1_text.get_rect(center=(mc1_button_surface.get_width() / 2, mc1_button_surface.get_height() / 2))

mc2_text = mc_font.render("MC2", True, (0, 0, 0))
mc2_text_rect = mc2_text.get_rect(center=(mc2_button_surface.get_width() / 2, mc2_button_surface.get_height() / 2))

mc3_text = mc_font.render("MC3", True, (0, 0, 0))
mc3_text_rect = mc3_text.get_rect(center=(mc3_button_surface.get_width() / 2, mc3_button_surface.get_height() / 2))

mc4_text = mc_font.render("MC4", True, (0, 0, 0))
mc4_text_rect = mc4_text.get_rect(center=(mc4_button_surface.get_width() / 2, mc4_button_surface.get_height() / 2))
# Blue

# Orange
PO_text = PO_font.render("Principal's Office", True, (0, 0, 0))
PO_text_rect = PO_text.get_rect(center=(PO_button_surface.get_width() / 2, PO_button_surface.get_height() / 2))

conf_text = PO_font.render("Conf. Room", True, (0, 0, 0))
conf_text_rect = PO_text.get_rect(center=(conf_button_surface.get_width() / 2, conf_button_surface.get_height() / 2))

nurse_text = nurse_font.render("Nurse", True, (0, 0, 0))
nurse_text_rect = nurse_text.get_rect(
 center=(nurse_button_surface.get_width() / 2, nurse_button_surface.get_height() / 2))

rgr_text = rgr_font.render("Registrar", True, (0, 0, 0))
rgr_text_rect = rgr_text.get_rect(center=(rgr_button_surface.get_width() / 2, rgr_button_surface.get_height() / 2))

attendance_text = PO_font.render("Attendance", True, (0, 0, 0))
attendance_text_rect = attendance_text.get_rect(
 center=(attendance_button_surface.get_width() / 2, attendance_button_surface.get_height() / 2))

rm_311_text = font2.render("311", True, (0, 0, 0))
rm_311_text_rect = rm_311_text.get_rect(
 center=(rm_311_button_surface.get_width() / 2, rm_311_button_surface.get_height() / 2))

rm_310_text = font2.render("310", True, (0, 0, 0))
rm_310_text_rect = rm_310_text.get_rect(
 center=(rm_310_button_surface.get_width() / 2, rm_310_button_surface.get_height() / 2))

ccc_text = PO_font.render("Counseling/College & Career", True, (0, 0, 0))
ccc_text_rect = ccc_text.get_rect(center=(ccc_button_surface.get_width() / 2, ccc_button_surface.get_height() / 2))

rm_304_text = font3.render("304", True, (0, 0, 0))
rm_304_text_rect = rm_304_text.get_rect(
 center=(rm_304_button_surface.get_width() / 2, rm_304_button_surface.get_height() / 2))

rr_orange_text = font3.render("RR", True, (0, 0, 0))
rr_orange_text_rect = rr_orange_text.get_rect(
 center=(rr_orange_button_surface.get_width() / 2, rr_orange_button_surface.get_height() / 2))

rm_309_text = font3.render("309", True, (0, 0, 0))
rm_309_text_rect = rm_309_text.get_rect(
 center=(rm_309_button_surface.get_width() / 2, rm_309_button_surface.get_height() / 2))

rm_308_text = font3.render("308", True, (0, 0, 0))
rm_308_text_rect = rm_308_text.get_rect(
 center=(rm_308_button_surface.get_width() / 2, rm_308_button_surface.get_height() / 2))

rm_305_text = font3.render("305", True, (0, 0, 0))
rm_305_text_rect = rm_305_text.get_rect(
 center=(rm_305_button_surface.get_width() / 2, rm_305_button_surface.get_height() / 2))

rm_306_text = font4.render("306", True, (0, 0, 0))
rm_306_text_rect = rm_306_text.get_rect(
 center=(rm_306_button_surface.get_width() / 2, rm_306_button_surface.get_height() / 2))

rm_307_text = font4.render("307", True, (0, 0, 0))
rm_307_text_rect = rm_307_text.get_rect(
 center=(rm_307_button_surface.get_width() / 2, rm_307_button_surface.get_height() / 2))

lunch_text = font5.render("Lunch", True, (0, 0, 0))
lunch_text_rect = lunch_text.get_rect(
 center=(lunch_button_surface.get_width() / 2, lunch_button_surface.get_height() / 2))
# Orange

# Brown
pool_button_text = font.render("Pool", True, (0, 0, 0))
pool_button_text_rect = pool_button_text.get_rect(
 center=(pool_button_surface.get_width() / 2, pool_button_surface.get_height() / 2))

rm_804_button_text = font.render("804", True, (0, 0, 0))
rm_804_button_text_rect = rm_804_button_text.get_rect(
 center=(rm_804_button_surface.get_width() / 2, rm_804_button_surface.get_height() / 2))

rm_805_button_text = font.render("805", True, (0, 0, 0))
rm_805_button_text_rect = rm_805_button_text.get_rect(
 center=(rm_805_button_surface.get_width() / 2, rm_805_button_surface.get_height() / 2))

locker_rooms_button_text = font.render("Locker", True, (0, 0, 0))
locker_rooms_button_text_rect = locker_rooms_button_text.get_rect(
 center=(locker_rooms_button_surface.get_width() / 2, locker_rooms_button_surface.get_height() / 2))

rm_207_button_text = font.render("207", True, (0, 0, 0))
rm_207_button_text_rect = rm_207_button_text.get_rect(
 center=(rm_207_button_surface.get_width() / 2, rm_207_button_surface.get_height() / 2))

rm_206_button_text = font.render("206", True, (0, 0, 0))
rm_206_button_text_rect = rm_206_button_text.get_rect(
 center=(rm_206_button_surface.get_width() / 2, rm_206_button_surface.get_height() / 2))

rm_205_button_text = font.render("205", True, (0, 0, 0))
rm_205_button_text_rect = rm_205_button_text.get_rect(
 center=(rm_205_button_surface.get_width() / 2, rm_205_button_surface.get_height() / 2))

rm_204_button_text = font.render("204", True, (0, 0, 0))
rm_204_button_text_rect = rm_204_button_text.get_rect(
 center=(rm_204_button_surface.get_width() / 2, rm_204_button_surface.get_height() / 2))

rm_203_button_text = font.render("203", True, (0, 0, 0))
rm_203_button_text_rect = rm_203_button_text.get_rect(
 center=(rm_203_button_surface.get_width() / 2, rm_203_button_surface.get_height() / 2))

rm_202_button_text = font.render("202", True, (0, 0, 0))
rm_202_button_text_rect = rm_202_button_text.get_rect(
 center=(rm_202_button_surface.get_width() / 2, rm_202_button_surface.get_height() / 2))

rm_201_button_text = font.render("201", True, (0, 0, 0))
rm_201_button_text_rect = rm_201_button_text.get_rect(
 center=(rm_201_button_surface.get_width() / 2, rm_201_button_surface.get_height() / 2))

rm_107_button_text = font.render("107", True, (0, 0, 0))
rm_107_button_text_rect = rm_107_button_text.get_rect(
 center=(rm_107_button_surface.get_width() / 2, rm_107_button_surface.get_height() / 2))

rm_106_button_text = font.render("106", True, (0, 0, 0))
rm_106_button_text_rect = rm_106_button_text.get_rect(
 center=(rm_106_button_surface.get_width() / 2, rm_106_button_surface.get_height() / 2))

rm_105_button_text = font.render("105", True, (0, 0, 0))
rm_105_button_text_rect = rm_105_button_text.get_rect(
 center=(rm_105_button_surface.get_width() / 2, rm_105_button_surface.get_height() / 2))

rm_104_button_text = font.render("104", True, (0, 0, 0))
rm_104_button_text_rect = rm_104_button_text.get_rect(
 center=(rm_104_button_surface.get_width() / 2, rm_104_button_surface.get_height() / 2))

rm_103_button_text = font.render("103", True, (0, 0, 0))
rm_103_button_text_rect = rm_103_button_text.get_rect(
 center=(rm_103_button_surface.get_width() / 2, rm_103_button_surface.get_height() / 2))

rm_102_button_text = font.render("102", True, (0, 0, 0))
rm_102_button_text_rect = rm_102_button_text.get_rect(
 center=(rm_102_button_surface.get_width() / 2, rm_102_button_surface.get_height() / 2))

rm_101_button_text = font.render("101", True, (0, 0, 0))
rm_101_button_text_rect = rm_101_button_text.get_rect(
 center=(rm_101_button_surface.get_width() / 2, rm_101_button_surface.get_height() / 2))
# Brown
#Back
back_button_text = font.render("Back", True, (0, 0, 0))
back_button_rect = back_button_text.get_rect(center=(back_button_surface.get_width()/2, back_button_surface.get_height()/2))
#Back

# Create a pygame.Rect object that represents the button's boundaries
# Red
rm_601_button_rect = pygame.Rect(775, 400, 50, 25)
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
# Red
# Purple
RR_400_button_rect = pygame.Rect(1018, 395, 36, 10)
rm_401_button_rect = pygame.Rect(1018, 410, 36, 44)
rm_402_button_rect = pygame.Rect(1018, 320, 36, 44)
rm_403_button_rect = pygame.Rect(1018, 265, 36, 44)
rm_404_button_rect = pygame.Rect(1018, 210, 36, 44)
rm_405_button_rect = pygame.Rect(1058, 210, 36, 44)
rm_406_button_rect = pygame.Rect(1058, 265, 36, 44)
rm_407_button_rect = pygame.Rect(1058, 320, 36, 44)
rm_408_button_rect = pygame.Rect(1058, 410, 36, 44)
rm_409_button_rect = pygame.Rect(1058, 467, 36, 44)
rm_410_button_rect = pygame.Rect(1018, 467, 35, 44)
# Purple
# Green
gym_button_rect = pygame.Rect(475, 414, 70, 50)
tennis_button_rect = pygame.Rect(441, 292, 39, 50)
rm_702_button_rect = pygame.Rect(499, 306, 50, 25)
circle_button_rect = pygame.Rect(645, 411, 49, 33)
rm_703_button_rect = pygame.Rect(560, 309, 48, 25)
rm_705_button_rect = pygame.Rect(639, 309, 23, 25)
rm_704_button_rect = pygame.Rect(611, 309, 23, 25)
rm_706_button_rect = pygame.Rect(666, 333, 22, 25)
rm_707_button_rect = pygame.Rect(666, 303, 22, 25)
rm_708_button_rect = pygame.Rect(666, 273, 22, 25)
rm_801_button_rect = pygame.Rect(572, 405, 22, 25)
rm_802_button_rect = pygame.Rect(572, 429, 22, 25)
rm_709_button_rect = pygame.Rect(638, 248, 25, 22)
rr_1_button_rect = pygame.Rect(666, 243, 21, 25)
weight_button_rect = pygame.Rect(505, 180, 30, 20)
# Green
# Yellow
rm_501_button_rect = pygame.Rect(1098, 429, 35, 25)
rm_502_button_rect = pygame.Rect(1097, 397, 37, 25)
rm_503_button_rect = pygame.Rect(1097.7, 345, 37, 25)
rm_504_button_rect = pygame.Rect(1097.7, 317, 37, 25)
rm_505_button_rect = pygame.Rect(1098.3, 284, 36, 25)
rm_506_button_rect = pygame.Rect(1097.5, 248, 35, 25)
rm_507_button_rect = pygame.Rect(1097.5, 210, 35, 25)
rm_508_button_rect = pygame.Rect(1137, 210, 38, 25)
rm_509_button_rect = pygame.Rect(1137, 248, 38.5, 25)
rm_510_button_rect = pygame.Rect(1137, 284, 35, 25)
rm_511_button_rect = pygame.Rect(1138, 317, 35, 25)
rm_512_button_rect = pygame.Rect(1137, 345.7, 35, 25)
rm_514_button_rect = pygame.Rect(1137, 397.5, 35, 25)
rm_515_button_rect = pygame.Rect(1137, 429, 35, 25)
rm_516_button_rect = pygame.Rect(1137, 478, 35, 25)
rm_517_button_rect = pygame.Rect(1098, 478, 35, 25)
RR_yellow_button_rect = pygame.Rect(1098, 372, 35, 10.5)
# Yellow
# Blue
rm_905_button_rect = pygame.Rect(420, 561, 50, 25)
rm_904_button_rect = pygame.Rect(500, 561, 50, 25)
tennis_courts_button_rect = pygame.Rect(162, 775, 120, 25)
lemon_parking_lot_button_rect = pygame.Rect(290, 760, 124, 50)
lawn_button_rect = pygame.Rect(470, 750, 70, 35)
media_center_button_rect = pygame.Rect(600, 805, 120, 25)
senate_room_button_rect = pygame.Rect(643, 675, 80, 25)
mc1_button_rect = pygame.Rect(600, 736, 40, 25)
mc2_button_rect = pygame.Rect(600, 712, 40, 25)
mc3_button_rect = pygame.Rect(600, 687, 40, 25)
mc4_button_rect = pygame.Rect(600, 663, 40, 25)
# Blue
# Orange
PO_button_rect = pygame.Rect(694, 545, 50, 25)
nurse_button_rect = pygame.Rect(779, 517, 50, 25)
rgr_button_rect = pygame.Rect(818, 517, 50, 25)
conf_button_rect = pygame.Rect(694, 585, 50, 25)
attendance_button_rect = pygame.Rect(876, 585, 50, 25)
rm_311_button_rect = pygame.Rect(876, 545, 50, 25)
rm_310_button_rect = pygame.Rect(960, 545, 50, 25)
ccc_button_rect = pygame.Rect(923, 585, 80, 25)
rm_304_button_rect = pygame.Rect(1031, 590, 50, 25)
rr_orange_button_rect = pygame.Rect(1062, 565, 16, 25)
rm_309_button_rect = pygame.Rect(1105, 551, 50, 25)
rm_308_button_rect = pygame.Rect(1152, 551, 50, 25)
rm_305_button_rect = pygame.Rect(1105, 590, 30, 25)
rm_306_button_rect = pygame.Rect(1143, 590, 25, 25)
rm_307_button_rect = pygame.Rect(1170, 590, 25, 25)
lunch_button_rect = pygame.Rect(910, 299, 70, 53)
# Orange
# Brown
pool_button_rect = pygame.Rect(775, 400, 50, 25)
rm_804_button_rect = pygame.Rect(385, 415, 50, 25)
rm_805_button_rect = pygame.Rect(385, 485, 50, 25)
locker_rooms_button_rect = pygame.Rect(385, 450, 50, 25)
rm_207_button_rect = pygame.Rect(795, 820, 50, 25)
rm_206_button_rect = pygame.Rect(850, 820, 50, 25)
rm_205_button_rect = pygame.Rect(905, 820, 50, 25)
rm_204_button_rect = pygame.Rect(963, 820, 50, 25)
rm_203_button_rect = pygame.Rect(1018, 820, 50, 25)
rm_202_button_rect = pygame.Rect(1072, 820, 50, 25)
rm_201_button_rect = pygame.Rect(1130, 820, 50, 25)
rm_107_button_rect = pygame.Rect(795, 857, 50, 25)
rm_106_button_rect = pygame.Rect(850, 857, 50, 25)
rm_105_button_rect = pygame.Rect(905, 857, 50, 25)
rm_104_button_rect = pygame.Rect(963, 857, 50, 25)
rm_103_button_rect = pygame.Rect(1018, 857, 50, 25)
rm_102_button_rect = pygame.Rect(1072, 857, 50, 25)
rm_101_button_rect = pygame.Rect(1130, 857, 50, 25)
# Brown
#Back
back_button_rect = pygame.Rect(30, 20, 100, 50)
#Back

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
         # Red
         if rm_601_button_rect.collidepoint(event.pos):
             current_screen = rm_601_image
         elif staff_lounge_button_rect.collidepoint(event.pos):
             current_screen = staff_lounge_image
         elif rm_216_button_rect.collidepoint(event.pos):
             current_screen = rm_216_image
         elif rm_215_button_rect.collidepoint(event.pos):
             current_screen = rm_215_image
         elif rm_214_button_rect.collidepoint(event.pos):
             current_screen = rm_214_image
         elif RR_1_button_rect.collidepoint(event.pos):
             current_screen = RR_1_image
         elif rm_116_button_rect.collidepoint(event.pos):
             current_screen = rm_116_image
         elif rm_115_button_rect.collidepoint(event.pos):
             current_screen = rm_115_image
         elif rm_114_button_rect.collidepoint(event.pos):
             current_screen = rm_114_image
         elif RR_2_button_rect.collidepoint(event.pos):
             current_screen = RR_2_image
         elif rm_213_button_rect.collidepoint(event.pos):
             current_screen = rm_213_image
         elif rm_113_button_rect.collidepoint(event.pos):
             current_screen = rm_113_image
         elif rm_108_button_rect.collidepoint(event.pos):
             current_screen = rm_108_image
         elif rm_208_button_rect.collidepoint(event.pos):
             current_screen = rm_208_image
         elif rm_212_button_rect.collidepoint(event.pos):
             current_screen = rm_212_image
         elif rm_211_button_rect.collidepoint(event.pos):
             current_screen = rm_211_image
         elif rm_210_button_rect.collidepoint(event.pos):
             current_screen = rm_210_image
         elif rm_209_button_rect.collidepoint(event.pos):
             current_screen = rm_209_image
         elif RR_3_button_rect.collidepoint(event.pos):
             current_screen = RR_3_image
         elif rm_112_button_rect.collidepoint(event.pos):
             current_screen = rm_112_image
         elif rm_111_button_rect.collidepoint(event.pos):
             current_screen = rm_111_image
         elif rm_110_button_rect.collidepoint(event.pos):
             current_screen = rm_110_image
         elif rm_109_button_rect.collidepoint(event.pos):
             current_screen = rm_109_image
         elif RR_4_button_rect.collidepoint(event.pos):
             current_screen = RR_4_image
         # Red
         # Purple
         elif RR_400_button_rect.collidepoint(event.pos):
             current_screen = RR_400_image
         elif rm_401_button_rect.collidepoint(event.pos):
             current_screen = rm_401_image
         elif rm_402_button_rect.collidepoint(event.pos):
             current_screen = rm_402_image
         elif rm_403_button_rect.collidepoint(event.pos):
             current_screen = rm_403_image
         elif rm_404_button_rect.collidepoint(event.pos):
             current_screen = rm_404_image
         elif rm_405_button_rect.collidepoint(event.pos):
             current_screen = rm_405_image
         elif rm_406_button_rect.collidepoint(event.pos):
             current_screen = rm_406_image
         elif rm_407_button_rect.collidepoint(event.pos):
             current_screen = rm_407_image
         elif rm_408_button_rect.collidepoint(event.pos):
             current_screen = rm_408_image
         elif rm_409_button_rect.collidepoint(event.pos):
             current_screen = rm_409_image
         elif rm_410_button_rect.collidepoint(event.pos):
             current_screen = rm_410_image
         # Purple
         # Green
         elif gym_button_rect.collidepoint(event.pos):
             current_screen = gym_image
         elif tennis_button_rect.collidepoint(event.pos):
             current_screen = tennis_image
         elif rm_702_button_rect.collidepoint(event.pos):
             current_screen = rm_702_image
         elif circle_button_rect.collidepoint(event.pos):
             current_screen = circle_image
         elif rm_703_button_rect.collidepoint(event.pos):
             current_screen = rm_703_image
         elif rm_705_button_rect.collidepoint(event.pos):
             current_screen = rm_705_image
         elif rm_704_button_rect.collidepoint(event.pos):
             current_screen = rm_704_image
         elif rm_706_button_rect.collidepoint(event.pos):
             current_screen = rm_706_image
         elif rm_707_button_rect.collidepoint(event.pos):
             current_screen = rm_707_image
         elif rm_708_button_rect.collidepoint(event.pos):
             current_screen = rm_708_image
         elif rm_709_button_rect.collidepoint(event.pos):
             current_screen = rm_709_image
         elif rm_801_button_rect.collidepoint(event.pos):
             current_screen = rm_801_image
         elif rm_802_button_rect.collidepoint(event.pos):
             current_screen = rm_802_image
         elif rr_1_button_rect.collidepoint(event.pos):
             current_screen = rr_1_image
         elif weight_button_rect.collidepoint(event.pos):
             current_screen = weight_image
         # Green
         # Yellow
         elif rm_501_button_rect.collidepoint(event.pos):
             current_screen = rm_501_image
         elif rm_502_button_rect.collidepoint(event.pos):
             current_screen = rm_502_image
         elif rm_503_button_rect.collidepoint(event.pos):
             current_screen = rm_503_image
         elif rm_504_button_rect.collidepoint(event.pos):
             current_screen = rm_504_image
         elif rm_505_button_rect.collidepoint(event.pos):
             current_screen = rm_505_image
         elif rm_506_button_rect.collidepoint(event.pos):
             current_screen = rm_506_image
         elif rm_507_button_rect.collidepoint(event.pos):
             current_screen = rm_507_image
         elif rm_508_button_rect.collidepoint(event.pos):
             current_screen = rm_508_image
         elif rm_509_button_rect.collidepoint(event.pos):
             current_screen = rm_509_image
         elif rm_510_button_rect.collidepoint(event.pos):
             current_screen = rm_510_image
         elif rm_511_button_rect.collidepoint(event.pos):
             current_screen = rm_511_image
         elif rm_512_button_rect.collidepoint(event.pos):
             current_screen = rm_512_image
         elif rm_514_button_rect.collidepoint(event.pos):
             current_screen = rm_514_image
         elif rm_515_button_rect.collidepoint(event.pos):
             current_screen = rm_515_image
         elif rm_516_button_rect.collidepoint(event.pos):
             current_screen = rm_516_image
         elif rm_517_button_rect.collidepoint(event.pos):
             current_screen = rm_517_image
         elif RR_yellow_button_rect.collidepoint(event.pos):
             current_screen = RR_yellow_image
         # Yellow
         # Blue
         elif rm_905_button_rect.collidepoint(event.pos):
             current_screen = rm_905_image
         elif rm_904_button_rect.collidepoint(event.pos):
             current_screen = rm_904_image
         elif tennis_courts_button_rect.collidepoint(event.pos):
             current_screen = tennis_courts_image
         elif lemon_parking_lot_button_rect.collidepoint(event.pos):
             current_screen = lemon_parking_lot_image
         elif lawn_button_rect.collidepoint(event.pos):
             current_screen = lawn_image
         elif media_center_button_rect.collidepoint(event.pos):
             current_screen = media_center_image
         elif senate_room_button_rect.collidepoint(event.pos):
             current_screen = senate_room_image
         elif mc1_button_rect.collidepoint(event.pos):
             current_screen = mc1_image
         elif mc2_button_rect.collidepoint(event.pos):
             current_screen = mc2_image
         elif mc3_button_rect.collidepoint(event.pos):
             current_screen = mc3_image
         elif mc4_button_rect.collidepoint(event.pos):
             current_screen = mc4_image
         # Blue
         # Orange
         elif PO_button_rect.collidepoint(event.pos):
             current_screen = principal_office
         elif nurse_button_rect.collidepoint(event.pos):
             current_screen = nurse
         elif rgr_button_rect.collidepoint(event.pos):
             current_screen = registrar
         elif conf_button_rect.collidepoint(event.pos):
             current_screen = conference_room
         elif rm_311_button_rect.collidepoint(event.pos):
             current_screen = rm_311
         elif attendance_button_rect.collidepoint(event.pos):
             current_screen = attendance_office
         elif rm_310_button_rect.collidepoint(event.pos):
             current_screen = rm_310
         elif ccc_button_rect.collidepoint(event.pos):
             current_screen = ccc
         elif rm_304_button_rect.collidepoint(event.pos):
             current_screen = rm_304
         elif rr_orange_button_rect.collidepoint(event.pos):
             current_screen = rr_orange
         elif rm_309_button_rect.collidepoint(event.pos):
             current_screen = rm_309
         elif rm_308_button_rect.collidepoint(event.pos):
             current_screen = rm_308
         elif rm_305_button_rect.collidepoint(event.pos):
             current_screen = rm_305
         elif rm_306_button_rect.collidepoint(event.pos):
             current_screen = rm_306
         elif rm_307_button_rect.collidepoint(event.pos):
             current_screen = rm_307
         elif lunch_button_rect.collidepoint(event.pos):
             current_screen = lunch
         # Orange
         # Brown
         elif pool_button_rect.collidepoint(event.pos):
             current_screen = pool_image
         elif rm_804_button_rect.collidepoint(event.pos):
             current_screen = rm_804_image
         elif rm_805_button_rect.collidepoint(event.pos):
             current_screen = rm_805_image
         elif locker_rooms_button_rect.collidepoint(event.pos):
             current_screen = locker_image
         elif rm_207_button_rect.collidepoint(event.pos):
             current_screen = rm_207_image
         elif rm_206_button_rect.collidepoint(event.pos):
             current_screen = rm_206_image
         elif rm_205_button_rect.collidepoint(event.pos):
             current_screen = rm_205_image
         elif rm_204_button_rect.collidepoint(event.pos):
             current_screen = rm_204_image
         elif rm_203_button_rect.collidepoint(event.pos):
             current_screen = rm_203_image
         elif rm_202_button_rect.collidepoint(event.pos):
             current_screen = rm_202_image
         elif rm_201_button_rect.collidepoint(event.pos):
             current_screen = rm_201_image
         elif rm_107_button_rect.collidepoint(event.pos):
             current_screen = rm_107_image
         elif rm_106_button_rect.collidepoint(event.pos):
             current_screen = rm_106_image
         elif rm_105_button_rect.collidepoint(event.pos):
             current_screen = rm_105_image
         elif rm_104_button_rect.collidepoint(event.pos):
             current_screen = rm_104_image
         elif rm_103_button_rect.collidepoint(event.pos):
             current_screen = rm_103_image
         elif rm_102_button_rect.collidepoint(event.pos):
             current_screen = rm_102_image
         elif rm_101_button_rect.collidepoint(event.pos):
             current_screen = rm_101_image
         # Brown
         # Back
         elif back_button_rect.collidepoint(event.pos):
               current_screen = map
         #Back

 # Check if the mouse is over the button. This will create the button hover effect
 # Red
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
 # Red
 # Purple
 button_hover_effect(RR_400_button_rect, RR_400_button_surface)
 button_hover_effect(rm_401_button_rect, rm_401_button_surface)
 button_hover_effect(rm_402_button_rect, rm_402_button_surface)
 button_hover_effect(rm_403_button_rect, rm_403_button_surface)
 button_hover_effect(rm_404_button_rect, rm_404_button_surface)
 button_hover_effect(rm_405_button_rect, rm_405_button_surface)
 button_hover_effect(rm_406_button_rect, rm_406_button_surface)
 button_hover_effect(rm_407_button_rect, rm_407_button_surface)
 button_hover_effect(rm_408_button_rect, rm_408_button_surface)
 button_hover_effect(rm_409_button_rect, rm_409_button_surface)
 button_hover_effect(rm_410_button_rect, rm_410_button_surface)
 # Purple
 # Green
 button_hover_effect(gym_button_rect, gym_button_surface)
 button_hover_effect(tennis_button_rect, tennis_button_surface)
 button_hover_effect(rm_702_button_rect, rm_702_button_surface)
 button_hover_effect(circle_button_rect, circle_button_surface)
 button_hover_effect(rm_703_button_rect, rm_703_button_surface)
 button_hover_effect(rm_705_button_rect, rm_705_button_surface)
 button_hover_effect(rm_704_button_rect, rm_704_button_surface)
 button_hover_effect(rm_706_button_rect, rm_706_button_surface)
 button_hover_effect(rm_707_button_rect, rm_707_button_surface)
 button_hover_effect(rm_708_button_rect, rm_708_button_surface)
 button_hover_effect(rm_709_button_rect, rm_709_button_surface)
 button_hover_effect(rm_801_button_rect, rm_801_button_surface)
 button_hover_effect(rm_802_button_rect, rm_802_button_surface)
 button_hover_effect(rr_1_button_rect, rr_1_button_surface)
 button_hover_effect(weight_button_rect, weight_button_surface)
 # Green
 # Yellow
 button_hover_effect(rm_501_button_rect, rm_501_button_surface)
 button_hover_effect(rm_502_button_rect, rm_502_button_surface)
 button_hover_effect(rm_503_button_rect, rm_503_button_surface)
 button_hover_effect(rm_504_button_rect, rm_504_button_surface)
 button_hover_effect(rm_505_button_rect, rm_505_button_surface)
 button_hover_effect(rm_506_button_rect, rm_506_button_surface)
 button_hover_effect(rm_507_button_rect, rm_507_button_surface)
 button_hover_effect(rm_508_button_rect, rm_508_button_surface)
 button_hover_effect(rm_509_button_rect, rm_509_button_surface)
 button_hover_effect(rm_510_button_rect, rm_510_button_surface)
 button_hover_effect(rm_511_button_rect, rm_511_button_surface)
 button_hover_effect(rm_512_button_rect, rm_512_button_surface)
 button_hover_effect(rm_514_button_rect, rm_514_button_surface)
 button_hover_effect(rm_515_button_rect, rm_515_button_surface)
 button_hover_effect(rm_516_button_rect, rm_516_button_surface)
 button_hover_effect(rm_517_button_rect, rm_517_button_surface)
 button_hover_effect(RR_yellow_button_rect, RR_yellow_button_surface)
 # Yellow
 # Blue
 button_hover_effect(rm_905_button_rect, rm_905_button_surface)
 button_hover_effect(rm_904_button_rect, rm_904_button_surface)
 button_hover_effect(tennis_courts_button_rect, tennis_courts_button_surface)
 button_hover_effect(lemon_parking_lot_button_rect, lemon_parking_lot_button_surface)
 button_hover_effect(lawn_button_rect, lawn_button_surface)
 button_hover_effect(media_center_button_rect, media_center_button_surface)
 button_hover_effect(senate_room_button_rect, senate_room_button_surface)
 button_hover_effect(mc1_button_rect, mc1_button_surface)
 button_hover_effect(mc2_button_rect, mc2_button_surface)
 button_hover_effect(mc3_button_rect, mc3_button_surface)
 button_hover_effect(mc4_button_rect, mc4_button_surface)
 # Blue
 # Orange
 button_hover_effect(PO_button_rect, PO_button_surface)
 button_hover_effect(nurse_button_rect, nurse_button_surface)
 button_hover_effect(rgr_button_rect, rgr_button_surface)
 button_hover_effect(conf_button_rect, conf_button_surface)
 button_hover_effect(rm_311_button_rect, rm_311_button_surface)
 button_hover_effect(attendance_button_rect, attendance_button_surface)
 button_hover_effect(rm_310_button_rect, rm_310_button_surface)
 button_hover_effect(ccc_button_rect, ccc_button_surface)
 button_hover_effect(rm_304_button_rect, rm_304_button_surface)
 button_hover_effect(rr_orange_button_rect, RR_3_button_surface)
 button_hover_effect(rm_309_button_rect, rm_309_button_surface)
 button_hover_effect(rm_308_button_rect, rm_308_button_surface)
 button_hover_effect(rm_305_button_rect, rm_305_button_surface)
 button_hover_effect(rm_306_button_rect, rm_306_button_surface)
 button_hover_effect(rm_307_button_rect, rm_307_button_surface)
 button_hover_effect(lunch_button_rect, lunch_button_surface)
 # Orange
 # Brown
 button_hover_effect(pool_button_rect, pool_button_surface)
 button_hover_effect(rm_804_button_rect, rm_804_button_surface)
 button_hover_effect(rm_805_button_rect, rm_805_button_surface)
 button_hover_effect(locker_rooms_button_rect, locker_rooms_button_surface)
 button_hover_effect(rm_207_button_rect, rm_207_button_surface)
 button_hover_effect(rm_206_button_rect, rm_206_button_surface)
 button_hover_effect(rm_205_button_rect, rm_205_button_surface)
 button_hover_effect(rm_204_button_rect, rm_204_button_surface)
 button_hover_effect(rm_203_button_rect, rm_203_button_surface)
 button_hover_effect(rm_202_button_rect, rm_202_button_surface)
 button_hover_effect(rm_201_button_rect, rm_201_button_surface)
 button_hover_effect(rm_107_button_rect, rm_107_button_surface)
 button_hover_effect(rm_106_button_rect, rm_106_button_surface)
 button_hover_effect(rm_105_button_rect, rm_105_button_surface)
 button_hover_effect(rm_104_button_rect, rm_104_button_surface)
 button_hover_effect(rm_103_button_rect, rm_103_button_surface)
 button_hover_effect(rm_102_button_rect, rm_102_button_surface)
 button_hover_effect(rm_101_button_rect, rm_101_button_surface)
 # Brown
 # Back
 button_hover_effect(back_button_rect, back_button_surface)
 # Back


 # Show the button text
 # Red
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
 # Red
 # Purple
 RR_400_button_surface.blit(RR_400_text, RR_400_text_rect)
 rm_401_button_surface.blit(rm_401_text, rm_401_text_rect)
 rm_402_button_surface.blit(rm_402_text, rm_402_text_rect)
 rm_403_button_surface.blit(rm_403_text, rm_403_text_rect)
 rm_404_button_surface.blit(rm_404_text, rm_404_text_rect)
 rm_405_button_surface.blit(rm_405_text, rm_405_text_rect)
 rm_406_button_surface.blit(rm_406_text, rm_406_text_rect)
 rm_407_button_surface.blit(rm_407_text, rm_407_text_rect)
 rm_408_button_surface.blit(rm_408_text, rm_408_text_rect)
 rm_409_button_surface.blit(rm_409_text, rm_409_text_rect)
 rm_410_button_surface.blit(rm_410_text, rm_410_text_rect)
 # Purple
 # Green
 gym_button_surface.blit(gym_text, gym_text_rect)
 tennis_button_surface.blit(tennis_text, tennis_text_rect)
 rm_702_button_surface.blit(rm_702_text, rm_702_text_rect)
 circle_button_surface.blit(circle_text, circle_text_rect)
 rm_703_button_surface.blit(rm_703_text, rm_703_text_rect)
 rm_705_button_surface.blit(rm_705_text, rm_705_text_rect)
 rm_704_button_surface.blit(rm_704_text, rm_704_text_rect)
 rm_706_button_surface.blit(rm_706_text, rm_706_text_rect)
 rm_707_button_surface.blit(rm_707_text, rm_707_text_rect)
 rm_708_button_surface.blit(rm_708_text, rm_708_text_rect)
 rm_709_button_surface.blit(rm_709_text, rm_709_text_rect)
 rm_801_button_surface.blit(rm_801_text, rm_801_text_rect)
 rm_802_button_surface.blit(rm_802_text, rm_802_text_rect)
 rr_1_button_surface.blit(rr_1_text, rr_1_text_rect)
 weight_button_surface.blit(weight_text, weight_text_rect)
 # Green
 # Yellow
 rm_501_button_surface.blit(rm_501_text, rm_501_text_rect)
 rm_502_button_surface.blit(rm_502_text, rm_502_text_rect)
 rm_503_button_surface.blit(rm_503_text, rm_503_text_rect)
 rm_504_button_surface.blit(rm_504_text, rm_504_text_rect)
 rm_505_button_surface.blit(rm_505_text, rm_505_text_rect)
 rm_506_button_surface.blit(rm_506_text, rm_506_text_rect)
 rm_507_button_surface.blit(rm_507_text, rm_507_text_rect)
 rm_508_button_surface.blit(rm_508_text, rm_508_text_rect)
 rm_509_button_surface.blit(rm_509_text, rm_509_text_rect)
 rm_510_button_surface.blit(rm_510_text, rm_510_text_rect)
 rm_511_button_surface.blit(rm_511_text, rm_511_text_rect)
 rm_512_button_surface.blit(rm_512_text, rm_512_text_rect)
 rm_514_button_surface.blit(rm_514_text, rm_514_text_rect)
 rm_515_button_surface.blit(rm_515_text, rm_515_text_rect)
 rm_516_button_surface.blit(rm_516_text, rm_516_text_rect)
 rm_517_button_surface.blit(rm_517_text, rm_517_text_rect)
 RR_yellow_button_surface.blit(RR_yellow_text, RR_yellow_text_rect)
 # Yellow
 # Blue
 rm_905_button_surface.blit(rm_905_text, rm_905_text_rect)
 rm_904_button_surface.blit(rm_904_text, rm_904_text_rect)
 tennis_courts_button_surface.blit(tennis_courts_text, tennis_courts_text_rect)
 lemon_parking_lot_button_surface.blit(lemon_parking_lot_text, lemon_parking_lot_text_rect)
 lawn_button_surface.blit(lawn_text, lawn_text_rect)
 media_center_button_surface.blit(media_center_text, media_center_text_rect)
 senate_room_button_surface.blit(senate_room_text, senate_room_text_rect)
 mc1_button_surface.blit(mc1_text, mc1_text_rect)
 mc2_button_surface.blit(mc2_text, mc2_text_rect)
 mc3_button_surface.blit(mc3_text, mc3_text_rect)
 mc4_button_surface.blit(mc4_text, mc4_text_rect)
 # Blue
 # Orange
 PO_button_surface.blit(PO_text, PO_text_rect)
 nurse_button_surface.blit(nurse_text, nurse_text_rect)
 rgr_button_surface.blit(rgr_text, rgr_text_rect)
 rm_311_button_surface.blit(rm_311_text, rm_311_text_rect)
 conf_button_surface.blit(conf_text, conf_text_rect)
 rm_310_button_surface.blit(rm_310_text, rm_310_text_rect)
 ccc_button_surface.blit(ccc_text, ccc_text_rect)
 rm_304_button_surface.blit(rm_304_text, rm_304_text_rect)
 rr_orange_button_surface.blit(rr_orange_text, rr_orange_text_rect)
 rm_309_button_surface.blit(rm_309_text, rm_309_text_rect)
 rm_308_button_surface.blit(rm_308_text, rm_308_text_rect)
 rm_305_button_surface.blit(rm_305_text, rm_305_text_rect)
 rm_306_button_surface.blit(rm_306_text, rm_306_text_rect)
 rm_307_button_surface.blit(rm_307_text, rm_307_text_rect)
 lunch_button_surface.blit(lunch_text, lunch_text_rect)
 attendance_button_surface.blit(attendance_text, attendance_text_rect)
 # Orange
 # Brown
 pool_button_surface.blit(pool_button_text, pool_button_text_rect)
 rm_804_button_surface.blit(rm_804_button_text, rm_804_button_text_rect)
 rm_805_button_surface.blit(rm_805_button_text, rm_805_button_text_rect)
 locker_rooms_button_surface.blit(locker_rooms_button_text, locker_rooms_button_text_rect)
 rm_207_button_surface.blit(rm_207_button_text, rm_207_button_text_rect)
 rm_206_button_surface.blit(rm_206_button_text, rm_206_button_text_rect)
 rm_205_button_surface.blit(rm_205_button_text, rm_205_button_text_rect)
 rm_204_button_surface.blit(rm_204_button_text, rm_204_button_text_rect)
 rm_203_button_surface.blit(rm_203_button_text, rm_203_button_text_rect)
 rm_202_button_surface.blit(rm_202_button_text, rm_202_button_text_rect)
 rm_201_button_surface.blit(rm_201_button_text, rm_201_button_text_rect)
 rm_107_button_surface.blit(rm_107_button_text, rm_107_button_text_rect)
 rm_106_button_surface.blit(rm_106_button_text, rm_106_button_text_rect)
 rm_105_button_surface.blit(rm_105_button_text, rm_105_button_text_rect)
 rm_104_button_surface.blit(rm_104_button_text, rm_104_button_text_rect)
 rm_103_button_surface.blit(rm_103_button_text, rm_103_button_text_rect)
 rm_102_button_surface.blit(rm_102_button_text, rm_102_button_text_rect)
 rm_101_button_surface.blit(rm_101_button_text, rm_101_button_text_rect)
 # Brown
 # Back
 back_button_surface.blit(back_button_text, back_button_rect)
 # Back


 # Draw the map and button on the screen
 if current_screen == map:
     screen.blit(current_screen, (0, 0))  # controls test_surface location
     # Red
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
     # Red
     # Purple
     screen.blit(RR_400_button_surface, (RR_400_button_rect.x, RR_400_button_rect.y))
     screen.blit(rm_401_button_surface, (rm_401_button_rect.x, rm_401_button_rect.y))
     screen.blit(rm_401_button_surface, (rm_401_button_rect.x, rm_401_button_rect.y))
     screen.blit(rm_402_button_surface, (rm_402_button_rect.x, rm_402_button_rect.y))
     screen.blit(rm_403_button_surface, (rm_403_button_rect.x, rm_403_button_rect.y))
     screen.blit(rm_404_button_surface, (rm_404_button_rect.x, rm_404_button_rect.y))
     screen.blit(rm_405_button_surface, (rm_405_button_rect.x, rm_405_button_rect.y))
     screen.blit(rm_406_button_surface, (rm_406_button_rect.x, rm_406_button_rect.y))
     screen.blit(rm_407_button_surface, (rm_407_button_rect.x, rm_407_button_rect.y))
     screen.blit(rm_408_button_surface, (rm_408_button_rect.x, rm_408_button_rect.y))
     screen.blit(rm_409_button_surface, (rm_409_button_rect.x, rm_409_button_rect.y))
     screen.blit(rm_410_button_surface, (rm_410_button_rect.x, rm_410_button_rect.y))
     # Purple
     # Green
     screen.blit(gym_button_surface, (gym_button_rect.x, gym_button_rect.y))
     screen.blit(tennis_button_surface, (tennis_button_rect.x, tennis_button_rect.y))
     screen.blit(rm_702_button_surface, (rm_702_button_rect.x, rm_702_button_rect.y))
     screen.blit(circle_button_surface, (circle_button_rect.x, circle_button_rect.y))
     screen.blit(rm_703_button_surface, (rm_703_button_rect.x, rm_703_button_rect.y))
     screen.blit(rm_705_button_surface, (rm_705_button_rect.x, rm_705_button_rect.y))
     screen.blit(rm_704_button_surface, (rm_704_button_rect.x, rm_704_button_rect.y))
     screen.blit(rm_706_button_surface, (rm_706_button_rect.x, rm_706_button_rect.y))
     screen.blit(rm_707_button_surface, (rm_707_button_rect.x, rm_707_button_rect.y))
     screen.blit(rm_708_button_surface, (rm_708_button_rect.x, rm_708_button_rect.y))
     screen.blit(rm_709_button_surface, (rm_709_button_rect.x, rm_709_button_rect.y))
     screen.blit(rm_801_button_surface, (rm_801_button_rect.x, rm_801_button_rect.y))
     screen.blit(rm_802_button_surface, (rm_802_button_rect.x, rm_802_button_rect.y))
     screen.blit(rr_1_button_surface, (rr_1_button_rect.x, rr_1_button_rect.y))
     screen.blit(weight_button_surface, (weight_button_rect.x, weight_button_rect.y))
     # Green
     # Yellow
     screen.blit(rm_501_button_surface, (rm_501_button_rect.x, rm_501_button_rect.y))
     screen.blit(rm_502_button_surface, (rm_502_button_rect.x, rm_502_button_rect.y))
     screen.blit(rm_503_button_surface, (rm_503_button_rect.x, rm_503_button_rect.y))
     screen.blit(rm_504_button_surface, (rm_504_button_rect.x, rm_504_button_rect.y))
     screen.blit(rm_505_button_surface, (rm_505_button_rect.x, rm_505_button_rect.y))
     screen.blit(rm_506_button_surface, (rm_506_button_rect.x, rm_506_button_rect.y))
     screen.blit(rm_507_button_surface, (rm_507_button_rect.x, rm_507_button_rect.y))
     screen.blit(rm_508_button_surface, (rm_508_button_rect.x, rm_508_button_rect.y))
     screen.blit(rm_509_button_surface, (rm_509_button_rect.x, rm_509_button_rect.y))
     screen.blit(rm_510_button_surface, (rm_510_button_rect.x, rm_510_button_rect.y))
     screen.blit(rm_511_button_surface, (rm_511_button_rect.x, rm_511_button_rect.y))
     screen.blit(rm_512_button_surface, (rm_512_button_rect.x, rm_512_button_rect.y))
     screen.blit(rm_514_button_surface, (rm_514_button_rect.x, rm_514_button_rect.y))
     screen.blit(rm_515_button_surface, (rm_515_button_rect.x, rm_515_button_rect.y))
     screen.blit(rm_516_button_surface, (rm_516_button_rect.x, rm_516_button_rect.y))
     screen.blit(rm_517_button_surface, (rm_517_button_rect.x, rm_517_button_rect.y))
     screen.blit(RR_yellow_button_surface, (RR_yellow_button_rect.x, RR_yellow_button_rect.y))
     # Yellow
     # Blue
     screen.blit(rm_905_button_surface, (rm_905_button_rect.x, rm_905_button_rect.y))
     screen.blit(rm_904_button_surface, (rm_904_button_rect.x, rm_904_button_rect.y))
     screen.blit(tennis_courts_button_surface, (tennis_courts_button_rect.x, tennis_courts_button_rect.y))
     screen.blit(lemon_parking_lot_button_surface,
                 (lemon_parking_lot_button_rect.x, lemon_parking_lot_button_rect.y))
     screen.blit(lawn_button_surface, (lawn_button_rect.x, lawn_button_rect.y))
     screen.blit(media_center_button_surface, (media_center_button_rect.x, media_center_button_rect.y))
     screen.blit(senate_room_button_surface, (senate_room_button_rect.x, senate_room_button_rect.y))
     screen.blit(mc1_button_surface, (mc1_button_rect.x, mc1_button_rect.y))
     screen.blit(mc2_button_surface, (mc2_button_rect.x, mc2_button_rect.y))
     screen.blit(mc3_button_surface, (mc3_button_rect.x, mc3_button_rect.y))
     screen.blit(mc4_button_surface, (mc4_button_rect.x, mc4_button_rect.y))
     # Blue
     # Orange
     screen.blit(PO_button_surface, (PO_button_rect.x, PO_button_rect.y))
     screen.blit(nurse_button_surface, (nurse_button_rect.x, nurse_button_rect.y))
     screen.blit(rgr_button_surface, (rgr_button_rect.x, rgr_button_rect.y))
     screen.blit(rm_311_button_surface, (rm_311_button_rect.x, rm_311_button_rect.y))
     screen.blit(conf_button_surface, (conf_button_rect.x, conf_button_rect.y))
     screen.blit(rm_310_button_surface, (rm_310_button_rect.x, rm_310_button_rect.y))
     screen.blit(ccc_button_surface, (ccc_button_rect.x, ccc_button_rect.y))
     screen.blit(rm_304_button_surface, (rm_304_button_rect.x, rm_304_button_rect.y))
     screen.blit(rr_orange_button_surface, (rr_orange_button_rect.x, rr_orange_button_rect.y))
     screen.blit(rm_309_button_surface, (rm_309_button_rect.x, rm_309_button_rect.y))
     screen.blit(rm_308_button_surface, (rm_308_button_rect.x, rm_308_button_rect.y))
     screen.blit(rm_305_button_surface, (rm_305_button_rect.x, rm_305_button_rect.y))
     screen.blit(rm_306_button_surface, (rm_306_button_rect.x, rm_306_button_rect.y))
     screen.blit(rm_307_button_surface, (rm_307_button_rect.x, rm_307_button_rect.y))
     screen.blit(lunch_button_surface, (lunch_button_rect.x, lunch_button_rect.y))
     screen.blit(attendance_button_surface, (attendance_button_rect.x, attendance_button_rect.y))
     # Orange
     # Brown
     screen.blit(pool_button_surface, (pool_button_rect.x, pool_button_rect.y))
     screen.blit(rm_804_button_surface, (rm_804_button_rect.x, rm_804_button_rect.y))
     screen.blit(rm_805_button_surface, (rm_805_button_rect.x, rm_805_button_rect.y))
     screen.blit(locker_rooms_button_surface, (locker_rooms_button_rect.x, locker_rooms_button_rect.y))
     screen.blit(rm_207_button_surface, (rm_207_button_rect.x, rm_207_button_rect.y))
     screen.blit(rm_206_button_surface, (rm_206_button_rect.x, rm_206_button_rect.y))
     screen.blit(rm_205_button_surface, (rm_205_button_rect.x, rm_205_button_rect.y))
     screen.blit(rm_204_button_surface, (rm_204_button_rect.x, rm_204_button_rect.y))
     screen.blit(rm_203_button_surface, (rm_203_button_rect.x, rm_203_button_rect.y))
     screen.blit(rm_202_button_surface, (rm_202_button_rect.x, rm_202_button_rect.y))
     screen.blit(rm_201_button_surface, (rm_201_button_rect.x, rm_201_button_rect.y))
     screen.blit(rm_107_button_surface, (rm_107_button_rect.x, rm_107_button_rect.y))
     screen.blit(rm_106_button_surface, (rm_106_button_rect.x, rm_106_button_rect.y))
     screen.blit(rm_105_button_surface, (rm_105_button_rect.x, rm_105_button_rect.y))
     screen.blit(rm_104_button_surface, (rm_104_button_rect.x, rm_104_button_rect.y))
     screen.blit(rm_103_button_surface, (rm_103_button_rect.x, rm_103_button_rect.y))
     screen.blit(rm_102_button_surface, (rm_102_button_rect.x, rm_102_button_rect.y))
     screen.blit(rm_101_button_surface, (rm_101_button_rect.x, rm_101_button_rect.y))
     # Brown

 else:
     screen.blit(current_screen, (0, 0))
     # Back
     screen.blit(back_button_surface, (back_button_rect.x, back_button_rect.y))
     # Back


 # Update the game state
 pygame.display.update()

