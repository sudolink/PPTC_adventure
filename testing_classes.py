class pavement():
    def __init__(self):
        self.width = 50
        self.height = 150
        self.x = 0
        self.y = sheight - self.height
        self.blocks = []

    def makeBlock(self,x,y,width,height):
        new_block = pygame.Rect(x,y,width,height)
        self.blocks.append(new_block)

    def makeBlocks(self,how_many):
        for block in how_many:
            self.makeBlock(self.x,self.y,self.width,self.height)
            self.x += self.width * 2

    def drawPavement(self):
        for block in self.blocks:
            pygame.draw.rect(screen,(100,100,100),block)

class sun():
    def __init__(self):
        self.x = 700
        self.y = 100
        self.center = (self.x,self.y)
        self.radius = 90
        self.color = (255,255,102)
        self.shadow_lines = []


    def stick_to_mouse(self):
        mouse_loc = pygame.mouse.get_pos()
        self.x = mouse_loc[0]
        self.y = mouse_loc[1]
        self.center = mouse_loc

    def draw_sun(self):
        self.stick_to_mouse()
        pygame.draw.circle(screen,self.color,self.center,self.radius)

    def cast_shadows(self,player_location,player_size):
        pass
        #imaginary line from center of sun to top of head
        #where it touches the ground (player x + player height -> feet)
        #is where the top of the shadow should be
        #the beginning of the shadow should be at feet
        #make just an elipse for now
        #pygame.draw.line(surface, color, start_pos, end_pos, width)

        #player_pos == (x,y), player_size == (width,height)
        start_pos = self.center
        end_pos_head = (player_location[0]+player_size[0]/2,player_location[1])
        end_pos_feet = (player_location[0]+player_size[0]/2,player_location[1]+player_size[1])
        pygame.draw.line(screen,(0,0,0),start_pos,end_pos_head) #NEED TO EXTEND THIS ONE TO THE FLOOR SOMEHOW
        pygame.draw.line(screen,(0,0,0),start_pos,end_pos_feet)
