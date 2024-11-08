import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1240, 930))
pygame.display.set_caption('TCHS Interactive Map')

map_image = pygame.image.load('graphics/map_copy.png')

image_paths = {
    'map': 'graphics/map_copy.png',
    'rm_601': 'graphics/601.png',
    'staff_lounge': 'graphics/staff_lounge.png',
    'rm_214': 'graphics/214.png',
    'rm_116': 'graphics/116.png',
    'rm_115': 'graphics/115.png',
    'rm_114': 'graphics/114.png',
    'rm_116': 'graphics/116.png',
    'rm_115': 'graphics/115.png',
    'rm_114': 'graphics/114.png',
    'rm_110': 'graphics/110.png',
    'rm_108': 'graphics/108.png',
    'rm_208': 'graphics/208.png',
    'rm_113': 'graphics/113.png',
    'rm_213': 'graphics/213.png',
    'rm_112': 'graphics/601.png',  
    'rm_111': 'graphics/601.png',
    'rm_109': 'graphics/601.png',
    'gym': 'graphics/Front Entrance to Gym.png',
    'tennis': 'graphics/Tennis Courts.png',
    'rm_702': 'graphics/Room 702 and Tennis Court Entrance.png',
    'circle': 'graphics/Senior Circle_1.png',
    'rm_703': 'graphics/601.png',
    'rm_704': 'graphics/700s side and gym stairs.png',
    'rm_705': 'graphics/room 705 (edt) and 704.png',
    'rm_706': 'graphics/room 706 and 707.png',
    'rm_707': 'graphics/room 707.png',
    'rm_708': 'graphics/601.png',
    'rm_709': 'graphics/Boys restroom and art room.png',
    'rm_801': 'graphics/601.png',
    'rm_802': 'graphics/601.png',
    'rr_1': 'graphics/room 707 windows and girls restroom.png',
    'weight': 'graphics/Weight Room.png',
    'rm_501': 'graphics/rm_501.png',
    'rm_502': 'graphics/rm_502.png',
    'rm_503': 'graphics/rm_503.png',
    'rm_504': 'graphics/rm_504.png',
    'rm_505': 'graphics/rm_505.png',
    'rm_506': 'graphics/rm_506.png',
    'rm_507': 'graphics/rm_507.png',
    'rm_508': 'graphics/rm_508.png',
    'rm_509': 'graphics/rm_509.png',
    'rm_510': 'graphics/rm_510.png',
    'rm_511': 'graphics/rm_511.png',
    'rm_512': 'graphics/rm_512.png',
    'rm_514': 'graphics/rm_514.png',
    'rm_515': 'graphics/rm_515.png',
    'rm_516': 'graphics/rm_516.png',
    'rm_517': 'graphics/rm_517.png',
    'rr_yellow': 'graphics/601.png',
    'rm_905': 'graphics/601 Entrance.PNG',
    'rm_904': 'graphics/601 Entrance.PNG',
    'tennis_courts': 'graphics/601 Entrance.PNG',
    'lemon_parking_lot': 'graphics/601 Entrance.PNG',
    'lawn': 'graphics/601 Entrance.PNG',
    'media_center': 'graphics/601 Entrance.PNG',
    'senate_room': 'graphics/601 Entrance.PNG',
    'mc1': 'graphics/601 Entrance.PNG',
    'mc2': 'graphics/601 Entrance.PNG',
    'mc3': 'graphics/601 Entrance.PNG',
    'mc4': 'graphics/601 Entrance.PNG',
    'principal_office': 'graphics/principal_s_office.png',
    'nurse': 'graphics/nurse_s_office.png',
    'registrar': 'graphics/601.png',
    'conference_room': 'graphics/conference_room.png',
    'rm_311': 'graphics/311_staff_entrance.png',
    'attendance_office': 'graphics/attendance_office_inner_entrance.png',
    'rm_310': 'graphics/rm_310.png',
    'ccc': 'graphics/counseling_office.png',
    'rm_304': 'graphics/rm_304.png',
    'rr_orange': 'graphics/601.png',
    'rm_309': 'graphics/601.png',
    'rm_308': 'graphics/601.png',
    'rm_305': 'graphics/rm_305.png',
    'rm_306': 'graphics/rm_306.png',
    'rm_307': 'graphics/rm_307.png',
    'lunch': 'graphics/601.png',
    'rm_101': 'graphics/rm_101.png',
    'rm_102': 'graphics/rm_102.png',
    'rm_103': 'graphics/rm_103.png',
    'rm_104': 'graphics/rm_104.png',
    'rm_105': 'graphics/rm_105.png',
    'rm_106': 'graphics/rm_106.png',
    'rm_107': 'graphics/rm_107.png',
    'rm_201': 'graphics/rm_201.png',
    'rm_202': 'graphics/rm_202.png',
    'rm_203': 'graphics/rm_203.png',
    'rm_204': 'graphics/rm_204.png',
    'rm_205': 'graphics/rm_205.png',
    'rm_206': 'graphics/rm_206.png',
    'rm_207': 'graphics/rm_207.png',
    'rm_804': 'graphics/rm_804.png',
    'rm_805': 'graphics/601.png',
    'locker': 'graphics/locker.png',
    'pool': 'graphics/pool.png',
}

