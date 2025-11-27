import random
from datetime import datetime

def greet_user():
    """Greet the user based on time of day."""
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning"
    elif hour < 17:
        return "Good afternoon"
    else:
        return "Good evening"

def get_lucky_numbers(count=3):
    """Generate a list of lucky numbers."""
    return [random.randint(1, 100) for _ in range(count)]

def get_fortune():
    """Return a random fortune."""
    fortunes = [
        "Today is your lucky day!",
        "Great things are coming your way.",
        "Take a chance - it might just work out!",
        "Your hard work will pay off soon.",
        "A surprise awaits you around the corner.",
        "Trust your instincts today.",
    ]
    return random.choice(fortunes)

def display_ascii_art():
    """Display a fun ASCII art."""
    art = """
    ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★
    ╔═══════════════════╗
    ║  FORTUNE TELLER   ║
    ╚═══════════════════╝
    ★ ☆ ★ ☆ ★ ☆ ★ ☆ ★
    """
    print(art)

def main():
    display_ascii_art()

    greeting = greet_user()
    print(f"\n{greeting}! Welcome to the Fortune Teller!\n")

    print("=" * 40)
    lucky_numbers = get_lucky_numbers()
    print(f"🎲 Your lucky numbers: {', '.join(map(str, lucky_numbers))}")
    print(f"🔮 Your fortune: {get_fortune()}")
    print(f"📅 Today's date: {datetime.now().strftime('%B %d, %Y')}")
    print("=" * 40)

    print("\nHave a wonderful day! ✨\n")

if __name__ == "__main__":
    main()
    print("go to heaven")