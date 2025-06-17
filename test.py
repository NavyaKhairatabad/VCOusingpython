import pygame
import numpy as np
import sounddevice as sd

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("VCO Game - Frequency Control")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# VCO Settings
sample_rate = 44100 # Audio sample rate
base_frequency = 220 # Starting frequency (Hz)
frequency = base_frequency # Current VCO frequency
amplitude = 0.5 # Signal amplitude
running = True

def generate_wave(frequency, duration=0.1):
    """Generate a sine wave for the given frequency."""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = amplitude * np.sin (2 * np.pi * frequency * t)
    return wave

def play_sound(frequency):
    """Play generated waveform."""
    wave = generate_wave(frequency)
    sd.play(wave, samplerate = sample_rate)
    
def draw_waveform():
    """Draw the waveform representation on the screen."""
    screen.fill(WHITE)
    wave_points = []
    for x in range(WIDTH):
        y = int(HEIGHT / 2 + 50 * np.sin(2 * np.pi * (frequency / 100) * (x / WIDTH)))
        wave_points.append((x, y))
    pygame.draw.lines(screen, GREEN, False, wave_points, 2)
    pygame.display.flip()

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Increase or decrease frequency using arrow keys
    if keys[pygame.K_UP]:
        frequency += 10
        play_sound(frequency)
    if keys[pygame.K_DOWN]:
        frequency -= 10
        play_sound(frequency)

    # Ensure frequency remains within limits
    frequency = max (100, min (frequency, 1000))

    # Draw waveform visualization
    draw_waveform ()

pygame.quit()