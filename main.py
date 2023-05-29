import pygame as py

title_py = "Scene 1 Starting scene"
frame = 50

# color setting for background and foreground
green = (0, 200, 0)
white = (255, 255, 255)

# this will set the font of the screen
font_size = None

# building the windows and initialising it
py.init()
clock = py.time.Clock()
screen = py.display.set_mode([740, 340])
py.display.set_caption(title_py)

# calling and building the fonts
screen_font = py.font.Font(font_size, 50)

# scene class in pygame
class Scene():
	def __init__(self):
		self.next_scene = self

	def process_input(self, events, press):
		raise NotImplementedError

	def update(self):
		raise NotImplementedError

	def rendering(self):
		raise NotImplementedError

	def terminate(self):
		self.next_scene = None

# this will be the first scene class as
# the prime and opening scene of our app
class starting_scene(Scene):
	def __init__(self):
		super().__init__()

	def process_input(self, events, press):
		for event in events:
			if event.type == py.KEYDOWN:
				if event.key == py.K_SPACE:
					self.next_scene = EndScene()

	def rendering(self):
		screen.fill(green)
		text = screen_font.render(title_py, 1, white)
		rect = text.get_rect()
		rect.centerx = 740 // 2
		rect.centery = 50
		screen.blit(text, rect)

	def update(self):
		pass

class EndScene(Scene):
	def __init__(self):
		super().__init__()

	def process_input(self, events, press):
		for event in events:
			if event.type == py.KEYDOWN:
				if event.key == py.K_SPACE:
					self.next_scene = starting_scene()

	def update(self):
		pass
	# rendering the scene function
	def rendering(self):
		screen.fill(green)
		
		# font color will be white
		text = screen_font.render("Scene 2 Game Ending ", 1, white)
		rect = text.get_rect()
		rect.centerx = 370 # location from x-axis
		rect.centery = 50 # location from y-axis
		screen.blit(text, rect)

class app_class():
	def __init__(self):
		self.running_scene = starting_scene()

	def control(self, event, press):
		x_out = event.type == py.QUIT
		quit = press[py.K_q]
		
		# if anyone click on the cross
		# button or press the 'q' button
		# it will quit the window
		return x_out or (quit)

	def run(self):
		while self.running_scene != None:
			eve = []
			press = py.key.get_pressed()
			for event in py.event.get():
				if self.control(event, press):
					self.running_scene.terminate()
				else:
					eve.append(event)

			# Manage scene
			self.running_scene.process_input(eve, press)
			self.running_scene.update()
			
			# dont move it as first we need to update then render
			self.running_scene.rendering()
			
			# moving the scene one by one
			self.running_scene = self.running_scene.next_scene
			
			# means it will allow user to change the scene
			py.display.flip()
			# Update and tick
			clock.tick(frame)

# main (our code will run from here)
if __name__ == "__main__":
	let_check = app_class()
	let_check.run()
	py.quit()
