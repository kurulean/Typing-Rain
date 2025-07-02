import pygame, random, sys, requests



# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Screen settings
WIDTH, HEIGHT = 800, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Typing Rain")


background = pygame.image.load("citywallpaper.png")
cloud_layer = pygame.image.load("cloud_layer.png").convert_alpha()


# Sounds and Music
pygame.mixer.music.load("bg_music.mp3")
pygame.mixer.music.set_volume(.2)
pygame.mixer.music.play(-1)

typing_sound = pygame.mixer.Sound("m.mp3")
typing_sound.set_volume(.9)


# Fonts and Colors
FALL_FONT = pygame.font.SysFont("Helvetica", 36)
TYPE_FONT = pygame.font.SysFont("8-bit Arcade In", 80)
GAME_OVER_FONT = pygame.font.SysFont("8-bit Arcade In", 35)
SCORE_FONT = pygame.font.SysFont("8-bit Arcade In", 40)
TITLE_FONT = pygame.font.SysFont("8-bit Arcade In", 120)


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BACKGROUND = (30, 30, 30)

heart_img = pygame.image.load("heart.png").convert_alpha()
heart_img = pygame.transform.scale(heart_img, (32, 32))  # Resize if needed


def show_start_screen():
    waiting = True
    while waiting:
        screen.fill(BACKGROUND)
        screen.blit(background, (-200, -150))

        draw_text_with_outline(
            "Typing Rain",
            TITLE_FONT,
            WHITE,
            (3, 0, 3),
            screen,
            WIDTH // 2 - TITLE_FONT.size("Typing Rain")[0] // 2,
            HEIGHT // 2 - 100
        )

        prompt = SCORE_FONT.render("Press ENTER to Start", True, WHITE)
        screen.blit(prompt, (WIDTH // 2 - prompt.get_width() // 2, HEIGHT // 2 + 50))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False


# Word list from Datamuse API with fallback
def fetch_api_words():
    import requests
    topics = ["light", "dark", "storm", "sky", "water", "tree", "fire", "wind", "earth", "music"]
    all_words = set()

    for topic in topics:
        try:
            url = f"https://api.datamuse.com/words?topics={topic}&max=50"
            response = requests.get(url)
            if response.status_code == 200:
                words = [item["word"] for item in response.json()
                         if item["word"].isalpha() and len(item["word"]) <= 10]
                all_words.update(words)
        except:
            pass  # Skip failed requests

    if len(all_words) >= 100:
        return list(all_words)
    else:
        # Fallback word list
        return [
        "the", "of", "to", "and", "a", "in", "is", "it", "you", "that",
        "he", "was", "for", "on", "are", "with", "as", "his", "they",
        "be", "at", "one", "have", "this", "from", "or", "had", "by", "hot",
        "but", "some", "what", "there", "we", "can", "out", "other", "were", "all",
        "your", "when", "up", "use", "word", "how", "said", "an", "each", "she",
        "which", "do", "their", "time", "if", "will", "way", "about", "many", "then",
        "them", "would", "write", "like", "so", "these", "her", "long", "make", "thing",
        "see", "him", "two", "has", "look", "more", "day", "could", "go", "come",
        "did", "my", "sound", "no", "most", "number", "who", "over", "know", "water",
        "than", "call", "first", "people", "may", "down", "side", "been", "now", "find",
        "any", "new", "work", "part", "take", "get", "place", "made", "live", "where",
        "after", "back", "little", "only", "round", "man", "year", "came", "show", "every",
        "good", "me", "give", "our", "under", "name", "very", "through", "just", "form",
        "sentence", "great", "think", "say", "help", "low", "line", "differ", "turn", "cause",
        "much", "mean", "before", "move", "right", "boy", "old", "too", "same", "tell",
        "does", "set", "three", "want", "air", "well", "also", "play", "small", "end",
        "put", "home", "read", "hand", "port", "large", "spell", "add", "even", "land",
        "here", "must", "big", "high", "such", "follow", "act", "why", "ask", "men",
        "change", "went", "light", "kind", "off", "need", "house", "picture", "try", "us",
        "again", "animal", "point", "mother", "world", "near", "build", "self", "earth", "father",
        "head", "stand", "own", "page", "should", "country", "found", "answer", "school", "grow",
        "study", "still", "learn", "plant", "cover", "food", "sun", "four", "between", "state",
        "keep", "eye", "never", "last", "let", "thought", "city", "tree", "cross", "farm",
        "hard", "start", "might", "story", "saw", "far", "sea", "draw", "left", "late",
        "run", "while", "press", "close", "night", "real", "life", "few", "north",
        "open", "seem", "together", "next", "white", "children", "begin", "got", "walk", "example",
        "ease", "paper", "group", "always", "music", "those", "both", "mark", "often", "letter",
        "until", "mile", "river", "car", "feet", "care", "second", "book", "carry", "took",
        "science", "eat", "room", "friend", "began", "idea", "fish", "mountain", "stop", "once",
        "base", "hear", "horse", "cut", "sure", "watch", "color", "face", "wood", "main",
        "enough", "plain", "girl", "usual", "young", "ready", "above", "ever", "red", "list",
        "though", "feel", "talk", "bird", "soon", "body", "dog", "family", "direct", "pose",
        "leave", "song", "measure", "door", "product", "black", "short", "numeral", "class", "wind",
        "question", "happen", "complete", "ship", "area", "half", "rock", "order", "fire", "south",
        "problem", "piece", "told", "knew", "pass", "since", "top", "whole", "king", "space",
        "heard", "best", "hour", "better", "true", "during", "hundred", "five", "remember", "step",
        "early", "hold", "west", "ground", "interest", "reach", "fast", "verb", "sing", "listen",
        "six", "table", "travel", "less", "morning", "ten", "simple", "several", "vowel", "toward",
        "war", "lay", "against", "pattern", "slow", "center", "love", "person", "money", "serve",
        "appear", "road", "map", "rain", "rule", "govern", "pull", "cold", "notice", "voice",
        "unit", "power", "town", "fine", "certain", "fly", "fall", "lead", "cry", "dark",
        "machine", "note", "wait", "plan", "figure", "star", "box", "noun", "field", "rest"
        ]

WORDS = fetch_api_words()
print("Fetched words from Datamuse API:")
print(WORDS)
print(f"Total words fetched: {len(WORDS)}")


# Game variables
clock = pygame.time.Clock()


# Out line text
def draw_text_with_outline(text, font, text_color, outline_color, surface, x, y):
    base = font.render(text, True, text_color)
    outline = font.render(text, True, outline_color)
    rect = base.get_rect(topleft = (x, y))

    # Draw outline in 8 directions
    for dx in range(-3, 3):
        for dy in range(-3, 3):
            if dx != 0 or dy != 0:
                surface.blit(outline, rect.move(dx, dy))

    # Draw main text
    surface.blit(base, rect)


class Word:
    def __init__(self, text):
        self.text = text
        self.x = random.randint(50, WIDTH - 150)
        self.y = -50
        self.speed = speed + random.uniform(0, 1)

    def draw(self):
        word_surface = FALL_FONT.render(self.text, True, WHITE)
        screen.blit(word_surface, (self.x, self.y))

    def update(self):

        self.y += self.speed

# Spawn word every N frames
SPAWN_EVENT = pygame.USEREVENT + 1

time1 = 2000
time2 = 1750
time3 = 1500

pygame.time.set_timer(SPAWN_EVENT, time1)  # Every 1 second
pygame.time.set_timer(SPAWN_EVENT, time2)   # Every 0.75 seconds
pygame.time.set_timer(SPAWN_EVENT, time3)   # Every 0.5 seconds


# Main loop
def main_game():
    global score, input_text, speed, falling_words, lives

    running = True
    score = 0
    input_text = ''
    speed = 1
    falling_words = []
    lives = 1

    cloud_scroll_x = 0

    while running:
        # Update cloud scroll position
        cloud_scroll_x -= 0.5
        cloud_width = cloud_layer.get_width()
        if cloud_scroll_x <= -cloud_width:
            cloud_scroll_x = 0

        # Draw scrolling cloud layer and background layer
        screen.blit(background, (-200,-150))

        cloud_offset = -200  # for aligning clouds to background
        cloud_y = -30   # vertical position

        screen.blit(cloud_layer, (cloud_scroll_x + cloud_offset, cloud_y))
        screen.blit(cloud_layer, (cloud_scroll_x + cloud_width + cloud_offset, cloud_y))



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == SPAWN_EVENT:
                new_word = Word(random.choice(WORDS))
                falling_words.append(new_word)

            elif event.type == pygame.KEYDOWN:
                typing_sound.play()
                if event.key == pygame.K_RETURN:
                    for word in falling_words:
                        if word.text == input_text:
                            falling_words.remove(word)
                            score += 1
                            speed += .05
                            break
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        for word in falling_words[:]:
            word.update()
            word.draw()
            if word.y > HEIGHT:
                falling_words.remove(word)
                lives -= 1
                if lives <= 0:
                    death_screen(score)
                    main_game()
                    return
                break
        

        input_surface = TYPE_FONT.render(input_text, True, RED)
        input_rect = input_surface.get_rect(center=(WIDTH // 2, HEIGHT - 75))
        screen.blit(input_surface, input_rect)

        draw_text_with_outline(f"Score {score}", SCORE_FONT, WHITE, (0, 0, 0), screen, 17, 7)
        for i in range(lives):
            screen.blit(heart_img, (WIDTH - 32 * (i + 1) - 20, 10))


        pygame.display.flip()
        clock.tick(60)

def death_screen(final_score):
    screen.fill((0, 0, 0))  # Clear screen
    game_over_text = TYPE_FONT.render("GAME OVER", True, RED)
    score_text = SCORE_FONT.render(f"Final Score {final_score}", True, WHITE)
    prompt_text = GAME_OVER_FONT.render("Press ENTER to play again or ESC to quit", True, WHITE)

    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, 300))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 400))
    screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, 500))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False  # restart game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()


show_start_screen()
main_game()
pygame.quit()
sys.exit()