images_cache = {}
for key, path in image_paths.items():
    try:
        img = pygame.image.load(path).convert_alpha()
        if key in [
            'gym', 'tennis', 'rm_702', 'circle', 'rm_703', 'rm_704',
            'rm_705', 'rm_706', 'rm_707', 'rm_708', 'rm_709', 'rm_801',
            'rm_802', 'rr_1', 'weight', 'principal_office', 'nurse',
            'registrar', 'conference_room', 'rm_311', 'attendance_office',
            'rm_310', 'ccc', 'rm_304', 'rr_orange', 'rm_309', 'rm_308',
            'rm_305', 'rm_306', 'rm_307', 'lunch'
        ]:
            img = pygame.transform.scale(img, (1240, 930))
        images_cache[key] = img
    except pygame.error as e:
        print(f"Unable to load image at {path}: {e}")
        images_cache[key] = None  

font_sizes = [33, 25, 20, 15, 30, 16, 18, 27, 28]
fonts_cache = {}
for size in font_sizes:
    fonts_cache[size] = pygame.font.Font(None, size)

buttons_info = [
    {'name': 'rm_601', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (775, 400), 'text': '601', 'font_size': 33},
    {'name': 'staff_lounge', 'image_key': 'staff_lounge', 'size': (115, 51), 'pos': (743, 268), 'text': 'Staff Lounge', 'font_size': 25},
    {'name': 'rm_216', 'image_key': 'rm_214', 'size': (50, 25), 'pos': (847, 655), 'text': '216', 'font_size': 33},
    {'name': 'rm_215', 'image_key': 'rm_214', 'size': (50, 25), 'pos': (904, 655), 'text': '215', 'font_size': 33},
    {'name': 'rm_214', 'image_key': 'rm_214', 'size': (50, 25), 'pos': (960, 655), 'text': '214', 'font_size': 33},
    {'name': 'RR_1', 'image_key': 'rm_214', 'size': (50, 25), 'pos': (1016, 655), 'text': 'RR', 'font_size': 33},
    {'name': 'rm_116', 'image_key': 'rm_116', 'size': (50, 25), 'pos': (847, 690), 'text': '116', 'font_size': 33},
    {'name': 'rm_115', 'image_key': 'rm_115', 'size': (50, 25), 'pos': (904, 690), 'text': '115', 'font_size': 33},
    {'name': 'rm_114', 'image_key': 'rm_114', 'size': (50, 25), 'pos': (960, 690), 'text': '114', 'font_size': 33},
    {'name': 'RR_2', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (1015, 690), 'text': 'RR', 'font_size': 33},
    {'name': 'rm_213', 'image_key': 'rm_213', 'size': (50, 25), 'pos': (1133, 655), 'text': '213', 'font_size': 33},
    {'name': 'rm_113', 'image_key': 'rm_113', 'size': (50, 25), 'pos': (1133, 692), 'text': '113', 'font_size': 33},
    {'name': 'rm_108', 'image_key': 'rm_108', 'size': (50, 25), 'pos': (1133, 773), 'text': '108', 'font_size': 33},
    {'name': 'rm_208', 'image_key': 'rm_208', 'size': (50, 25), 'pos': (1133, 738), 'text': '208', 'font_size': 33},
    {'name': 'rm_212', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (795, 738), 'text': '212', 'font_size': 33},
    {'name': 'rm_211', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (852, 738), 'text': '211', 'font_size': 33},
    {'name': 'rm_210', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (908, 738), 'text': '210', 'font_size': 33},
    {'name': 'rm_209', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (963, 738), 'text': '209', 'font_size': 33},
    {'name': 'RR_3', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (1020, 738), 'text': 'RR', 'font_size': 33},
    {'name': 'rm_112', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (795, 773), 'text': '112', 'font_size': 33},
    {'name': 'rm_111', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (852, 773), 'text': '111', 'font_size': 33},
    {'name': 'rm_110', 'image_key': 'rm_110', 'size': (50, 25), 'pos': (908, 773), 'text': '110', 'font_size': 33},
    {'name': 'rm_109', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (963, 773), 'text': '109', 'font_size': 33},
    {'name': 'RR_4', 'image_key': 'rm_601', 'size': (50, 25), 'pos': (1020, 773), 'text': 'RR', 'font_size': 33},
    
    {'name': 'RR_400', 'image_key': 'rm_601', 'size': (36, 10), 'pos': (1018, 395), 'text': 'RR', 'font_size': 20},
    {'name': 'rm_401', 'image_key': 'rm_401', 'size': (36, 44), 'pos': (1018, 410), 'text': '401', 'font_size': 30},
    {'name': 'rm_402', 'image_key': 'rm_402', 'size': (36, 44), 'pos': (1018, 320), 'text': '402', 'font_size': 30},
    {'name': 'rm_403', 'image_key': 'rm_403', 'size': (36, 44), 'pos': (1018, 265), 'text': '403', 'font_size': 30},
    {'name': 'rm_404', 'image_key': 'rm_404', 'size': (36, 44), 'pos': (1018, 210), 'text': '404', 'font_size': 30},
    {'name': 'rm_405', 'image_key': 'rm_405', 'size': (36, 44), 'pos': (1058, 210), 'text': '405', 'font_size': 30},
    {'name': 'rm_406', 'image_key': 'rm_406', 'size': (36, 44), 'pos': (1058, 265), 'text': '406', 'font_size': 30},
    {'name': 'rm_407', 'image_key': 'rm_407', 'size': (36, 44), 'pos': (1058, 320), 'text': '407', 'font_size': 30},
    {'name': 'rm_408', 'image_key': 'rm_408', 'size': (36, 44), 'pos': (1058, 410), 'text': '408', 'font_size': 30},
    {'name': 'rm_409', 'image_key': 'rm_409', 'size': (36, 44), 'pos': (1058, 467), 'text': '409', 'font_size': 30},
    {'name': 'rm_410', 'image_key': 'rm_410', 'size': (35, 44), 'pos': (1018, 467), 'text': '410', 'font_size': 30},
    
    {'name': 'gym', 'image_key': 'gym', 'size': (70, 50), 'pos': (475, 414), 'text': 'Gym', 'font_size': 33},
    {'name': 'tennis', 'image_key': 'tennis', 'size': (39, 50), 'pos': (441, 292), 'text': 'Tennis', 'font_size': 15},
    {'name': 'rm_702', 'image_key': 'rm_702', 'size': (50, 25), 'pos': (499, 306), 'text': '702', 'font_size': 33},
    {'name': 'circle', 'image_key': 'circle', 'size': (49, 33), 'pos': (645, 411), 'text': 'Sr. Circle', 'font_size': 15},
    {'name': 'rm_703', 'image_key': 'rm_703', 'size': (48, 25), 'pos': (560, 309), 'text': '703', 'font_size': 33},
    {'name': 'rm_705', 'image_key': 'rm_705', 'size': (23, 25), 'pos': (639, 309), 'text': '705', 'font_size': 20},
    {'name': 'rm_704', 'image_key': 'rm_704', 'size': (23, 25), 'pos': (611, 309), 'text': '704', 'font_size': 20},
    {'name': 'rm_706', 'image_key': 'rm_706', 'size': (22, 25), 'pos': (666, 333), 'text': '706', 'font_size': 20},
    {'name': 'rm_707', 'image_key': 'rm_707', 'size': (22, 25), 'pos': (666, 303), 'text': '707', 'font_size': 20},
    {'name': 'rm_708', 'image_key': 'rm_708', 'size': (22, 25), 'pos': (666, 273), 'text': '708', 'font_size': 20},
    {'name': 'rm_709', 'image_key': 'rm_709', 'size': (25, 22), 'pos': (638, 248), 'text': '709', 'font_size': 20},
    {'name': 'rm_801', 'image_key': 'rm_801', 'size': (22, 25), 'pos': (572, 405), 'text': '801', 'font_size': 20},
    {'name': 'rm_802', 'image_key': 'rm_802', 'size': (22, 25), 'pos': (572, 429), 'text': '802', 'font_size': 20},
    {'name': 'rr_1', 'image_key': 'rr_1', 'size': (21, 25), 'pos': (666, 243), 'text': 'RR', 'font_size': 20},
    {'name': 'weight', 'image_key': 'weight', 'size': (30, 20), 'pos': (505, 180), 'text': 'Image', 'font_size': 15},
    
    {'name': 'rm_501', 'image_key': 'rm_501', 'size': (35, 25), 'pos': (1098, 429), 'text': '501', 'font_size': 30},
    {'name': 'rm_502', 'image_key': 'rm_502', 'size': (37, 25), 'pos': (1097, 397), 'text': '502', 'font_size': 30},
    {'name': 'rm_503', 'image_key': 'rm_503', 'size': (37, 25), 'pos': (1097.7, 345), 'text': '503', 'font_size': 30},
    {'name': 'rm_504', 'image_key': 'rm_504', 'size': (37, 25), 'pos': (1097.7, 317), 'text': '504', 'font_size': 30},
    {'name': 'rm_505', 'image_key': 'rm_505', 'size': (36, 25), 'pos': (1098.3, 284), 'text': '505', 'font_size': 30},
    {'name': 'rm_506', 'image_key': 'rm_506', 'size': (35, 25), 'pos': (1097.5, 248), 'text': '506', 'font_size': 30},
    {'name': 'rm_507', 'image_key': 'rm_507', 'size': (35, 25), 'pos': (1097.5, 210), 'text': '507', 'font_size': 30},
    {'name': 'rm_508', 'image_key': 'rm_508', 'size': (38, 25), 'pos': (1137, 210), 'text': '508', 'font_size': 30},
    {'name': 'rm_509', 'image_key': 'rm_509', 'size': (38.5, 25), 'pos': (1137, 248), 'text': '509', 'font_size': 30},
    {'name': 'rm_510', 'image_key': 'rm_510', 'size': (35, 25), 'pos': (1137, 284), 'text': '510', 'font_size': 30},
    {'name': 'rm_511', 'image_key': 'rm_511', 'size': (35, 25), 'pos': (1138, 317), 'text': '511', 'font_size': 30},
    {'name': 'rm_512', 'image_key': 'rm_512', 'size': (35, 25), 'pos': (1137, 345.7), 'text': '512', 'font_size': 30},
    {'name': 'rm_514', 'image_key': 'rm_514', 'size': (35, 25), 'pos': (1137, 397.5), 'text': '514', 'font_size': 30},
    {'name': 'rm_515', 'image_key': 'rm_515', 'size': (35, 25), 'pos': (1137, 429), 'text': '515', 'font_size': 30},
    {'name': 'rm_516', 'image_key': 'rm_516', 'size': (35, 25), 'pos': (1137, 478), 'text': '516', 'font_size': 30},
    {'name': 'rm_517', 'image_key': 'rm_517', 'size': (35, 25), 'pos': (1098, 478), 'text': '517', 'font_size': 30},
    {'name': 'rr_yellow', 'image_key': 'rr_yellow', 'size': (35, 10.5), 'pos': (1098, 372), 'text': 'RR', 'font_size': 20},
    
    {'name': 'rm_905', 'image_key': 'rm_905', 'size': (50, 25), 'pos': (420, 561), 'text': '905', 'font_size': 33},
    {'name': 'rm_904', 'image_key': 'rm_904', 'size': (50, 25), 'pos': (500, 561), 'text': '904', 'font_size': 33},
    {'name': 'tennis_courts', 'image_key': 'tennis_courts', 'size': (120, 25), 'pos': (162, 775), 'text': 'Tennis Courts', 'font_size': 25},
    {'name': 'lemon_parking_lot', 'image_key': 'lemon_parking_lot', 'size': (124, 50), 'pos': (290, 760), 'text': 'Lemon Parking Lot', 'font_size': 16},
    {'name': 'lawn', 'image_key': 'lawn', 'size': (70, 35), 'pos': (470, 750), 'text': 'Lawn', 'font_size': 33},
    {'name': 'media_center', 'image_key': 'media_center', 'size': (120, 25), 'pos': (600, 805), 'text': 'Media Center', 'font_size': 25},
    {'name': 'senate_room', 'image_key': 'senate_room', 'size': (80, 25), 'pos': (643, 675), 'text': 'Senate Room', 'font_size': 16},
    {'name': 'mc1', 'image_key': 'mc1', 'size': (40, 25), 'pos': (600, 736), 'text': 'MC1', 'font_size': 25},
    {'name': 'mc2', 'image_key': 'mc2', 'size': (40, 25), 'pos': (600, 712), 'text': 'MC2', 'font_size': 25},
    {'name': 'mc3', 'image_key': 'mc3', 'size': (40, 25), 'pos': (600, 687), 'text': 'MC3', 'font_size': 25},
    {'name': 'mc4', 'image_key': 'mc4', 'size': (40, 25), 'pos': (600, 663), 'text': 'MC4', 'font_size': 25},
    
    {'name': 'principal_office', 'image_key': 'principal_office', 'size': (50, 25), 'pos': (694, 545), 'text': "Principal's Office", 'font_size': 13},
    {'name': 'conf', 'image_key': 'conference_room', 'size': (43, 35), 'pos': (694, 585), 'text': 'Conf. Room', 'font_size': 13},
    {'name': 'nurse', 'image_key': 'nurse', 'size': (36, 24), 'pos': (779, 517), 'text': 'Nurse', 'font_size': 28},
    {'name': 'registrar', 'image_key': 'registrar', 'size': (38, 24), 'pos': (818, 517), 'text': 'Registrar', 'font_size': 28},
    {'name': 'rm_311', 'image_key': 'rm_311', 'size': (40, 35), 'pos': (876, 545), 'text': '311', 'font_size': 30},
    {'name': 'attendance', 'image_key': 'attendance_office', 'size': (40, 35), 'pos': (876, 585), 'text': 'Attendance', 'font_size': 13},
    {'name': 'rm_310', 'image_key': 'rm_310', 'size': (60, 35), 'pos': (960, 545), 'text': '310', 'font_size': 30},
    {'name': 'ccc', 'image_key': 'ccc', 'size': (100, 35), 'pos': (923, 585), 'text': 'Counseling/College & Career', 'font_size': 20},
    {'name': 'rm_304', 'image_key': 'rm_304', 'size': (27, 25), 'pos': (1031, 590), 'text': '304', 'font_size': 20},
    {'name': 'rr_orange', 'image_key': 'rr_orange', 'size': (16, 40), 'pos': (1062, 565), 'text': 'RR', 'font_size': 20},
    {'name': 'rm_309', 'image_key': 'rm_309', 'size': (30, 25), 'pos': (1105, 551), 'text': '309', 'font_size': 20},
    {'name': 'rm_308', 'image_key': 'rm_308', 'size': (30, 25), 'pos': (1152, 551), 'text': '308', 'font_size': 20},
    {'name': 'rm_305', 'image_key': 'rm_305', 'size': (30, 25), 'pos': (1105, 590), 'text': '305', 'font_size': 20},
    {'name': 'rm_306', 'image_key': 'rm_306', 'size': (25, 25), 'pos': (1143, 590), 'text': '306', 'font_size': 18},
    {'name': 'rm_307', 'image_key': 'rm_307', 'size': (25, 25), 'pos': (1170, 590), 'text': '307', 'font_size': 18},
    {'name': 'lunch', 'image_key': 'lunch', 'size': (65, 30), 'pos': (910, 299), 'text': 'Lunch', 'font_size': 27},
    
    {'name': 'pool', 'image_key': 'pool', 'size': (50, 25), 'pos': (300, 450), 'text': 'Pool', 'font_size': 33},
    {'name': 'rm_804', 'image_key': 'rm_804', 'size': (50, 25), 'pos': (385, 415), 'text': '804', 'font_size': 33},
    {'name': 'rm_805', 'image_key': 'rm_805', 'size': (50, 25), 'pos': (385, 485), 'text': '805', 'font_size': 33},
    {'name': 'locker', 'image_key': 'locker', 'size': (50, 25), 'pos': (385, 450), 'text': 'Locker', 'font_size': 33},
    {'name': 'rm_207', 'image_key': 'rm_207', 'size': (50, 25), 'pos': (795, 820), 'text': '207', 'font_size': 33},
    {'name': 'rm_206', 'image_key': 'rm_206', 'size': (50, 25), 'pos': (850, 820), 'text': '206', 'font_size': 33},
    {'name': 'rm_205', 'image_key': 'rm_205', 'size': (50, 25), 'pos': (905, 820), 'text': '205', 'font_size': 33},
    {'name': 'rm_204', 'image_key': 'rm_204', 'size': (50, 25), 'pos': (963, 820), 'text': '204', 'font_size': 33},
    {'name': 'rm_203', 'image_key': 'rm_203', 'size': (50, 25), 'pos': (1018, 820), 'text': '203', 'font_size': 33},
    {'name': 'rm_202', 'image_key': 'rm_202', 'size': (50, 25), 'pos': (1072, 820), 'text': '202', 'font_size': 33},
    {'name': 'rm_201', 'image_key': 'rm_201', 'size': (50, 25), 'pos': (1130, 820), 'text': '201', 'font_size': 33},
    {'name': 'rm_107', 'image_key': 'rm_107', 'size': (50, 25), 'pos': (795, 857), 'text': '107', 'font_size': 33},
    {'name': 'rm_106', 'image_key': 'rm_106', 'size': (50, 25), 'pos': (850, 857), 'text': '106', 'font_size': 33},
    {'name': 'rm_105', 'image_key': 'rm_105', 'size': (50, 25), 'pos': (905, 857), 'text': '105', 'font_size': 33},
    {'name': 'rm_104', 'image_key': 'rm_104', 'size': (50, 25), 'pos': (963, 857), 'text': '104', 'font_size': 33},
    {'name': 'rm_103', 'image_key': 'rm_103', 'size': (50, 25), 'pos': (1018, 857), 'text': '103', 'font_size': 33},
    {'name': 'rm_102', 'image_key': 'rm_102', 'size': (50, 25), 'pos': (1072, 857), 'text': '102', 'font_size': 33},
    {'name': 'rm_101', 'image_key': 'rm_101', 'size': (50, 25), 'pos': (1130, 857), 'text': '101', 'font_size': 33},
        {'name': 'back', 'image_key': 'back', 'size': (100, 50), 'pos': (30, 20), 'text': 'Back', 'font_size': 33},
]

class Button:
    def __init__(self, info):
        self.name = info['name']
        self.image = images_cache.get(info['image_key'])
        self.size = info['size']
        self.pos = info['pos']
        self.text = info['text']
        self.font = fonts_cache.get(info['font_size'], pygame.font.Font(None, 25))
        self.surface = pygame.Surface(self.size, pygame.SRCALPHA)
        self.rect = pygame.Rect(self.pos, self.size)
        self.text_surface = self.font.render(self.text, True, (0, 0, 0))
        self.text_rect = self.text_surface.get_rect(center=(self.size[0] / 2, self.size[1] / 2))
    
    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            pygame.draw.rect(self.surface, (127, 255, 212), self.surface.get_rect())
        else:
            pygame.draw.rect(self.surface, (255, 255, 255), self.surface.get_rect())
        

        self.surface.blit(self.text_surface, self.text_rect)
        
        screen.blit(self.surface, self.pos)
    
    def is_clicked(self, event_pos):
        return self.rect.collidepoint(event_pos)

buttons = [Button(info) for info in buttons_info]

current_screen = map_image

running = True
while running:
    clock.tick(60)  
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for button in buttons:
                if button.is_clicked(event.pos):
                    if button.name == 'back':
                        current_screen = map_image
                    else:
                        current_screen = button.image
                    break
    
    screen.fill((155, 255, 155))
    
    screen.blit(current_screen, (0, 0))
    
    if current_screen == map_image:
        for button in buttons:
            button.draw(screen)
    else:
        for button in buttons:
            if button.name == 'back':
                button.draw(screen)
                break
    
    pygame.display.flip()

pygame.quit()
sys.exit()
